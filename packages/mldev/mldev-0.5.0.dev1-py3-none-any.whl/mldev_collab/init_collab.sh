#!/bin/bash

# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://gitlab.com/mlrep/mldev/-/blob/master/NOTICE.md

set -eo pipefail

# ask user for missing required parameters or fail
# 0 - ask always and provide current values
# 1 - ask missing only
# 2 - do not ask, fail
# ASK_MISSING=0

init_collab() {
  echo "INFO:mldev: collab init"

  SUB='darwin'
  if [[ "$OSTYPE" == *"$SUB"* ]]; then
    dir_name=$(greadlink -f "$1");
    else
      dir_name=$(readlink -f "$1");
  fi
  cd "$dir_name"

  if ! [ -x "$(command -v git)" ]; then
    echo "ERROR:mldev: There is no Git. Please, install Git."
    exit 1
  fi

  git_version="$(echo a version 2.17.1; git --version)"
  if [[ $(echo $git_version | sort -Vk3 | tail -1 | grep -q git) ]]; then
    echo "ERROR:mldev: The collaboration tool requires Git v2.17.1 and upper. Please, upgrade Git."
    exit 1
  fi
  if ! [[ $(git status) ]]; then
    echo "ERROR:mldev: Not a git repository. Please, initialize a repository."
    exit 1
  fi

  if [ -f .gitattributes ]; then
    if ! [[ $(grep -Fx "* merge=mldev" .gitattributes) ]]; then
      echo "* merge=mldev" >> .gitattributes
      git add .gitattributes || true
      git commit -m "(mldev-collab) Add collab templates to .gitattributes" || true
    fi
  else
    echo "* merge=mldev" >> .gitattributes
    git add .gitattributes || true
    git commit -m "(mldev-collab) Add collab templates to .gitattributes" || true
  fi

  if ! [[ $(git config --get merge.mldev.name) ]]; then
    git config --local merge.mldev.name "the merge driver for MLDev experiment config files"
    git config --local merge.mldev.driver 'mldev collab merge-driver %O %A %B %L %P \
    || (code=$?; [ $? -eq 10 ] && git-merge-file -q --marker-size=%L %A %O %B || exit $code)'
  fi

  if ! [ -e .mldev/collab/operations/.gitkeep ]; then
    mkdir -p .mldev/collab/operations
    mkdir -p .mldev/collab/tracked
    touch .mldev/collab/operations/.gitkeep
    touch .mldev/collab/tracked/.gitkeep
    git add .mldev/collab/operations/.gitkeep .mldev/collab/tracked/.gitkeep || true
    git commit -m "(mldev-collab) Create collab directories"
  fi

  if [ -f .git/hooks/pre-commit ]; then
    if ! [[ $(grep -Fx "exec mldev collab precommit" .git/hooks/pre-commit) ]]; then
      case ${ASK_MISSING:-0} in
        0|1)
          echo "The pre-commit hook already exists."
          echo "Please add the line below to .git/hooks/pre-commit manually:"
          echo "exec mldev collab precommit"
          read -p "(mldev) Press any key to continue..."
          ;;
        2)
          exit 1
          ;;
      esac
    fi
  else
    echo "#!/bin/bash" > .git/hooks/pre-commit
    echo "exec mldev collab precommit" >> .git/hooks/pre-commit
    chmod +x .git/hooks/pre-commit
  fi

  echo "INFO:mldev: collab init done"
}

if [ $# -eq 0 ]; then
  >&2 echo "INFO:mldev:Usage: $0 <folder> "; exit 1;
fi

>&2 echo "INFO:mldev:Setting up collab tool"
init_collab "$1"

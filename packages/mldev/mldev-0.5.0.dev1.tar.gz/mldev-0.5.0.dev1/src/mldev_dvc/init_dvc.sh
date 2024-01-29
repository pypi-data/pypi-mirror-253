#!/bin/bash

# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://gitlab.com/mlrep/mldev/-/blob/master/NOTICE.md

set -eo pipefail

# enable debug
#set -x

# ask user for missing required parameters or fail
# 0 - ask always and provide current values
# 1 - ask missing only
# 2 - do not ask, fail
# ASK_MISSING=0

# DVC Google Drive Folder
# DVC_REMOTE_NAME=google_drive_remote
# DVC_REMOTE_GDRIVE=""

# environment vars
# LOG_LEVEL=   - same as logging.*

DVC_VERBOSE="-q"
if [[ ${#LOG_LEVEL} -lt 20 ]]; then
  set -x
  GIT_TRACE=True
  export GIT_TRACE
  DVC_VERBOSE="-v"
fi

init_dvc() {
  SUB='darwin'
  if [[ "$OSTYPE" == *"$SUB"* ]]; then
    dir_name=$(greadlink -f "$1");
    else
      dir_name=$(readlink -f "$1");
  fi
  cd "$dir_name"

  # check if we have DVC already configured (e.g. from git repo)
  is_dvc_present=$(dvc remote list 1>/dev/null 2>&1 ; echo $?)

  if [[ $is_dvc_present != "0" ]]; then
    # init dvc
    dvc $DVC_VERBOSE init -f
    dvc $DVC_VERBOSE config core.analytics false
    dvc $DVC_VERBOSE config core.check_update false

    # commit dvc init
    git commit -m "(mldev) Initialize DVC"
  fi

  dvc_remote=$(dvc remote list 2>&1 | grep "${DVC_REMOTE_NAME:-google_drive_remote}" | cut -f 2 ; true)

  if [[ -z "$dvc_remote" ]]; then
    case ${ASK_MISSING:-0} in
      0|1)
        read -eri "$DVC_REMOTE_GDRIVE" -p "(mldev) Please provide Google drive link id to mldev-data folder: " dvc_remote
        ;;
      2)
        dvc_remote=$DVC_REMOTE_GDRIVE
        ;;
    esac

    dvc $DVC_VERBOSE remote add -d "${DVC_REMOTE_NAME:-google_drive_remote}" "gdrive://${dvc_remote}"

    git add .dvc/config
    git commit -m "(mldev) Initialize remote google drive"

    dvc push $DVC_VERBOSE
  fi
}

if [ $# -eq 0 ]; then
  >&2 echo "INFO:mldev:Usage: $0 <folder>"; exit 1;
fi

>&2 echo "INFO:mldev:Setting up DVC"
init_dvc "$1"
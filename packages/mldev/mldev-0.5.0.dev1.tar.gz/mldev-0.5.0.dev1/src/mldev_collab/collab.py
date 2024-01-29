# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://gitlab.com/mlrep/mldev/-/blob/master/NOTICE.md

"""
Collaboration module
====================

This module is a realisation of a collaboration tool that provides
the capability for researchers to work together.

Compatible with Git v2.17.1

"""


import hashlib
import os
from pathlib import Path
import pickle

from mldev import logger

try:
    from git import Repo
except ModuleNotFoundError as ex:
    logger.warn(f"{__name__}: Cannot import Repo from git", exc_info=ex)


MLDEV_COLLAB_PATH = ".mldev/collab"
MLDEV_OPERATIONS_PATH = f"{MLDEV_COLLAB_PATH}/operations"
MLDEV_TRACKED_PATH = f"{MLDEV_COLLAB_PATH}/tracked"


def precommit(operations_cls):
    """
    Operations are atomic actions into which introduced changes are decomposed.
    This function gets operations from the algorithm and saves them in the MLDEV_OPERATIONS_PATH.

    :param operations_cls: The class of algorithm to create an operations' delta between the current and previous
        contents of the file.

    .. note::
        This function assumes that the version control system (VCS) Git is initialized in the current working directory.
        It operates on tracked files that have been added to the Git index and are not in the "untracked" state.

    .. note::
        Before using this function, ensure that the ``MLDEV_OPERATIONS_PATH`` variable contains the path
        to the directory where operation files will be saved.
    """

    def read_file_from_commit(commit, path):
        try:
            return (commit.tree / str(path)).data_stream
        except:
            return None

    def generate_unique_filename(path, content):
        salt = 1
        while True:
            salt_bytes = salt.to_bytes((salt.bit_length() + 7) // 8, "big")
            sha1 = hashlib.sha1(content + salt_bytes).hexdigest()
            p = f"{path}/{sha1}.ops"
            if not Path(p).exists():
                return p
            salt += 1

    # What is staged files:
    # https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository
    rp = Repo(".", search_parent_directories=True)
    head = rp.head.object
    staged_files = [(i.a_path, i.b_path, i.change_type) for i in rp.index.diff(head)]
    tracked = _tracked_set(head)
    for new_filename, prev_filename, change_type in staged_files:
        if change_type == 'R' and prev_filename in tracked:
            original_filename, i = tracked[prev_filename]
            _add_track_event(rp, original_filename, new_filename, i)
        elif _get_tracked_status(head, prev_filename) != "tracked":
            continue
        contents = operations_cls.get_operations_delta(
            Path(new_filename),
            cur_contents=Path(new_filename).open("r"),
            prev_contents=read_file_from_commit(head, Path(prev_filename)),
        )
        data = {
            "filename": new_filename,
            "type": "content",
            "payload": contents,
        }
        binary = pickle.dumps(data)
        fpath = generate_unique_filename(MLDEV_OPERATIONS_PATH, binary)
        Path(fpath).open("wb").write(binary)
        rp.index.add([fpath])


def merge_driver(experiment_file, merge_file, operations_cls):
    """
    Merge driver function to apply operations from multiple commits and update the experiment file.

    :param experiment_file: The path to the experiment specification file.
    :param merge_file: The path to the current version of experiment specification file that needs to be processed
        and updated.
    :param operations_cls: The class of the algorithm to create an operations' delta between the current and previous
        contents of the file.

    This merge driver function applies a series of operations from multiple commits to update the experiment file.
    The merge process starts by obtaining the source and destination commits from the Git repository.

    The merge process involves iterating through the new commits and applying their respective operations to the
    experiment file using the provided ``operations_cls`` algorithm.

    .. note::
        This function assumes that the version control system (VCS) Git is initialized in the current working directory.
        It operates on tracked files that have been added to the Git index and are not in the "untracked" state.

    .. important::
        - The function will raise an exception if the merge cannot be performed due to an unsupported octopus merge
          or if there is nothing to merge (source or destination commit is not found).
        - Ensure that the provided merge driver function is registered correctly with Git for it to be triggered
          during the merge process.
    """

    def get_source_commit():
        """
        Extracts the source commit from the environment variables. Octopus merge is not
        supported.

        Used git internals from
        https://github.com/git/git/blob/5f9953d2c365bffed6f9ee0c6966556bd4d7e2f4/builtin/merge.c#L1317-L1321
        """
        source_commit = None
        for name, value in os.environ.items():
            if name.startswith("GITHEAD_"):
                if source_commit is not None:
                    raise Exception("Octopus merge is not supported.")
                source_commit = Repo(".", search_parent_directories=True).commit(name[8:])
        return source_commit

    def get_new_commits(src_commit, dst_commit, base_file):
        """
        Determines the new commits to be merged by performing a topological sort on the commit graph.

        :param src_commit: the source commit (commit in their branch)
        :param dst_commit: the destination commit (commit in our branch)
        :param base_file: the file name as it was at the base commit (common ancestor)
        """

        def topological_sort(start_commit):
            stack = []
            visited = set()
            processing = set()

            def _sort(commit):
                if commit in processing:
                    raise Exception(
                        "The commit graph contains cycles, can not make topological sort."
                    )
                processing.add(commit)
                for pcommit in commit.parents:
                    if pcommit not in visited:
                        _sort(pcommit)
                stack.append(commit)
                processing.remove(commit)
                visited.add(commit)

            _sort(start_commit)
            return stack

        def get_renamed_filename(commit_a, commit_b, file):
            for f in commit_a.diff(commit_b):
                if Path(file) == Path(f.a_path):
                    return f.b_path
            return file

        dst_commits = topological_sort(dst_commit)
        src_commits = topological_sort(src_commit)
        i = 0
        if dst_commits[i] != src_commits[i]:
            raise Exception(
                "Destination and source commits haven't any common ancestor."
            )
        while dst_commits[i + 1] == src_commits[i + 1]:
            i += 1
        new_commits = []
        file = base_file
        for j in range(i, len(src_commits) - 1):
            file = get_renamed_filename(src_commits[j], src_commits[j + 1], file)
            new_commits.append((src_commits[j + 1], file))
        return new_commits

    def get_renamed_files(a_commit, b_commit):
        """
        Maps files renamed in ``b_commit`` with files from ``a_commit``

        :param a_commit: some commit
        :param b_commit: some commit
        """
        res = {}
        for diff_renamed in a_commit.diff(b_commit).iter_change_type("R"):
            res[diff_renamed.a_path] = diff_renamed.b_path
        return res

    def get_original_filenames(a_commit, b_commit, file):
        """
        This function tries to determine the original files' names as they were at their branches.

        :param a_commit: some commit
        :param b_commit: some commit
        :param file: filename provided by git while resolving merge conflict
        """
        base_commit = a_commit.repo.merge_base(a_commit, b_commit)[0]
        a_renamed = get_renamed_files(a_commit, base_commit)
        b_renamed = get_renamed_files(b_commit, base_commit)

        if file in a_renamed and file not in b_renamed:
            return file, a_renamed[file], a_renamed[file]
        if file not in a_renamed and file in b_renamed:
            return b_renamed[file], file, b_renamed[file]
        if file in a_renamed and file in b_renamed:
            assert False
        if file not in a_renamed and file not in b_renamed:
            if Path(file).exists():
                return file, file, file
            else:
                # rename/rename conflict
                return (
                    get_renamed_files(base_commit, a_commit)[file],
                    get_renamed_files(base_commit, b_commit)[file],
                    get_renamed_files(base_commit, a_commit)[
                        file
                    ],  # Any from a_commit and b_commit
                )

    def get_commit_data(commit, filename, data_type="content"):
        """
        Get data from an internal storage format.
        """

        if commit.parents:
            parent_commit = commit.parents[0]
        else:
            # In the case when a parent commit is absent, we have to compare a commit with
            # the empty commit (the null tree). To find out this tree's SHA1, use `git hash-object -t tree /dev/null`.
            # More details: https://github.com/gitpython-developers/GitPython/issues/732#issuecomment-394701104
            null_tree_hashsha = "4b825dc642cb6eb9a060e54bf8d69288fbee4904"
            parent_commit = commit.repo.tree(null_tree_hashsha)
        diff = parent_commit.diff(commit, paths=MLDEV_OPERATIONS_PATH)
        for file in diff:
            if file.new_file and file.b_path.startswith(MLDEV_OPERATIONS_PATH) and file.b_path.endswith(".ops"):
                try:
                    blob = commit.tree / file.b_path
                except KeyError:
                    continue
                if blob:
                    try:
                        data = pickle.loads(blob.data_stream.read())
                        if data["filename"] == filename and data["type"] == data_type:
                            return data["payload"]
                    except (pickle.UnpicklingError, KeyError):
                        raise Exception(f"Corrupted collab file {file.b_path}")

    src_commit = get_source_commit()
    dst_commit = Repo(".", search_parent_directories=True).head.object
    if src_commit is None or dst_commit is None:
        raise Exception("There is nothing to merge.")
    dst_file, src_file, base_file = get_original_filenames(
        dst_commit, src_commit, experiment_file
    )
    dst_status = _get_tracked_status(dst_commit, dst_file)
    src_status = _get_tracked_status(src_commit, src_file)
    # statuses: tracked, untracked, removed
    if dst_status == "untracked" and src_status == "untracked":
        return "untracked"
    elif dst_status == "tracked" and src_status == "tracked":
        new_commits = get_new_commits(src_commit, dst_commit, base_file)  # base???
        for commit, experiment_file in new_commits:
            commit_ops = get_commit_data(commit, experiment_file)
            if commit_ops:
                res = operations_cls.apply_operations(merge_file, commit_ops)
                if res and res == "conflict":
                    return "conflict"
        return "merged"
    else:
        raise Exception("Unsupported merge operation.")


def is_tracked(filename, path="."):
    """
    Check is a file in the tracked ones.

    :param filename: name of the file
    :param path: path to the MLDev template
    """
    rp = Repo(path, search_parent_directories=True)
    return filename in _tracked_set(rp.head.object)


def track_file(filename):
    """
    Add a new file to the tracked ones.

    :param filename: name of the file
    """
    rp = Repo(".", search_parent_directories=True)
    if rp.is_dirty(untracked_files=True):
        return 1
    _add_track_event(rp, filename, new_filename=None, i=0)
    rp.index.commit(f"(mldev-collab) Add `{filename}` to the tracked ones.")


def _get_tracked_status(commit, filename):
    if filename in _tracked_set(commit):
        return "tracked"
    return "untracked"


def _tracked_set(commit):
    import base64
    from itertools import groupby

    files = []
    for item in commit.tree[MLDEV_TRACKED_PATH].traverse():
        if item.type == 'blob':
            if item.name.startswith('.'):
                continue
            original_filename, file_commit, i, salt = item.name.split('_')
            i = int(i)
            original_filename = base64.b16decode(original_filename.encode('utf-8')).decode('utf-8')
            files.append((original_filename, i, file_commit, item.name,))

    files.sort(key=lambda x: x[0])
    last_versions = []
    for key, group in groupby(files, key=lambda x: x[0]):
        max_i_tuple = max(group, key=lambda x: x[1])
        last_versions.append(max_i_tuple)

    res = {}
    for version in last_versions:
        original_filename, i, file_commit, filename = version
        f = commit.tree / MLDEV_TRACKED_PATH / filename
        new_filename = f.data_stream.read().decode('utf-8')
        if new_filename != '/deleted':
            res[new_filename] = (original_filename, i,)
    return res


def _add_track_event(rp, original_filename, new_filename=None, i=0):
    import base64

    encoded_filename = base64.b16encode(original_filename.encode('utf-8')).decode('utf-8')
    track_filename = Path(MLDEV_TRACKED_PATH) / f"{encoded_filename}_{rp.head.object}_{i+1}_{_generate_salt()}"
    f = Path(rp.working_dir) / track_filename
    if new_filename:
        f.write_text(new_filename)
    else:
        assert i == 0
        f.write_text(original_filename)
    rp.index.add([track_filename.as_posix()])


def _generate_salt(salt_length=10):
    import secrets
    import string

    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(salt_length))

from mldev.experiment_objects import FilePath
import os


def test_basic():
    file_path = {
        "path": "./local",
        "files": ["file1", "file2.txt"]
    }

    assert os.path.abspath("./local/file1") == \
           FilePath(**file_path).get_files()[0]
    assert os.path.abspath("./local/file2.txt") == \
           FilePath(**file_path).get_files()[1]
    assert f"{os.path.relpath('./local/file1')} " \
           f"{os.path.relpath('./local/file2.txt')}" == \
           str(FilePath(**file_path))

def test_path():
    file_path = {
        "files": ["file1", "file2.txt"]
    }

    assert os.path.abspath("./file1") == \
           FilePath(**file_path).get_files()[0]
    assert os.path.abspath("./file2.txt") == \
           FilePath(**file_path).get_files()[1]

    file_path = {
        "path": "./local"
    }

    assert os.path.relpath("./local") == \
           str(FilePath(**file_path))

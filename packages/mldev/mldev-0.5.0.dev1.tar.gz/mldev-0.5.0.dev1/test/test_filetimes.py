import pytest
import tempfile
import os
import time

from mldev.utils import get_path_times, set_path_times
from mldev.experiment import FilePath


@pytest.fixture(scope="function")
def init_tmp():
    tmpdir = tempfile.TemporaryDirectory()
    tmpfile1 = tempfile.NamedTemporaryFile(dir=tmpdir.name)
    tmpfile2 = tempfile.NamedTemporaryFile(dir=tmpdir.name)

    times = time.time() - 10
    os.utime(tmpfile2.name, (times, times))

    try:
        yield tmpdir.name, (tmpfile1.name, tmpfile2.name), times
    finally:
        tmpfile1.close()
        tmpfile2.close()
        tmpdir.cleanup()


def test_getmtimes(init_tmp):
    tmpdir, _, times = init_tmp

    assert os.path.exists(tmpdir)
    assert times > 0

    min_ts = time.time()
    max_ts = 0

    min_ts, max_ts, missing = get_path_times(tmpdir, min_ts, max_ts)
    assert int(min_ts) == int(times)
    assert not missing
    assert int(max_ts) >= int(min_ts)
    assert int(max_ts) <= int(time.time())


def test_setmtimes(init_tmp):
    tmpdir, (tmpfile1, tmpfile2), times = init_tmp

    assert os.path.exists(tmpdir)
    assert times > 0

    min_ts = time.time() - 100
    max_ts = 0

    result = set_path_times(tmpfile1, (min_ts, min_ts))
    assert result

    _min_ts, _max_ts, missing = get_path_times(tmpdir, min_ts=time.time(), max_ts=max_ts)
    assert int(min_ts) == int(_min_ts)
    assert not missing
    assert int(_max_ts) >= int(min_ts)
    assert int(_max_ts) <= int(time.time())


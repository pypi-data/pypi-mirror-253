import pytest

from mldev.main import run_experiment
# noinspection PyUnresolvedReferences
# import required to create MockStage tag constructor
import mock_stage
from mldev import logger

logger.setLevel('DEBUG')


def index_containing_substring(lst, substr):
    for index, str in enumerate(lst):
        if substr in str:
            return index
    return -1


@pytest.mark.parametrize("pipeline", ["mock_stage", "mock_stage2", "mock_stages_list2", "mock_stage3"])
def test_run_stage_calls_stage_prepare_and_call(caplog, pipeline):
    run_experiment('./test/data/test_experiment_stage_run.yaml', pipeline=pipeline)

    log_lines = caplog.text.split('\n')

    assert len(list(filter(lambda s: s.endswith('MockStage prepare called'), log_lines))) == 1
    assert len(list(filter(lambda s: s.endswith('MockStage __call__ called'), log_lines))) == 1

    index_containing_prepare_called = index_containing_substring(log_lines, 'MockStage prepare called')
    index_containing_run_called = index_containing_substring(log_lines, 'MockStage __call__ called')

    assert index_containing_prepare_called < index_containing_run_called


@pytest.mark.parametrize("pipeline", ["pipeline", "pipeline2"])
def test_run_pipeline_calls_stage_prepare_and_call(caplog, pipeline):
    run_experiment('./test/data/test_experiment_stage_run.yaml', pipeline=pipeline)

    log_lines = caplog.text.split('\n')

    assert len(list(filter(lambda s: s.endswith('MockStage prepare called'), log_lines))) == 1
    assert len(list(filter(lambda s: s.endswith('MockStage __call__ called'), log_lines))) == 1

    index_containing_prepare_called = index_containing_substring(log_lines, 'MockStage prepare called')
    index_containing_run_called = index_containing_substring(log_lines, 'MockStage __call__ called')

    assert index_containing_prepare_called < index_containing_run_called


@pytest.mark.parametrize("pipeline", ["recursive_pipeline", "failed_stage", "failed_pipeline", "failed_pipeline2", "failed_pipeline3"])
def test_failed_pipeline(caplog, pipeline):
    result = run_experiment('./test/data/test_experiment_stage_run.yaml', pipeline=pipeline)
    assert result == 1

    log_lines = caplog.text.split('\n')

    assert len(list(filter(lambda s: s.endswith('MockStage prepare called'), log_lines))) == 0
    assert len(list(filter(lambda s: s.endswith('MockStage __call__ called'), log_lines))) == 0

from mldev.main import run_experiment

# import required to create tags constructors
# noinspection PyUnresolvedReferences
import iterable_wrapper

from mldev import logger
logger.setLevel('DEBUG')


def _assert_stage_is_called_times(stage, log_lines, times):
    assert len(list(filter(
        lambda s: s.endswith(f'LazyConstructionTestStage {stage} __call__ called with mode run'),
        log_lines))) == times
    assert len(list(filter(
        lambda s: s.endswith(f'LazyConstructionTestStage {stage} prepare called'),
        log_lines))) == times
    assert len(list(filter(
        lambda s: s.endswith(f'LazyConstructionTestStage {stage} run called'),
        log_lines))) == times


def test_stage_inside_iterable_is_not_created_if_pipeline_is_not_called(caplog):

    run_experiment('./test/data/test_experiment_iterable_wrapper.yaml', pipeline='do_nothing_pipeline')

    log_lines = caplog.text.split('\n')

    assert len(list(filter(lambda s: s.endswith('LazyConstructionTestStage stage1 constructor called'), log_lines))) \
           == 0
    assert len(list(filter(lambda s: s.endswith('LazyConstructionTestStage stage2 constructor called'), log_lines))) \
           == 1

    _assert_stage_is_called_times('stage1', log_lines, 0)
    _assert_stage_is_called_times('stage2', log_lines, 0)


def test_stage_inside_iterable_is_created_if_pipeline_is_called(caplog):

    run_experiment('./test/data/test_experiment_iterable_wrapper.yaml', pipeline='lazy_pipeline')

    log_lines = caplog.text.split('\n')

    assert len(list(filter(lambda s: s.endswith('LazyConstructionTestStage stage1 constructor called'), log_lines))) \
           == 1
    assert len(list(filter(lambda s: s.endswith('LazyConstructionTestStage stage2 constructor called'), log_lines))) \
           == 1

    _assert_stage_is_called_times('stage1', log_lines, 1)
    _assert_stage_is_called_times('stage2', log_lines, 0)


def test_attribute_of_stage_inside_normal_pipeline_is_evaluated(caplog):

    run_experiment('./test/data/test_experiment_iterable_wrapper.yaml', pipeline='eager_pipeline')

    log_lines = caplog.text.split('\n')

    assert len(list(filter(lambda s: s.endswith('LazyConstructionTestStage stage2 evaluated = stage2'), log_lines))) \
           == 1

def test_attribute_of_stage_inside_iterable_is_evaluated_if_called(caplog):

    run_experiment('./test/data/test_experiment_iterable_wrapper.yaml', pipeline='lazy_pipeline_with_expression')

    log_lines = caplog.text.split('\n')

    _assert_stage_is_called_times('stage3', log_lines, 1)
    assert len(list(filter(lambda s: s.endswith('LazyConstructionTestStage stage3 evaluated = stage3'), log_lines))) \
           == 1

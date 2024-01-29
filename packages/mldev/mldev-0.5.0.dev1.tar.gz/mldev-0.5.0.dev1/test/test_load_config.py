# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://gitlab.com/mlrep/mldev/-/blob/master/NOTICE.md

import os
import yaml


from mldev.experiment import *
from mldev.yaml_loader import stage_context
from mldev.expression import Expression
from mldev.yaml_loader import YamlLoaderWithEnvVars
from test import logger
import pytest

os.makedirs(MLDevSettings().temp_dir, exist_ok=True)

@pytest.fixture(scope="function")
def mldev_env():
    os.environ["NGROK_TOKEN"] = "token_for_test"
    os.environ["TELEGRAM_TOKEN"] = "token_for_telegram"
    yield

    del os.environ["NGROK_TOKEN"]
    del os.environ["TELEGRAM_TOKEN"]


def test_parameterizable():
    obj = {
        'a':1,
        'b':"123"
    }
    p = Expression("a=${self['a']}", ctx=lambda : obj)
    assert p == "a=1"

    p = Expression("--json \"${json(self)}\"", ctx=lambda : obj)
    # json() also escapes the resulting string json
    assert p == '--json "{\\"a\\": 1, \\"b\\": \\"123\\"}"'

    p = Expression("${path('./')}", ctx=None)
    assert p == os.path.abspath("./")


def test_load_config_with_env_var_successful(mldev_env):
    logger.debug("\n\n\ntest_load_config_with_env_var_successful")
    loader = YamlLoaderWithEnvVars("./test/data/test_experiment_v2.yaml")
    cfg = loader.load_config()
    logger.info(cfg)

    assert cfg['ngrok'].params['token'] == "token_for_test"
    assert cfg['notification_bot'].params['token'] == "token_for_telegram"


def test_load_config_with_var_in_file_successful():
    logger.debug("\n\n\ntest_load_config_with_var_in_file_successful")

    path = os.path.expanduser("~") + "/.config/mldev"
    settings_file = path + "/config.yaml"
    logger.debug("NGROK_TOKEN in env vars: {}".format(os.getenv("NGROK_TOKEN")))
    logger.debug("TELEGRAM_TOKEN in env vars: {}".format(os.getenv("TELEGRAM_TOKEN")))

    if not os.path.exists(path):
        os.makedirs(path)

    with open(settings_file, "w+") as f:
        yaml.dump({"environ": {"NGROK_TOKEN": "token_from_env_yaml", "TELEGRAM_TOKEN": "token_from_env_telegram"}}, f)

    MLDevSettings.forget()

    loader = YamlLoaderWithEnvVars("./test/data/test_experiment_v2.yaml")
    cfg = loader.load_config()
    logger.debug(cfg)

    os.remove(settings_file)
    assert cfg['ngrok'].params['token'] == "token_from_env_yaml"
    assert cfg['notification_bot'].params['token'] == "token_from_env_telegram"


def test_load_config_script_parameters(mldev_env):
    logger.debug("\n\n\ntest_load_config_with_env_var_successful")

    loader = YamlLoaderWithEnvVars("./test/data/test_experiment_v2.yaml")
    cfg = loader.load_config()
    logger.debug(cfg)

    with stage_context(cfg['train']) as stage:
        assert stage.script[0] == 'python3 src/train.py --n 10'


def test_load_config_lines(mldev_env):

    loader = YamlLoaderWithEnvVars("./test/data/test_experiment_v2.yaml")
    cfg = loader.load_config()
    logger.debug(cfg)

    with stage_context(cfg['prepare']) as stage:
        assert stage.outputs[1].path == './logs/logs2'


def test_load_config_core(mldev_env):

    loader = YamlLoaderWithEnvVars("./test/data/test_experiment_core.yaml")
    cfg = loader.load_config()
    logger.debug(cfg)

    assert isinstance(cfg['prepare'], BasicStage)
    assert isinstance(cfg['train'], BasicStage)
    with stage_context(cfg['prepare']) as stage:
        assert stage.outputs[1].path == './test/temp/logs/logs2'
        assert str(stage.script[1]) == 'python3 test/data/sample_function.py "prepare part 2"'


def test_load_config_params(mldev_env):
    loader = YamlLoaderWithEnvVars("./test/data/test_experiment_v2.yaml")
    cfg = loader.load_config()
    logger.debug(cfg)

    with stage_context(cfg['present_model']) as stage:
        assert str(stage.script[0]) == f'mldev run run_model --input "[[\\"{os.path.abspath("models/default/model.pickle-6")}\\"]]"'
        assert str(stage.script[1]) == 'mldev run run_model --MLDEV_MODEL_PATH "models/default/model.pickle" --num_path "1"'


def test_load_config_ipython(mldev_env):

    loader = YamlLoaderWithEnvVars("./test/data/test_experiment_ipython.yaml")
    cfg = loader.load_config()
    logger.debug(cfg)

    with stage_context(cfg['ipython_pipeline']) as stage:
        assert str(stage.env['FILES']) == "X_train.pickle y_train.pickle"
        assert str(stage.script[0]) == "mldev run -f experiment_ipython.yml pipeline"


def test_load_config_ipython_stage(mldev_env):

    loader = YamlLoaderWithEnvVars("./test/data/test_experiment_ipython_stage.yaml")
    cfg = loader.load_config()
    logger.debug(cfg)

    assert cfg['ipython'].__class__.__name__ == 'JupyterStage'
    assert cfg['ipython'].name == 'iris_visualization'
    assert cfg['ipython'].notebook_pipeline_name == 'test/data/test_ipython.test_pipeline'
    assert cfg['ipython'].outputs is None
    assert cfg['ipython'].compare_results is None


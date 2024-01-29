# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://gitlab.com/mlrep/mldev/-/blob/master/NOTICE.md

"""
Config parser module
====================

This module provides a config for all mldev components

See ``_MLDevSettings`` for documentation on ``MLDevSettings`` class

"""


import importlib.util as import_lib
import logging
import os

import functools
import yaml
import pkg_resources


class _SingletonWrapper:

    def __init__(self, cls):
        self.__wrapped__ = cls
        self.__dict__.update(cls.__dict__)
        self._instance = None

    def forget(self):
        """
        Purges current instance. A new instance is created on the next ''__call__''
        :return:
        """
        del self._instance
        self._instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = self.__wrapped__(*args, **kwargs)
        return self._instance


def singleton(cls):
    return _SingletonWrapper(cls)


class _MLDevSettings:
    """
    Contains mldev configuration for the experiment.

    The following are the sources of the configuration:

     - ``config.yaml`` or compatible file, see docs for more details.
     - current environment variables

    ``MLDevSettings`` looks for the config file until it is found in the following places:

     - ``config_path`` parameter for constructor
     - env var ``MLDEV_CONFIG_PATH``
     - ``./.mldev/config.yaml``
     - ``<user_home>/.config/mldev/config.yaml``

    Configuration parameters can be retrieved with ``MLDevSettings().get_value(name)``

    Important ``environ`` parameters that are added automatically:

     - ``LOG_LEVEL`` is the current log level as defined by ``logging`` module
     - ``TOOL_DIR`` is the MLDev location

    """

    DEFAULT_EXTRAS = {
        'base': 'mldev.experiment_objects',
    }

    ALL_EXTRAS = {
        'base': 'mldev.experiment_objects',
        'bot': 'mldev_bot.bot_service',
        'tensorboard': 'mldev_tensorboard.tensorboard_service',
        'dvc': 'mldev_dvc.dvc_stage',
        'ipython': 'mldev_jupyter.ipython',
        'controller': 'mldev_controller.controller_service'
    }


    def default_config_path(self):
        """
        Returns current path to config.yaml for mldev
        :return: path to config
        """

        if hasattr(self, 'app_config_path') and self.app_config_path:
            return self.app_config_path

        home = os.path.expanduser("~")
        environ_app_config_path = os.environ.get('MLDEV_CONFIG_PATH', None)

        paths = [
            f"./.mldev/config.yaml",
            f"{home}/.config/mldev/config.yaml"
        ]

        if environ_app_config_path:
            paths.insert(0, environ_app_config_path)

        for p in paths:
            if os.path.exists(p):
                return p

        return paths[-1]

    def __init__(self, config_path=None, raise_deps=False):

        # this is relative to experiment dir
        self.temp_dir = ".mldev"
        self.tool_dir = os.path.abspath(os.path.dirname(__file__) + "/../")

        if not config_path:
            self.app_config_path = os.path.abspath(self.default_config_path())

            if not os.path.exists(self.app_config_path):
                os.makedirs(os.path.dirname(self.app_config_path), exist_ok=True)
                with open(self.app_config_path, "w+"):
                    pass
        else:
            if not os.path.exists(config_path):
                raise Exception(f"Config file not found: {config_path}")
            self.app_config_path = os.path.abspath(config_path)

        with open(self.app_config_path, "r+") as f:
            self.cfg = yaml.load(f, Loader=yaml.SafeLoader)
            if not self.cfg:
                self.cfg = dict()

        self.environ = self.cfg.get("environ", dict())
        self.environ['TOOL_DIR'] = self.tool_dir

        self.logs_dir = None
        if self.get_value("LOG_LEVEL") is None:
            self.set_value("LOG_LEVEL", logging.INFO)

        if "logger" in self.cfg:
            if "path" in self.cfg["logger"]:
                self.logs_dir = self.cfg["logger"]["path"]
                os.makedirs(self.logs_dir, exist_ok=True)

            if "level" in self.cfg["logger"]:
                if self.cfg["logger"]["level"] == "DEBUG":
                    self.set_value("LOG_LEVEL", logging.DEBUG)
                elif self.cfg["logger"]["level"] == "INFO":
                    self.set_value("LOG_LEVEL", logging.INFO)
                elif self.cfg["logger"]["level"] == "ERROR":
                    self.set_value("LOG_LEVEL", logging.ERROR)
                else:
                    raise Exception(f"Invalid log level: {self.cfg['logger']['level']}")

        logger = logging.getLogger("mldev.mldev_config_parser")
        logger.setLevel(self.get_value("LOG_LEVEL"))

        self._extras = self.cfg.get("extras", MLDevSettings.DEFAULT_EXTRAS)
        logger.info(f"Loading extras: {self._extras.keys()}")
        for extra in self._extras:
            module_name = str(self._extras[extra])
            path = os.path.join(self.tool_dir, module_name.replace(".",os.path.sep) + ".py")
            logger.info(f"Trying to load extra {extra} with {module_name} from {path}")
            if os.path.exists(path):
                _import_module(path, module_name)
            else:
                # try __init__.py
                path = os.path.join(self.tool_dir,
                                    module_name.replace(".", os.path.sep),
                                    os.path.sep, "__init__.py")
                logger.info(f"Trying to load extra {extra} with {module_name} from {path}")
                if os.path.exists(path):
                    _import_module(path, module_name)
                else:
                    raise ModuleNotFoundError(module_name)

            # checking dependencies are installed
            err_msg = f"Could not check dependencies for extra {extra}. " \
                      f"Please install missing extras using ./install_mldev.sh {extra}. "
            try:
                pkg_resources.require(f"mldev[{extra}]")
            except (pkg_resources.ContextualVersionConflict,
                    pkg_resources.UnknownExtra,
                    pkg_resources.DistributionNotFound) as ex:

                ex._template = err_msg + (ex._template if hasattr(ex, "_template") else "")
                if raise_deps:
                    logger.error(err_msg, exc_info=ex)
                    raise ex
                else:
                    logger.warning(err_msg, exc_info=ex)
            except Exception as ex:
                logger.error(err_msg, exc_info=ex)
                raise ex

        #self.__class__._instance = self

    def get_value(self, name):
        """
        Get a parameter from the ``environ`` config section.
        :param name:
        :return:
        """
        return self.environ.get(name, None)

    def set_value(self, name, value):
        """
        Update a parameter from the ``environ`` config section
        :param name:
        :param value:
        :return:
        """
        if value is None:
            del self.environ[name]
        else:
            self.environ[name] = value

    def is_feature(self, name):
        """
        Checks if an ``environ`` parameter is set to ``True``

        :param name:
        :return:
        """
        return self.environ.get(name, "False") == "True"

    def is_extra(self, name):
        """
        Checks if an ``extra`` feature is defined for this experiment

        :param name:
        :return:
        """
        return name in self._extras

    def get_extra(self, name):
        """
        Retrieves a path to the module defining the extra

        :param name:
        :return:
        """
        return self._extras.get(name)

    def get_extra_base(self, name):
        """
        Retrieves a top-level package name for the ``extra``

        :param name:
        :return:
        """
        return str(self._extras.get(name, "")).split('.')[0]

    def set_feature(self, name, value):
        """
        Enables/disables the feature in ``environ``. For ``bool(True/False)`` sets string ``True/False``

        :param name:
        :param value:
        :return:
        """

        if value is None:
            self.environ[name] = None
        else:
            self.environ[name] = "True" if bool(value) else "False" if not bool(value) else None


def _import_module(path, module_name):
    spec = import_lib.spec_from_file_location(module_name, path)
    module = import_lib.module_from_spec(spec)
    spec.loader.exec_module(module)

MLDevSettings = singleton(_MLDevSettings)
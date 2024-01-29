# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://gitlab.com/mlrep/mldev/-/blob/master/NOTICE.md

"""
DVC integration module
======================

This module allows to use MLDev together with DVC.

See ``Stage`` class that implements a stage which uses DVC to set up dependencies.

"""

from mldev.experiment import *
from mldev.yaml_loader import stage_context
from mldev import *
from mldev.utils import *


@experiment_tag()
class Stage(object):
    """
    Main class for DVC pipeline stages.

    Converts ``script`` to a single command line and creates a stage in DVC in ``prepare``.
    Reproduces the stage via DVC ``repro`` in ``run``.

    Adds ``inputs`` as input dependencies and ``outputs`` as results and places
    them under version control. If ``MLDEV_NO_COMMIT`` feature is not set
    also makes a git commit with DVC's files.

    Accepts the following parameters:

    :param inputs: lists files and folders that this stage depends upon
    :param outputs: lists files and folders that this stage produces
    and that will be added to version control
    :param params: parameters for the commands being invoked
    :param env: additional environmental variables to pass to commands
    :param script: a list of commands to invoke
    """

    def __init__(self, name="", params={}, env={}, inputs={}, outputs={}, script=[]):
        super().__init__()
        self.prepared = False
        self.name = name
        self.params = params
        self.env = env
        self.inputs = inputs
        self.outputs = outputs
        self.script = script

    def __repr__(self):
        with stage_context(self):
            return str(self.__dict__)

    def __call__(self, name, *args, experiment={}, **kwargs):
        with stage_context(self):
            stage_name = name if name else self.name
            logger.debug(f"{self.__class__.__name__}({stage_name}).__call__()")
            if stage_name:
                self.run(stage_name)
                dvc_verbose = ""
                git_verbose = ""
                if MLDevSettings().get_value("LOG_LEVEL") <= LOG_DEBUG:
                    dvc_verbose = "-v"
                    git_verbose = "export GIT_TRACE=true && "
                if not MLDevSettings().is_feature("MLDEV_NOCOMMIT"):

                    # TODO dvc has a bug - it ignores -q parameter
                    # capture and discard the output if log level is high
                    capture = not (MLDevSettings().get_value("LOG_LEVEL") <= LOG_INFO)
                    exec_command(f"dvc push {dvc_verbose}", capture=capture)
                    exec_command(f'{git_verbose} git add ./dvc.lock ./dvc.yaml && git commit -m '
                                 '"(mldev) data config lock" || true')

    def prepare(self, stage_name):
        if stage_name:
            with stage_context(self):
                no_commit = ""
                dvc_verbose = "-q"
                if MLDevSettings().is_feature("MLDEV_NOCOMMIT"):
                    no_commit = "--no-commit"
                if MLDevSettings().get_value("LOG_LEVEL") <= LOG_DEBUG:
                    dvc_verbose = "-v"

                script = prepare_experiment_command(' && '.join([str(s) for s in self.script]),
                                                    env=self.env)
                s = f"dvc {dvc_verbose} run {no_commit} --no-exec -f -n {stage_name}{self._build_dependency_string()} " +\
                    '"{}"'.format(shell_escape(script, shell_symbols='\"'))

                logger.info(f"Prepare ({stage_name}): " + s)

                # TODO dvc has a bug - it ignores -q parameter
                # capture and discard the output if log level is high
                capture = not (MLDevSettings().get_value("LOG_LEVEL") <= LOG_INFO)
                exec_command(s, capture=capture)

                self.prepared = True

    def run(self, stage_name):
        with stage_context(self):
            run_cache = ""
            no_commit = ""
            dvc_verbose = "-q"

            if MLDevSettings().get_value("LOG_LEVEL") < LOG_INFO:
                dvc_verbose = "-v"
            if MLDevSettings().is_feature("FORCE_RUN"):
                run_cache = "--no-run-cache --force"
            if MLDevSettings().is_feature("MLDEV_NOCOMMIT"):
                no_commit = "--no-commit"

            s = f"dvc {dvc_verbose} repro {run_cache} {no_commit} {stage_name}"
            logger.info(f"Run ({stage_name}): " + s)

            # TODO dvc has a bug - it ignores -q parameter
            # capture and discard the output if log level is high
            # capture = not (MLDevSettings().get_value("LOG_LEVEL") <= LOG_INFO)
            capture = False # contains user program output
            exec_command(s, capture=capture)

    def _add_file_deps(self, deps, inputs=True, create_deps=True):
        result = ""
        key = "-d" if inputs else "-o"
        for file_path in deps:
            if isinstance(file_path, FilePath):
                for file in file_path.get_files(start=os.path.curdir):
                    result += f" {key} {shell_quote(file)}"
                    if not os.path.exists(file) and create_deps:
                        is_dir = file.endswith(os.path.sep)
                        touch_file(file, is_dir=is_dir)
                if len(file_path.files) == 0:
                    result += f" {key} {shell_quote(file_path.get_path(start=os.path.curdir))}"
                    if not os.path.exists(str(file_path.path)) and create_deps:
                        touch_file(str(file_path.path), is_dir=True)
            else:
                result += f" {key} {shell_quote(file_path)}"
        return result

    def _build_dependency_string(self):
        input_deps = ""
        output_deps = ""
        if self.inputs:
            input_deps += self._add_file_deps(self.inputs, inputs=True)
        if self.outputs:
            output_deps += self._add_file_deps(self.outputs, inputs=False)
        return " ".join([input_deps, output_deps])

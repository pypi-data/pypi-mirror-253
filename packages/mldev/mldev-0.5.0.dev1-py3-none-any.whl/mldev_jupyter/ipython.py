# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://gitlab.com/mlrep/mldev/-/blob/master/NOTICE.md

"""
Jupyter integration module
==========================

This module allows to use MLDev together with Jupyter notebooks.

See ``NotebookRunner`` class that runs code cells from Jupyter notebook.

"""

import os
import re

from IPython.core.interactiveshell import InteractiveShell
import nbformat
import yaml
import dill
from markdown_it import MarkdownIt
from matplotlib.pyplot import Figure

from mldev import logger
from mldev.experiment import FilePath
from mldev.experiment_tag import experiment_tag
from mldev.utils import shell_quote, touch_file, exec_command
from mldev.yaml_loader import stage_context


@experiment_tag()
class JupyterStage(object):
    """
        A main class for IPython notebooks pipeline stages

        Accepts the following parameters:

        :param name: stage name
        :param notebook_pipeline: a string in format <path_to_notebook>.<pipeline_name>
        :param outputs: lists files and folders that this stage produces or files from
                        which variables are taken for comparison
        :param compare_results: if True, will load saved results and compare with received during the run,
                        if False or None, results received during the run will be saved
    """

    def __init__(self, name="", notebook_pipeline='', outputs=None, compare_results=None):
        super().__init__()
        self.name = name
        self.notebook_pipeline_name = notebook_pipeline
        self.outputs = outputs
        self.compare_results = compare_results
        self.notebook_pipeline = None

    def __repr__(self):
        with stage_context(self):
            return str(self.__dict__)

    def __call__(self, *args, **kwargs):
        with stage_context(self):
            stage_name = args[0] if args[0] else self.name
            logger.debug(f"{self.__class__.__name__}({stage_name}).__call__()")
            if stage_name:
                self.run(stage_name)

    def prepare(self, stage_name):
        if stage_name:
            with stage_context(self):
                deps = self._build_dependency_string()
                if deps:
                    s = f"git lfs track {deps}"
                    logger.info(f"{self.__class__.__name__} prepare ({stage_name}): " + s)
                    exec_command(s)

    def run(self, stage_name):
        self.notebook_pipeline = NotebookPipeline(
            stage_name, self.notebook_pipeline_name, self.outputs, self.compare_results
        )

        with stage_context(self):
            self.notebook_pipeline.run()

    def _add_file_deps(self, deps, create_deps=True):
        result = ""
        for file_path in deps:
            if isinstance(file_path, FilePath):
                for file in file_path.get_files(start=os.path.curdir):
                    result += f"{shell_quote(file)}"
                    if not os.path.exists(file) and create_deps:
                        is_dir = file.endswith(os.path.sep)
                        touch_file(file, is_dir=is_dir)
                if len(file_path.files) == 0:
                    result += f"{shell_quote(file_path.get_path(start=os.path.curdir))}"
                    if not os.path.exists(str(file_path.path)) and create_deps:
                        touch_file(str(file_path.path), is_dir=True)
            else:
                result += f"{shell_quote(file_path)}"
        return result

    def _build_dependency_string(self):
        output_deps = ""
        if self.outputs:
            output_deps += self._add_file_deps(self.outputs)
        return output_deps


class NotebookPipeline:
    def __init__(self, stage_name, pipeline_config, outputs, compare):
        """
            A class that opens Jupyter notebook and gets pipeline from it.
            Creates NotebookRunner instance and triggers it to run pipeline.

            Accepts the following parameters:

            :param stage_name: stage name
            :param pipeline_config: a string in format <path_to_notebook>.<pipeline_name>
            :param outputs: lists files and folders that this stage produces or files from
                            which variables are taken for comparison
            :param compare: if True, will load saved results and compare with received during the run,
                            if False or None, results received during the run will be saved
        """
        split_params = pipeline_config.split('.')
        notebook_name = split_params[0] + '.ipynb'
        self.notebook = nbformat.read(notebook_name, nbformat.NO_CONVERT)
        self.pipeline_name = split_params[1]
        self.runner = NotebookRunner(stage_name, self.notebook, outputs, compare, self.get_context_from_notebook())

    def __repr__(self):
        return str(self.__dict__)

    def get_context_from_notebook(self):
        """Returns the dict with pipeline information from notebook"""
        md = MarkdownIt()
        for cell in self.notebook.cells:
            if cell.cell_type == 'markdown':
                parsed_cell = md.parse(cell.source)
                for token in parsed_cell:
                    token_dict = token.as_dict()
                    if token_dict['type'] == 'fence' and token_dict['tag'] == 'code' and token_dict['info'] == 'yaml':
                        if '%mldev nb_context' in token_dict['content']:
                            logger.debug(f"{self.__class__.__name__} mldev nb_context: " + str(token_dict['content']))
                            return yaml.load(token_dict['content'], Loader=yaml.SafeLoader)
        return {}

    def run(self):
        """Starts running pipeline"""
        self.runner.run_pipeline(self.pipeline_name)


class NotebookRunner:
    """
        A class that runs Jupyter notebook cells with IPython InteractiveShell.
        Reads all cells that marked with '#%mldev' comment, run them in the order given in nb_context.
        After run can save received variables or compare them to previously saved ones.

        Accepts the following parameters:

        :param stage_name: stage name
        :param notebook: Jupyter notebook parsed to dict
        :param outputs: lists files and folders that this stage produces or files from
                        which variables are taken for comparison
        :param compare: if True, will load saved results and compare with received during the run,
                        if False or None, results received during the run will be saved
        :param nb_context: dict with cells pipeline, cell dependencies and variables for save or compare
    """
    def __init__(self, stage_name, notebook, outputs, compare, nb_context):
        self.stage_name = stage_name
        self.nb_context = nb_context
        self.notebook = notebook
        self.outputs = outputs
        self.compare = compare
        self.cells = self.get_mldev_code_cells()

        self.user_ns = {}
        self.ip_shell = InteractiveShell(user_ns=self.user_ns)

    def get_mldev_code_cells(self):
        """Returns dict with all cells, marked with '#%mldev' comment"""
        cell_sources = {}
        started_block = ''
        for cell in self.notebook.cells:
            if cell.cell_type == 'code':
                if started_block:
                    cell_sources[started_block].append(cell.source)
                for line in cell.source.split('\n'):
                    cell_names = re.findall(r'#\s*%mldev\s+(\w+\s*\w+)', line)
                    if len(cell_names):
                        cell_name = cell_names[0].split()
                        logger.debug(f"{self.__class__.__name__} cell_name: " + str(cell_name))

                        if len(cell_name) == 1:
                            cell_sources[cell_name[0]] = [cell.source]
                        else:
                            if cell_name[1] == 'start':
                                started_block = cell_name[0]
                                cell_sources[started_block] = [cell.source]
                            elif cell_name[1] == 'end':
                                started_block = ''
        return cell_sources

    def get_cell_code(self, cell_name):
        """Returns code of cell with name cell_name"""
        return self.cells[cell_name]

    def run_cell_with_deps(self, cell_name):
        """Runs cells, checks if cell has dependencies and runs them first, throws exceptions"""
        if 'notebook_deps' in self.nb_context.keys():
            if cell_name in self.nb_context['notebook_deps'].keys():
                for cell in self.nb_context['notebook_deps'][cell_name].split():
                    self.run_cell_with_deps(cell)
        for code in self.get_cell_code(cell_name):
            cell_result = self.ip_shell.run_cell(code)
            if cell_result.error_in_exec is not None:
                cell_result.raise_error()

    def get_results(self):
        """Returns dict with variables from 'results' field, which received during the run"""
        saving_vars = self.nb_context['results']
        vars_dict = {}
        for var in saving_vars:
            if type(self.user_ns[var]) != Figure:
                vars_dict[var] = self.user_ns[var]
        return vars_dict

    def save_results(self):
        """Saves dict with variables to file, if var is Figure - saves it to PNG file"""
        if 'results' not in self.nb_context.keys():
            return
        os.makedirs('results', exist_ok=True)
        vars_dict = self.get_results()
        if self.outputs:
            file_to_open = self.outputs[0]
        else:
            file_to_open = './results/{}.pickle'.format(self.stage_name)
        if len(list(vars_dict.keys())) != 0:
            with open(file_to_open, mode='wb') as f:
                dill.dump(vars_dict, f)
        saving_vars = self.nb_context['results']
        for var in saving_vars:
            if type(self.user_ns[var]) == Figure:
                self.user_ns[var].savefig('./results/{}.png'.format(var))

    def compare_results(self):
        """Gets saved variables, compares them with variables received during the run"""
        if 'results' not in self.nb_context.keys():
            return
        vars_dict = self.get_results()
        if self.outputs:
            file_to_open = self.outputs[0]
        else:
            file_to_open = './results/{}.pickle'.format(self.stage_name)
        with open(file_to_open, mode='rb') as f:
            saved_results = dill.load(f)
        for key in vars_dict.keys():
            if saved_results[key] != vars_dict[key]:
                print('Variables for key {} are not equal:' +
                      '\nsaved: {} \n new: {}'.format(key, saved_results[key], vars_dict[key]))
            else:
                print('equal:', key, saved_results[key], vars_dict[key])

    def run_pipeline(self, seq_name):
        if seq_name == 'all_cells':
            for cell in self.notebook.cells:
                if cell.cell_type == 'code':
                    self.ip_shell.run_cell(cell.source)
        else:
            seq = self.nb_context[seq_name]
            for cell_name in seq:
                self.run_cell_with_deps(cell_name)
        if self.compare:
            self.compare_results()
        else:
            self.save_results()

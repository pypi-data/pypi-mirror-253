# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://gitlab.com/mlrep/mldev/-/blob/master/NOTICE.md

"""
Operations module
=================

This module is a realisation of an operation approach to merging experiment files.

See ``CollabOperations`` and ``YamlPatchCollabOperations`` classes for more documentation.

"""


from abc import ABC, abstractmethod


class CollabOperations(ABC):
    """
    This abstract base class defines the interface for operations on experiment files in the context of collaboration.

    Subclasses must implement the two abstract methods: `get_operations_delta` and `apply_operations`.
    """

    @staticmethod
    @abstractmethod
    def get_operations_delta(experiment_filepath, cur_contents, prev_contents):
        """
        Return a set of operations on the two specified versions
        of the experiment file.

        :param experiment_filepath: the experiment file path
        :param cur_contents: the contents of the current version
            of the experiment file
        :param prev_contents: the contents of the previous version
        :return: the operations (any format which can be used with `json.dumps`)
        """
        ...

    @staticmethod
    @abstractmethod
    def apply_operations(experiment_filepath, op_contents):
        """
        Return the contents of a new version of the experiment file
        after applying the `op_contents` operations.

        :param experiment_filepath: the experiment file path
        :param op_contents: operations for apply
        :return: the contents of the new version
        """
        ...


class YamlPatchCollabOperations(CollabOperations):
    """
        The `YamlPatchCollabOperations` class provides operations for merging changes in experiment specification files
        stored in YAML format. It is designed to track differences (operations) between two versions of the YAML file
        and apply those differences to update the experiment specification file. This class is specifically tailored
        for handling YAML files.

        Note:
            The `YamlPatchCollabOperations` class relies on the `ruamel.yaml` library for parsing and handling
            YAML data. Additionally, it depends on the `deepdiff` library to create and apply
            patches (sets of operations) for tracking changes in YAML files.

        Example:
            Here's an example of how to use the `YamlPatchCollabOperations` class to create and apply a patch:

            ```python
            yaml_operations = YamlPatchCollabOperations()
            cur_contents = load_current_yaml_contents()  # Load the current YAML file contents
            prev_contents = load_previous_yaml_contents()  # Load the previous YAML file contents
            op_contents = yaml_operations.get_operations_delta('experiment.yaml', cur_contents, prev_contents)

            if op_contents:
                result = yaml_operations.apply_operations('experiment.yaml', op_contents)
                if result == "conflict":
                    print("Merge conflict detected. Manual intervention required.")
            ```
    """

    @staticmethod
    def get_operations_delta(experiment_path, cur_contents, prev_contents):
        """
        Return a set of operations that represent the changes between two versions
        of the experiment specification file in YAML format.

        :param str experiment_path: The file path of the experiment file.
        :param cur_contents: The contents of the current version of the specification file.
        :param prev_contents: The contents of the previous version of the specification file.
        :return: the operations dumped from the Delta object
        """

        from deepdiff import DeepDiff, Delta
        from ruamel.yaml import YAML

        yaml = YAML()
        yaml.indent(mapping=4, sequence=4, offset=2)
        yaml.preserve_quotes = True
        delta = Delta(
            DeepDiff(
                yaml.load(prev_contents),
                yaml.load(cur_contents),
                ignore_order=True,
                report_repetition=True,
            ),
            verify_symmetry=True,
        )
        return delta.dumps()

    @staticmethod
    def apply_operations(experiment_filepath, op_contents):
        """
        Apply a set of operations on the experiment file and write the contents.

        :param experiment_filepath: The file path of the experiment specification file to be updated.
        :param op_contents: The operations to apply.
        :raises ForbiddenModule: If the applied operations contain changes to forbidden modules,
            this exception will be raised.
        :raises Exception: If there is a merge conflict while applying the operations,
            this exception will be raised.
        """

        from deepdiff.delta import Delta, DeltaError
        from deepdiff.serialization import ForbiddenModule
        from ruamel.yaml import YAML

        with open(experiment_filepath, "r") as f:
            yaml = YAML()
            yaml.indent(mapping=4, sequence=4, offset=2)
            yaml.preserve_quotes = True
            experiment = yaml.load(f)

        safe_to_import = {
            "ruamel.yaml.anchor.Anchor",
            "ruamel.yaml.comments.Comment",
            "ruamel.yaml.comments.CommentedMap",
            "ruamel.yaml.comments.CommentedSeq",
            "ruamel.yaml.comments.Format",
            "ruamel.yaml.comments.LineCol",
            "ruamel.yaml.comments.Tag",
            "ruamel.yaml.comments.TaggedScalar",
            "ruamel.yaml.error.FileMark",
            "ruamel.yaml.scalarstring.DoubleQuotedScalarString",
            "ruamel.yaml.scalarstring.FoldedScalarString",
            "ruamel.yaml.scalarstring.LiteralScalarString",
            "ruamel.yaml.scalarstring.PlainScalarString",
            "ruamel.yaml.tag.Tag",
            "ruamel.yaml.tokens.CommentToken",
        }
        try:
            delta = Delta(
                diff=op_contents,
                safe_to_import=safe_to_import,
                raise_errors=True,
            )
            new_experiment = experiment + delta
        except ForbiddenModule:
            # You need to explicitly pass some module into a safe_to_import
            raise
        except DeltaError:
            # There is a merge conflict.
            return "conflict"

        with open(experiment_filepath, "w") as f:
            YAML().dump(new_experiment, f)

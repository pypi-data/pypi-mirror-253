import pytest
import shlex
import shutil
import subprocess
import tempfile

from git import Repo, config as git_config
from pathlib import Path


class TempMLDevTemplate:
    """
    Creates a temporary MLDev template.
    """
    def __init__(self, clone=None, experiment_file=True, config_file=True):
        tempdir = Path(tempfile.mkdtemp())
        self.path = tempdir
        if git_config.GitConfigParser().get_value(section='user', option='name', default='') == '':
            self.run('git config --global user.name "Test Test"')
        if git_config.GitConfigParser().get_value(section='user', option='email', default='') == '':
            self.run('git config --global user.email "test@test.com"')
        if clone:
            self.run(f'git clone {clone} template')
            self.run('echo "" | mldev init template -p collab', shell=True)
        else:
            self._mldev_init()
        self.path = self.path / 'template'
        if config_file:
            self._add_config_file()
        self.path = tempdir
        self.run('echo "" | mldev init template -p collab', shell=True)
        self.path = self.path / 'template'
        if experiment_file:
            self._add_experiment_file()
        self.path = tempdir
        self.run('cp -R template template_base')
        self.path = self.path / 'template'
        self.repo = Repo(self.path)

    def run(self, cmd, **kwargs):
        """
        Run a command in the temporary MLDev template.
        """
        if isinstance(cmd, str) and not kwargs.get('shell'):
            cmd = shlex.split(cmd)
        p = subprocess.Popen(cmd, cwd=self.path, **kwargs)
        (out, _) = p.communicate()
        if p.returncode != 0:
            err = subprocess.CalledProcessError(p.returncode, cmd)
            err.output = out
            raise err
        return out

    def _mldev_init(self):
        self.run('echo "" | mldev init template', shell=True)

    def _add_experiment_file(self):
        self.run('rm experiment.yml experiment-basic.yml')
        self.run('git rm experiment.yml experiment-basic.yml')
        file = self.path / 'experiment.yml'
        file.write_text(BASE_EXPERIMENT_FILE_CONTENT)
        self.run('git add .')
        self.run("git commit -m 'Change experiment files.'")
        self.run("mldev collab add experiment.yml")

    def _add_config_file(self):
        self.run('rm .mldev/config.yaml')
        config_path = Path(__file__).parent.resolve() / f'data/collab/config.yaml'
        self.run(f'cp {config_path} .mldev/config.yaml')
        self.run('git add .')
        try:
            self.run("git commit -m 'Change the logging level'", shell=True)
        except subprocess.CalledProcessError:
            # maybe there's nothing to commit
            ...

    def _set_log_level(self, level='DEBUG'):
        self.run(f"sed \'s/level: \"INFO\"/level: \"{level}\"/g\' .mldev/config.yaml > .mldev/config_new.yaml",
                 shell=True)
        self.run('rm .mldev/config.yaml')
        self.run('mv .mldev/config_new.yaml .mldev/config.yaml')
        self.run('git add .')
        try:
            self.run("git commit -m 'Change the logging level'", shell=True)
        except subprocess.CalledProcessError:
            # maybe there's nothing to commit
            ...

    def restore(self):
        """
        Restore the original version of the temporary MLDev template.
        """
        self.path = self.path.resolve().parents[0]
        self.run("rm -rf template")
        self.run("cp -R template_base template")
        self.path = self.path / 'template'

    def cleanup(self):
        """
        Remove all artifacts.
        """
        shutil.rmtree(self.path.resolve().parents[0], ignore_errors=True)


@pytest.fixture(scope="module")
def temp_repo():
    r = TempMLDevTemplate()
    yield r
    r.cleanup()


@pytest.fixture(autouse=True)
def cleanup(temp_repo):
    yield
    temp_repo.restore()


class TempMLDevTemplatePartialInit(TempMLDevTemplate):
    """
    Creates a temporary MLDev template with partial initialization.
    """
    def _mldev_init(self):
        self.run('echo "" | mldev init template -p template', shell=True)
        self.run('echo "" | mldev init template -p git', shell=True)
        self.run('echo "" | mldev init template -p collab', shell=True)


@pytest.fixture
def temp_repo_partial_init():
    r = TempMLDevTemplatePartialInit()
    yield r
    r.cleanup()


BASE_EXPERIMENT_FILE_CONTENT = """# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://gitlab.com/mlrep/mldev/-/blob/master/NOTICE.md

random_seed: 47

pipeline: !GenericPipeline
  runs:
    - !BasicStage
      name: simple-stage1
"""


@pytest.fixture
def merged_file():
    return """# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://gitlab.com/mlrep/mldev/-/blob/master/NOTICE.md

random_seed: 47

pipeline: !GenericPipeline
  runs:
  - !BasicStage
    name: simple-stage1
  - !BasicStage
    name: simple-stage2
  - !BasicStage
    name: simple-stage-master
"""


@pytest.fixture
def temp_repo_no_collab():
    r = TempMLDevTemplate(experiment_file=False, config_file=False)
    yield r
    r.cleanup()


def test_no_init(temp_repo_no_collab):
    folder = temp_repo_no_collab.path / '.mldev/collab'
    assert folder.exists() is False


def test_init(temp_repo):
    from mldev_collab.collab import is_tracked

    assert is_tracked('experiment.yml', path=temp_repo.path) is True


def test_partial_init(temp_repo_partial_init):
    from mldev_collab.collab import is_tracked

    assert is_tracked('experiment.yml', path=temp_repo_partial_init.path) is True


@pytest.mark.parametrize(
    "answer, expected", [
        ("yes", False), # disable prompt in collab beta
        ("no", False),
    ])
def test_run_untracked_file(temp_repo, answer, expected):
    from mldev_collab.collab import is_tracked

    file = temp_repo.path / 'new_untracked_experiment.yml'
    assert file.exists() is False
    assert is_tracked('new_untracked_experiment.yml', path=temp_repo.path) is False
    file.write_text('')
    temp_repo.run('git add new_untracked_experiment.yml')
    temp_repo.run("git commit -m 'Add the new_untracked_experiment.yml file.'")
    out = temp_repo.run(f'echo "{answer}" | mldev run -f new_untracked_experiment.yml', shell=True)
    if out:
        assert "Do you want to add" not in out.read(), "MLDev should not ask for tracking experiment file yet"
    assert is_tracked('new_untracked_experiment.yml', path=temp_repo.path) is expected


def test_merge_untracked_file(temp_repo):
    temp_repo.run('cp experiment.yml untracked_experiment.yml')
    temp_repo.run('git add .')
    temp_repo.run("git commit -m 'Add the untracked file.'")

    temp_repo.run('git checkout -b branch')
    temp_repo.run("echo '    - !BasicStage\n      name: simple-stage2' >> untracked_experiment.yml", shell=True)
    temp_repo.run('git add .')
    temp_repo.run("git commit -m 'Add stage #2.'")

    temp_repo.run('git checkout master')
    temp_repo.run("echo '    - !BasicStage\n      name: simple-stage-master' >> untracked_experiment.yml", shell=True)
    temp_repo.run('git add .')
    temp_repo.run("git commit -m 'Add stage #MASTER'")
    with pytest.raises(subprocess.CalledProcessError) as err:
        temp_repo.run("git merge branch --no-edit")
        assert err.output is not None
        assert 'Automatic merge failed' in err.output


def test_untracked_file_no_operations_created(temp_repo):
    temp_repo.run('cp experiment.yml untracked_experiment.yml')
    temp_repo.run('git add .')
    temp_repo.run("git commit -m 'Add the untracked file.'")

    from mldev_collab.collab import MLDEV_OPERATIONS_PATH
    ops = set((Path(temp_repo.path) / MLDEV_OPERATIONS_PATH).iterdir())
    temp_repo.run("echo '    - !BasicStage\n      name: simple-stage2' >> untracked_experiment.yml", shell=True)
    temp_repo.run('git add .')
    temp_repo.run("git commit -m 'Add stage #2.'")
    assert ops == set((Path(temp_repo.path) / MLDEV_OPERATIONS_PATH).iterdir())


def test_merge_tracked_file(temp_repo, merged_file):
    temp_repo.run('git checkout -b branch')
    temp_repo.run("echo '    - !BasicStage\n      name: simple-stage2' >> experiment.yml", shell=True)
    temp_repo.run('git add .')
    temp_repo.run("git commit -m 'Add stage #2.'")

    temp_repo.run('git checkout master')
    temp_repo.run("echo '    - !BasicStage\n      name: simple-stage-master' >> experiment.yml", shell=True)
    temp_repo.run('git add .')
    temp_repo.run("git commit -m 'Add stage #MASTER'")
    res = temp_repo.run("git merge branch --no-edit")
    assert res is None or 'Automatic merge failed' not in res

    file = temp_repo.path / 'experiment.yml'
    assert file.exists() is True
    content = file.read_text()
    assert content == merged_file


def test_branch_rename_tracked_file_with_changes(temp_repo, merged_file):
    temp_repo.run('git checkout -b branch')
    temp_repo.run('git mv experiment.yml experiment2.yml')
    temp_repo.run("echo '    - !BasicStage\n      name: simple-stage2' >> experiment2.yml", shell=True)
    temp_repo.run('git add .')
    temp_repo.run("git commit -m 'Add stage #2; rename experiment.yml -> experiment2.yml'")

    temp_repo.run('git checkout master')
    temp_repo.run("echo '    - !BasicStage\n      name: simple-stage-master' >> experiment.yml", shell=True)
    temp_repo.run('git add .')
    temp_repo.run("git commit -m 'Add stage #MASTER'")
    res = temp_repo.run("git merge branch --no-edit")
    assert res is None or 'Automatic merge failed' not in res

    file = temp_repo.path / 'experiment.yml'
    assert file.exists() is False
    file = temp_repo.path / 'experiment2.yml'
    assert file.exists() is True
    content = file.read_text()
    assert content == merged_file


def test_master_rename_tracked_file_with_changes(temp_repo, merged_file):
    temp_repo.run('git checkout -b branch')
    temp_repo.run("echo '    - !BasicStage\n      name: simple-stage2' >> experiment.yml", shell=True)
    temp_repo.run('git add .')
    temp_repo.run("git commit -m 'Add stage #2.'")

    temp_repo.run('git checkout master')
    temp_repo.run("echo '    - !BasicStage\n      name: simple-stage-master' >> experiment.yml", shell=True)
    temp_repo.run('git mv experiment.yml experiment2.yml')
    temp_repo.run('git add .')
    temp_repo.run("git commit -m 'Add stage #MASTER; rename experiment.yml -> experiment2.yml'")
    res = temp_repo.run("git merge branch --no-edit")
    assert res is None or 'Automatic merge failed' not in res

    file = temp_repo.path / 'experiment.yml'
    assert file.exists() is False
    file = temp_repo.path / 'experiment2.yml'
    assert file.exists() is True
    content = file.read_text()
    assert content == merged_file


def test_branch_rename_tracked_file_without_changes(temp_repo):
    # Fast-forward without using the merge driver
    temp_repo.run('git checkout -b branch')
    temp_repo.run('git mv experiment.yml experiment2.yml')
    temp_repo.run('git add .')
    temp_repo.run("git commit -m 'Rename experiment.yml -> experiment2.yml'")

    temp_repo.run('git checkout master')
    res = temp_repo.run("git merge branch --no-edit")
    assert res is None or 'Automatic merge failed' not in res

    file = temp_repo.path / 'experiment.yml'
    assert file.exists() is False
    file = temp_repo.path / 'experiment2.yml'
    assert file.exists() is True


def test_add_new_untracked_file_while_renaming_experiment(temp_repo):
    temp_repo.run('git checkout -b branch')
    file = temp_repo.path / 'dummy'
    file.write_text('dummy')
    temp_repo.run('git add .')
    temp_repo.run("git commit -m 'Dummy commit.'")

    temp_repo.run('git checkout master')
    temp_repo.run('git mv experiment.yml experiment2.yml')
    temp_repo.run('git add .')
    temp_repo.run("git commit -m 'Rename experiment.yml -> experiment2.yml'")
    res = temp_repo.run("git merge branch --no-edit")
    assert res is None or 'Automatic merge failed' not in res

    file = temp_repo.path / 'experiment.yml'
    assert file.exists() is False
    file = temp_repo.path / 'experiment2.yml'
    assert file.exists() is True


def test_rename_rename_merge_conflict(temp_repo):
    temp_repo.run('git checkout -b branch')
    temp_repo.run("echo '    - !BasicStage\n      name: simple-stage2' >> experiment.yml", shell=True)
    temp_repo.run('git mv experiment.yml experiment_branch.yml')
    temp_repo.run('git add .')
    temp_repo.run("git commit -m 'Add stage #2.'")

    temp_repo.run('git checkout master')
    temp_repo.run("echo '    - !BasicStage\n      name: simple-stage-master' >> experiment.yml", shell=True)
    temp_repo.run('git mv experiment.yml experiment_master.yml')
    temp_repo.run('git add .')
    temp_repo.run("git commit -m 'Add stage #MASTER.'")

    with pytest.raises(subprocess.CalledProcessError) as err:
        temp_repo.run("git merge branch --no-edit")
        assert err.output is not None
        assert 'Automatic merge failed' in err.output
        assert 'CONFLICT (rename/rename)' in err.output

    file = temp_repo.path / 'experiment.yml'
    assert file.exists() is False
    file = temp_repo.path / 'experiment_branch.yml'
    assert file.exists() is True
    file = temp_repo.path / 'experiment_master.yml'
    assert file.exists() is True


def test_tracked_set(temp_repo):
    import base64
    from mldev_collab.collab import MLDEV_TRACKED_PATH, _tracked_set

    def encode_filename(f):
        return base64.b16encode(f.encode('utf-8')).decode('utf-8')

    def add_rename_event(original_filename, i, new_filename=None):
        fn = f"{encode_filename(original_filename)}_{temp_repo.repo.head.object}_{i}_salt"
        f = temp_repo.path / MLDEV_TRACKED_PATH / fn
        if new_filename:
            f.write_text(new_filename)
        else:
            assert i == 1
            f.write_text(original_filename)
        temp_repo.run("git add .")
        temp_repo.run(f"git commit -m 'Rename {original_filename} -> {new_filename} (#{i}).'")

    def add_delete_event(original_filename, i):
        fn = f"{encode_filename(original_filename)}_{temp_repo.repo.head.object}_{i}_salt"
        f = temp_repo.path / MLDEV_TRACKED_PATH / fn
        f.write_text('/deleted')
        temp_repo.run("git add .")
        temp_repo.run(f"git commit -m 'Delete {original_filename} (#{i}).'")

    add_rename_event('experiment_a.yml', 1)
    add_rename_event('experiment_a.yml', 2, 'experiment_a_new2.yml')
    add_rename_event('experiment_a.yml', 3, 'experiment_a_new3.yml')
    add_rename_event('experiment_a.yml', 4, 'experiment_a_new4.yml')
    add_rename_event('experiment_a.yml', 5, 'experiment_a_new5.yml')

    add_rename_event('experiment_b.yml', 1)
    add_rename_event('experiment_b.yml', 2, 'experiment_b_new2.yml')

    add_rename_event('experiment_c.yml', 1)

    add_rename_event('experiment_d.yml', 1)
    add_rename_event('experiment_d.yml', 2, 'experiment_d_new2.yml')
    add_delete_event('experiment_d.yml', 3)

    assert {
        'experiment.yml': ('experiment.yml', 1),
        'experiment_a_new5.yml': ('experiment_a.yml', 5),
        'experiment_b_new2.yml': ('experiment_b.yml', 2),
        'experiment_c.yml': ('experiment_c.yml', 1),
    } == _tracked_set(temp_repo.repo.head.object)


def test_is_tracked(temp_repo):
    def add_file(filename):
        f = temp_repo.path / filename
        f.write_text(f"dummy {filename}")
        temp_repo.run("git add .")
        temp_repo.run(f"git commit -m 'Add file {filename}.'")

    def rename_file(filename_from, filename_to):
        temp_repo.run(f"git mv {filename_from} {filename_to}")
        temp_repo.run("git add .")
        temp_repo.run(f"git commit -m 'Rename {filename_from} -> {filename_to}'")

    for i in range(5):
        add_file(f"dummy{i}")
    add_file("experiment_tracked.yml")
    for i in range(10, 15):
        add_file(f"dummy{i}")
    rename_file("experiment_tracked.yml", "experiment_tracked_new.yml")
    for i in range(20, 25):
        add_file(f"dummy{i}")
    temp_repo.run("mldev collab add experiment_tracked_new.yml")

    f = temp_repo.path / "experiment_tracked_new.yml"
    f.write_text(f"This is the new content")
    temp_repo.run("git add .")
    temp_repo.run(f"git commit -m 'Change the experiment_tracked_new.yml content'")

    for i in range(30, 35):
        add_file(f"dummy{i}")
    rename_file("experiment_tracked_new.yml", "experiment_tracked_new2.yml")
    for i in range(40, 45):
        add_file(f"dummy{i}")
    rename_file("experiment_tracked_new2.yml", "experiment_tracked_new3.yml")
    for i in range(50, 55):
        add_file(f"dummy{i}")

    from mldev_collab.collab import is_tracked
    assert is_tracked('experiment_tracked.yml', temp_repo.path) is False
    assert is_tracked('experiment_tracked_new.yml', temp_repo.path) is False
    assert is_tracked('experiment_tracked_new2.yml', temp_repo.path) is False
    assert is_tracked('experiment_tracked_new3.yml', temp_repo.path) is True
    assert is_tracked('experiment_tracked_new_absent.yml', temp_repo.path) is False


@pytest.fixture
def multiple_temp_repos():
    base_template = TempMLDevTemplate(experiment_file=False)
    # setup base template
    base_template.run('rm experiment.yml')
    base_template.run('git rm experiment.yml')
    file = base_template.path / 'experiment.yml'
    file.write_text(
        (Path(__file__).parent.resolve() / 'data/collab/experiment.yml').read_text()
    )
    base_template.run('git add .')
    base_template.run("git commit -m 'Change experiment files.'")
    base_template.run("mldev collab add experiment.yml")

    researchers_count = 10
    templates = []
    for r in range(1, researchers_count + 1):
        template = TempMLDevTemplate(clone=base_template.path, experiment_file=False)
        templates.append(template)

    yield base_template, templates

    # cleanup
    base_template.cleanup()
    for template in templates:
        template.cleanup()


def test_multiple_researchers(multiple_temp_repos):
    base_template, templates = multiple_temp_repos
    for i, template in enumerate(templates):
        template.run(f"git checkout -b work_branch_researcher{i+1}")
        file = template.path / 'experiment.yml'
        file.write_text(
            (Path(__file__).parent.resolve() / f'data/collab/experiment_researcher{i+1}.yml').read_text()
        )
        template.run("git add .")
        template.run(f"git commit -m 'Modified experiment.yml by researcher{i+1}'")
        template.run(f"git push --set-upstream origin work_branch_researcher{i+1}")

    for i, template in enumerate(templates):
        base_template.run(f'git merge work_branch_researcher{i+1} --no-edit')

    for template in templates:
        template.run('git checkout master')
        template.run('git pull origin master')

    file = base_template.path / 'experiment.yml'
    content = file.read_text()
    for i in range(len(templates)):
        assert f'researcher{i+1}_' in content

    for template in templates:
        file = template.path / 'experiment.yml'
        content = file.read_text()
        for i in range(len(templates)):
            assert f'researcher{i+1}_' in content

# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://gitlab.com/mlrep/mldev/-/blob/master/NOTICE.md

import sh

from mldev.experiment import *
from mldev.utils import *

@experiment_tag()
class ModelControllerService(MonitoringService):
    """
    This service implements a simple `flask` REST web service to run your sklearn model

    Note: it uses `pickle` to deserialize model classes, therefore restrictions apply.
    Currently early-stage

    See example experiment.yml for parameters
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.temp_dir = os.path.join(self.temp_dir, 'controller')
        os.makedirs(self.temp_dir, exist_ok=True)

    def __call__(self, *args, **kwargs):
        logger.debug(f"Running python3 {self.config_dir}"
                     f"/mldev_controller/flaskModelController.py")
        sh.Command("python3")(f"{self.config_dir}"
                              f"/mldev_controller/flaskModelController.py", self.port,
                              self.params.get("model_path"),
                              _err=f"{self.logs_dir}/{self.name}Log.txt",
                              _out=f"{self.logs_dir}/{self.name}Log.txt",
                              _bg=True)

    def prepare(self, service_name):
        self.port = str(self.params.get("port", "8090"))
        proc = exec_command(f"lsof -i :{self.port} || true", capture=True) # ok to fail - means no service is running
        lines = proc.stdout.splitlines()

        pid = ""
        for line in lines:
            fields = line.split()
            if fields[0] == 'python' or fields[0] == "python3":
                pid += " " + fields[1]

        if len(pid.split()) > 1:
            os.kill(int(pid.split()[1]), signal.SIGKILL)

# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://gitlab.com/mlrep/mldev/-/blob/master/NOTICE.md

import sh

from mldev.experiment import *
from mldev.utils import *

@experiment_tag()
class TensorBoardService(MonitoringService):
    """
    This service starts Tensorboard webapp to provide access to the current state
    of the experiment if the experiment code writes any data to tensorboard

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.temp_dir = os.path.join(self.temp_dir, 'tensorboard')
        os.makedirs(self.temp_dir, exist_ok=True)

    def __call__(self, *args, **kwargs):
        sh.tensorboard(f"--logdir={self.params.get('logdir')}",
                       f"--port={self.params.get('port')}",
                       _err=f"{self.logs_dir}/{self.name}Log.txt", _bg=True)

    def prepare(self, service_name):
        try:
            check_kill_process("tensorboard")
        except sh.SignalException:
            pass
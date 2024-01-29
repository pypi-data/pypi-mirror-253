# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://gitlab.com/mlrep/mldev/-/blob/master/NOTICE.md

import sh

from mldev.experiment import *
from mldev import *
import os

@experiment_tag()
class NotificationBot(MonitoringService):
    """
    Starts a Telegram bot that notifies you then something happens with the runnning experiment

    Note: you will beed to provide a valid `TELEGRAM_TOKEN` in mldev config (.mldev/config.yaml)
    or as an environmental variable

    See example experiment.yml for parameters
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.temp_dir = os.path.join(self.temp_dir, 'bot')
        os.makedirs(self.temp_dir, exist_ok=True)

    def __call__(self, *args, **kwargs):
        # todo kill bot
        try:
            sh.python3(f"{self.config_dir}/mldev_bot/app.py",
                       str(self.params.get("token")), str(self.params.get("warnings")),
                       _err=f"{self.logs_dir}/{self.name}Log.txt",
                       _out=f"{self.logs_dir}/{self.name}Log.txt",
                       _bg=True)
        except sh.ErrorReturnCode as ex:
            logger.error("check your notification bot config (token, port)", ex)

    def prepare(self, service_name):
        pass

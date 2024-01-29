# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://gitlab.com/mlrep/mldev/-/blob/master/NOTICE.md

import os
import json

this_folder = os.path.dirname(os.path.abspath(__file__))
constants_filename = os.path.join(this_folder, 'config.json')
with open(constants_filename, "r") as data_file:
	proxies = json.load(data_file).get('proxies')

current_proxy = proxies.get('frankfurt')

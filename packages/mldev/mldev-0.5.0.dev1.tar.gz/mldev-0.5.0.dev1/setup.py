# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://gitlab.com/mlrep/mldev/-/blob/master/NOTICE.md

from setuptools import setup
from itertools import chain
from src.mldev.version import __version__


packages = ["mldev", "mldev_bot", "mldev_controller", "mldev_tensorboard",
            "mldev_config_parser", 'mldev_dvc', 'mldev_jupyter', 'mldev_collab']
requirements = {}
extras_require = {}
install_requires = []
try:
    for p in packages:
        requirements[p] = list()
        with open(f"./src/{p}/requirements.txt", 'r') as f:
            for l in f.readlines():
                l = l.split('#')[0].strip()
                if len(l) > 0:
                    requirements[p].append(l)

    EXTRAS_BASE = list(chain(requirements['mldev'], requirements['mldev_config_parser']))
    install_requires = EXTRAS_BASE
    extras_require = {
        'base': EXTRAS_BASE,
        'dvc': list(chain(EXTRAS_BASE, requirements.get('mldev_dvc', []))),
        'jupyter': list(chain(EXTRAS_BASE, requirements.get('mldev_jupyter', []))),
        'tensorboard': list(chain(EXTRAS_BASE, requirements.get('mldev_tensorboard', []))),
        'controller': list(chain(EXTRAS_BASE, requirements.get('mldev_controller', []))),
        'bot': list(chain(EXTRAS_BASE, requirements.get('mldev_bot', []))),
        'collab': list(chain(EXTRAS_BASE, requirements.get('mldev_collab', []))),
    }
    extras_require['all'] = list(set(chain(*extras_require.values())))

except OSError:
    # check if there is EGG_INFO then load from there
    # will happen if installing from source tar
    from pkg_resources import Distribution, PathMetadata

    dist = Distribution(metadata=PathMetadata('.', './src/mldev.egg-info'))
    install_requires = [str(s) for s in dist.requires()]
    for extra in dist.extras:
        extras_require[extra] = [str(s) for s in dist.requires([extra])]

# todo extract this from README.md
long_description = """
MLDev software
==============

This repository contains the MLDev software, that facilitates running data science experiments, 
help in results presentation and eases paper preparation for students, data scientists and researchers.

The MLDev software provides the following features to help with automating machine learning experiments:


* Configure stages and parameters of a data science experiment separately from your code
* Conduct a repeatable experiment in Google Colab or PaperSpace
* Keep versions of your code, results and intermediate files on Google Drive (other repos coming soon)
* Use a variety of pre-built templates to get started

MLDev also provides some services that run alongside your experiment code:
You can have the notifications via Telegram about the exeptions while training your model


* Keep updated on current experiment state using TensorBoard (even on Colab)
* Deploy and demo your model with a model controller (feature in progress) 

Install mldev
=============

MLDev comes with a couple of extensions (extras), see the homepage for details. 

- base
- dvc
- tensorboard
- controller
- bot
- jupyter
- collab

Install using ``install_mldev.sh`` script
-----------------------------------------

Get the latest version of our install file to your local machine and run it.

``$ curl https://gitlab.com/mlrep/mldev/-/raw/develop/install_mldev.sh -o install_mldev.sh`` 

``$ chmod +x ./install_mldev.sh``

``$ ./install_mldev.sh``

You may be asked for ``root`` privileges if there are system packages to be installed.

Wait a couple of minutes until installation will complete, congrats!


Install from PyPI
-----------------

Use ``pip`` to install MLDev package from PyPI. This will not install any system dependencies.

Useful for including MLDev into ``requirements.txt`` in your experiments.

``$ python3 -m pip install mldev[base]``



Contacts
========

You can reach developers at the `Telegram user group <https://t.me/mldev_betatest>`_

Homepage https://gitlab.com/mlrep/mldev

See the project page at the Open Data Science website https://ods.ai/projects/mldev

License
=======

The software is licensed under Apache 2.0 license
"""

setup(
    name='mldev',
    version=__version__,
    url='https://gitlab.com/mlrep/mldev.git',
    author='MLREP team',
    author_email='dev@mlrep.org',
    description='mldev is a tool for running reproducible experiments',
    license='Apache 2.0 license',
    long_description=long_description,
    package_dir={'': 'src'},
    packages=packages,
    entry_points={
        # Install a script as "mldev".
        'console_scripts': [
            'mldev = mldev.main:do_main'
        ],
    },
    setup_requires=["wheel","future"],
    install_requires=install_requires,
    extras_require=extras_require,
    package_data={
        "": ["LICENSE", "NOTICE.md", "README.md"],
        "mldev_config_parser": ["requirements.txt"],
        "mldev":
         ["init_template.sh",
          "init_venv.sh",
          "init_git.sh",
          "init_lfs.sh",
          "ngrok_urls.sh",
          "install_ngrok.sh",
          "setenv.sh"],
        "mldev_dvc":["init_dvc.sh"],
        "mldev_bot":
         ["requirements.txt",
         "config.json"],
        "mldev_controller":
         ["requirements.txt"],
        "mldev_jupyter":
         ["requirements.txt"],
        "mldev_tensorboard":
         ["requirements.txt"],
        "mldev_collab":
         ["init_collab.sh",
          "requirements.txt"],
    },
    keywords="data-science developer-tools reproducibility collaboration ai",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)

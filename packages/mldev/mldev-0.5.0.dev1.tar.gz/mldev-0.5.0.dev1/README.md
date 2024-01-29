# MLDev software

This repository contains the MLDev software, that facilitates running data science experiments, 
help in results presentation and eases paper preparation for students, data scientists and researchers.

The MLDev software provides the following features to help with automating machine learning experiments:
 - Configure stages and parameters of a data science experiment separately from your code
 - Conduct a repeatable experiment in Google Colab or PaperSpace
 - Keep versions of your code, results and intermediate files on Google Drive (other repos coming soon)
 - Use a variety of pre-built templates to get started: see [template-default](../../../../template-default) and [template-intelligent-systems](../../../../template-intelligent-systems)
 - [Run Jupyter notebooks](../../wikis/mldev-user-guide#jupyter-integration) as part of the pipeline
 

MLDev also provides some services that run alongside your experiment code:
You can have the notifications via Telegram about the exeptions while training your model
 - Keep updated on current experiment state using TensorBoard (even on Colab)
 - Deploy and demo your model with a model controller (feature in progress) 

# Quick setup

The preferred way to use ``mldev`` is inside a [Docker container](https://docker.com). 
The following instructions have been tested for ``ubuntu:18.04`` and ``ubuntu:20.04`` images.

Get the latest version of our install file to your local machine and run it. This will install a full version of ``mldev`` (may require up to 500Mb of storage space with dependencies, see also minimal version below).

```shell script
$ curl https://gitlab.com/mlrep/mldev/-/raw/develop/install_mldev.sh -o install_mldev.sh 
$ chmod +x ./install_mldev.sh
$ ./install_mldev.sh   # answer 'N' if running outside container
```

Replace the last line with the following to install only the minimal (base) version of ``mldev`` (may take up to 1Mb of storage space).

```shell script
$ ./install_mldev.sh base
```

You may be asked for ``root`` privileges if there are [system packages to be installed](../../wikis/mldev-user-guide#install-system-packages). You may prefer to answer ```N``` to a prompt to install system libraries if you install ``mldev`` outside a container.


If your system does not have ``curl`` installed, you may use ``wget`` or install it yourself

```shell script
$ sudo apt-get update && sudo apt-get install curl
```

Wait a couple of minutes until installation will be done and then you are almost ready to use ``mldev``, congrats!

Then get the default minimal experiment [``template-default``](../../../../template-default) or try [``template-full``](../../../../template-full) (may take up to 500Mb of storage space)

```shell script
$ mldev init <new_folder>
```

Answer the questions the setup wizard asks or skip where possible.

Then run the default pipeline of the experiment

```shell script
$ cd <new_folder>
$ mldev run
```

# Install using pip

Alternatively, you may install ``mldev`` using ``pip``. Since version ``0.4.0.dev2``, ``mldev`` is available on PyPI.

```shell script
$ pip install mldev[base] 
```

This can be useful when installing ``mldev`` within experiments or when adding ``mldev`` to ``requirements.txt``. 


# Documentation and tutorials

User and developer documentation is available here 

http://mlrep.gitlab.io/mldev/


## Tutorial

A [Quick start tutorial](../../wikis/mldev-tutorial-basic) to get familiar with MLDev is available [here](../../wikis/mldev-tutorial-basic)

## User Guide

A [User guide](../../wikis/mldev-user-guide) is available on the project wiki [here](../../wikis/mldev-user-guide).
    
## Contributing

Please check the [CONTRIBUTING.md](CONTRIBUTIONG.md) guide if you'd like to participate in the project, ask a question or give a suggestion.

# Project partners and supporters

### Partners and endorsers

<p>
<a href="http://m1p.org"><img src="../../wikis/images/m1p_logo.png" alt="My First Scientific Paper" height="80px"></a>
<a href="http://fpmi.tilda.ws/algo-tech/"><img src="../../wikis/images/atp-mipt.jpg" alt="ATP MIPT" height="80px"></a>
<a href="http://www.machinelearning.ru"><img src="http://www.machinelearning.ru/wiki/logo.png" alt="MachineLearning.ru" height="120px"/></a>
</p>

### GitLab open source

<p>
<a href="https://about.gitlab.com/solutions/open-source/"><img src="../../wikis/images/gitlab-logo-gray-stacked-rgb.png" alt="GitLab Open Source program" height="80px"></a>
</p> 

### Initial support provided by

<p>
<a href="https://fund.mipt.ru"><img height="50px" src="../../wikis/images/fund-logo.svg" alt="MIPT Fund"/></a>
<a href="https://mipt.ru/education/departments/fpmi/"><img src="https://mipt.ru/docs/download.php?code=logotip_fpmi_2019" height="100px" alt="FPMI"/></a>
<a href="https://mipt.ru"><img src="https://mipt.ru/docs/download.php?code=mipt_eng_base_png" alt="MIPT" height="100px"/></a>
</p>

# Contacts 

You can reach developers at the [Telegram user group](https://t.me/mldev_betatest) or at the [#mlrep](https://opendatascience.slack.com) channel at OpenDataScience.

# Citing

If you would like, please cite MLDev as following

```
@InProceedings{10.1007/978-3-031-12285-9_1,
 author="Khritankov, Anton and Pershin, Nikita and Ukhov, Nikita and Ukhov, Artem",
 editor="Pozanenko, Alexei and Stupnikov, Sergey and Thalheim, Bernhard and Mendez, Eva and Kiselyova, Nadezhda",
 title="MLDev: Data Science Experiment Automation and Reproducibility Software",
 booktitle="Data Analytics and Management in Data Intensive Domains",
 year="2022",
 publisher="Springer International Publishing",
 address="Cham",
 pages="3--18",
 isbn="978-3-031-12285-9"
}
```

# License

The software is licensed under [Apache 2.0 license](LICENSE)

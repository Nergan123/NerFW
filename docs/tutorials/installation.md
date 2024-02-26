# Installing Python and NerFW


## Installing Python

Before you start using NerFW, you need to have Python 3.10 or higher installed on your computer.
You can download Python from the [official website](https://www.python.org/downloads/).
Or you can install it with [conda](https://www.anaconda.com/download).

### If you have installed Conda

Open conda command prompt and run the following command to create a new python environment.
Environment is a separate python installation, which allows you to have different 
versions of python and different packages installed in different environments.

```bash
conda create -n YourEnvironmentName python=3.10
```
Use any name instead of *YourEnvironmentName*.

Then activate the environment

```bash
conda activate YourEnvironmentName
```

### If you have installed Python from the official website

Use the following command to create a new environment. Open your console and run the following command.

```bash
python -m venv YourEnvironmentName
```

To activate the environment run the following command

```bash
source YourEnvironmentName/bin/activate
```


## After you have installed Python.

You can install the framework using pip. Run the following in your console

```bash
pip install nerfw
```

## Useful links

- [Installing python and Venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
- [Installing python with conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
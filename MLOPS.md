MLOPS
==============================

# Project initialization

## Poetry

In this project we are going to use poetry dependency management packing.

### Step 1 : Install poetry on your system
* Poetry documentation
osx / linux / bashonwindows install instructions

```shell
$ pip3 install poetry
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

```
windows powershell install instructions

```shell
$ (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -


```

### Step 2 : Set the path of your environment

```shell
$ source $HOME/.poetry/env

```

### Step 3 : colone repository

```shell
$ git clone  repo..
```

### Step 4 : Activate  poetry environment

```shell
$ cd repo
$ poetry shell

```

### Step 5 : Install all poetry dependencies

```shell
$ poetry install
```

### Some features of poetry


1. Install package view poetry

```shell
# point python module to python script for make it packag

[tool.poetry.scripts]
calc-simp = "python_lifecycle(travel from pyproject.toml).calculator.simple(module name):main"
calc-complex = "python_lifecycle.calculator.complex:main"

$ poetry install

$ modulename parameters (parameters are receive by command line intrepreater fire,sys.argv[]... )


```

## Virtual environment(requirements.txt)

```shell
python3 -m venv venv
source venv/bin/activate
pip3 freeze > requirements.txt
pip3 install requirements.txt
```

## Git initialize

1. Set github credential
```shell
$ git config --global user.name "Madan Baduwal"
$ git config --global user.email madan@fusemachines.com

```
2. Setup ssh-key (check garihalni tyo location ma key generate vako x ki xaina vanyara tyo file bhitra gayara nai)

```shell
# ssh-keygen le ssh key generate gardenxa
# Why ssh key vanyasi github ma everytime username and password hannu vanda ssh-keygen le ssh key generate garni ani tyai ssh key use garni.


# Generate ssh-key
$ ssh-keygen -t rsa -b 4096 -C "github email" # ssh key generate vayo

# ssh key lai ssh-agent ma add garni
$ ssh-add ~/.ssh/id_rsa # rsa agent ma tyo key add gardeni
# yadi timle pailai kunai key generate gareko xau vanyasi tyo key ko file name id_rsa ma tyo file ko name rakhdeni

# Copy the SSH key to your clipboard.
$ sudo apt install xclip -y   # xclip install garni paila

$ xclip -sel clip < ~/.ssh/id_rsa.pub # copy ssh-key to clipbord

```

3. Setup key to github(aba mathi create gareko ssh-key git ma add gaenuparyo)


* In the upper-right corner of any page, click your profile photo, then click Settings.
* In the user settings sidebar, click SSH and GPG keys.
* Click New SSH key or Add SSH key.
* In the "Title" field, add a descriptive label for the new key. For example, if you're using a personal Mac, you might call this key "Personal MacBook Air".
* Paste your key into the "Key" field.
* Click Add SSH key.
* If prompted, confirm your GitHub password.


4. Project initialization


```shell
$ git init
$ git add .
$ git commit -m "first commit"
$ git remote add origin git@github.com:sp-fm/python-lifecycle.git
$ git push -u origin master

```
5. .gitignore

```shell
$ git add .gitignore
$ git commit -m "chore: Add .gitignore file"
```
* Look at .gitignore , what are the things that we are ignore

* Note :
    * akchoti commit gariskyako file lai ignore garna sakdaina so , paila tyo file lai git repository bata remove garni (note : repository bata matra remove hunxa tara , hamro directory bata remove hudana
    * Git will not ignore the file if you've already committed it. You'll have to untrack the file first, then it will start ignoring it. You can untrack the file with this command:

    * ``` git rm --cached FILENAME ```
    * ``` git check-ignore -v example.log``` Debugging ( kun kun file ignore vairaxa vanyara herna lai)

## Linting , codeformatting = pre-commit hooks


* [EditorConfig](https://editorconfig.org/)
* [Flake8](https://flake8.pycqa.org/en/latest/)
* [Black](https://black.readthedocs.io/en/stable/)
* [Isort](https://black.readthedocs.io/en/stable/)
* [Mypy](http://mypy-lang.org/)

All above linting and code formatting are handle by pre-commit hook.

 **Pre-commit hooks (linting,code formatting,testing)**

* Look at .pre-commit-hooks.yaml and .pre-commit-config.yaml , what are doing codeformatting,linting,testing so on.

* Look some command of pre-commit hook :
```shell
$ poetry add pre-commit # this is already install while installing poetry install

$ pre-commit install  # Note : yo chai poetry install le install gareko hudaina so yo afai garni ok. Install the git hook scripts (every commit garda afai precommit hook check garna)

$ pre-commit run --all-files

```

* Note :
    * Jun file/folder ma error auxa tyo file folder yellow color le dekhauxa
    * Terminal ma ni ramro sanga padni k error x vanyara.


------------
# Project setup

------------

    ├── Package               <- Folder Contain Many programming files(modules)
        ├── Module_name  (.py)          <- File (i.e  .h(in c and c++),.py,.js ,.java,php...)
        ├── Module attribute
          ├── Class_name
          │   ├── Class attribute
          │        ├── Method
          │            ├── Method attribute
          ├── Function
             ├── Function attribute
          ├── Generator
             ├── Generator attribute
------------

from package import module

* call first module attributes (eg: if __name =="main": )
* Create obj = Class_name(), call methods obj.methodname()/method attributes
* Directly call function
* Directly all generator

## Statically typed languages

Simply : A language is statically typed if the type of a variable is known at compile time.

Example : Examples: C, C++, Java, Rust, Go, Scala

## Dynamically typed languages

Simply : A language is dynamically typed if the type is associated with run-time

Example : Examples: Perl, Ruby, Python, PHP, JavaScript

**Why statically typed language?**

Answer : In a static language, updating the declared type signature and fixing any compile errors will catch most, if not all places that need updating. Static types can ease the mental burden of writing programs, by automatically tracking information the programmer would otherwise have to track mentally in some fashion.

## Statically typed in python

```python
from typing import Union

def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float](return int or flot j ni hunxa sakxa):

    return a + b
```

## Command line
We have lots command line sys.argv[],fire .... so on.

Why command line ?

Answer : before creating a complete project we need to compile each module(.py) , to chat what is function return and what is happening in each function so , command line is most important.

Note : test each module through command line.

### [Fire](https://google.github.io/python-fire/guide/) (fire le ststic , non-static dubai method ko lagi kam garxa))
We have used Fire in this project.

1. Install fire on your poetry


```shell
$ poetry add fire

```
2. Pass function or class to the fire then fire treate it automatically.

```python
import fire

def main():
   fire.Fire(class name/function name)  # yasari function or  class pass gariyasi


if __name__ == "__main__":
   main()


```
pass argumet from command line :

```
...module_name params (note module ma  if __name__ == "__main__": yo hunuparxa natra sidai module execute hudaina)

...module_name function_name params (note module ma  if __name__ == "__main__": yo hunuparxa natra sidai module execute hudaina)

```
## Logging
We have lots of logging library and inbuilt logging tools:

* Logging
    ```python
     Import logging

     logging.basicconfiguration(...)

     Logger = logging.getLogger(..)

     Logger.functions(...)

    ```
* [Mlflow](https://www.mlflow.org/docs/latest/index.html)

```shell
$ pip install mlflow
```
```python
from mlflow import log_metric, log_param, log_artifacts

Log_param(...)

Log_metric(...)

Log_artifacts(...)

We can save model
We can make dashboard in databrick.

```


Why logging?


What are the things that we need to log?


### [Loguru](https://github.com/Delgan/loguru)

In this project we are going to use loguru as a logging library.

1. Install loguru

```shell
$ poetry add loguru

```
2. Set log location and configuration

Note : we need to add some config to __init__.py of our project

Add the following to your package __init__.py file

```python
from logging
from loguru import logger

logger.add("logs(logs folder afai banaidenxa)/critical.log", level="CRITICAL", rotation="10MB")
logger.add("logs/error.log", level="ERROR", rotation="10MB")
logger.add("logs/warning.log", level="WARNING", rotation="10MB")
logger.add("logs/info.log", level="INFO", rotation="10MB")
logger.add("logs/debug.log", level="DEBUG", rotation="10MB")

class PropagateHandler(logging.Handler):
    def emit(self,record):
        logging.getLogger(record.name).handler(record)

logger.add(PropagateHandler(),format="{message}")

# ENV = "development"

```

3. Use loguru
```python
from loguru import logger

logger.info(f"Adding {a} with {b}")


```
Now you can use logger on your project

```python
logger.info(f"Adding {a} with {b}")

```
## Configuration management

There are lats of library for configuration


Why configuration management?

Answer : There are lots of secrets we did't want to push this library in git so we need to use configuration .

Note : we did't push secrets in github , we put our secrets in .secrets.yaml and give sample setting.yaml to put there secrets in this formate.

### Dynaconf


1. Install Dynaconf.
```shell
$ poetry add dynaconf

$ mkdir configs
$ dynaconf init -p configs -f yaml
```
2. Keep secrets

Keep secrets in .secrets.yaml and settings.yaml

```
.secrets.yaml

password : "s3cr3t"
token : "dfgrfg5d4g56ds4gsdf5g74984we5345-"
message : "This file doesn't go to your pub repo"
```
settings.yaml
Note : inherit follow garxa.
```
Default:
key : "value"
a_boolean : false
number : 1234
a_float : 56.8
a_list : [1, 2, 3, 4]
a_dict : {hello="world"}
[a_dict.nested]
other_level : "nested value"

Development:
key : "value"
a_boolean : false
number : 1234
a_float : 56.8
a_list : [1, 2, 3, 4]
a_dict : {hello="world"}
[a_dict.nested]
other_level : "nested value"

production:

```
3. Set config.py
Config.py ma  setting object banauni :
```python
from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=['configs/settings.yaml', 'configs/.secrets.yaml'],
    environments=True,
)

```

4. Use credential in code

```python
from config import settings

assert settings.key == "value"
assert settings.number == 789
assert settings.a_dict.nested.other_level == "nested value"
assert settings['a_boolean'] is False
assert settings.get("DONTEXIST", default=1) == 1

```

5. Environment variable

variable =  setting.key
```shell
$ export DYNACONF(seeting ma set gareko name)_variable=1

```

To unset the variable:
```shell

$ unset DYNACONF_variable


```

5. Switching Environment (hamle jun environment ko variable jun mathi setting default,develpment,production ma use gareko xam tesko credential use garna switch garni)

```shell
$ export ENV_FOR_DYNACONF = production

$ unset ENV_FOR_DYNACONF
```

6. Command line

## Testing
There are lots of testing methods in

Note : we can set test folder anywhere , pytest automatically find the function which prefix test_..  and execute this function.

### Pytest


1. Install Pytest
```shell
$ poetry add pytest

```

2. Run test
```shell
$ pytest # pytest automatically find function which has test_prefix and run them

```

### coverage (first run pytest then generate report)

1. Install coverage

```shell
poetry add coverage

```

2. Configuration

Add the following lines in pyproject.toml

```
[tool.coverage.run]
branch = true
source = [
    "python_lifecycle",
]

[tool.coverage.report]
# Regexes for lines to exclude from consideration
exclude_lines = [
    # Have to re-enable the standard pragma
    "pragma: no cover",

    # Don't complain about missing debug-only code:
    "def __repr__",
    "if self.debug",

    # Don't complain if tests don't hit defensive assertion code:
    "raise AssertionError",
    "raise NotImplementedError",

    # Don't complain if non-runnable code isn't run:
    "if 0:",
    "if __name__ == .__main__.:",

    # Don't complain about fire commands
    "fire.Fire",
]
fail_under = 90

ignore_errors = true


```
3. RUN

```shell
$ coverage run -m pytest

$ coverage report -m

```
4. Test exception

Exception haru ni test garna milxa , exception through garirako thick x ki xaina vanyara.


Example :

```python

@staticmethod
def test_div_zero():
    with pytest.raises(ZeroDivisionError) as excinfo:
        complex.Calculator.div(2, 0)
    assert str(excinfo.value) == "division by zero"

```
```shell
$ coverage run -m pytest

```

### tox (mathiko pytest and coverage lai akkaichoti different python ma run garxa)

1. Install tox
```shell
poetry add tox

```

2. Configuration

Put tox.ini file is at root of project.

```
[tox]
envlist = py37, py38, flake8  # yasari different different python version ma test(pytest,...) garna milxa
skipsdist = true

[testenv] # command haru lekhnalai
deps = poetry  #
commands_pre = poetry install # command
commands = poetry run pytest

[testenv:flake8]  #
basepython = python
deps = flake8
commands = flake8 python_lifecycle tests # command
```
2. Run tox

```
# tox
```
### Automate testing : Pre-commit hooks
```
- repo: local
    hooks:
      - id: install-dependencies
        name: Install Dependencies
        entry: poetry install # poetry install --no-root : poetry.toml or poetry.lock ma dependencies haru capture vako hunxa tyo kura run garxa
        language: python
        always_run: true
        pass_filenames: false

      - id: test  # yadi test xaina vanya yo comment garni
        name: Run tests
        entry: poetry run pytest  # commit garnu vanda paila test ta garna ni sakinxa so, sabai test file haru run garxa
        language: python
        always_run: true
        pass_filenames: false
```



------------

# CI/CD(github/workflows ma .yml file  haru lekhni and gitub project page ma action ma hernu debug k vairaxa vanyara purai code nai debug hunxa)

## Documentation Hosting

There are lots of documentation tools one of them is Sphinx.

### Sphinx

1. Install sphinx

```shell

$ poetry add sphinx --dev

```

2. setup

```shell
$ sphinx-quickstart -v ‘ poetry version -s’ docs

```

3. Create documentation

```shell
$ make -C docs html
$ chromium docs/_build/html/index.html

```


4. Change theme

```shell
# First insall theme
$ poetry add sphinx-rtd-theme --dev

```
In config.py of docs

```
html_theme = "sphinx_rtd_theme"

```
Clean existing build then build again.

```shell

$ Make clean
$ make html
$ chromium docs/_build/html/index.html


```

5. Auto Documentation
In above we have not create documentation yet.

Give path of you project to make documentation for it.

config.py

```python
import os
import sys
sys.path.insert(0, os.path.abspath('.'))  # . lai milauni thyakkia afno package huni gari.

```

Add extension:
```
extensions = [
   "sphinx.ext.autodoc"
]

```
index.rst

```
.. toctree::      # yaha nira  lastai error aerako  x
   :maxdepth: 2
   :caption: Contents:

   modules # Hamro module haru generate garda add gardenxa

```

Add a .gitignore in your docs folder with the following content

```
# Ignore module docs
python_lifecycle*.rst #.gitignor bhitra rakhni your_root_foldername*.rst

```

Clean previous build and build again

```shell
$ Make clean
$ make html
$ chromium docs/_build/html/index.html
```

At this stage your modules docs generate so , if it did't generate try to change

*  sys.path.insert(0, os.path.abspath('..'))  # different path location


6. Add doc string to your project methods

Example : google docstring

```python

def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
   """Add two numbers

   Args:
       a (Union[int, float]): The first number
       b (Union[int, float]): The second number

   Returns:
       int or float: Sum of two numbers

   """
   logger.info(f"Adding {a} with {b}")
   return a + b



```

Now build again

```shell
$ Make clean
$ make html
$ chromium docs/_build/html/index.html

```

To handle google docs add napolean in extension:

```
extensions = [
   "sphinx.ext.autodoc",
   "sphinx.ext.napoleon",
]

```

At this time you can see your beautiful documentation of your package/modules

7. Generate automatic documentation through tox

```

[tox]
envlist = ..., docs
...

[testenv:docs]
basepython = python
changedir = docs
deps =
   sphinx-rtd-theme
   toml
commands =
   sphinx-build -b html -d {envtmpdir}/doctrees . {envtmpdir}


```
run tox

```shell
$ tox
```

8. Add other documentation extension


```

extensions = [
   "sphinx.ext.autodoc",
   "sphinx.ext.coverage",
   "sphinx.ext.doctest",
   "sphinx.ext.githubpages",
   "sphinx.ext.napoleon",
   "sphinx.ext.todo",
   "sphinx.ext.viewcode",
]

```
Don’t show todos

add this in config.py

```

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


```
Better syntax highlighting

add this in config.py


```
# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

```
Auto-generate your project meta

```shell
$ poetry add toml --dev

```
Add this in config.py
```python
import toml

def _get_project_meta():
   return toml.load("../pyproject.toml")["tool"]["poetry"]


pkg_meta = _get_project_meta()
project = str(pkg_meta["name"])
copyright = "2020, Shashanka Prajapati"
authors = str(pkg_meta["authors"])

# The short X.Y version
version = str(pkg_meta["version"])

# The full version, including alpha/beta/rc tags
release = version

```
## Continuous integration : Testing (Pytest matra garxam tox ko help le)=

Simply vannu parda tox run garxa yasle (tox ma pytest haru matra x )




### Branch(Dev) testing
.python-package.yml is for branch testing:

Note : Master lai ignore garyara aru branch ma push garda yo action run hunxa.

### Master  branch testing

master-python-package.yml

Note : master ma push huda matra run hunxa


Note : branch bata master ko lagi pull request pathuda sabai testing heryara balla merge garni.


## Documentation hosting
Note : First you need to setup your github page  For that you need to create github.io extension page.
1. Create a new ssh key, using the provided email as a label.
```shell
$ ssh-keygen -t rsa -b 4096 -C "git gmil" -f ~/.ssh/python-lifecycle-gh-pages -N ""

```
2. Copy the SSH key to your clipboard.

```shell
xclip -sel clip < ~/.ssh/python-lifecycle-gh-pages.pub

```

Paste it to Deploy Keys section in your project settings with Allow write access(github ko repository ko deploy key section ma pest garni)

3. Copy private key
```shell
xclip -sel clip < ~/.ssh/python-lifecycle-gh-pages

```
Paste it to Secrets section as ACTIONS_DEPLOY_KEY (github ko repository ko secrets section ma pest garni)

### Automated Document Hosting

```shell

$ git add .github/workflows/gh-pages.yml
$ git commit -m "docs: Document Hosting via GitHub Pages"
$ git push



```
Create one more pull request and merge your changes to master. Check the actions tab once your changes have been merged.


## Package hosting

For package hosting

### [Publishing to a private repository](https://python-poetry.org/docs/libraries/) :
1. Note : While you are working with any company you need to make private anything:

2. Add following code to your pyproject.toml :

```
[[tool.poetry.source]]
    name = 'private'
    url = 'your github link(https://github.com/MadanBaduwal/ssev2_project.git(collebrator can install), git@github.com:MadanBaduwal/ssev2_project.git(completely private) )'
    default = true ```
    * Note : if you set set : default = true then the package public defult is private , not publish as public.

```
3. Packaging

```shell
poetry build

```
4. Set config to poetry(build gareko kun repo ma push garni jastai vayo):

```
poetry config repositories.your_root_package_to_publish githublink(https://github.com/MadanBaduwal/ssev2_project.git(collebrator can install), git@github.com:MadanBaduwal/ssev2_project.git(completely private) )

```

    * Note : While creating package your all package put into a particular root package

5. Set credential(push garna lai credential ta chiyo ni tyo set gareko) :

```shell

poetry config http-basic.your_root_package_to_publish github_username github_password

```
    * Note : For public package we use token not username and password ok.

6. Publish on your git repository: Once above is done, you can actually publish to it like so:

```
poetry publish -r my-repository(mina)

note:
[[tool.poetry.source]]
name = 'mina'
url = 'https://github.com/madanb-nicn/mina.git'
default = true

my-repository name rakhni ok.

```
Note : git push garyasi ani balla dist folder banauxa git ma ani tya whil file hunxa ok.

7. Install package on your system :

```shell
#
$ poetry add git+https://github.com/sdispater/pendulum.git
$ poetry add git+ssh://git@github.com/sdispater/pendulum.git
# If you need to checkout a specific branch, tag or revision, you can specify it when using add
$ poetry add git+https://github.com/sdispater/pendulum.git#develop
$ poetry add git+https://github.com/sdispater/pendulum.git#2.0.5

```

### [Publishing to a public repository poetry or setup.py similar way](https://python-poetry.org/docs/libraries/):

1. Add following code to your pyproject.toml

```
[tool.poetry]
name = "mina"
version = "0.0.1"
description = "Artificial intelligence packages"
authors = [
    "Madan Baduwal <madan.baduwal@nicnepal.org>"
    ]
readme = "README.md"
homepage = "https://github.com/madanb-nicn/mina"

repository = "https://github.com/madanb-nicn/mina"

documentation = "https://github.com/madanb-nicn/mina/wiki"

keywords = ["artificial intelligence", "robotic", "mina"]


packages = [
    { include = "package name which you want to publish" }
]

```
2. Packaging:

```$ poetry build````

3. Set PYPI token to publish(publish garna lai token chiyo nita):

4. Publish:

```$ poetry publish```

### Automation Publish package githubaction

1. Token Setup :
    * Create a PyPi account if you don’t have one.
    * Goto Account Settings from the top right corner
    * Click Add API token
    * Set the Token name and Scope
    * Click Add token
    IMPORTANT NOTICE: Save this token ID somewhere very safe as it represents your PyPi identity. You’ll need this to deploy packages. If you lose it then you’ll have to generate a new one. If others get hold of this token then they can host packages in your name.
2. Add Token to your Project

    * Go to your project settings
    * Click on Secrets
    * Click on New secret
    * Add your token as PYPI_TOKEN

3. Tagged Commit :

Note : hamle jatibela ni commit garda(master or dev) ma package bannu ta vayana ni so togged commit ako ho:



* publish through github action :
    * Setup pypi token in github secrets : name as $ POETRY_PYPI_TOKEN_PYPI
    * Look at github/workflow/upload-python-package.yml
    * github ma push garda auta tag rakhyara push garni
    * Then tag ma gayara release garni,

```shell

$ poetry version minor
$ git add pyproject.toml
$ git commit -m "chore: bump version from 0.1.0 to 0.2.0"
$ git tag `poetry version -s`
$ git push --tags


```
4. Release (Release package):

* Click on tags in your project repo
* Go to Releases
* Draft a new release
* Add the tag version, release title, and the description. You can edit the PR description
* Click on Publish Release
* Action tab ma gayara kai error ayo ki k vairaxa vanyara herni.
* Check if your package is there in PyPi

NOTE: Generally a pre-release is published until it’s stable. It’s published as an official release at a later date.


5. install :
```
poetry add packagename

```

## Dockerization and [Automatic docker hosting of github in container registry](https://docs.docker.com/ci-cd/github-actions/)

* Package hoating garya jastai ho
* Setup  Dockerfile or docker.yml file

* Dokerhub(or any contain registry) ma gayara token create garni and tyo token lai git ko secrets ma rakhni
* .github/workflow ma gayara .yml job banauni docker ho lagi
* Package jasati auta tag ma kam garni banauni


## Run docker image in server

------------


# Run project

## Run githubclone project
* Befor run project we have sure that
    * In configs you must set credentials
    * You must set your models in models folder
```
$ cd webapp
$ streamlit run streamlitapp

```
## Run or import published package

See above how to install private and public package.

```
from packagename import modules

module.classname or module.functionname

```

## Run dockerizeed project
* Docker hub(or any container registry)  bata image pull garni and local ma run garni.
* Git ko replo lai clone garyara , Docker file ko help le image banayara run ni garna sakinxa

------------

# Use this project as templet

## Github template
We can make this repository as template project for other project:

1. Enable this project for template:

* Go to the seeting of this repository
* Enable checkbox of Template repository

2. Create new repository using this template repository:

* After doing above in our repository there is green Use this template is enable

* After click button we can create new repo.

## Cookiecutter

# Production 

## Dashbord 
### Streamlit

## Monotoring
### Datadog

## Pipeline
### Airflow






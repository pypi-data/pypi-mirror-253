# CrashKit

An instrumentation hardware orchestration platform.

## Background

Crashkit was founded on the idea of creating rapidly
deployable production troubleshooting and test equipment
carts, fondly referred to as "Crash Carts".  In order to
simplify the equipment configuration and setup process, a
SCPI command orchestration backend was needed. 

## Install

### PyPI

Install and update using pip:

```shell
pip install -U crashkit
```

### Repository

When using git, clone the repository and change your 
present working directory.

```shell
git clone http://github.com/mcpcpc/crashkit
cd crashkit/
```

Create and activate a virtual environment.

```shell
python -m venv venv
source venv/bin/activate
```

Install CrashKit to the virtual environment.

```shell
pip install -e .
```

## Commands

### db-init

The backend database can be initialized or re-initialized 
with the following command.

```shell
quart --app crashkit init-db
```

## Deployment

Before deployment, overriding the default `SECRET_KEY`
variable is *strongly* encourage. This can be done by
creating a `conf.py` file and placing it in the
same root as the instance (i.e. typically where the
backend database resides).

```python
SECRET_KEY = “192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf“
```

There are a number of ways to generate a secret key
value. The simplest would be to use the built-in secrets
Python library.

```shell
$ python -c ‘import secrets; print(secrets.token_hex())’
‘192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf’
```

### Quart

Non-production ASGI via quart for development and
debugging.

```shell
quart --app crashkit run --debug
```

### Uvicorn

Production ASGI via uvicorn.

```shell
pip install waitress
waitress-serve --factory crashkit:create_app
```

## Test

```shell
python3 -m unittest
```

Run with coverage report.

```shell
coverage run -m unittest
coverage report
coverage html  # open htmlcov/index.html in a browser
```

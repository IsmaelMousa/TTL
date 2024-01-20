# TODO Task List

![CI](https://img.shields.io/github/actions/workflow/status/IsmaelMousa/todo-task-list/ci.yml?style=flat-square&logo=github&label=CI)

## Overview

Fullstack project that simulates a simple TODO task manager application.

## Description

Provide a more detailed explanation of the project. What problem does it solve? Why is it useful?

## Goal

The main goal of this project is to apply the technologies & tools I have learned, and learn how to build a project
from scratch to deployment through all development stages.

## Technologies

<br />
<a href="https://www.python.org"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png" alt="Python" title="Python" height="50"></a>
<a href="https://fastapi.tiangolo.com" target="_blank"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI" title="FastAPI" height="50"></a>
<a href="https://www.postgresql.org" target="_blank"><img src="https://cdn.icon-icons.com/icons2/2415/PNG/512/postgresql_plain_wordmark_logo_icon_146390.png" alt="PostgreSQL" title="PostgreSQL" height="50"></a>
<a href="https://www.docker.com"><img src="https://logos-world.net/wp-content/uploads/2021/02/Docker-Symbol.png" alt="Docker" title="Docker" height="50"></a>
<a href="https://python-poetry.org"><img src="https://avatars.githubusercontent.com/u/48722593?s=200&v=4" alt="Poetry" title="Poetry" height="50"></a>

## Development Principles

Software development principles and best practices applied in this project

- **Scalability**
- **Testability**
- **Modularity**
- **Maintainability**
- **Reliability**
- **CI/CD**

## Installation

Here are the steps you must follow to install the project correctly

1. Clone the project

```zsh
git clone https://github.com/IsmaelMousa/todo-task-list.git
```

2. Setup virtual environment **inside the project**

```zsh
python3 -m venv .venv
```

3. Activate the virtual environment

```zsh
source .venv/bin/activate
```

4. Install the required dependencies

```zsh
make install
```

## Usage

Here is the example of how to use the project

```
make run
```

## Modules

You will see this when you open the project

```zsh
todo-task-list
 ├── .github
 │   └── workflows
 │   │   └── ci.yml
 ├── errors
 │   ├── __init__.py
 │   └── custom.py
 ├── infrastructures
 │   ├── __init__.py
 │   └── crud
 │   │   ├── __init__.py
 │   │   └── task.py
 │   └── database.py
 ├── models
 │   ├── __init__.py
 │   └── task.py
 ├── routers
 │   ├── __init__.py
 │   └── task.py
 ├── schemas
 │   ├── __init__.py
 │   └── task.py 
 ├── tests
 │   ├── __init__.py
 │   ├── infrastructures_database.py
 │   ├── utils_config.py
 │   └── utils_logger.py    
 ├── utils
 │   ├── __init__.py
 │   ├── config.py
 │   └── logger.py     
 ├── view
 ├── .gitignore
 ├── config.yaml
 ├── main.py
 ├── Makefile
 ├── poetry.lock
 ├── poetry.toml
 └── README.md
```

<br />
Briefly description of the purpose of each major module in the project

|      Module       |                  Description                   |
|:-----------------:|:----------------------------------------------:|
| `infrastructures` | Show file differences that haven't been staged |
|     `models`      | Show file differences that haven't been staged |
|     `schemas`     | Show file differences that haven't been staged |
|     `routers`     | Show file differences that haven't been staged |
|      `utils`      | Show file differences that haven't been staged |
|     `errors`      | Show file differences that haven't been staged |
|      `tests`      | Show file differences that haven't been staged |
|      `view`       | Show file differences that haven't been staged |

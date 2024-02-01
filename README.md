# TTL (Todo Task List) ✍

What's your plan today? 🤔

![CI](https://img.shields.io/github/actions/workflow/status/IsmaelMousa/todo-task-list/ci.yml?style=flat-square&logo=github&label=CI)
![coverage](https://img.shields.io/codecov/c/github/IsmaelMousa/todo-task-list?style=flat-square)

## Overview

Welcome to my humble **full-stack** project 👋

This project is simulating a **todo task list application**, combined with some fun features using **AI** ✨.

## Description

This TTL project provides a smart AI suggestion feature 💎.
While writing and preparing your assignment,
you will receive intelligent suggestions related to the content of your task 💬.
This feature saves your time and provides relevant options.
The most important thing is that sometimes when we start writing our assignment,
we don't know how to formulate it.
However, with this feature, writing and preparing the task become very easy and enjoyable 🤗.

**Note**: When using the project, you will directly write your task; there is no Sign In/Sign Up yet.

## Goal

The main goal of this project is to apply the technologies & tools I have learned 💡, and learn how to build a project
from scratch to deployment through all development stages 🎖️.

## Technologies

Technologies & Tools 🚀 ️used in this project:

<br/>
<a href="https://www.python.org"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png" alt="Python" title="Python" height="50"></a>
<a href="https://fastapi.tiangolo.com" target="_blank"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI" title="FastAPI" height="50"></a>
<a href="https://www.postgresql.org" target="_blank"><img src="https://cdn.icon-icons.com/icons2/2415/PNG/512/postgresql_plain_wordmark_logo_icon_146390.png" alt="PostgreSQL" title="PostgreSQL" height="50"></a>
<a href="https://www.docker.com"><img src="https://logos-world.net/wp-content/uploads/2021/02/Docker-Symbol.png" alt="Docker" title="Docker" height="50"></a>
<a href="https://python-poetry.org"><img src="https://avatars.githubusercontent.com/u/48722593?s=200&v=4" alt="Poetry" title="Poetry" height="50"></a>
<a href="https://docs.pytest.org/en/8.0.x/contents.html"><img src="https://545767148-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdBdUMSCcMYTyNwZf80%2Fuploads%2Fgit-blob-f08a97a4a9cff017c204a21b66514ee07045dba8%2Fpytest.png?alt=media" alt="Poetry" title="Poetry" height="50"></a>

## Installation

Here are the steps you must follow to install the project correctly 🎯:

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

## Modules

After completing the installation steps ✅, the projects files should be like this when you open the project:

```zsh
todo-task-list
 ├── .github
 │   └── workflows
 │   │   └── ci.yml
 ├── dependencies 
 │   ├── __init__.py
 │   └── util.py
 ├── errors
 │   ├── __init__.py
 │   └── custom.py
 ├── infrastructures
 │   ├── crud
 │   │   ├── __init__.py
 │   │   └── task.py
 │   ├── __init__.py 
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
 │   ├── dependencies_util.py
 │   ├── infrastructures_crud_task.py
 │   ├── infrastructures_database.py
 │   ├── models_task.py
 │   ├── routers_task.py
 │   ├── schemas_task.py
 │   ├── utils_config.py
 │   └── utils_logger.py    
 ├── utils
 │   ├── __init__.py
 │   ├── config.py
 │   └── logger.py     
 ├── .gitignore
 ├── config.yml
 ├── main.py
 ├── Makefile
 ├── poetry.lock
 ├── pyproject.toml
 └── README.md
```

<br/>
Here is a summary 📝 for the purpose of each major module or component in the project:

|      Module       | Description                                                                                            |
|:-----------------:|:-------------------------------------------------------------------------------------------------------|
| `infrastructures` | Responsible for handling database-related elements, including preparation, maintenance and operations. |
|     `main.py`     | Represents the entry point which is the starting point of the application.                             |
|   `config.yml`    | Represents the main configurations of the application, including database configuration, ...etc.       |
|     `models`      | Responsible for defining the schemas of the database's tables/entities.                                |
|     `schemas`     | Responsible for defining the schemas of the pydantic models.                                           |
|     `routers`     | Responsible for managing and creating the application's routers/endpoints.                             |
|      `utils`      | Represents the utilities/common elements used throughout the application including logging, ...etc.    |
|     `errors`      | Responsible for preparing and customizing exceptions for custom issues.                                |
|      `tests`      | Responsible for handling and preparing the unittests.                                                  |
|  `dependencies`   | Responsible for managing and creating the dependencies that used to do some operations.                |

## Usage

Here is the example of how to use the project 💁‍♂️:

```
make run
```

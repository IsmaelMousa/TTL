# TTL (Todo Task List) <a href="#" target="_blank"><img src="./views/images/website-icon.png" alt="CSS" title="CSS" height="20"></a>

What's your plan today? 🤔

![CI](https://img.shields.io/github/actions/workflow/status/IsmaelMousa/todo-task-list/ci.yml?style=flat-square&logo=github&label=CI)
![coverage](https://img.shields.io/codecov/c/github/IsmaelMousa/todo-task-list?style=flat-square)

<img src=".github/website.png" alt="example" title="example">

## Overview

Welcome to my humble **full-stack** project 👋

**TTL** is simulating a **todo task list** manager application, combined with an **AI Assistant** ✨.

## Description

**TTL** Where simplicity meets innovation ⚡! Seamlessly combining the efficiency of a traditional task manager with the
intuitive support of an **AI Assistant** 💎, Our application strives to streamline your productivity journey. Whether
you're
juggling multiple projects, planning your day, or prioritizing your tasks, our user-friendly interface and intelligent
assistant are here to support you every step of the way. Let us help you stay organized, focused, and empowered to
manage all your tasks with ease. Welcome aboard **TTL** 🤗!

**Note**: When using the project, you will directly write your task; there is no Sign in/up yet 🫣.

## Goal

The primary aim of **TTL** 🪄 is to enhance my technical and development skills by applying the technologies and tools
I've
learned. It serves as a journey of learning, starting from building a project from scratch to deployment, traversing
through all development stages 🎖️.

## Technologies

Technologies & Tools 🚀 used in **TTL**:

<br/>
<a href="https://www.python.org" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png" alt="Python 3.10" title="Python 3.10" height="50"></a>
<a href="https://fastapi.tiangolo.com" target="_blank"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI" title="FastAPI" height="50"></a>
<a href="https://www.postgresql.org" target="_blank"><img src="https://cdn.icon-icons.com/icons2/2415/PNG/512/postgresql_plain_wordmark_logo_icon_146390.png" alt="PostgreSQL" title="PostgreSQL" height="50"></a>
<a href="https://www.docker.com" target="_blank"><img src="https://logos-world.net/wp-content/uploads/2021/02/Docker-Symbol.png" alt="Docker" title="Docker" height="50"></a>
<a href="https://python-poetry.org" target="_blank"><img src="https://avatars.githubusercontent.com/u/48722593?s=200&v=4" alt="Poetry" title="Poetry" height="50"></a>
<a href="https://docs.pytest.org/en/8.0.x/contents.html" target="_blank"><img src="https://545767148-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdBdUMSCcMYTyNwZf80%2Fuploads%2Fgit-blob-f08a97a4a9cff017c204a21b66514ee07045dba8%2Fpytest.png?alt=media" alt="Pytest" title="Pytest" height="50"></a>
<a href="https://getbootstrap.com/docs/5.3/getting-started/introduction" target="_blank"><img src="https://getbootstrap.com/docs/5.3/assets/brand/bootstrap-logo.svg" alt="Bootstrap 5.3" title="Bootstrap 5.3" height="50"></a>
<a href="https://developer.mozilla.org/en-US/docs/Web/HTML" target="_blank"><img src="https://www.w3.org/html/logo/downloads/HTML5_Badge_512.png" alt="HTML" title="HTML" height="50"></a>
<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank"><img src="https://www.vhv.rs/dpng/f/456-4562295_library-of-javascript-icon-graphic-freeuse-png-files.png" alt="JavaScript" title="JavaScript" height="50"></a>
<a href="https://developer.mozilla.org/en-US/docs/Web/CSS" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/CSS3_logo.svg/2048px-CSS3_logo.svg.png" alt="CSS" title="CSS" height="50"></a>

## Installation

Here are the steps you must follow to install **TTL** correctly 🎯:

1. Clone the project

```zsh
git clone https://github.com/IsmaelMousa/todo-task-list.git
```

2. Navigate to the project

```zsh
cd todo-task-list
```

3. Setup virtual environment

```zsh
python3 -m venv .venv
```

4. Activate the virtual environment

```zsh
source .venv/bin/activate
```

5. Install the required dependencies

```zsh
make install
```

## Modules

After completing the installation steps ✅, the project files should be like this when you open **TTL**:

```zsh
todo-task-list
 ├── .github
 │   ├── workflows
 │   │   └── ci.yml
 │   └── website.png
 ├── .venv 
 │   ├── bin
 │   ├── include
 │   ├── lib
 │   ├── .gitignore
 │   └── pyvenv.cfg
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
 ├── views
 │   ├── images
 │   │   └── website-icon.png
 │   ├── index.html
 │   ├── index.js
 │   └── style.css     
 ├── .gitignore
 ├── config.yml
 ├── main.py
 ├── Makefile
 ├── poetry.lock
 ├── pyproject.toml
 └── README.md
```

<br/>

Here is a summary 📝 for the purpose of each major module or component in **TTL**:

|      Module       | Description                                                                                              |
|:-----------------:|:---------------------------------------------------------------------------------------------------------|
| `infrastructures` | Manages database-related elements, including preparation, maintenance, and operations.                   |
|     `main.py`     | Serves as the entry point, initiating the application.                                                   |
|   `config.yml`    | Contains main configurations such as database settings, ...etc.                                          |
|     `models`      | Defines the schemas of the database tables/entities.                                                     |
|     `schemas`     | Defines the schemas of the Pydantic models used in the application.                                      |
|     `routers`     | Manages and creates the application's routers/endpoints.                                                 |
|      `utils`      | Houses common utilities/logic utilized throughout the application, including logging mechanisms, ...etc. |
|     `errors`      | Prepares and customizes exceptions for handling specific issues.                                         |
|      `tests`      | Handles the preparation and execution of unit tests.                                                     |
|  `dependencies`   | Manages and creates dependencies utilized for various operations within the application.                 |
|      `views`      | Represents the user interface (UI) files, or can say front-end side.                                     |

## Usage

Here is how to use the **TTL** 💁‍♂️:

1.

```
make run
```

2. Navigate to: [http://localhost:8000/ttl/index.html](http://localhost:8000/ttl/index.html) 😀
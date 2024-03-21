# TTL (Todo Task List) <a href="#" target="_blank"><img src="./views/images/website-icon.png" alt="TTL" title="TTL" height="20"></a>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Helvetica&weight=600&size=15&pause=1000&color=F7F7F7&random=false&width=435&lines=What's+your+plan+today%3F+%F0%9F%A4%94)](https://git.io/typing-svg)

![CI](https://img.shields.io/github/actions/workflow/status/IsmaelMousa/todo-task-list/ci.yml?style=flat-square&logo=github&label=CI)
![coverage](https://img.shields.io/codecov/c/github/IsmaelMousa/todo-task-list?style=flat-square)

## Demo 👀

![Demo](.github/demo.gif)

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

## Goal

The primary aim of **TTL** 🪄 is to enhance my technical and development skills by applying the technologies and tools
I've
learned. It serves as a journey of learning, starting from building a project from scratch to deployment, traversing
through all development stages 🎖️.

## Technologies

Technologies & Tools 🚀 used in **TTL**:

<br/>
<a href="https://www.python.org" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png" alt="Python 3.10" title="Python 3.10" height="50"></a>
<a href="https://huggingface.co/docs/transformers/en/index" target="_blank"><img src="https://huggingface.co/datasets/huggingface/brand-assets/resolve/main/hf-logo.png" alt="HF Transformers" title="Transformers" height="50"></a>
<a href="https://fastapi.tiangolo.com" target="_blank"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI" title="FastAPI" height="50"></a>
<a href="https://www.postgresql.org" target="_blank"><img src="https://cdn.icon-icons.com/icons2/2415/PNG/512/postgresql_plain_wordmark_logo_icon_146390.png" alt="PostgreSQL" title="PostgreSQL" height="50"></a>
<a href="https://docs.sqlalchemy.org/en/20/" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/SQLAlchemy.svg/800px-SQLAlchemy.svg.png" alt="SQLAlchemy" title="SQLAlchemy" height="50"></a>
<a href="https://python-poetry.org" target="_blank"><img src="https://avatars.githubusercontent.com/u/48722593?s=200&v=4" alt="Poetry" title="Poetry" height="50"></a>
<a href="https://getbootstrap.com/docs/5.3/getting-started/introduction" target="_blank"><img src="https://getbootstrap.com/docs/5.3/assets/brand/bootstrap-logo.svg" alt="Bootstrap 5.3" title="Bootstrap 5.3" height="50"></a>
<a href="https://developer.mozilla.org/en-US/docs/Web/HTML" target="_blank"><img src="https://www.w3.org/html/logo/downloads/HTML5_Badge_512.png" alt="HTML" title="HTML" height="50"></a>
<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank"><img src="https://www.vhv.rs/dpng/f/456-4562295_library-of-javascript-icon-graphic-freeuse-png-files.png" alt="JavaScript" title="JavaScript" height="50"></a>
<a href="https://developer.mozilla.org/en-US/docs/Web/CSS" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/CSS3_logo.svg/2048px-CSS3_logo.svg.png" alt="CSS" title="CSS" height="50"></a>

## Prerequisites

- **Python 3.10** [download](https://www.python.org/downloads/)
- **PostgreSQL** [download](https://www.postgresql.org/download/)

> [!NOTE]
>
> You need also to set up the database, where:
> - DB Name: **TODO**
> - DB Username: **postgres**
> - DB Password: **test**
> - DB Host: **localhost**
> - DB Port: **5432**
>
> I **recommend** using [pgAdmin4](https://www.pgadmin.org/download/) to facilitate the setup process and also monitor
> changes.

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
 │   └── demo.gif
 ├── .venv 
 │   ├── bin
 │   ├── include
 │   ├── lib
 │   ├── .gitignore
 │   └── pyvenv.cfg
 ├── assistants 
 │   ├── __init__.py
 │   └── chat.py
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
 │   ├── assistant.py
 │   └── task.py
 ├── schemas
 │   ├── __init__.py
 │   ├── assistant.py
 │   └── task.py 
 ├── tests
 │   ├── __init__.py
 │   ├── assistants_chat.py
 │   ├── dependencies_util.py
 │   ├── infrastructures_crud_task.py
 │   ├── infrastructures_database.py
 │   ├── models_task.py
 │   ├── routers_assistant.py
 │   ├── routers_task.py
 │   ├── schemas_assistant.py
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
 ├── LICENSE.md
 ├── main.py
 ├── Makefile
 ├── poetry.lock
 ├── pyproject.toml
 ├── README.md
 └── SECURITY.md
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
|   `assistants`    | Contains the hugging face transformers models, for the specific NLP tasks.                               |
|      `views`      | Represents the user interface (UI) files, or can say front-end side.                                     |

## Usage

Here is how to use the **TTL** 💁‍♂️:

1.

```
make run
```

2. Navigate to: [http://localhost:8000/ttl/index.html](http://localhost:8000/ttl/index.html) 😀

> [!TIP]
>
> To enhance your user experience, I recommend running the backend and frontend separately where:
> 1. Start the Server-side using the instructions provided in [Step No.1](#usage).
> 2. Execute the frontend by opening the [index.html](./views/index.html) file in the browser.
>
> This approach ensures optimal performance and usability for both sides of the application.

<br/>

## Feedback 💌

We value your feedback and suggestions 🤟! If you've used **TTL** or explored its features, we'd love to hear
from you 🫡. share your thoughts, ideas, or any issues you encountered while using the application 💡.

Feel free to open an issue on GitHub or reach out to us
via [email](https://mail.google.com/mail/ismaelramzimousa@gmail.com) with your feedback.
Your feedback helps us improve **TTL**
and make it even better for our users 🎭.

**Thank You!** 🌹🫵
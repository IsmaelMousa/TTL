from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models import Base
from dependencies import get_db
from schemas import TaskRequest, TaskResponse
from infrastructures import get_database_stuff
from infrastructures.crud import get_task_manager
from utils import get_config, get_logger

engine = get_database_stuff().engine
Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/manager/tasks", tags=["Tasks"])

app_cfg = get_config().app
level = app_cfg.log_level
logger = get_logger(level=level)


@router.post(path="/new",
             summary="Creating a new task",
             status_code=201)
def create(task: TaskRequest,
           db: Annotated[Session, Depends(get_db)]) -> dict[str, int | str]:
    """
    Creating a new task based on the received data.

    :param task: instance of pydantic TaskCreate model
    :param db: the database session
    :return: the task creation details that come from the create operation
    """
    try:
        manager = get_task_manager(db=db)
        new_task = manager.creator.create(task=task)

        return new_task

    except Exception as exc:
        logger.error(msg=str(exc))
        raise HTTPException(status_code=500, detail=str(exc))


@router.get(path="/all",
            summary="Get all tasks",
            status_code=200)
def get_all(db: Annotated[Session, Depends(get_db)]) -> list[TaskResponse] | dict[str, int | str]:
    """
    Getting all tasks at once

    :param db: the database session
    :return: a list of tasks (instances of TaskRead)
    """
    try:
        manager = get_task_manager(db=db)
        all_tasks = manager.reader.get_all()

        return all_tasks

    except Exception as exc:
        logger.error(msg=str(exc))
        raise HTTPException(status_code=500, detail=str(exc))


@router.get(path="/query",
            summary="Get tasks by query",
            status_code=200)
def get_by_query(query: str,
                 db: Annotated[Session, Depends(get_db)]) -> (
        list[TaskResponse] | dict[str, int | str]):
    """
    Getting all tasks based on the query.

    :param query: the search query
    :param db: the database session
    :return: a list of tasks (instances of TaskRead)
    """
    try:
        manager = get_task_manager(db)
        tasks_by_query = manager.reader.get_by_query(query=query)

        return tasks_by_query

    except Exception as exc:
        logger.error(msg=str(exc))
        raise HTTPException(status_code=500, detail=str(exc))


@router.put(path="/update/{task_id}",
            summary="Update task by id",
            status_code=200)
def update(task_id: int,
           task: TaskRequest,
           db: Annotated[Session, Depends(get_db)]) -> dict[str, int | str]:
    """
    Updating a task based on the task's ID with the updated fields.

    :param task_id: the task's id
    :param task: instance of pydantic TaskUpdate model (updated fields)
    :param db: the database session
    :return: the task modification details that come from the update operation
    """
    try:
        manager = get_task_manager(db)
        update_task = manager.updater.update(task_id=task_id, task=task)

        return update_task

    except Exception as exc:
        logger.error(msg=str(exc))
        raise HTTPException(status_code=500, detail=str(exc))


@router.delete(path="/delete/id={task_id}",
               summary="Delete task by id",
               status_code=200)
def delete_by_id(task_id: int,
                 db: Annotated[Session, Depends(get_db)]) -> dict[str, int | str]:
    """
    Deleting a task based on the task's ID.

    :param db: the database session
    :param task_id: the task's id
    :return: the task deletion details that come from the delete_by_id operation
    """
    try:
        manager = get_task_manager(db)
        delete_task = manager.deleter.delete_by_id(task_id=task_id)

        return delete_task

    except Exception as exc:
        logger.error(msg=str(exc))
        raise HTTPException(status_code=500, detail=str(exc))


@router.delete(path="/delete/status={status}",
               summary="Delete all tasks according to the status",
               status_code=200)
def delete_all_by_status(status: str,
                         db: Annotated[Session, Depends(get_db)]) -> dict[str, int | str]:
    """
    Deleting all tasks based on the status, example: deleting all "backlog" tasks.

    :param status:
    :param db: the database session
    :return: the task deletion details that come from the delete_all operation
    """
    try:
        manager = get_task_manager(db)
        delete_tasks = manager.deleter.delete_all_by_status(status=status)

        return delete_tasks

    except Exception as exc:
        logger.error(msg=str(exc))
        raise HTTPException(status_code=500, detail=str(exc))

from typing import Annotated, Union

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models import Base
from dependencies import get_db
from schemas import TaskCreate, TaskUpdate, TaskRead
from infrastructures import get_database_stuff
from infrastructures.crud import get_task_manager

engine = get_database_stuff().engine
Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/manager/tasks", tags=["Tasks"])


@router.post(path="/new",
             summary="Creating a new task",
             response_model=dict[int | str, str | int],
             status_code=201)
async def create(task: TaskCreate, db: Annotated[Session, Depends(get_db)]):
    """
    Creating a new task based on the received data.

    :param task: instance of pydantic TaskCreate model
    :param db: the database session
    :return: the task creation details that come from the create operation
    """
    manager = get_task_manager(db=db)
    new_task = manager.creator.create(task=task)

    return new_task


@router.get(path="/all",
            summary="Get all tasks",
            response_model=list[TaskRead],
            status_code=200)
async def get_all(db: Annotated[Session, Depends(get_db)], offset: int = 0, limit: int = 100):
    """
    Getting all tasks based on the offset/limit.

    :param db: the database session
    :param offset: the point at which to start getting
    :param limit: the point at which to stop getting
    :return: a list of tasks (instances of TaskRead)
    """
    manager = get_task_manager(db=db)
    all_tasks = manager.reader.get_all(offset=offset, limit=limit)

    return all_tasks


@router.get(path="/query",
            summary="Get tasks by query",
            response_model=list[TaskRead],
            status_code=200)
async def get_by_query(query: str, db: Annotated[Session, Depends(get_db)]):
    """
    Getting all tasks based on the query.

    :param query: the search query
    :param db: the database session
    :return: a list of tasks (instances of TaskRead)
    """
    manager = get_task_manager(db)
    tasks_by_query = manager.reader.get_by_query(query=query)

    return tasks_by_query


@router.get(path="/{task_id}",
            summary="Get task by id",
            response_model=Union[TaskRead, dict[int, str]],
            status_code=200)
async def get_by_id(task_id: int, db: Annotated[Session, Depends(get_db)]):
    """
    Getting a task based on the task's ID.

    :param task_id: the task's id
    :param db: the database session
    :return: a single task (instance of TaskRead)
    """
    manager = get_task_manager(db)
    task_by_id = manager.reader.get_by_id(task_id=task_id)

    return task_by_id


@router.put(path="/update/{task_id}",
            summary="Update task by id",
            response_model=dict[int | str, str | int],
            status_code=200)
async def update(task_id: int, task: TaskUpdate, db: Annotated[Session, Depends(get_db)]):
    """
    Updating a task based on the task's ID with the updated fields.

    :param task_id: the task's id
    :param task: instance of pydantic TaskUpdate model (updated fields)
    :param db: the database session
    :return: the task modification details that come from the update operation
    """
    manager = get_task_manager(db)
    update_task = manager.updater.update(task_id=task_id, task=task)

    return update_task


@router.delete(path="/delete/all",
               summary="Delete all tasks",
               response_model=dict[int, str],
               status_code=200)
async def delete_all(db: Annotated[Session, Depends(get_db)]):
    """
    Deleting all tasks at once.

    :param db: the database session
    :return: the task deletion details that come from the delete_all operation
    """
    manager = get_task_manager(db)
    delete_tasks = manager.deleter.delete_all()

    return delete_tasks


@router.delete(path="/delete/{task_id}",
               summary="Delete task by id",
               response_model=dict[int | str, str | int],
               status_code=200)
async def delete_by_id(task_id: int, db: Annotated[Session, Depends(get_db)]):
    """
    Deleting a task based on the task's ID.

    :param db: the database session
    :param task_id: the task's id
    :return: the task deletion details that come from the delete_by_id operation
    """
    manager = get_task_manager(db)
    delete_task = manager.deleter.delete_by_id(task_id=task_id)

    return delete_task

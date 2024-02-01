from dataclasses import dataclass
from typing import Type

from sqlalchemy import or_
from sqlalchemy.orm import Session

from models import Task
from schemas import TaskCreate, TaskUpdate
from utils import get_config, get_logger

database_cfg = get_config().database
level = database_cfg.log_level
logger = get_logger(level=level)


class Creator:
    """
    Responsible to create new records in the tasks table in the database.
    """

    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, task: TaskCreate) -> dict[int | str, str | int]:
        """
        Creating a new record based on the provided data.

        :param task: instance of pydantic TaskCreate model
        :return: the task creation details.
        """
        if task.attachment_url:
            task.attachment_url = str(task.attachment_url)

        task_db = Task(**task.model_dump())

        self.db.add(task_db)
        self.db.commit()
        self.db.refresh(task_db)

        return {201: "Successfully Created!", "id": task_db.id}


class Reader:
    """
    Responsible to read/get the records from the tasks table in the database.
    """

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self, offset: int, limit: int) -> list[Type[Task]]:
        """
        Getting all records based on the provided offset/limit.

        :param offset: the point at which to start reading
        :param limit: the point at which to stop reading
        :return: a list of records (instances of Task model)
        """
        tasks_db = self.db.query(Task).offset(offset=offset).limit(limit=limit).all()

        return tasks_db

    def get_by_query(self, query: str) -> list[Type[Task]]:
        """
        Getting all records based on the provided query according to one of these:

        - title
        - priority
        - status

        :param query: the search query used to find the records
        :return: a list of records (instances of Task model)
        """
        if query in ["1", "2", "3", "4"]:
            tasks_db = self.db.query(Task).filter(Task.priority == int(query)).all()

            return tasks_db

        tasks_db = self.db.query(Task).filter(or_(Task.title.ilike(f"%{query}%"),
                                                  Task.status == query)).all()
        return tasks_db

    def get_by_id(self, task_id: int) -> Type[Task] | dict[int, str]:
        """
        Getting a record based on the provided ID.

        :param task_id: the task's id
        :return: a single record (instance of Task model)
        """
        task_db = self.db.query(Task).filter(Task.id == task_id).first()

        if not task_db:  # pragma: no cover
            logger.error(f"404: Task's id {task_id} not found!")
            return {404: f"Task's id {task_id} not found!"}

        return task_db


class Updater:
    """
    Responsible to update the records in the tasks table in the database.
    """

    def __init__(self, db: Session) -> None:
        self.db = db

    def update(self, task_id: int, task: TaskUpdate) -> dict[int | str, str | int]:
        """
        Updating a record based on the provided ID with the updated data.

        :param task_id: the task's id
        :param task: instance of pydantic TaskUpdate model (updated data)
        :return: the task modification details
        """
        db_task = self.db.query(Task).filter(Task.id == task_id).first()

        if not db_task:  # pragma: no cover
            logger.error(f"404: Updating failed, Task's id {task_id} not found!")
            return {404: f"Updating failed, Task's id {task_id} not found!"}

        updated_data = task.model_dump(exclude_unset=True)

        if "attachment_url" in updated_data:  # pragma: no cover
            updated_data["attachment_url"] = str(updated_data["attachment_url"])

        for key, value in updated_data.items():
            setattr(db_task, key, value)

        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)

        return {200: "Successfully Updated!", "id": task_id}


class Deleter:
    """
    Responsible to delete the records in the tasks table in the database.
    """

    def __init__(self, db: Session) -> None:
        self.db = db

    def delete_all(self) -> dict[int, str]:
        """
        Deleting all records from the table, making it empty.

        :return: the tasks deletion details
        """
        self.db.query(Task).delete()
        self.db.commit()

        return {200: "Tasks Successfully Deleted!"}

    def delete_by_id(self, task_id: int) -> dict[int | str, str | int]:
        """
        Deleting a record based on the provided ID.

        :param task_id: the task's id
        :return: the task deletion details
        """
        db_task = self.db.query(Task).filter(Task.id == task_id).first()

        if not db_task:  # pragma: no cover
            logger.error(f"404: Deletion failed, Task's id {task_id} not found!")
            return {404: f"Deletion failed, Task's id {task_id} not found!"}

        self.db.delete(db_task)
        self.db.commit()

        return {200: "Successfully Deleted!", "id": task_id}


@dataclass(frozen=True)
class Manager:
    """
    Represents the interface for managing the CRUD operations.
    """
    creator: Creator
    reader: Reader
    updater: Updater
    deleter: Deleter


def get_task_manager(db: Session) -> Manager:
    """
    Getting the manager of the CRUD operations.

    :param db: the database session
    :return: instance of Manager
    """
    creator = Creator(db=db)
    reader = Reader(db=db)
    updater = Updater(db=db)
    deleter = Deleter(db=db)

    manager = Manager(creator=creator, reader=reader, updater=updater, deleter=deleter)

    return manager

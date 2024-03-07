from dataclasses import dataclass
from typing import Type

from sqlalchemy import or_
from sqlalchemy.orm import Session

from models import Task
from schemas import TaskRequest


class Creator:
    """
    Responsible to create new records in the tasks table in the database.
    """

    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, task: TaskRequest) -> dict[str, int | str]:
        """
        Creating a new record based on the provided data.

        :param task: instance of pydantic TaskCreate model
        :return: the task creation details.
        """
        task_db = Task(**task.model_dump())

        if not task_db:  # pragma: no cover
            return {"status": 404,
                    "message": "Task Creation Failed!"}

        self.db.add(task_db)
        self.db.commit()
        self.db.refresh(task_db)

        return {"status": 201,
                "message": "Successfully Created!",
                "id": task_db.id}


class Reader:
    """
    Responsible to read/get the records from the tasks table in the database.
    """

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> list[Type[Task]] | dict[str, int | str]:
        """
        Getting all records at once.

        :return: a list of records (instances of Task model)
        """
        tasks_db = self.db.query(Task).all()

        return tasks_db

    def get_by_query(self, query: str) -> list[Type[Task]] | dict[str, int | str]:
        """
        Getting all records based on the provided query according to one of these:

        - title
        - priority
        - label

        :param query: the search query used to find the records
        :return: a list of records (instances of Task model)
        """
        tasks_db = self.db.query(Task).filter(or_(Task.title.ilike(f"%{query}%"),
                                                  Task.label == query,
                                                  Task.priority == query)).all()
        return tasks_db


class Updater:
    """
    Responsible to update the records in the tasks table in the database.
    """

    def __init__(self, db: Session) -> None:
        self.db = db

    def update(self, task_id: int, task: TaskRequest) -> dict[str, int | str]:
        """
        Updating a record based on the provided ID with the updated data.

        :param task_id: the task's id
        :param task: instance of pydantic TaskUpdate model (updated data)
        :return: the task modification details
        """
        db_task = self.db.query(Task).filter(Task.id == task_id).first()

        if not db_task:  # pragma: no cover
            return {"status": 404,
                    "message": "Updating failed, task not found!",
                    "id": task_id}

        updated_data = task.model_dump(exclude_unset=True)

        for key, value in updated_data.items():
            setattr(db_task, key, value)

        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)

        return {"status": 200,
                "message": "Successfully Updated!",
                "id": task_id}


class Deleter:
    """
    Responsible to delete the records in the tasks table in the database.
    """

    def __init__(self, db: Session) -> None:
        self.db = db

    def delete_all_by_status(self, status: str) -> dict[str, int | str]:
        """
        Deleting all records from the table, making it empty.
        :param status: the status of the task
        :return: the tasks deletion details
        """
        if status not in ["backlog", "todo", "in progress", "done"]:  # pragma: no cover
            return {"status": 404,
                    "message": "Invalid status value"}

        self.db.query(Task).filter(Task.status == status).delete()
        self.db.commit()

        return {"status": 200,
                "message": "Tasks Successfully Deleted!"}

    def delete_by_id(self, task_id: int) -> dict[str, int | str]:
        """
        Deleting a record based on the provided ID.

        :param task_id: the task's id
        :return: the task deletion details
        """
        db_task = self.db.query(Task).filter(Task.id == task_id).first()

        if not db_task:  # pragma: no cover
            return {"status": 404,
                    "message": "Deletion failed, task not found!",
                    "id": task_id}

        self.db.delete(db_task)
        self.db.commit()

        return {"status": 200,
                "message": "Successfully Deleted!",
                "id": task_id}


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

    manager = Manager(creator=creator,
                      reader=reader,
                      updater=updater,
                      deleter=deleter)

    return manager

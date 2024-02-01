from typing import Optional

from enum import Enum
from datetime import datetime, timedelta

from pydantic import BaseModel, HttpUrl


class Priority(int, Enum):
    """
    Represents the special values for the task's priority.

    - low(1): it's not really important.
    - medium(2): maybe it's important.
    - high(3): it's important.
    - critical(4): it's very important.
    """
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


class Status(str, Enum):
    """
    Represents the special values for the task's status.
    """
    TODO = "todo"
    IN_PROGRESS = "in progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class TaskBase(BaseModel):
    """
    Represents the foundational schema/structure of the tasks.
    """
    title: str = "Untitled"
    description: Optional[str] = None
    label: Optional[str] = None
    priority: Priority = Priority.MEDIUM.value
    status: Status = Status.TODO.value
    completed_at: datetime = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d %H:%M:%S")

    attachment_url: Optional[HttpUrl] = None
    attachment_file_content: Optional[bytes] = None
    attachment_file_name: Optional[str] = None
    attachment_title: Optional[str] = None


class TaskCreate(TaskBase):
    """
    Represents the schema/structure used for the task's creation.
    """


class TaskUpdate(TaskBase):
    """
    Represents the schema/structure used for the task's modification.
    """


class TaskRead(TaskBase):
    """
    Represents the schema/structure used for reading the tasks.
    """
    id: int
    created_at: datetime
    last_update: datetime

    class ConfigDict:
        """
        Responsible to provide the configuration for Pydantic models.
        """
        from_attributes = True

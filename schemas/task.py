from typing import Optional

from enum import Enum
from datetime import datetime, timedelta

from pydantic import BaseModel


class Priority(str, Enum):
    """
    Represents the special values for the task's priority.
    """
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class Status(str, Enum):
    """
    Represents the special values for the task's status.
    """
    BACKLOG = "backlog"
    TODO = "todo"
    IN_PROGRESS = "in progress"
    DONE = "done"


class TaskRequest(BaseModel):
    """
    Represents the foundational schema/structure of the tasks.
    """
    title: str = "Untitled"
    description: Optional[str] = None
    label: Optional[str] = None
    priority: Priority = Priority.MEDIUM.value
    status: Status = Status.BACKLOG.value
    completed_at: str = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d %H:%M:%S")

    attachment: Optional[str] = None


class TaskResponse(TaskRequest):
    """
    Represents the schema/structure used for reading the tasks.
    """
    id: int
    created_at: str
    last_update: str

    class ConfigDict:
        """
        Responsible to provide the configuration for Pydantic models.
        """
        from_attributes = True

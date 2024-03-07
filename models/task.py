from datetime import datetime, timedelta
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

from infrastructures import Base


class Task(Base):
    """
    Represents the tasks table/entity in the Database.

    - id: Unique ID for the task.
    - title: The Title/Name of the task, default is "Untitled"
    - description: The Description of the task, it's optional.
    - label: Labels for the task, it's optional.
    - priority: The Priority level of the task, default is "medium".
    - status: The Status of the task, default is "backlog".
    - attachment: The Attachment's URL for the task, it's optional.
    - created_at: The Datetime the task was created.
    - last_update: The Datetime the task was last updated.
    - completed_at: The Datetime the task will be finished.
    """
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(index=True, default="Untitled")
    description: Mapped[Optional[str]]
    label: Mapped[Optional[str]]
    priority: Mapped[str] = mapped_column(index=True, default="medium")
    status: Mapped[str] = mapped_column(default="backlog")
    attachment: Mapped[Optional[str]]

    created_at: Mapped[str] = mapped_column(
        default=datetime.now().strftime("%Y-%m-%d %H:%M"))
    last_update: Mapped[str] = mapped_column(
        default=datetime.now().strftime("%Y-%m-%d %H:%M"),
        onupdate=datetime.now().strftime("%Y-%m-%d %H:%M"))
    completed_at: Mapped[str] = mapped_column(
        default=(datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d %H:%M"))

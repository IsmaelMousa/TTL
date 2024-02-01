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
    - priority: The Priority level of the task, default is 2 (medium).
    - status: The Status of the task, default is "todo".
    - attachment_url: The Attachment's URL for the task, it's optional.
    - attachment_file_content: The Attachment's File Content for the task, it's optional.
    - attachment_file_name: The Attachment's File Name for the task, it's optional.
    - attachment_title: The Attachment's Title for the task, it's optional.
    - created_at: The Datetime the task was created.
    - last_update: The Datetime the task was last updated.
    - completed_at: The Datetime the task will be finished.

    Example:
        task = Task(
                    id=1,
                    title="Linkedin Account",
                    description="Creating a new Linkedin account.",
                    label="Social Media",
                    priority=2,
                    status="in progress",
                    attachment_url="https://linkedin.com",
                    attachment_file_content=b"example content" (bytes),
                    attachment_file_name="example",
                    attachment_title="Steps",
                    created_at="2024-01-28 15:42:18",
                    last_update="2024-01-29 12:00:00",
                    completed_at="2024-02-05 12:30:00")
    """
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(index=True, default="Untitled")
    description: Mapped[Optional[str]]
    label: Mapped[Optional[str]]
    priority: Mapped[int] = mapped_column(index=True, default=2)
    status: Mapped[str] = mapped_column(default="todo")

    attachment_url: Mapped[Optional[str]]
    attachment_file_content: Mapped[Optional[bytes]]
    attachment_file_name: Mapped[Optional[str]]
    attachment_title: Mapped[Optional[str]]

    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    last_update: Mapped[datetime] = mapped_column(
        default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        onupdate=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    completed_at: Mapped[datetime] = mapped_column(
        default=(datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d %H:%M:%S"))

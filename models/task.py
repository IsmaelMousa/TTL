from sqlalchemy import Column, Integer, String, ARRAY, DateTime

from infrastructures import Base


class Task(Base):  # pragma: no cover
    """
    **Represents the tasks table/entity in the Database.**

    - **id** (Integer): Unique ID for the task.
    - **title** (String): The Title/Name of the task.
    - **description** (String): The Description of the task, it's optional.
    - **attachments_url** (ARRAY(String)): List of Attachments url for the task, it's optional.
    - **attachments_name** (ARRAY(String)): List of Attachments name for the task, it's optional.
    - **labels** (ARRAY(String)): List of Labels for the task, it's optional.
    - **priority** (Integer): The Priority level of the task.
    - **status** (String): The Status of the task, default is "todo"
    - **created_at** (DateTime): The Datetime the task was created.
    - **completed_at** (DateTime): The Datetime the task will be finished.
    """

    __tablename__ = "tasks"

    id = Column(type_=Integer, primary_key=True)
    title = Column(type_=String, index=True)
    description = Column(type_=String, nullable=True)
    attachments_url = Column(type_=ARRAY(String), nullable=True)
    attachments_name = Column(type_=ARRAY(String), nullable=True)
    labels = Column(type_=ARRAY(String), nullable=True)
    priority = Column(type_=Integer, index=True)
    status = Column(type_=String, default="todo")
    created_at = Column(type_=DateTime)
    completed_at = Column(type_=DateTime)

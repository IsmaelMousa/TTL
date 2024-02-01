from typing import Optional
from datetime import datetime
from unittest import TestCase

from sqlalchemy.orm import Mapped

from models import Task


class TestTaskModel(TestCase):
    """
    Unit tests class for the Task model (tasks table/entity).
    """

    def setUp(self) -> None:
        """
        Setup test variables and values for the columns of the tasks table.

        :return: None
        """
        self.fake_task_dtypes = {"id": Mapped[int],
                                 "title": Mapped[str],
                                 "description": Mapped[Optional[str]],
                                 "label": Mapped[Optional[str]],
                                 "priority": Mapped[int],
                                 "status": Mapped[str],
                                 "attachment_url": Mapped[Optional[str]],
                                 "attachment_file_content": Mapped[Optional[bytes]],
                                 "attachment_file_name": Mapped[Optional[str]],
                                 "attachment_title": Mapped[Optional[str]],
                                 "created_at": Mapped[datetime],
                                 "last_update": Mapped[datetime],
                                 "completed_at": Mapped[datetime]}

    def test_task_model_dtypes(self) -> None:
        """
        Testing if the Task model's columns matches the expected data types.

        :return: None
        """
        fake_dtypes = self.fake_task_dtypes
        dtypes = Task.__annotations__

        for fake_dtype, dtype in zip(fake_dtypes, dtypes):
            self.assertEqual(first=dtypes[dtype],
                             second=fake_dtypes[fake_dtype],
                             msg=f"dtype of: '{dtype}' must be: {fake_dtypes[fake_dtype]}")

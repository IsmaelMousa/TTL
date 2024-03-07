from typing import Optional
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
                                 "priority": Mapped[str],
                                 "status": Mapped[str],
                                 "attachment": Mapped[Optional[str]],
                                 "created_at": Mapped[str],
                                 "last_update": Mapped[str],
                                 "completed_at": Mapped[str]}

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

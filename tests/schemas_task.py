from typing import Optional
from datetime import datetime
from unittest import TestCase

from pydantic import HttpUrl

from schemas.task import Priority, Status, TaskBase, TaskRead


class TestTaskSchema(TestCase):
    """
    Unit tests class for the Task schemas (pydantic task models).
    """

    def setUp(self) -> None:
        """
        Setup test variables and values for the test cases.

        :return: None
        """
        self.fake_priorities = [1, 2, 3, 4]
        self.fake_statuses = ["todo", "in progress", "completed", "cancelled"]
        self.fake_task_base_fields_dtypes = {"title": str,
                                             "description": Optional[str],
                                             "label": Optional[str],
                                             "priority": Priority,
                                             "status": Status,
                                             "completed_at": datetime,
                                             "attachment_url": Optional[HttpUrl],
                                             "attachment_file_content": Optional[bytes],
                                             "attachment_file_name": Optional[str],
                                             "attachment_title": Optional[str]}
        self.fake_task_read_fields_dtypes = {"id": int,
                                             "created_at": datetime,
                                             "last_update": datetime}

    def test_priority_enum_values(self) -> None:
        """
        Testing if the enum values of the priority match the expected values.

        :return: None
        """
        fake_priorities = self.fake_priorities
        priorities = Priority.__members__.values()

        for fake_priority, priority in zip(fake_priorities, priorities):
            self.assertEqual(first=priority,
                             second=fake_priority,
                             msg=f"priority: {priority} must be: {fake_priority}")

    def test_status_enum_values(self) -> None:
        """
        Testing if the enum values of the status match the expected values.

        :return: None
        """
        fake_statuses = self.fake_statuses
        statuses = Status.__members__.values()

        for fake_status, status in zip(fake_statuses, statuses):
            self.assertEqual(first=status,
                             second=fake_status,
                             msg=f"status: {status} must be: {fake_status}")

    def test_task_base_dtypes(self) -> None:
        """
        Testing if the TaskBase model's fields matches the expected data types.

        :return: None
        """
        fake_dtypes = self.fake_task_base_fields_dtypes
        dtypes = TaskBase.__annotations__

        for fake_dtype, dtype in zip(fake_dtypes, dtypes):
            self.assertEqual(first=dtypes[dtype],
                             second=fake_dtypes[fake_dtype],
                             msg=f"dtype of: '{dtype}' must be: {fake_dtypes[fake_dtype]}")

    def test_task_read_dtypes(self) -> None:
        """
        Testing if the TaskRead model's fields matches the expected data types.

        :return: None
        """
        fake_dtypes = self.fake_task_read_fields_dtypes
        dtypes = TaskRead.__annotations__

        for fake_dtype, dtype in zip(fake_dtypes, dtypes):
            self.assertEqual(first=dtypes[dtype],
                             second=fake_dtypes[fake_dtype],
                             msg=f"dtype of: '{dtype}' must be: {fake_dtypes[fake_dtype]}")

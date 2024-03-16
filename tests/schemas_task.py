from typing import Optional
from unittest import TestCase

from schemas.task import Priority, Status, TaskRequest, TaskResponse


class TestTaskSchema(TestCase):
    """
    Unit tests class for the Task schemas (pydantic task models).
    """

    def setUp(self) -> None:
        """
        Setup test variables and values for the test cases.

        :return: None
        """
        self.fake_priorities = ["low", "medium", "high", "critical"]
        self.fake_statuses = ["backlog", "todo", "in progress", "done"]
        self.fake_task_request_fields_dtypes = {"title": str,
                                                "description": Optional[str],
                                                "label": Optional[str],
                                                "priority": Priority,
                                                "status": Status,
                                                "completed_at": str,
                                                "attachment": Optional[str]}
        self.fake_task_response_fields_dtypes = {"id": int,
                                                 "created_at": str,
                                                 "last_update": str}

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

    def test_task_request_dtypes(self) -> None:
        """
        Testing if the TaskRequest model's fields matches the expected data types.

        :return: None
        """
        fake_dtypes = self.fake_task_request_fields_dtypes
        dtypes = TaskRequest.__annotations__

        for fake_dtype, dtype in zip(fake_dtypes, dtypes):
            self.assertEqual(first=dtypes[dtype],
                             second=fake_dtypes[fake_dtype],
                             msg=f"dtype of: '{dtype}' must be: {fake_dtypes[fake_dtype]}")

    def test_task_response_dtypes(self) -> None:
        """
        Testing if the TaskResponse model's fields matches the expected data types.

        :return: None
        """
        fake_dtypes = self.fake_task_response_fields_dtypes
        dtypes = TaskResponse.__annotations__

        for fake_dtype, dtype in zip(fake_dtypes, dtypes):
            self.assertEqual(first=dtypes[dtype],
                             second=fake_dtypes[fake_dtype],
                             msg=f"dtype of: '{dtype}' must be: {fake_dtypes[fake_dtype]}")

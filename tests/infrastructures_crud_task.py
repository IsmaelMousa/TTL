from unittest import TestCase
from unittest.mock import Mock

from sqlalchemy.orm import Session

from infrastructures.crud.task import Manager, get_task_manager
from schemas import TaskRequest
from models import Task


class TestTaskCRUD(TestCase):
    """
    Unit tests class for the CRUD operations on the Task model (tasks table).
    """

    def setUp(self) -> None:
        """
        Setup test variables and initialize the mock database session before each test case.

        :return: None
        """
        self.fake_db = Mock(spec=Session)
        self.fake_manager = get_task_manager(db=self.fake_db)

        self.fake_db.add.reset_mock()
        self.fake_db.commit.reset_mock()
        self.fake_db.refresh.reset_mock()
        self.fake_db.query.reset_mock()
        self.fake_db.delete.reset_mock()

    def test_get_task_manager(self) -> None:
        """
        Testing if the get_task_manager() matches the expected criteria.

        :return: None
        """
        manager = get_task_manager(db=self.fake_db)

        self.assertIsInstance(obj=manager,
                              cls=Manager,
                              msg="get_task_manager() must return an instance of Manager")

    def test_create(self) -> None:
        """
        Testing if the create() operation works as expected.

        :return: None
        """
        fake_new_task = TaskRequest(title="Linkedin",
                                    description="Creating a new Linkedin account.",
                                    label="SM",
                                    priority="high",
                                    status="in progress",
                                    completed_at="2024-02-05 12:30",
                                    attachment="https://linkedin.com/")

        result = self.fake_manager.creator.create(task=fake_new_task)
        status = result["status"]
        message = result["message"]

        fake_status = 201
        fake_message = "Successfully Created!"

        self.fake_db.add.assert_called()
        self.fake_db.commit.assert_called()
        self.fake_db.refresh.assert_called()

        self.assertEqual(first=status,
                         second=fake_status,
                         msg=f"expected status_code: {fake_status}, got {status}")

        self.assertEqual(first=message,
                         second=fake_message,
                         msg=f"expected message: {fake_message}, got {message}")

    def test_get_all(self) -> None:
        """
        Testing if the get_all() operation works as expected.

        :return: None
        """
        result = self.fake_manager.reader.get_all()
        fake_result = self.fake_db.query(Task).all()

        self.fake_db.query.assert_called()
        self.assertEqual(first=result,
                         second=fake_result,
                         msg="values returned by get_all() must match the expected values")

    def test_get_by_query_priority(self) -> None:
        """
        Testing if the get_by_query() operation works as expected
        when the query searches based on the 'priority'.

        :return: None
        """
        fake_priority = "medium"

        result = self.fake_manager.reader.get_by_query(query=fake_priority)
        fake_result = self.fake_db.query(Task).filter(Task.priority == fake_priority).all()

        self.fake_db.query.assert_called()
        self.assertEqual(first=result,
                         second=fake_result,
                         msg="values returned based on 'priority' must match the expected values")

    def test_get_by_query_label(self) -> None:
        """
        Testing if the get_by_query() operation works as expected
        when the query searches based on the 'label'.

        :return: None
        """
        fake_label = "fake label"

        result = self.fake_manager.reader.get_by_query(query=fake_label)
        fake_result = self.fake_db.query(Task).filter(Task.status == fake_label).all()

        self.fake_db.query.assert_called()
        self.assertEqual(first=result,
                         second=fake_result,
                         msg="values returned based on 'label' must match the expected values")

    def test_get_by_query_title(self) -> None:
        """
        Testing if the get_by_query() operation works as expected
        when the query searches based on the 'title'.

        :return: None
        """
        fake_title = "Untitled"

        result = self.fake_manager.reader.get_by_query(query=fake_title)
        fake_result = self.fake_db.query(Task).filter(Task.title.ilike(f"%{fake_title}%")).all()

        self.fake_db.query.assert_called()
        self.assertEqual(first=result,
                         second=fake_result,
                         msg="values returned based on 'title' must match the expected values")

    def test_update(self) -> None:
        """
        Testing if the update() operation works as expected.

        :return: None
        """
        fake_task_id = 1
        fake_updated_data = TaskRequest(title="Linkedin Account", priority="low")

        result = self.fake_manager.updater.update(task_id=fake_task_id, task=fake_updated_data)
        status = result["status"]
        message = result["message"]

        fake_status = 200
        fake_message = "Successfully Updated!"

        self.fake_db.query.assert_called()
        self.fake_db.add.assert_called()
        self.fake_db.commit.assert_called()
        self.fake_db.refresh.assert_called()

        self.assertEqual(first=status,
                         second=fake_status,
                         msg=f"expected message: {fake_status}, got {status}")

        self.assertEqual(first=message,
                         second=fake_message,
                         msg=f"expected message: {fake_message}, got {message}")

    def test_delete_all_by_status(self) -> None:
        """
        Testing if the delete_all_by_status() operation works as expected.

        :return: None
        """
        fake_task_status = "backlog"

        result = self.fake_manager.deleter.delete_all_by_status(status=fake_task_status)
        status = result["status"]
        message = result["message"]

        fake_status = 200
        fake_message = "Tasks Successfully Deleted!"

        self.fake_db.query.assert_called()
        self.fake_db.query(Task).filter().delete.assert_called()

        self.assertEqual(first=status,
                         second=fake_status,
                         msg=f"expected status_code: {fake_status}, got {status}")

        self.assertEqual(first=message,
                         second=fake_message,
                         msg=f"expected status_code: {message}, got {fake_message}")

    def test_delete_by_id(self) -> None:
        """
        Testing if the delete_by_id() operation works as expected.

        :return: None
        """
        fake_task_id = 1

        result = self.fake_manager.deleter.delete_by_id(task_id=fake_task_id)
        status = result["status"]
        message = result["message"]

        fake_status = 200
        fake_message = "Successfully Deleted!"

        self.fake_db.query.assert_called()
        self.fake_db.delete.assert_called()
        self.fake_db.commit.assert_called()

        self.assertEqual(first=status,
                         second=fake_status,
                         msg=f"expected status_code: {fake_status}, got {status}")

        self.assertEqual(first=message,
                         second=fake_message,
                         msg=f"expected status_code: {message}, got {fake_message}")

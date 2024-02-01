from unittest import TestCase
from unittest.mock import MagicMock
from warnings import filterwarnings

from sqlalchemy.orm import Session

from infrastructures.crud.task import Manager, get_task_manager
from schemas import TaskCreate, TaskUpdate
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
        filterwarnings(action="ignore", category=UserWarning)

        self.fake_db = MagicMock(spec=Session)
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
        fake_new_task = TaskCreate(title="Linkedin",
                                   description="Creating a new Linkedin account.",
                                   label="Social Media",
                                   priority=2,
                                   status="in progress",
                                   completed_at="2024-02-05 12:30:00",
                                   attachment_url="https://linkedin.com/",
                                   attachment_file_content=b"example content",
                                   attachment_file_name="example",
                                   attachment_title="Steps")

        result = self.fake_manager.creator.create(task=fake_new_task)

        actual_id = self.fake_db.add.call_args[0][0].id

        fake_result = {201: "Successfully Created!", "id": actual_id}

        self.fake_db.add.assert_called()
        self.fake_db.commit.assert_called()
        self.fake_db.refresh.assert_called()
        self.assertEqual(first=result,
                         second=fake_result,
                         msg="values returned by create() must match the expected values")

    def test_get_all(self) -> None:
        """
        Testing if the get_all() operation works as expected.

        :return: None
        """
        result = self.fake_manager.reader.get_all(offset=0, limit=100)
        fake_result = self.fake_db.query(Task).offset().limit().all()

        self.fake_db.query.assert_called()
        self.assertEqual(first=result,
                         second=fake_result,
                         msg="values returned by get_all() must match the expected values")

    def test_get_by_id(self) -> None:
        """
        Testing if the get_by_id() operation works as expected.

        :return: None
        """
        fake_task_id = 1

        result = self.fake_manager.reader.get_by_id(task_id=fake_task_id)
        fake_result = self.fake_db.query(Task).filter(Task.id == fake_task_id).first()

        self.fake_db.query.assert_called()
        self.assertEqual(first=result,
                         second=fake_result,
                         msg="values returned by get_by_id() must match the expected values")

    def test_get_by_query_priority(self) -> None:
        """
        Testing if the get_by_query() operation works as expected
        when the query searches based on the 'priority'.

        :return: None
        """
        fake_priority = "2"

        result = self.fake_manager.reader.get_by_query(query=fake_priority)
        fake_result = self.fake_db.query(Task).filter(Task.priority == int(fake_priority)).all()

        self.fake_db.query.assert_called()
        self.assertEqual(first=result,
                         second=fake_result,
                         msg="values returned based on 'priority' must match the expected values")

    def test_get_by_query_status(self) -> None:
        """
        Testing if the get_by_query() operation works as expected
        when the query searches based on the 'status'.

        :return: None
        """
        fake_status = "in progress"

        result = self.fake_manager.reader.get_by_query(query=fake_status)
        fake_result = self.fake_db.query(Task).filter(Task.status == fake_status).all()

        self.fake_db.query.assert_called()
        self.assertEqual(first=result,
                         second=fake_result,
                         msg="values returned based on 'status' must match the expected values")

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
        fake_updated_data = TaskUpdate(title="Linkedin Account", priority=4)

        result = self.fake_manager.updater.update(task_id=fake_task_id, task=fake_updated_data)
        fake_result = {200: "Successfully Updated!", "id": fake_task_id}

        self.fake_db.query.assert_called()
        self.fake_db.add.assert_called()
        self.fake_db.commit.assert_called()
        self.fake_db.refresh.assert_called()
        self.assertEqual(first=result,
                         second=fake_result,
                         msg="values returned by update() must match the expected values")

    def test_delete_all(self) -> None:
        """
        Testing if the delete_all() operation works as expected.

        :return: None
        """
        result = self.fake_manager.deleter.delete_all()
        fake_result = {200: "Tasks Successfully Deleted!"}

        self.fake_db.query.assert_called()
        self.fake_db.query(Task).delete.assert_called()
        self.assertEqual(first=result,
                         second=fake_result,
                         msg="values returned by delete_all() must match the expected values")

    def test_delete_by_id(self) -> None:
        """
        Testing if the delete_by_id() operation works as expected.

        :return: None
        """
        fake_task_id = 1

        result = self.fake_manager.deleter.delete_by_id(task_id=fake_task_id)
        fake_result = {200: "Successfully Deleted!", "id": fake_task_id}

        self.fake_db.query.assert_called()
        self.fake_db.delete.assert_called()
        self.fake_db.commit.assert_called()
        self.assertEqual(first=result,
                         second=fake_result,
                         msg="values returned by delete_by_id() must match the expected values")

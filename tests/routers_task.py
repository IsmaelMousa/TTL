from datetime import datetime, timedelta
from unittest import TestCase
from warnings import filterwarnings

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import StaticPool

from infrastructures import Base
from dependencies import get_db
from main import app


class TestTaskRouters(TestCase):
    """
    Unit tests class for the task routers.
    """

    def setUp(self) -> None:
        """
        Setup test variables and values for the test routers.

        :return: None
        """
        filterwarnings(action="ignore", category=UserWarning)
        self.sqlalchemy_database_url = "postgresql://postgres:test@localhost:5432/TestTodo"
        self.engine = create_engine(url=self.sqlalchemy_database_url, poolclass=StaticPool)
        self.testing_session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.db = self.testing_session()
        Base.metadata.create_all(bind=self.engine)

    def override_get_db(self) -> Session:
        """
        Preparing the alternative database session for testing.

        :return: Session
        """
        try:
            yield self.db
        finally:
            self.db.close()

    def get_client_to_test(self) -> TestClient:
        """
        Overriding the database session, and getting the TestClient used for testing the routers.

        :return: TestClient
        """
        app.dependency_overrides[get_db] = self.override_get_db
        client = TestClient(app)
        return client

    def test_create(self) -> None:
        """
        Testing if the create() router works as expected.

        :return: None
        """
        client = self.get_client_to_test()
        data = {"title": "Linkedin",
                "description": "Create Linkedin account.",
                "label": "Social Media",
                "priority": 2,
                "status": "in progress",
                "completed_at": (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d %H:%M:%S"),
                "attachment_url": "https://linkedin.com",
                "attachment_file_content": "example content",
                "attachment_file_name": "example",
                "attachment_title": "Steps"}

        response = client.post(url="/manager/tasks/new", json=data)

        status_code = response.status_code
        fake_status_code = 201

        self.assertEqual(first=status_code,
                         second=fake_status_code,
                         msg=f"expected status_code {fake_status_code}, got {status_code}")

    def test_get_all(self) -> None:
        """
        Testing if the get_all() router works as expected.

        :return: None
        """
        client = self.get_client_to_test()
        query_params = {"offset": 0, "limit": 100}

        response = client.get(url="/manager/tasks/all", params=query_params)

        status_code = response.status_code
        fake_status_code = 200

        self.assertEqual(first=status_code,
                         second=fake_status_code,
                         msg=f"expected status_code {fake_status_code}, got {status_code}")

    def test_get_by_query(self) -> None:
        """
        Testing if the get_by_query() router works as expected.

        :return: None
        """
        client = self.get_client_to_test()
        query_params = {"query": "Untitled"}

        response = client.get(url="/manager/tasks/query", params=query_params)

        status_code = response.status_code
        fake_status_code = 200

        self.assertEqual(first=status_code,
                         second=fake_status_code,
                         msg=f"expected status_code {fake_status_code}, got {status_code}")

    def test_get_by_id(self) -> None:
        """
        Testing if the get_by_id() router works as expected.

        :return: None
        """
        client = self.get_client_to_test()
        task_id = 1

        response = client.get(url=f"/manager/tasks/{task_id}")

        status_code = response.status_code
        fake_status_code = 200

        self.assertEqual(first=status_code,
                         second=fake_status_code,
                         msg=f"expected status_code {fake_status_code}, got {status_code}")

    def test_update(self) -> None:
        """
        Testing if the update() router works as expected.

        :return: None
        """
        client = self.get_client_to_test()
        task_id = 1
        body_params = {"title": "Linkedin Account"}

        response = client.put(url=f"/manager/tasks/update/{task_id}", json=body_params)

        status_code = response.status_code
        fake_status_code = 200

        self.assertEqual(first=status_code,
                         second=fake_status_code,
                         msg=f"expected status_code {fake_status_code}, got {status_code}")

    def test_delete_by_id(self) -> None:
        """
        Testing if the delete_by_id() router works as expected.

        :return: None
        """
        client = self.get_client_to_test()
        task_id = 1

        response = client.delete(url=f"/manager/tasks/delete/{task_id}")

        status_code = response.status_code
        fake_status_code = 200

        self.assertEqual(first=status_code,
                         second=fake_status_code,
                         msg=f"expected status_code {fake_status_code}, got {status_code}")

    def test_delete_all(self) -> None:
        """
        Testing if the delete_all() router works as expected.

        :return: None
        """
        client = self.get_client_to_test()

        response = client.delete(url="/manager/tasks/delete/all")

        status_code = response.status_code
        fake_status_code = 200

        self.assertEqual(first=status_code,
                         second=fake_status_code,
                         msg=f"expected status_code {fake_status_code}, got {status_code}")

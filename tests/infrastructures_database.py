from unittest import TestCase

from utils import get_config
from infrastructures.database import DATABASE_URL


class TestDatabaseURL(TestCase):
    """
    **Unit test class for sqlalchemy database url.**
    """

    def setUp(self) -> None:
        """
        **Setup test values and pattern for DATABASE_URL**

        :return: None
        """

        database_cfg = get_config().database

        self.fake_database_url = "{}://{}:{}@{}:{}/{}".format(database_cfg.driver_name,
                                                              database_cfg.username,
                                                              database_cfg.password,
                                                              database_cfg.host,
                                                              database_cfg.port,
                                                              database_cfg.name)

    def test_database_url(self) -> None:
        """
        **Testing if the DATABASE_URL matches the expected values and pattern.**

        :return: None
        """

        self.assertEqual(first=DATABASE_URL, second=self.fake_database_url)

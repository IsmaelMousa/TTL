from unittest import TestCase

from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker
from utils import get_config
from infrastructures.database import DataBaseStuff, get_database_stuff


class TestDatabaseStuff(TestCase):
    """
    Unit tests class for the database stuff.
    """

    def setUp(self) -> None:
        """
        Setup test variables and values for the stuff of the database.

        :return: None
        """

        database_cfg = get_config().database

        self.fake_database_url = "{}://{}:{}@{}:{}/{}".format(database_cfg.driver_name,
                                                              database_cfg.username,
                                                              database_cfg.password,
                                                              database_cfg.host,
                                                              database_cfg.port,
                                                              database_cfg.name)

    def test_get_database_stuff(self) -> None:
        """
        Testing whether the value returned by the get_database_stuff()
        is an instance of DataBaseStuff, and check if the database stuff
        values matches the expected values.

        :return: None
        """
        database_stuff = get_database_stuff()

        self.assertIsInstance(obj=database_stuff,
                              cls=DataBaseStuff,
                              msg="get_database_stuff() must return instance of DataBaseStuff")

        self.assertIsInstance(obj=database_stuff.engine,
                              cls=Engine,
                              msg="get_database_stuff().engine must be instance of Engine")

        self.assertIsInstance(obj=database_stuff.session,
                              cls=sessionmaker,
                              msg="get_database_stuff().session must be instance of sessionmaker")

        self.assertEqual(first=database_stuff.database_url,
                         second=self.fake_database_url,
                         msg="get_database_stuff().database_url doesn't match the expected values")

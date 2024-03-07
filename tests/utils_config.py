from unittest import TestCase
from utils.config import get_config, Config, AppConfig, DataBaseConfig


class TestConfig(TestCase):
    """
    Unit tests class for the configurations.
    """

    def setUp(self) -> None:
        """
        Setup test variables and values for the configurations.

        :return: None
        """
        self.app_cfg = AppConfig(host="localhost",
                                 port=8000,
                                 path="ttl",
                                 version="1.1.0",
                                 log_level="ERROR")
        self.database_cfg = DataBaseConfig(driver_name="postgresql",
                                           username="postgres",
                                           password="test",
                                           host="localhost",
                                           port=5432,
                                           name="TODO")
        self.cfg = Config(app=self.app_cfg, database=self.database_cfg)

    def test_get_config(self) -> None:
        """
        Testing if the get_config() matches the expected criteria.

        :return: None
        """
        self.assertIsInstance(obj=get_config(),
                              cls=Config,
                              msg="get_config() must return an instance of Config")

        self.assertIsInstance(obj=self.app_cfg,
                              cls=AppConfig,
                              msg="app_cfg must be an instance of AppConfig")

        self.assertIsInstance(obj=self.database_cfg,
                              cls=DataBaseConfig,
                              msg="database_cfg must be an instance of DataBaseConfig")

        self.assertEqual(first=self.cfg,
                         second=get_config(),
                         msg="values returned by get_config() must match the expected values")

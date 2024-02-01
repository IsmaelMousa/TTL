from unittest import TestCase

from utils.config import get_config, AppConfig, DataBaseConfig, Config


class TestConfig(TestCase):
    """
    Unit tests class for the configurations.
    """

    def setUp(self) -> None:
        """
        Setup test variables and values for the configurations.

        :return: None
        """
        fake_app_cfg = AppConfig(name="TTL",
                                 port=8000,
                                 version="1.1.0",
                                 log_level="ERROR")

        fake_database_cfg = DataBaseConfig(name="TODO",
                                           driver_name="postgresql",
                                           username="postgres",
                                           password="test",
                                           host="localhost",
                                           port=5432,
                                           log_level="ERROR")

        self.fake_config = Config(app=fake_app_cfg, database=fake_database_cfg)

    def test_get_config(self) -> None:
        """
        Testing if the get_config() matches the expected criteria.

        :return: None
        """

        cfg = get_config()

        self.assertIsInstance(obj=cfg,
                              cls=Config,
                              msg="get_config() must return instance of Config")

        self.assertEqual(first=cfg,
                         second=self.fake_config,
                         msg="values returned by get_config() must match the expected values")

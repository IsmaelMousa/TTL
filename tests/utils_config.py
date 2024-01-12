from unittest import TestCase

from utils.config import get_config, AppConfig, DataBaseConfig, Config


class TestConfig(TestCase):
    """
    **Unit test class for the configurations.**
    """

    def setUp(self) -> None:
        """
        **Setup test variables for the configurations.**

        :return: None
        """
        fake_app_cfg = AppConfig(name="TODO Task List",
                                 port=8080,
                                 version=1,
                                 log_level="ERROR")

        fake_database_cfg = DataBaseConfig(name="TODO",
                                           driver_name="postgresql",
                                           username="postgres",
                                           password="test",
                                           host="localhost",
                                           port=5432)

        self.fake_config = Config(app=fake_app_cfg, database=fake_database_cfg)

    def test_get_config(self) -> None:
        """
        **Testing get_config function, that must return an instance of the Config.**

        :return: None
        """

        cfg = get_config()

        self.assertIsInstance(obj=cfg,
                              cls=Config,
                              msg="cfg must be an instance of Config!")

        self.assertEqual(first=cfg,
                         second=self.fake_config,
                         msg="expected to be equal!")

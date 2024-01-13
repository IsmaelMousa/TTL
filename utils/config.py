import sys
import os
from dataclasses import dataclass
from functools import lru_cache
from logging import getLogger

from yaml import safe_load, YAMLError


@dataclass(frozen=True)
class AppConfig:
    """
    **The configuration of the Application.**

    - **name**: The name of the application.
    - **port**: The port of the application.
    - **version**: The version of the application.
    - **log_level**: The log level of the application.
    """

    name: str
    port: int
    version: int
    log_level: str


@dataclass(frozen=True)
class DataBaseConfig:
    """
    **The configuration of the Database**.

    - **name**: The name of the Database.
    - **username**: The username to connect to the Database.
    - **password**: The password associated with the provided username.
    - **host**: The host where the Database server is running.
    - **port**: The port number on which the Database server is listening for connections.
    """

    name: str
    driver_name: str
    username: str
    password: str
    host: str
    port: int


@dataclass(frozen=True)
class Config:
    """
    **The base of all configurations.**

    - **app**: Represents the configuration of the Application.
    - **databases**: Represents the configuration of the Database.
    """

    app: AppConfig
    database: DataBaseConfig


@lru_cache(maxsize=1)
def get_config() -> Config:
    """
    **Getting the base of all configurations**

    :return: instance of Config
    """

    base_path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_path, "../config.yaml")

    logger = getLogger()

    try:
        with open(path, "r") as file:
            configurations: dict = safe_load(file)

            app_cfg: dict = configurations.get("app", {})
            database_cfg: dict = configurations.get("database", {})

            app = AppConfig(name=app_cfg.get("name"),
                            port=app_cfg.get("port"),
                            version=app_cfg.get("version"),
                            log_level=app_cfg.get("logLevel"))

            database = DataBaseConfig(name=database_cfg.get("name"),
                                      driver_name=database_cfg.get("driverName"),
                                      username=database_cfg.get("username"),
                                      password=database_cfg.get("password"),
                                      host=database_cfg.get("host"),
                                      port=database_cfg.get("port"))

            config = Config(app=app, database=database)

        return config

    except IOError:  # pragma: no cover
        logger.error(f"unable to open the config file with path {path}!")
        sys.exit(os.EX_IOERR)

    except YAMLError:  # pragma: no cover
        logger.error("unable to parse the config file!")
        sys.exit(os.EX_IOERR)

import os
from dataclasses import dataclass
from functools import lru_cache

from yaml import safe_load, YAMLError

from errors import UnhandledError


@dataclass(frozen=True)
class AppConfig:
    """
    Represents the interface of the application's configuration.
    """

    host: str
    port: int
    path: str
    version: str
    log_level: str


@dataclass(frozen=True)
class DataBaseConfig:
    """
    Represents the interface of the database's configuration.
    """

    driver_name: str
    username: str
    password: str
    host: str
    port: int
    name: str


@dataclass(frozen=True)
class Config:
    """
    Represents the interface of the base configurations.

    - app: Application's configuration.
    - databases: Database's configuration.
    """

    app: AppConfig
    database: DataBaseConfig


@lru_cache(maxsize=1)
def get_config() -> Config:
    """
    Getting the base configurations.

    :return: instance of Config
    """

    base_path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_path, "../config.yml")

    try:
        with open(path, "r") as file:
            configurations: dict = safe_load(file)

            app_cfg: dict = configurations.get("app", {})
            database_cfg: dict = configurations.get("database", {})

            app = AppConfig(host=app_cfg.get("host"),
                            port=app_cfg.get("port"),
                            path=app_cfg.get("path"),
                            version=app_cfg.get("version"),
                            log_level=app_cfg.get("logLevel"))

            database = DataBaseConfig(driver_name=database_cfg.get("driverName"),
                                      username=database_cfg.get("username"),
                                      password=database_cfg.get("password"),
                                      host=database_cfg.get("host"),
                                      port=database_cfg.get("port"),
                                      name=database_cfg.get("name"))

            config = Config(app=app, database=database)

        return config
    except IOError:  # pragma: no cover
        raise IOError(f"Unable to open the config file with path {path}")

    except YAMLError:  # pragma: no cover
        raise YAMLError("Unable to parse the config file")

    except Exception as exc:  # pragma: no cover
        raise UnhandledError(exc) from None

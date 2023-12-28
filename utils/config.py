import sys
import os
from dataclasses import dataclass
from functools import lru_cache
from logging import getLogger

from yaml import safe_load, YAMLError


@dataclass(frozen=True)
class AppConfig:
    """TODO: Docstring for AppConfig."""
    name: str
    port: int
    version: int
    log_level: str


@dataclass(frozen=True)
class Config:
    """TODO: Docstring for Config."""
    app: AppConfig


@lru_cache(maxsize=1)
def get_config() -> Config:
    """ TODO: Docstring for get_config."""

    base_path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_path, "../config.yaml")

    logger = getLogger()

    try:
        with open(path, "r") as file:
            configurations: dict = safe_load(file)

            app_cfg: dict = configurations.get("app", {})

            app = AppConfig(name=app_cfg.get("name"),
                            port=app_cfg.get("port"),
                            version=app_cfg.get("version"),
                            log_level=app_cfg.get("logLevel"))

            config = Config(app=app)

        return config

    except IOError:  # pragma: no cover
        logger.error(f"unable to open the config file with path {path}!")
        sys.exit(os.EX_IOERR)

    except YAMLError:  # pragma: no cover
        logger.error("unable to parse the config file!")
        sys.exit(os.EX_IOERR)

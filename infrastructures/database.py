import sys
from dataclasses import dataclass

from sqlalchemy.engine import Engine, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import NoSuchModuleError, ArgumentError

from utils import get_config, get_logger


@dataclass(frozen=True)
class DataBaseStuff:
    """
    Represents the interface for database components.
    """
    database_url: str
    engine: Engine
    session: sessionmaker


def get_database_stuff() -> DataBaseStuff:
    """
    Getting the database components.

    :return: instance of DataBaseStuff
    """

    database_cfg = get_config().database
    level = database_cfg.log_level
    logger = get_logger(level=level)

    try:
        database_url = "{}://{}:{}@{}:{}/{}".format(database_cfg.driver_name,
                                                    database_cfg.username,
                                                    database_cfg.password,
                                                    database_cfg.host,
                                                    database_cfg.port,
                                                    database_cfg.name)
        engine = create_engine(url=database_url)
        session = sessionmaker(bind=engine)

        database_stuff = DataBaseStuff(database_url=database_url,
                                       engine=engine,
                                       session=session)

        return database_stuff

    except NoSuchModuleError as exc:  # pragma: no cover
        logger.error(exc)
        sys.exit(1)

    except ArgumentError as exc:  # pragma: no cover
        logger.error(exc)
        sys.exit(1)

    except ValueError as exc:  # pragma: no cover
        logger.error(exc)
        sys.exit(1)

    except KeyError as exc:  # pragma: no cover
        logger.error(f"Invalid key: {exc}")
        sys.exit(1)

    except Exception as exc:  # pragma: no cover
        logger.error(f"Unhandled Exception: {exc}")
        sys.exit(1)


Base = declarative_base()

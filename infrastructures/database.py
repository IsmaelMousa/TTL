from dataclasses import dataclass

from sqlalchemy.engine import Engine, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import NoSuchModuleError, ArgumentError

from errors import UnhandledError, DataBaseConnectionError
from utils import get_config


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

    except (NoSuchModuleError, ArgumentError, ValueError, KeyError) as exc:  # pragma: no cover
        raise DataBaseConnectionError(exc) from None

    except Exception as exc:  # pragma: no cover
        raise UnhandledError(exc) from None


Base = declarative_base()

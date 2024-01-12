import sys
from logging import getLogger

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import NoSuchModuleError, ArgumentError

from utils import get_config

logger = getLogger()

try:
    database_cfg = get_config().database

    DATABASE_URL = "{}://{}:{}@{}:{}/{}".format(database_cfg.driver_name,
                                                database_cfg.username,
                                                database_cfg.password,
                                                database_cfg.host,
                                                database_cfg.port,
                                                database_cfg.name)

    engine = create_engine(url=DATABASE_URL)
    session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()

except (NoSuchModuleError, ArgumentError, ValueError) as exc:  # pragma: no cover
    logger.error(f"{type(exc).__name__}: in {__name__} module: {exc}!")
    sys.exit(1)

except Exception as exc:  # pragma: no cover
    logger.error(f"Unhandled Exception: in {__name__} module: {exc}!")
    sys.exit(1)

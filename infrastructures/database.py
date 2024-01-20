import sys

from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import NoSuchModuleError, ArgumentError

from utils import get_config, get_logger

database_cfg = get_config().database
logger = get_logger(level=database_cfg.log_level)

try:
    DATABASE_URL = "{}://{}:{}@{}:{}/{}".format(database_cfg.driver_name,
                                                database_cfg.username,
                                                database_cfg.password,
                                                database_cfg.host,
                                                database_cfg.port,
                                                database_cfg.name)

    engine = create_engine(url=DATABASE_URL)
    session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()

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

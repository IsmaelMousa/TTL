from fastapi.exceptions import ValidationException

from infrastructures import get_database_stuff
from utils import get_config, get_logger

Session = get_database_stuff().session


def get_db() -> Session:
    """
    Responsible for opening the database session and closing it after each request.

    :return: the database session (instance of Session)
    """
    app_cfg = get_config().app
    level = app_cfg.log_level
    logger = get_logger(level=level)

    db = Session()

    try:
        yield db

    except ValidationException as exc:  # pragma: no cover
        logger.error(f"Unprocessable Entity: {exc}")

    except Exception as exc:  # pragma: no cover
        logger.error(f"Unhandled Exception: {exc}")

    finally:
        db.close()

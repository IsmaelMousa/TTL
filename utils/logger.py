from logging import Logger, getLogger, StreamHandler, Formatter

from errors import LogLevelError


def get_logger(level: str) -> Logger:
    """
    Getting the logger according to a specified level.

    :param level: logging level
    :return: Logger for the specified level
    """

    custom_fmt = ('{"datetime": "%(asctime)s",'
                  ' "level": "%(levelname)s",'
                  ' "pathname": "%(pathname)s",'
                  ' "message": "%(message)s"}')

    custom_date_fmt = "%b %d %Y %-I:%M %p"

    try:
        logger = getLogger(name=__name__)
        handler = StreamHandler()
        formatter = Formatter(fmt=custom_fmt, datefmt=custom_date_fmt)

        handler.setFormatter(fmt=formatter)
        logger.setLevel(level=level.upper())
        logger.addHandler(hdlr=handler)

        return logger

    except ValueError:  # pragma: no cover
        raise LogLevelError(f"Invalid logging level: {level}") from None

    except Exception as exc:  # pragma: no cover
        raise exc

from json import dumps
from datetime import datetime
from logging import Logger, getLogger, StreamHandler, Formatter

from errors import LogLevelError, UnhandledError


class JSONFormatter(Formatter):
    """
    A custom json formatter for the logging messages.
    """

    def formatTime(self, record, datefmt="%Y-%m-%d %H:%M:%S") -> datetime.date:
        """
        Override formatTime to use the specified datetime format.

        :param record: the record to format
        :param datefmt: the specified datetime format
        :return: the formatted datetime
        """
        fmt_datetime = datetime.fromtimestamp(record.created).strftime(datefmt)

        return fmt_datetime

    def format(self, record) -> str:
        """
        override format to use the specified logging format.
        """
        custom_fmt = {"time": self.formatTime(record=record),
                      "level": record.levelname,
                      "pathname": record.pathname,
                      "message": record.getMessage()}

        return dumps(obj=custom_fmt)


def get_logger(level: str) -> Logger:
    """
    Getting the logger according to a specified level.

    :param level: logging level
    :return: Logger for the specified level
    """
    try:
        logger = getLogger(name=__name__)
        handler = StreamHandler()
        formatter = JSONFormatter()

        handler.setFormatter(fmt=formatter)
        logger.setLevel(level=level.upper())
        logger.addHandler(hdlr=handler)

        return logger

    except ValueError:  # pragma: no cover
        raise LogLevelError(f"Invalid logging level: {level}") from None

    except Exception as exc:  # pragma: no cover
        raise UnhandledError(exc) from None

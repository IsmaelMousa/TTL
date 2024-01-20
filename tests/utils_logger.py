from unittest import TestCase

from testfixtures import log_capture

from utils import get_logger


class TestLogger(TestCase):
    """
    Unit tests class for the logger.
    """

    @log_capture()
    def test_get_logger(self, capture) -> None:
        """
        Testing if the log sequence match the expected sequence.

        :param capture: Log capture
        :return: None
        """
        logger = get_logger(level="DEBUG")

        logger.debug(msg="fake debug message")
        logger.info(msg="fake info message")
        logger.warning(msg="fake warning message")
        logger.error(msg="fake error message")
        logger.critical(msg="fake critical message")

        capture.check(
            ("utils.logger", "DEBUG", "fake debug message"),
            ("utils.logger", "INFO", "fake info message"),
            ("utils.logger", "WARNING", "fake warning message"),
            ("utils.logger", "ERROR", "fake error message"),
            ("utils.logger", "CRITICAL", "fake critical message"),
        )

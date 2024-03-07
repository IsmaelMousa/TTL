class LogLevelError(Exception):
    """
    Occurs when using none of these valid levels:

    - DEBUG
    - INFO
    - WARNING
    - ERROR
    - CRITICAL
    """


class DataBaseConnectionError(Exception):
    """
    Occurs when there is an error while connecting to the database, potential reasons:

    - Invalid url format
    - Invalid driver
    - Invalid username
    - Invalid password
    - Invalid database name
    - Database does not exist
    - Database already exists
    """


class UnhandledError(Exception):
    """
    Generic exception raised when an unhandled exception occurs.
    """

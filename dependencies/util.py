from infrastructures import get_database_stuff

Session = get_database_stuff().session


def get_db() -> Session:
    """
    Responsible for opening the database session and closing it after each request.

    :return: the database session (instance of Session)
    """
    db = Session()
    try:
        yield db

    finally:
        db.close()

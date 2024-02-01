from unittest import TestCase

from sqlalchemy.orm import Session

from dependencies import get_db


class TestUtilDependencies(TestCase):
    """
    Unit tests for the util/common dependencies.
    """

    def test_get_db(self):
        """
        Testing if the get_db() matches the expected criteria.
        """
        db = next(get_db())
        self.assertIsInstance(obj=db,
                              cls=Session,
                              msg="get_db() must generate an instance of Session")

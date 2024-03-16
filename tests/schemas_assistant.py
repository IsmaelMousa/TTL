from unittest import TestCase

from schemas import ChatAssistantRequest, ChatAssistantResponse


class TestChatAssistantSchema(TestCase):
    """
    Unit tests class for the ChatAssistant schemas (pydantic chat assistant models).
    """

    def setUp(self) -> None:
        """
        Setup test variables and values for the test cases.

        :return: None
        """
        self.fake_assistant_request_fields_dtypes = {"question": str}
        self.fake_assistant_response_fields_dtypes = {"answer": str}

    def test_chat_assistant_request_dtypes(self) -> None:
        """
        Testing if the ChatAssistantRequest model's fields matches the expected data types.

        :return: None
        """
        fake_dtypes = self.fake_assistant_request_fields_dtypes
        dtypes = ChatAssistantRequest.__annotations__

        for fake_dtype, dtype in zip(fake_dtypes, dtypes):
            self.assertEqual(first=dtypes[dtype],
                             second=fake_dtypes[fake_dtype],
                             msg=f"dtype of: '{dtype}' must be: {fake_dtypes[fake_dtype]}")

    def test_chat_assistant_response_dtypes(self) -> None:
        """
        Testing if the ChatAssistantResponse model's fields matches the expected data types.

        :return: None
        """
        fake_dtypes = self.fake_assistant_response_fields_dtypes
        dtypes = ChatAssistantResponse.__annotations__

        for fake_dtype, dtype in zip(fake_dtypes, dtypes):
            self.assertEqual(first=dtypes[dtype],
                             second=fake_dtypes[fake_dtype],
                             msg=f"dtype of: '{dtype}' must be: {fake_dtypes[fake_dtype]}")

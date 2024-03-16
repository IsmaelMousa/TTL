from unittest import TestCase
from unittest.mock import Mock, patch
from assistants import chat
from schemas import ChatAssistantResponse


class TestChatAssistant(TestCase):
    """
    Unit tests class for the chat assistant transformers model.
    """

    def setUp(self) -> None:
        """
        Setup test variables and values for the chat assistant.

        :return: None
        """
        self.fake_generated_text = "This is a generated answer."
        self.fake_question = "What is the meaning of life?"

    @patch("assistants.chat.pipeline")
    def test_get_answer(self, mock_pipeline) -> None:
        """
        Testing if the chat assistant works as expected according to the inputs.

        :return: None
        """
        mock_pipeline.return_value = Mock(return_value=
                                          [{"generated_text": self.fake_generated_text}])

        result = chat.get_answer(question=self.fake_question)

        self.assertIsInstance(obj=result,
                              cls=ChatAssistantResponse,
                              msg="get_answer() must return an instance of ChatAssistantResponse")

        self.assertIsInstance(obj=result.answer,
                              cls=str,
                              msg="the answer of ChatAssistantResponse must be string")

        self.assertEqual(first=result.answer,
                         second=self.fake_generated_text,
                         msg="values returned by get_answer() must match the expected values")

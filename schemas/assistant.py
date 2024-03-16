from pydantic import BaseModel


class ChatAssistantRequest(BaseModel):
    """
    Represents the request schema/structure of the chat assistant.
    """
    question: str


class ChatAssistantResponse(BaseModel):
    """
    Represents the response schema/structure of the chat assistant.
    """
    answer: str

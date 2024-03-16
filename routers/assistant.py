from fastapi import APIRouter, HTTPException

from schemas import ChatAssistantResponse
from assistants import chat
from utils import get_config, get_logger

router = APIRouter(prefix="/manager/assistants", tags=["Assistants"])

app_cfg = get_config().app
chat_model_cfg = get_config().chat_model

name = chat_model_cfg.name
level = app_cfg.log_level
logger = get_logger(level=level)


@router.get(path=f"/{name}",
            summary=f"Get the answer from {name} model",
            status_code=200)
def get_chat_answer(question: str) -> ChatAssistantResponse:
    """
    Getting the chat generated answer from the transformer model, according to the question.
    
    :param question: the user question
    :return: the chat generated answer
    """
    try:
        answer = chat.get_answer(question=question)

        return answer

    except Exception as exc:
        logger.error(msg=str(exc))
        raise HTTPException(status_code=500, detail=str(exc))

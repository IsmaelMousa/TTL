from transformers import pipeline

from utils import get_config
from schemas import ChatAssistantResponse


def get_answer(question: str) -> ChatAssistantResponse:
    """
    Getting the generated answer from the transformers model according to the input question.

    :param question: the text question
    :return: the generated text answer
    """
    cfg = get_config()
    model_cfg = cfg.chat_model

    assistant = pipeline(task=model_cfg.task,
                         model=model_cfg.checkpoint,
                         tokenizer=model_cfg.checkpoint)

    answer = ChatAssistantResponse(answer=assistant(question, max_length=300)[0]["generated_text"])

    return answer

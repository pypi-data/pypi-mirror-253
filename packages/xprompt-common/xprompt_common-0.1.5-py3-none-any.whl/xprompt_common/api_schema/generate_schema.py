from enum import Enum
from typing import Any, Optional

from pydantic import BaseModel


# Request


class OpenAIMessage(BaseModel):
    role: str
    content: str
    function_call: Optional[dict[str, str]] = None

    # Extra message
    byte_content: Optional[bytes] = None


class OpenAIRequest(BaseModel):
    """
    {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "Say this is a test!"}],
        "temperature": 0.7
    }
    """

    model: str
    messages: list[OpenAIMessage]
    functions: Optional[list[dict[str, Any]]] = None
    temperature: float = 0
    top_p: float = 1

    @classmethod
    def create_from_api_request(cls, api_request: dict[str, Any]):
        return cls(**api_request)


# Response


class OpenAIUsage(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class OpenAIChoice(BaseModel):
    index: int
    message: OpenAIMessage
    finish_reason: str


class OpenAIResponse(BaseModel):
    """
    {
        "id": "chatcmpl-abc123",
        "object": "chat.completion",
        "created": 1677858242,
        "model": "gpt-3.5-turbo-0613",
        "usage": {
            "prompt_tokens": 13,
            "completion_tokens": 7,
            "total_tokens": 20
        },
        "choices": [
            {
                "message": {
                    "role": "assistant",
                    "content": "\n\nThis is a test!"
                },
                "finish_reason": "stop",
                "index": 0
            }
        ]
    }
    """

    id: str
    object: str
    created: int
    model: str
    choices: list[OpenAIChoice]
    usage: OpenAIUsage

    # gptcache params
    is_cached: bool = False

    @classmethod
    def create_from_api_response(cls, api_response: dict[str, Any]):
        return cls(**api_response)


class CachePolicy(BaseModel):
    user_id: int


class OpenAIClientType(Enum):
    CHAT_COMPLETION = "chat_completion"
    COMPLETION = "completion"
    EMBEDDING = "embedding"


class AnswerQuality(BaseModel):
    answer_corroboration_count: int = 0
    include_confidence: bool = False


class OutputFormat(Enum):
    """convert text to some other types"""

    AUDIO = "audio"


class RichRequest(OpenAIRequest):
    client_type: OpenAIClientType
    openai_api_key: str
    cache_policy: Optional[CachePolicy] = None
    answer_quality: Optional[AnswerQuality] = None


class OutputConversionRequest(BaseModel):
    text: str
    output_format: Optional[OutputFormat] = None


class ResponseStatus(str, Enum):
    COMPLETED = "completed"
    RECEIVED = "received"
    FAILED = "failed"
    PENDING = "pending"


class AnswerQualityResponse(BaseModel):
    pass_corroboration: Optional[bool] = None
    controversial_tokens: Optional[list[str]] = None
    confidence_score: Optional[int] = None


class ParsingInfo(BaseModel):
    token_saved: Optional[int]
    compression_ratio: Optional[float]

    def update_new(self, info):
        cur_dict = self.dict()
        cur_dict.update(info.dict())
        return ParsingInfo(**cur_dict)


class RichResponse(OpenAIResponse):
    status: ResponseStatus
    request_id: Optional[str]
    answer_quality: Optional[AnswerQualityResponse]
    prompt_messages: list[OpenAIMessage]
    parsing_info: Optional[ParsingInfo]

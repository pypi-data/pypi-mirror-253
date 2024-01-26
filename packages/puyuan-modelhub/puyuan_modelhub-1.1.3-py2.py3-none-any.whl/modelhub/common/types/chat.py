from typing import Dict, Optional, List, Union, Any
from typing_extensions import TypedDict, NotRequired
from openai.types.chat import (
    ChatCompletionToolParam,
    ChatCompletionToolChoiceOptionParam,
    completion_create_params,
)
import httpx
from .message import BaseMessage


class BaseParameters(TypedDict):
    history: NotRequired[List[BaseMessage]]


class OpenAIParameters(BaseParameters):
    frequency_penalty: NotRequired[float]
    function_call: NotRequired[completion_create_params.FunctionCall]
    functions: NotRequired[List[completion_create_params.Function]]
    logit_bias: NotRequired[Dict[str, int]]
    max_tokens: NotRequired[int]
    n: NotRequired[int]
    presence_penalty: NotRequired[float]
    response_format: NotRequired[completion_create_params.ResponseFormat]
    seed: NotRequired[int]
    stop: NotRequired[Union[Optional[str], List[str]]]
    temperature: NotRequired[float]
    tool_choice: NotRequired[ChatCompletionToolChoiceOptionParam]
    tools: NotRequired[List[ChatCompletionToolParam]]
    top_p: NotRequired[float]
    user: NotRequired[str]
    timeout: NotRequired[float]


class BaichuanParameters(BaseParameters):
    temperature: NotRequired[float]
    top_p: NotRequired[float]
    top_k: NotRequired[int]
    with_search_enhance: NotRequired[bool]


class ChatGLMParameters(BaseParameters):
    temperature: NotRequired[float]
    top_p: NotRequired[float]


class GeminiGenerationConfig(TypedDict):
    candidate_count: NotRequired[int]
    stop_sequences: NotRequired[List[str]]
    max_output_tokens: NotRequired[int]
    temperature: NotRequired[float]
    top_p: NotRequired[float]
    top_k: NotRequired[int]


class GeminiParameters(BaseParameters):
    generation_config: NotRequired[GeminiGenerationConfig]


class ChatGLM2Parameters(BaseParameters):
    max_length: NotRequired[int]
    top_p: NotRequired[float]
    temperature: NotRequired[float]


class ChatGLM3Parameters(ChatGLM2Parameters):
    role: NotRequired[str]


ChatParameters = Union[
    OpenAIParameters,
    BaichuanParameters,
    ChatGLMParameters,
    GeminiParameters,
    ChatGLM2Parameters,
    ChatGLM3Parameters,
    Dict[str, Any],
]

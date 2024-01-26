from fastapi.responses import JSONResponse
from typing import Dict, Optional, Any, List, Literal
from .base import BaseModel
from .message import BaseMessage


class GenerationParams(BaseModel):
    inputs: str
    parameters: Dict[str, Any] = {}


class TextGenerationStreamToken(BaseModel):
    id: int = 0
    text: str
    logprob: float = 0
    special: bool = False


class TextGenerationDetails(BaseModel):
    finish_reason: Optional[str] = None
    request_time: Optional[float] = None
    prompt_tokens: Optional[int] = None
    generated_tokens: Optional[int] = None
    seed: Optional[int] = None
    tokens: Optional[List[TextGenerationStreamToken]] = None


class BaseOutput(BaseModel):
    success: bool = True
    code: int = 200
    msg: str = "success"

    def to_response(self):
        return JSONResponse(self.dict(), status_code=self.code)

    class Config:
        extra = "allow"


class TextGenerationStreamOutput(BaseOutput):
    token: TextGenerationStreamToken
    generated_text: Optional[str] = None
    history: List[Dict[str, Any]] = []
    details: Optional[TextGenerationDetails] = None


class StreamErrorOutput(TextGenerationStreamOutput):
    success: bool = False
    code: int = 500
    msg: str = "error"
    token: TextGenerationStreamToken = TextGenerationStreamToken(text="error")
    details: Optional[TextGenerationDetails] = TextGenerationDetails(
        finish_reason="error"
    )


class TextGenerationOutput(BaseOutput):
    generated_text: str
    history: List[BaseMessage] = []
    details: Optional[TextGenerationDetails] = None


class ErrorMessage(BaseOutput):
    code: int = 500
    success: bool = False
    msg: str = "failed"


class ModelInfo(BaseModel):
    types: List[Literal["chat", "embedding", "audio", "reranker"]]


class ModelInfoOutput(BaseOutput):
    models: Dict[str, ModelInfo]


class ModelParamsOutput(BaseOutput):
    param_schema: Dict[str, Any]


class NTokensOutput(BaseOutput):
    n_tokens: int


class EmbeddingOutput(BaseOutput):
    embeddings: List[List[float]]

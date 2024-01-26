import pydantic

if pydantic.VERSION < "2.0.0":
    from pydantic import BaseModel
else:
    from pydantic.v1 import BaseModel
import httpx
from httpx import Response
import os
from modelhub.common.types import (
    TextGenerationOutput,
    BaseMessage,
    ModelInfo,
    ModelInfoOutput,
    NTokensOutput,
    Transcription,
    TextGenerationStreamOutput,
    EmbeddingOutput,
    ChatParameters,
    CrossEncoderParams,
    CrossEncoderOutput,
)
from .errors import (
    APIConnectionError,
    APIRateLimitError,
    AuthenticationError,
    InternalServerError,
)
from typing import Dict, List, Any, Literal, Generator, Optional, Union
import modelhub.common.constants as constants
import json
import retrying
from io import TextIOWrapper


class ModelhubClient(BaseModel):
    """
    ModelhubClient: A Python client for the Modelhub API
    """

    user_name: str = os.getenv("MODELHUB_USER_NAME", "")
    """user name for authentication"""
    user_password: str = os.getenv("MODELHUB_USER_PASSWORD", "")
    """user password for authentication"""
    host: str = os.getenv("MODELHUB_HOST", "")
    model: str = ""
    max_retries: int = 3
    wait_fixed: int = 1000
    timeout: Optional[httpx.Timeout | float] = 600
    """host URL of the Modelhub API"""
    """list of supported models"""
    headers: Dict[str, Any] = {}

    class Config:
        arbitrary_types_allowed = True
        extra = "forbid"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.headers["Authorization"] = f"{self.user_name}:{self.user_password}"
        self.host = self.host.rstrip("/")

    @property
    def supported_models(self) -> Dict[str, ModelInfo]:
        return self._get_supported_models()

    def raise_for_status(self, response: Response, status_code: int, text: str):
        if status_code == constants.ERR_AUTH_FAILED:
            raise AuthenticationError()
        if status_code == constants.ERR_ISE:
            raise InternalServerError(text)
        if status_code == constants.ERR_API_CONNECTION_ERROR:
            raise APIConnectionError(text)
        if status_code == constants.ERR_API_RATE_LIMIT:
            raise APIRateLimitError(text)
        response.raise_for_status()

    @retrying.retry(
        wait_fixed=wait_fixed,
        stop_max_attempt_number=max_retries,
        retry_on_exception=lambda e: not isinstance(e, AuthenticationError),
    )
    def _post(
        self,
        url: str,
        method: Literal["get", "post"] = "post",
        **kwargs,
    ) -> Response:
        """Make a GET request"""
        response = getattr(httpx, method)(
            url=url, timeout=self.timeout, headers=self.headers, **kwargs
        )
        self.raise_for_status(response, response.status_code, response.text)
        return response

    @retrying.retry(
        wait_fixed=wait_fixed,
        stop_max_attempt_number=max_retries,
        retry_on_exception=lambda e: not isinstance(e, AuthenticationError),
    )
    async def _apost(self, url: str, **kwargs) -> Response:
        async with httpx.AsyncClient() as client:
            r = await client.post(
                url, headers=self.headers, timeout=self.timeout, **kwargs
            )
            self.raise_for_status(r, r.status_code, r.text)
            return r

    def _get_supported_models(self) -> ModelInfoOutput:
        """Get a list of supported models from the Modelhub API"""
        response = self._post(
            self.host + "/models",
            method="get",
        )
        return ModelInfoOutput(**response.json()).models

    def get_supported_params(self, model: str) -> List[str]:
        """
        Get a list of supported parameters for a given model from the Modelhub API
        params:
            model: the model name
        """
        response = self._post(
            self.host + "/models/" + model,
            method="get",
        )
        return response.json()["params"]

    def n_tokens(self, prompt: str, model: str = "", params={}) -> NTokensOutput:
        """
        Get the number of tokens in a prompt
        params:
            prompt: the prompt
            model: the model name
        """
        model = model or self.model
        if model not in self.supported_models:
            raise ValueError(f"Model {model} not supported")
        response = self._post(
            self.host + "/tokens",
            json={
                "prompt": prompt,
                "model": model,
                "params": params,
            },
        )
        return NTokensOutput(**response.json())

    def chat(
        self,
        prompt: str,
        model: str = "",
        history: List[Union[BaseMessage, Dict[str, Any]]] = [],
        parameters: ChatParameters = {},
    ) -> TextGenerationOutput:
        model = model or self.model
        if (model not in self.supported_models) or (
            "chat" not in self.supported_models[model].types
        ):
            raise ValueError(f"Model {model} not supported")

        parameters["history"] = [
            m.dict() if isinstance(m, BaseMessage) else m for m in history
        ]
        response = self._post(
            self.host + "/chat",
            json={
                "prompt": prompt,
                "model": model,
                "parameters": parameters,
            },
        )
        out = TextGenerationOutput(**response.json())
        return out

    async def achat(
        self,
        prompt: str,
        model: str = "",
        history: List[BaseMessage] = [],
        parameters: ChatParameters = {},
    ) -> TextGenerationOutput:
        model = model or self.model
        if (model not in self.supported_models) or (
            "chat" not in self.supported_models[model].types
        ):
            raise ValueError(f"Model {model} not supported")

        parameters["history"] = [
            m.dict() if isinstance(m, BaseMessage) else m for m in history
        ]
        response = await self._apost(
            self.host + "/chat",
            json={
                "prompt": prompt,
                "model": model,
                "parameters": parameters,
            },
        )
        out = TextGenerationOutput(**response.json())
        return out

    @retrying.retry(wait_fixed=wait_fixed, stop_max_attempt_number=max_retries)
    def stream_chat(
        self,
        prompt: str,
        model: str = "",
        history: List[BaseMessage] = [],
        parameters: Dict[str, Any] = {},
    ) -> Generator[TextGenerationStreamOutput, None, None]:
        model = model or self.model
        if (model not in self.supported_models) or (
            "chat" not in self.supported_models[model].types
        ):
            raise ValueError(f"Model {model} not supported")

        parameters["history"] = [
            m.dict() if isinstance(m, BaseMessage) else m for m in history
        ]
        with httpx.stream(
            "post",
            url=self.host + "/chat",
            headers=self.headers,
            timeout=self.timeout,
            json={
                "prompt": prompt,
                "model": model,
                "parameters": parameters,
                "stream": True,
            },
        ) as r:
            for line in r.iter_lines():
                if line.startswith("data:"):
                    out = TextGenerationStreamOutput(**json.loads(line[5:]))
                    self.raise_for_status(r, out.code, out.msg)
                    yield out

    @retrying.retry(wait_fixed=wait_fixed, stop_max_attempt_number=max_retries)
    async def astream_chat(
        self,
        prompt: str,
        model: str = "",
        history: List[BaseMessage] = [],
        parameters: Dict[str, Any] = {},
    ) -> Generator[TextGenerationStreamOutput, None, None]:
        model = model or self.model
        if (model not in self.supported_models) or (
            "chat" not in self.supported_models[model].types
        ):
            raise ValueError(f"Model {model} not supported")

        parameters["history"] = [
            m.dict() if isinstance(m, BaseMessage) else m for m in history
        ]
        async with httpx.AsyncClient() as client:
            async with client.stream(
                "post",
                url=self.host + "/chat",
                headers=self.headers,
                timeout=self.timeout,
                json={
                    "prompt": prompt,
                    "model": model,
                    "parameters": parameters,
                    "stream": True,
                },
            ) as r:
                async for line in r.aiter_lines():
                    if line.startswith("data:"):
                        out = TextGenerationStreamOutput(**json.loads(line[5:]))
                        self.raise_for_status(r, out.code, out.msg)
                        yield out

    def get_embeddings(
        self, prompt: str, model: str = "", parameters: Dict[str, Any] = {}
    ) -> EmbeddingOutput:
        """
        Get embeddings from a model
        params:
            prompt: the prompt to start the chat
            model: the model name
            parameters: the parameters for the model
        """
        model = model or self.model
        if (model not in self.supported_models) or (
            "embedding" not in self.supported_models[model].types
        ):
            raise ValueError(f"Model {model} not supported")

        response = self._post(
            self.host + "/embedding",
            json={
                "prompt": prompt,
                "model": model,
                "parameters": parameters,
            },
        )
        return EmbeddingOutput(**response.json())

    async def aget_embeddings(
        self, prompt: str, model: str = "", parameters: Dict[str, Any] = {}
    ) -> EmbeddingOutput:
        model = model or self.model
        if (model not in self.supported_models) or (
            "embedding" not in self.supported_models[model].types
        ):
            raise ValueError(f"Model {model} not supported")

        response = await self._apost(
            self.host + "/embedding",
            json={
                "prompt": prompt,
                "model": model,
                "parameters": parameters,
            },
        )
        return EmbeddingOutput(**response.json())

    def cross_embedding(
        self,
        sentences: List[List[str]],
        model: str = "",
        parameters: CrossEncoderParams = {},
    ) -> CrossEncoderOutput:
        """
        Performs predicts with the CrossEncoder on the given sentence pairs.
        :param sentences: A list of sentence pairs [[Sent1, Sent2], [Sent3, Sent4]]
        """
        model = model or self.model
        if (model not in self.supported_models) or (
            "reranker" not in self.supported_models[model].types
        ):
            raise ValueError(f"Model {model} not supported")
        res = self._post(
            self.host + "/cross_embedding",
            json={
                "sentences": sentences,
                "model": model,
                "parameters": parameters,
            },
        )
        return CrossEncoderOutput(**res.json())

    async def across_embedding(
        self,
        sentences: List[List[str]],
        model: str = "",
        parameters: CrossEncoderParams = {},
    ) -> CrossEncoderOutput:
        model = model or self.model
        if (model not in self.supported_models) or (
            "reranker" not in self.supported_models[model].types
        ):
            raise ValueError(f"Model {model} not supported")
        res = await self._apost(
            self.host + "/across_embedding",
            json={
                "sentences": sentences,
                "model": model,
                "parameters": parameters,
            },
        )
        return CrossEncoderOutput(**res.json())

    def transcribe(
        self,
        file: str | TextIOWrapper,
        model: str = "",
        language: str = "",
        temperature: float = 0.0,
    ) -> Transcription:
        model = model or self.model
        if (model not in self.supported_models) or (
            "audio" not in self.supported_models[model].types
        ):
            raise ValueError(f"Model {model} not supported")

        if isinstance(file, str):
            file = open(file, "rb")

        r = self._post(
            url=self.host + "/audio/transcriptions",
            files={"file": file},
            data={
                "model": model,
                "language": language,
                "temperature": temperature,
            },
        )
        self.raise_for_status(r, r.status_code, r.text)
        return Transcription(**r.json())

    async def atranscribe(
        self,
        file: str | TextIOWrapper,
        model: str = "",
        language: str = "",
        temperature: float = 0.0,
    ) -> Transcription:
        model = model or self.model
        if (model not in self.supported_models) or (
            "audio" not in self.supported_models[model].types
        ):
            raise ValueError(f"Model {model} not supported")

        if isinstance(file, str):
            file = open(file, "rb")

        r = await self._apost(
            url=self.host + "/audio/transcriptions",
            files={"file": file},
            data={
                "model": model,
                "language": language,
                "temperature": temperature,
            },
        )
        self.raise_for_status(r, r.status_code, r.text)
        return Transcription(**r.json())


class VLMClient(ModelhubClient):
    """Visual Language Model Client"""

    def chat(self, prompt, image_path, model="cogvlm", parameters={}, **kwargs):
        """
        Chat with a model
        params:
            prompt: the prompt to start the chat
            image_path: the path to the image
            model: the model name
            parameters: the parameters for the model
        """
        image_path = self._post(
            self.host + "/upload",
            files={"file": open(image_path, "rb")},
            params={
                "user_name": self.user_name,
                "user_password": self.user_password,
            },
        ).json()["file_path"]
        parameters["image_path"] = image_path
        return super().chat(prompt=prompt, model=model, parameters=parameters, **kwargs)

# Description

📦 ModelhubClient: A Python client for the Modelhub. Support various models including LLMs, embedding models, audio models and multi-modal models. These models are implemented by either 3rdparty APIs or self-host instances.

# Installation

```shell
pip install puyuan_modelhub --user
```


# Quick Start 

## ModelhubClient

### Initialization
```python
from modelhub import ModelhubClient

client = ModelhubClient(
    host="https://modelhub.puyuan.tech/api/",
    user_name="xxxx",
    user_password="xxxx",
    model="xxx", # Optional
)
```

### Get supported models

```python
client.supported_models
```

### Create a stateless chat
```python
response = client.chat(
    query,
    model="xxx", # Optional(be None to use the model specific in initialization)
    history=history,
    parameters=dict(
        key1=value1,
        key2=value2
    )
)
```

## Get embeddings

```python
client.get_embeddings(["你好", "Hello"], model="m3e")
```

## Context Compression/Distillation

Chat using [lingua](https://github.com/microsoft/LLMLingua) will return a compressed/distillated context. Currently we use `Llama-2-7B-Chat-GPTQ` as LLMlingua backend. Theorically, any local model(Baichuan, ChatGLM, etc.) which can be loaded using `AutoModelForCasualLM` can be used as the backend, thus should provide a `compress` API for every local model, this is a future work since `LLMlingua` doesn't support it naively.

Parameters for `lingua` model:

```python
client.chat(
    prompt: str,
    model = "lingua",
    history: List[Dict[str, str]],
    parameters = dict(
        question: str = "",
        ratio: float = 0.5,
        target_token: float = -1,
        iterative_size: int = 200,
        force_context_ids: List[int] = None,
        force_context_number: int = None,
        use_sentence_level_filter: bool = False,
        use_context_level_filter: bool = True,
        use_token_level_filter: bool = True,
        keep_split: bool = False,
        keep_first_sentence: int = 0,
        keep_last_sentence: int = 0,
        keep_sentence_number: int = 0,
        high_priority_bonus: int = 100,
        context_budget: str = "+100",
        token_budget_ratio: float = 1.4,
        condition_in_question: str = "none",
        reorder_context: str = "original",
        dynamic_context_compression_ratio: float = 0.0,
        condition_compare: bool = False,
        add_instruction: bool = False,
        rank_method: str = "llmlingua",
        concate_question: bool = True,
    )
)
```

## Async Support

Every sync method has the corresponding async one starts with "a"(See [API Documentation](#ModelhubClient) below). For example:

Use async mechanism to make concurrent requests.

**Note** Unlike API models, local models are now single threaded, requested will be queued when using async. In the future, we need to adopt a more flexible inference pipeline. [Github Topic](https://github.com/topics/llm-inference)

```python
import anyio

async with anyio.create_task_group() as tg:
    async def query(question):
        print(await client.achat(question, model="gpt-3.5-turbo"))
    questions = ["hello", "nihao", "test", "test1", "test2"]
    for q in questions:
        tg.start_soon(query, q)
```

### `gemini-pro` embedding need extra parameters

Use the `embed_content` method to generate embeddings. The method handles embedding for the following tasks (`task_type`):

|Task Type |	Description|
|----------|---------------|
|RETRIEVAL_QUERY |	Specifies the given text is a query in a search/retrieval setting.|
|RETRIEVAL_DOCUMENT	|Specifies the given text is a document in a search/retrieval setting. Using this task type requires a `title`. |
|SEMANTIC_SIMILARITY|	Specifies the given text will be used for Semantic Textual Similarity (STS).|
|CLASSIFICATION	|Specifies that the embeddings will be used for classification.|
|CLUSTERING	|Specifies that the embeddings will be used for clustering.|


## Response

```yaml
generated_text: response_text from model
history: generated history, **only chatglm3 return this currently.**
details: generation details. Include tokens used, request duration, ...
```

## History Parameter

You can either use list of pre-defined message types or raw dicts containing `role` and `content` KV as history.

**Note that not every model support role type like `system`**

```python
# import some pre-defined message types
from modelhub.common.types import SystemMessage, AIMessage, UserMessage
# construct history of your own
history = [
    SystemMessage(content="xxx", other_value="xxxx"),
    UserMessage(content="xxx", other="xxxx"),
]
```

## VLMClient (Deprecated)

**No Visual Language Models are hosted currently, cogvlm specifically. And this Client will be migrated to ModelhubClient in the future.**

### Initailization
```python
from modelhub import VLMClient
client = VLMClient(...)
client.chat(prompt=..., image_path=..., parameters=...)
```

### Chat with model

VLM Client chat add `image_path` param to Modelhub Client and other params are same.

```python
client.chat("Hello?", image_path="xxx", model="m3e")
```

## OpenAI Client

**Only a small subset of models are supported to use in this manner currently. Others will rasie Exception.**

```python
from openai import OpenAI

client = OpenAI(
    api_key=f"{user_name}:{user_password}",
    base_url="https://modelhub.puyuan.tech/api/v1"
)

client.chat.completions.create(..., model="self-host-models")
```

# Examples

## Use ChatCLM3 for tools calling

```python
from modelhub import ModelhubClient, VLMClient
from modelhub.common.types import SystemMessage

client = ModelhubClient(
    host="https://xxxxx/api/",
    user_name="xxxxx",
    user_password="xxxxx",
)
tools = [
    {
        "name": "track",
        "description": "追踪指定股票的实时价格",
        "parameters": {
            "type": "object",
            "properties": {"symbol": {"description": "需要追踪的股票代码"}},
            "required": ["symbol"],
        },
    },
    {
        "name": "text-to-speech",
        "description": "将文本转换为语音",
        "parameters": {
            "type": "object",
            "properties": {
                "text": {"description": "需要转换成语音的文本"},
                "voice": {"description": "要使用的语音类型（男声、女声等）"},
                "speed": {"description": "语音的速度（快、中等、慢等）"},
            },
            "required": ["text"],
        },
    },
]

# construct system history
history = [
    SystemMessage(
        content="Answer the following questions as best as you can. You have access to the following tools:",
        tools=tools,
    )
]
query = "帮我查询股票10111的价格"

# call ChatGLM3
response = client.chat(query, model="ChatGLM3", history=history)
history = response.history
print(response.generated_text)
```
```shell
Output:
{"name": "track", "parameters": {"symbol": "10111"}}
```

```python
# generate a fake result for track function call

result = {"price": 1232}

res = client.chat(
    json.dumps(result),
    parameters=dict(role="observation"), # Tell ChatGLM3 this is a function call result
    model="ChatGLM3",
    history=history,
)
print(res.generated_text)
```

```shell
Output:
根据API调用结果，我得知当前股票的价格为1232。请问您需要我为您做什么？
```
# Contact

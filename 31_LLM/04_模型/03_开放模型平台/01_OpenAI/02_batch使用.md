# 1. 简介

- 24小时内跑出结果，非实时，但更便宜，接近半价
- 实测虽说时24小时，但实际跑一个任务，大概无需等待

使用文档：https://platform.openai.com/docs/guides/batch/overview
- batch usage: https://platform.openai.com/docs/guides/batch/getting-started
- price: https://openai.com/api/pricing/
- embed api: https://platform.openai.com/docs/api-reference/embeddings

注意：
- custom_id必须是字符串
- 任务数量有限。比如原本是96个文章，96个任务可以正常跑，切割成1280个，token数不变，但是会报错 (也可能是你本地的网络限制)

# 2. 使用

## 2.1 准备jsonl数据

- GPT接口：/v1/chat/completions
- embedding接口：/v1/embeddings

文件里写明调用的模型接口，并按照平时的接口调用格式写如数据。其中custom_id是任务的唯一标识，用于后续查看任务状态，必须是字符串类型

```json
{"custom_id": "request-1", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gpt-3.5-turbo-0125", "messages": [{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": "Hello world!"}],"max_tokens": 1000}}
{"custom_id": "request-2", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "gpt-3.5-turbo-0125", "messages": [{"role": "system", "content": "You are an unhelpful assistant."},{"role": "user", "content": "Hello world!"}],"max_tokens": 1000}}
```

## 2.2 上传文件

```python
from openai import OpenAI
client = OpenAI()

batch_input_file = client.files.create(
  file=open("batchinput.jsonl", "rb"),
  purpose="batch"
)
```

## 2.3 创建任务

注意：
- completion_window必须写24小时
- batch_input_file变量来源上一步

```python
batch_input_file_id = batch_input_file.id

client.batches.create(
    input_file_id=batch_input_file_id,
    endpoint="/v1/chat/completions",
    completion_window="24h",
    metadata={
      "description": "nightly eval job"
    }
)
```

返回结果如下：

```python
{
  "id": "batch_abc123",
  "object": "batch",
  "endpoint": "/v1/chat/completions",
  "errors": null,
  "input_file_id": "file-abc123",
  "completion_window": "24h",
  "status": "validating",
  "output_file_id": null,
  "error_file_id": null,
  "created_at": 1714508499,
  "in_progress_at": null,
  "expires_at": 1714536634,
  "completed_at": null,
  "failed_at": null,
  "expired_at": null,
  "request_counts": {
    "total": 0,
    "completed": 0,
    "failed": 0
  },
  "metadata": null
}
```

你需要记录id用于后续查看任务状态

## 2.4 查看任务状态

```python
from openai import OpenAI
client = OpenAI()

client.batches.retrieve("batch_abc123")
```

返回结果中：
- status为任务状态
- request_counts为任务完成和失败数量
- output_file_id为结果文件id

## 2.5 下载结果

其中文件id来自上一步

```python
from openai import OpenAI
client = OpenAI()

file_response = client.files.content("file-xyz123")
print(file_response.text)
```

输出结果如下：
```json
{"id": "batch_req_123", "custom_id": "request-2", "response": {"status_code": 200, "request_id": "req_123", "body": {"id": "chatcmpl-123", "object": "chat.completion", "created": 1711652795, "model": "gpt-3.5-turbo-0125", "choices": [{"index": 0, "message": {"role": "assistant", "content": "Hello."}, "logprobs": null, "finish_reason": "stop"}], "usage": {"prompt_tokens": 22, "completion_tokens": 2, "total_tokens": 24}, "system_fingerprint": "fp_123"}}, "error": null}
{"id": "batch_req_456", "custom_id": "request-1", "response": {"status_code": 200, "request_id": "req_789", "body": {"id": "chatcmpl-abc", "object": "chat.completion", "created": 1711652789, "model": "gpt-3.5-turbo-0125", "choices": [{"index": 0, "message": {"role": "assistant", "content": "Hello! How can I assist you today?"}, "logprobs": null, "finish_reason": "stop"}], "usage": {"prompt_tokens": 20, "completion_tokens": 9, "total_tokens": 29}, "system_fingerprint": "fp_3ba"}}, "error": null}
```

```text
注意：上述结果可能存在乱序，需要使用之前的任务id去对应
```

## 2.6 取消任务

```python
from openai import OpenAI
client = OpenAI()

client.batches.cancel("batch_abc123")
```

## 2.8 获取任务列表

```python
from openai import OpenAI
client = OpenAI()

client.batches.list(limit=10)
```

# 3. 限制

- 每个batch最多50,000个请求
- batch文件最多100M
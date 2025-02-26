import argparse
import functools
import os

from transformers import AutoTokenizer

from userdef import UserDef as BaseUserDef

max_tokens = 512
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3-8B-Instruct")

default_system_prompt = """You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.

If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information."""

system_prompt = default_system_prompt if os.environ.get("SYSTEM_PROMPT") == "1" else ""
base_url = os.environ.get("BASE_URL", "http://localhost:3000")


@functools.lru_cache(maxsize=8)
def get_prompt_set(min_input_length=0, max_input_length=500):
    """
    return a list of prompts with length between min_input_length and max_input_length
    """
    import json
    import requests
    import os

    # check if the dataset is cached
    if os.path.exists("databricks-dolly-15k.jsonl"):
        print("Loading cached dataset")
        with open("databricks-dolly-15k.jsonl", "r") as f:
            dataset = [json.loads(line) for line in f.readlines()]
    else:
        print("Downloading dataset")
        raw_dataset = requests.get(
            "https://huggingface.co/datasets/databricks/databricks-dolly-15k/resolve/main/databricks-dolly-15k.jsonl"
        )
        content = raw_dataset.content
        open("databricks-dolly-15k.jsonl", "wb").write(content)
        dataset = [json.loads(line) for line in content.decode().split("\n")]
        print("Dataset downloaded")

    for d in dataset:
        d["question"] = d["context"] + d["instruction"]
        d["input_tokens"] = len(tokenizer(d["question"])["input_ids"])
        d["output_tokens"] = len(tokenizer(d["response"]))
    return [
        d["question"]
        for d in dataset
        if min_input_length <= d["input_tokens"] <= max_input_length
    ]

prompts = get_prompt_set(30, 150)


class UserDef(BaseUserDef):
    BASE_URL = base_url
    PROMPTS = prompts

    @classmethod
    def make_request(cls):
        import json
        import random

        prompt = random.choice(cls.PROMPTS)
        headers = {"Content-Type": "application/json"}
        url = f"{cls.BASE_URL}/generate"
        data = {
            "prompt": prompt,
            "system_prompt": system_prompt,  # this is important because there's a default system prompt
            "max_tokens": max_tokens,
        }
        return url, headers, json.dumps(data)

    @staticmethod
    def parse_response(chunk: bytes):
        import json
        text = chunk.decode("utf-8").strip()
        return tokenizer.encode(text, add_special_tokens=False)


if __name__ == "__main__":
    import asyncio
    from common import start_benchmark_session

    # arg parsing
    parser = argparse.ArgumentParser(description="Benchmark")
    parser.add_argument("--max_users", type=int, required=True)
    parser.add_argument("--session_time", type=float, default=None)
    parser.add_argument("--ping_correction", action="store_true")
    args = parser.parse_args()

    asyncio.run(start_benchmark_session(args, UserDef))
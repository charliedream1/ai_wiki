import asyncio
from openllm_llama2_20_prompt import UserDef as BaseUserDef
from common import get_prompt_set, start_benchmark_session


class UserDef(BaseUserDef):
    @classmethod
    def make_request(cls):
        import openllm
        import json
        import random

        prompt = random.choice(get_prompt_set(300, 500))

        headers = {"accept": "application/json", "Content-Type": "application/json"}
        config = (
            openllm.AutoConfig.for_model("llama")
            .model_construct_env(max_new_tokens=200, top_p=0.21)
            .model_dump()
        )
        data = {"prompt": prompt, "llm_config": config, "adapter_name": None}
        url = f"{cls.BASE_URL}/v1/generate_stream"
        return url, headers, json.dumps(data)


if __name__ == "__main__":
    asyncio.run(start_benchmark_session(UserDef))

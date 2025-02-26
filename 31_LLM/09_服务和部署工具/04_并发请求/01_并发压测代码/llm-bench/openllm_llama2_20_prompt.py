from common import start_benchmark_session, get_tokenizer, get_prompt_set
import asyncio

class UserDef:
    # BASE_URL = "http://llama27bchat-org-ss-org-1--aws-us-east-1.mt2.bentoml.ai"
    # BASE_URL= "http://llama2-7b-org-ss-org-1--aws-us-east-1.mt2.bentoml.ai"
    # BASE_URL = "http://llama2-13b-org-ss-org-1--aws-us-east-1.mt2.bentoml.ai"
    # BASE_URL = "http://184.105.5.107:3000"
    BASE_URL = "http://184.105.217.197:3000"  # Aaron's machine

    @classmethod
    def ping_url(cls):
        return f"{cls.BASE_URL}/healthz"

    @classmethod
    def make_request(cls):
        """
        return url, headers, body
        """
        import openllm
        import json
        import random

        prompt = random.choice(get_prompt_set(15, 25))

        headers = {"accept": "application/json", "Content-Type": "application/json"}
        config = (
            openllm.AutoConfig.for_model("llama")
            .model_construct_env(max_new_tokens=20, top_p=0.21)
            .model_dump()
        )
        data = {"prompt": prompt, "llm_config": config, "adapter_name": None}
        url = f"{cls.BASE_URL}/v1/generate_stream"
        return url, headers, json.dumps(data)

    @classmethod
    def parse_response(cls, chunk):
        """
        take chunk and return list of tokens, used for token counting
        """
        text = chunk.decode("utf-8").strip()
        return get_tokenizer()(text)

    @staticmethod
    async def rest():
        import asyncio

        await asyncio.sleep(0.01)


if __name__ == "__main__":
    asyncio.run(start_benchmark_session(UserDef))

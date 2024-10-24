from openai import OpenAI

client = OpenAI(api_key="EMPTY", base_url="http://localhost:8000/v1/")
print(client.models.list())

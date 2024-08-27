import dashscope
from http import HTTPStatus

# 或者：export DASHSCOPE_API_KEY=YOUR_DASHSCOPE_API_KEY
api_key = ""


def embed_with_str():
    resp = dashscope.TextEmbedding.call(
        model=dashscope.TextEmbedding.Models.text_embedding_v3,
        api_key=api_key,  # 如果您没有配置环境变量，请将您的APIKEY填写在这里
        # api_key=os.getenv('DASHSCOPE_API_KEY'),  # 如果您没有配置环境变量，请将您的APIKEY填写在这里
        # input='衣服的质量杠杠的，很漂亮，不枉我等了这么久啊，喜欢，以后还来这里买')
        input=['你好', '1'])
    if resp.status_code == HTTPStatus.OK:
        print(resp)
    else:
        print(resp)


if __name__ == '__main__':
    embed_with_str()

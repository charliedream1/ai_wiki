
import os
import qianfan

# 使用安全认证AK/SK鉴权，通过环境变量方式初始化；替换下列示例中参数，安全认证Access Key替换your_iam_ak，Secret Key替换your_iam_sk
os.environ["QIANFAN_ACCESS_KEY"] = ""
os.environ["QIANFAN_SECRET_KEY"] = ""

emb = qianfan.Embedding()

resp = emb.do(model="Embedding-V1", texts=[
    "推荐一些美食","给我讲个故事"
])
print(resp["body"])
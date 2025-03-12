# 1. 资源

- Github (2.9k stars): https://github.com/Lightning-AI/litserve/
- 文档：lightning.ai/litserve
- 每月提供35小时免费GPU资源
- Lightning-fast serving engine for any AI model of any size. Flexible. Easy. Enterprise-scale.
- 大模型部署版本
  - Github (11.8k stars): https://github.com/Lightning-AI/litgpt?tab=readme-ov-file#deploy-an-llm

优点：
- 适合快速部署任何规模的AI模型，提供Restful服务端
- 比原始FastAPI快2倍
- 支持批处理、GPU、流式、一个端管理模型分别部署在一个卡上

缺点：
- 免费版不支持负载均衡

# 2. 使用

```bash
pip install litserve
```

服务端

```python
# server.py
import litserve as ls

# (STEP 1) - DEFINE THE API (compound AI system)
class SimpleLitAPI(ls.LitAPI):
    def setup(self, device):
        # setup is called once at startup. Build a compound AI system (1+ models), connect DBs, load data, etc...
        self.model1 = lambda x: x**2
        self.model2 = lambda x: x**3

    def decode_request(self, request):
        # Convert the request payload to model input.
        return request["input"] 

    def predict(self, x):
        # Easily build compound systems. Run inference and return the output.
        squared = self.model1(x)
        cubed = self.model2(x)
        output = squared + cubed
        return {"output": output}

    def encode_response(self, output):
        # Convert the model output to a response payload.
        return {"output": output} 

# (STEP 2) - START THE SERVER
if __name__ == "__main__":
    # scale with advanced features (batching, GPUs, etc...)
    server = ls.LitServer(SimpleLitAPI(), accelerator="auto", max_batch_size=1)
    server.run(port=8000)
```

启动服务端：

```bash
python server.py
```

客户端

```bash
curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d '{"input": 4.0}'
```


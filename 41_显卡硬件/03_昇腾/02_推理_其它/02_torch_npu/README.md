凡是支持torch的模型，简单修改就可以使用，另外，像FlagEmbedding中的bge-m3的embedding和bge-m3-v2-reranker都支持了NPU推理

但实际测试发现，一旦输入变长，首次推理速度会很慢，但如果固定长推理，第二次开始会很快

实际测试，自己直接按torch-npu导致推理失败，可能是某些依赖安装错误，可以使用[llama-factory](https://github.com/hiyouga/LLaMA-Factory.git)

```shell
git clone --depth 1 https://github.com/hiyouga/LLaMA-Factory.git
cd LLaMA-Factory
pip install -e ".[torch,metrics]"
```
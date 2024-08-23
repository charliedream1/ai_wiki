**注意事项**

- 模型的config.json中写了依赖jina-bert-implementation，需要手动下载，并修改路径
  - 手动下载路径如下，再config.json中指定jina-bert-implementation的路径
    -  https://huggingface.co/jinaai/jina-bert-implementation
    -  或者：https://huggingface.co/jinaai/jina-bert-implementation/tree/main
  - 自动下载
    - 如果可以连接huggingface则会自动下载
    - 或者：配置hf-mirror路径，自动下载

参考代码如下：

```python
import os
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
from transformers import AutoModel
from numpy.linalg import norm

mdl_path = './jinaai/jina-embeddings-v2-base-zh'
cos_sim = lambda a,b: (a @ b.T) / (norm(a)*norm(b))
model = AutoModel.from_pretrained(mdl_path, trust_remote_code=True) # trust_remote_code is needed to use the encode method
embeddings = model.encode(['How is the weather today?', 'What is the current weather like today?'])
print(cos_sim(embeddings[0], embeddings[1]))
```

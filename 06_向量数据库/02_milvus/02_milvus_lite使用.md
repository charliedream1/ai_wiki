# 1. 资源

Github (287 stars): https://github.com/milvus-io/milvus-lite

# 2. 简介

Milvus Lite 是一个轻量级的向量相似度搜索引擎，直接安装python包pymilvus后，即可自动安装。

缺点：检索类型只支持：FLAT or IVF_FLAT，不支持HNSW。

# 3. langchain使用

```bash
pip install pymilvus
pip install langchain_milvus
```

```python
from langchain_milvus import Milvus
import getpass
import os

# Set OpenAI
if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

from langchain_openai import OpenAIEmbeddings

# Define the OpenAI embedding model
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

# The easiest way is to use Milvus Lite where everything is stored in a local file.
# If you have a Milvus server you can use the server URI such as "http://localhost:19530".
URI = "./milvus_example.db"

vector_store = Milvus(
    embedding_function=embeddings,
    connection_args={"uri": URI},
    index_params={"index_type": "IVF_FLAT"}  # Change to IVF_FLAT or FLAT
)

# Here's how you can create a new collection
from langchain_core.documents import Document

vector_store_saved = Milvus.from_documents(
    [Document(
    page_content="I have a bad feeling I am going to get deleted :(",
    metadata={"source": "tweet"},
    )],
    embeddings,
    collection_name="langchain_example",
    connection_args={"uri": URI},
)

# Here's how to retrieve data with similarity
results = vector_store_saved.similarity_search_with_score(
    "Will it be hot tomorrow?", k=1, expr='source == "tweet"'
)
for res, score in results:
    print(f"* [SIM={score:3f}] {res.page_content} [{res.metadata}]")
```

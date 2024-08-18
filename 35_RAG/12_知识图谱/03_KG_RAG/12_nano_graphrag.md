# 1. 简介

😭 GraphRAG很好很强大，但是官方实现很难/痛苦地阅读或修改。

😊 这个项目提供了一个更小、更快、更干净的GraphRAG，同时保留了核心功能（见基准测试和问题）。 

🎁 除了测试和提示，nano-graphrag大约有800行代码。 

👌 小而可扩展，异步且完全类型化。

Github: https://github.com/gusye1234/nano-graphrag

# 2. 使用

安装

```bash
pip install nano-graphrag
```

下载查尔斯·狄更斯的《圣诞颂歌》副本

```text

curl https://raw.githubusercontent.com/gusye1234/nano-graphrag/main/tests/mock_data.txt > ./book.txt
```

使用下面的Python代码片段

```python

from nano_graphrag import GraphRAG, QueryParam
graph_func = GraphRAG(working_dir="./dickens")

with open("./book.txt") as f:
    graph_func.insert(f.read())

# Perform global graphrag search
print(graph_func.query("What are the top themes in this story?"))

# Perform local graphrag search (I think is better and more scalable one)
print(graph_func.query("What are the top themes in this story?", param=QueryParam(mode="local")))
```

下次你从相同的工作目录初始化GraphRAG时，它将自动重新加载所有上下文。

增量插入 

nano-graphrag 支持增量插入，不会添加任何重复的计算或数据

```python

with open("./book.txt") as f:
    book = f.read()
    half_len = len(book) // 2
    graph_func.insert(book[:half_len])
    graph_func.insert(book[half_len:])
```

nano-graphrag 使用内容的 md5 哈希作为键，因此不会有重复的区块。

然而，每次你进行插入操作时，图的社区将被重新计算，社区报告也将被重新生成

# 参考

[1] 一个更小、更快、更干净的GraphRAG！，https://mp.weixin.qq.com/s/gdWINeUR2Qq3Rz_7TuhBIw
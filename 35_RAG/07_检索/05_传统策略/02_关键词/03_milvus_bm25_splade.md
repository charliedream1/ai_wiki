# 资源

如果你想深入研究稀疏向量，可以参考下面的资料：

精通BM25：深入探讨算法及其在Milvus中的应用（https://zilliz.com.cn/blog/mastering-bm25-a-deep-dive-into-the-algorithm-and-application-in-milvu）

详解如何通过稀疏向量优化信息检索（https://mp.weixin.qq.com/s/ZvId2vm8PDdA1fW3hJY1bA）

splade的github（https://github.com/naver/splade）

BM25-wiki（https://en.wikipedia.org/wiki/Okapi_BM25）

代码可通过链接获取：

https://pan.baidu.com/s/18BgYOdKw2suuwhTggNlINA?pwd=1234 提取码: 1234

# 代码

我们已经了解了两种稀疏向量的特点，以及生成方法，下面就在搜索中体会下它们的区别吧。

我们需要用 Milvus 创建集合，然后导入数据，创建索引，加载数据，就可以搜索了。这个过程我在 《朋友圈装腔指南：如何用向量数据库把大白话变成古诗词》中有详细介绍，就不多赘述了。

创建集合。

```python
from pymilvus import MilvusClient, DataType
import time

def create_collection(collection_name):
    # 检查同名集合是否存在，如果存在则删除
    if milvus_client.has_collection(collection_name):
        print(f"集合 {collection_name} 已经存在")
        try:
            # 删除同名集合
            milvus_client.drop_collection(collection_name)
            print(f"删除集合：{collection_name}")
        except Exception as e:
            print(f"删除集合时出现错误: {e}")
    # 创建集合模式
    schema = MilvusClient.create_schema(
        auto_id=True,
        enable_dynamic_field=True,
        # 设置分区数量，默认为16
        num_partitions=16,
        description=""
    )
    # 添加字段到schema
    schema.add_field(field_name="id", datatype=DataType.INT64, is_primary=True, max_length=256)
    schema.add_field(field_name="text", datatype=DataType.VARCHAR, max_length=256)
    # bm25稀疏向量
    schema.add_field(field_name="sparse_vectors_bm25", datatype=DataType.SPARSE_FLOAT_VECTOR)
    # splade稀疏向量
    schema.add_field(field_name="sparse_vectors_splade", datatype=DataType.SPARSE_FLOAT_VECTOR)
    # 创建集合
    try:
        milvus_client.create_collection(
            collection_name=collection_name,
            schema=schema,
            shards_num=2
        )
        print(f"创建集合：{collection_name}")
    except Exception as e:
        print(f"创建集合的过程中出现了错误: {e}")
    # 等待集合创建成功
    while not milvus_client.has_collection(collection_name):
        # 获取集合的详细信息
        time.sleep(1)
    if milvus_client.has_collection(collection_name):
        print(f"集合 {collection_name} 创建成功")

# 示例
collection_name = "docs"
uri="http://localhost:19530"
milvus_client = MilvusClient(uri=uri)
create_collection(collection_name)
```

导入数据。

```python
# 准备数据
entities = [
    {
        # 文本字段
        "text": docs[i],
        "text_en": docs_en[i],
        # bm25稀疏向量字段
        "sparse_vectors_bm25": list(sparse_vectors_bm25)[i].reshape(1, -1),
        # splade稀疏向量字段
        "sparse_vectors_splade": list(sparse_vectors_splade)[i].reshape(1, -1),
    }
    for i in range(len(docs))
]

# 导入数据
milvus_client.insert(collection_name=collection_name, data=entities)
```

创建索引。

```python
# 创建索引参数
index_params = milvus_client.prepare_index_params()

# 为稀疏向量bm25创建索引参数
index_params.add_index(
    index_name="sparse_vectors_bm25",
    field_name="sparse_vectors_bm25",
    # SPARSE_INVERTED_INDEX是传统的倒排索引，SPARSE_WAND使用Weak-AND算法来减少搜索过程中的完整IP距离计算
    index_type="SPARSE_INVERTED_INDEX",
    # 目前仅支持IP
    metric_type="IP",
    # 创建索引时，排除向量值最小的20%的向量。对于稀疏向量来说，向量值越大，说明在该维度上的重要性越大。范围[0,1]。
    params={"drop_ratio_build": 0.2}
)


# 为稀疏向量splade创建索引参数
index_params.add_index(
    index_name="sparse_vectors_splade",
    field_name="sparse_vectors_splade",
    # SPARSE_INVERTED_INDEX是传统的倒排索引，SPARSE_WAND使用Weak-AND算法来减少搜索过程中的完整IP距离计算
    index_type="SPARSE_INVERTED_INDEX",
    # 目前仅支持IP
    metric_type="IP",
    # 创建索引时，排除向量值最小的20%的向量。对于稀疏向量来说，向量值越大，说明在该维度上的重要性越大。范围[0,1]。
    params={"drop_ratio_build": 0.2}
)

# 创建索引
milvus_client.create_index(
    collection_name=collection_name,
    index_params=index_params
)
```

查看索引是否创建成功。

```python
# 查看索引信息
def show_index_info(collection_name: str) -> None:
    """
    显示指定集合中某个索引的详细信息。

    参数:
    collection_name (str): 集合的名称。

    返回:
    None: 该函数仅打印索引信息，不返回任何值。
    """
    # 查看集合的所有索引
    indexes = milvus_client.list_indexes(
        collection_name=collection_name  
    )
    print(f"已经创建的索引：{indexes}")
    print()
    # 查看索引信息
    if indexes:
        for index in indexes:
            index_details = milvus_client.describe_index(
                collection_name=collection_name,  
                # 指定索引名称，这里假设使用第一个索引
                index_name=index
            )
            print(f"索引 {index} 详情：{index_details}")
            print()
    else:
        print(f"集合 {collection_name} 中没有创建索引。")

# 示例
show_index_info(collection_name)
```

如果创建成功，你会看到下面的输出：

```text
已经创建的索引：['sparse_vectors_bm25', 'sparse_vectors_splade']

索引 sparse_vectors_bm25 详情：{'drop_ratio_build': '0.2', 'index_type': 'SPARSE_INVERTED_INDEX', 'metric_type': 'IP', 'field_name': 'sparse_vectors_bm25', 'index_name': 'sparse_vectors_bm25', 'total_rows': 0, 'indexed_rows': 0, 'pending_index_rows': 0, 'state': 'Finished'}

索引 sparse_vectors_splade 详情：{'drop_ratio_build': '0.2', 'index_type': 'SPARSE_INVERTED_INDEX', 'metric_type': 'IP', 'field_name': 'sparse_vectors_splade', 'index_name': 'sparse_vectors_splade', 'total_rows': 0, 'indexed_rows': 0, 'pending_index_rows': 0, 'state': 'Finished'}
```

加载集合。

```python
# 加载集合
print(f"正在加载集合：{collection_name}")
milvus_client.load_collection(collection_name=collection_name)

# 验证加载状态
print(milvus_client.get_load_state(collection_name=collection_name))
```

如果加载成功，会显示：

```text
正在加载集合：docs
{'state': <LoadState: Loaded>}
```

加载完成，下面就是重头戏了，搜索。

定义搜索函数：

```python
# 定义稀疏向量搜索参数
search_params_sparse_vectors = {
    "metric_type": "IP",
    "params": {"drop_ratio_search": 0.2},
}

# 执行向量搜索
def vector_search(
        query_vectors,
        field_name,
        search_params,
        output_fields,
    ):
    # 向量搜索
    res = milvus_client.search(
        collection_name=collection_name,
        # 指定查询向量。
        data=query_vectors,
        # 指定要搜索的向量字段
        anns_field=field_name,
        # 设置搜索参数
        search_params=search_params,
        output_fields=output_fields
    )
    return res
```

再定义一个打印结果的函数，方便查看结果。

```python
# 打印向量搜索结果
def print_vector_results(res):
    for hits in res:
        for hit in hits:
            entity = hit.get("entity")
            print(f"text: {entity['text']}")
            print(f"distance: {hit['distance']:.3f}")
            print("-"*50)
        print(f"数量：{len(hits)}")
```

首先，我们使用 BM25搜索。

```python
# 使用稀疏向量BM25搜索
query1 = ["人工智能如何影响汽车行业？"]

query_sparse_vectors_bm25 = bm25_ef.encode_queries(query1)

field_name = "sparse_vectors_bm25"
output_fields = ["text"]
# 指定搜索的分区，或者过滤搜索
res_sparse_vectors_bm25 = vector_search(query_sparse_vectors_bm25, field_name, search_params_sparse_vectors, output_fields)

print_vector_results(res_sparse_vectors_bm25)
```

但是并没有搜索到任何结果：

```text
数量：0
```

为什么呢？我们查看下 query1的分词结果：

```python
# 查看query1的分词结果
print(analyzer(query1[0]))
```

分词结果只有“人工智能”一个词：

```text
['人工智能', '影响', '汽车行业']
```

BM25的词汇表中虽然有“智能”这个词，但是并不包含“人工智能”、“影响”和“汽车行业”这些词，所以没有返回任何结果。

我们把“人工智能”替换成“机器智能”，就可以搜索到了。

```python
# 使用稀疏向量BM25搜索
query2 = ["机器智能如何影响汽车行业？"]

query_sparse_vectors_bm25 = bm25_ef.encode_queries(query2)

field_name = "sparse_vectors_bm25"
output_fields = ["text"]
# 指定搜索的分区，或者过滤搜索
res_sparse_vectors_bm25 = vector_search(query_sparse_vectors_bm25, field_name, search_params_sparse_vectors, output_fields)

print_vector_results(res_sparse_vectors_bm25)
```

而且，这次还搜索到了包含“机器学习”的句子。

```text
text: 机器智能的未来充满潜力。
distance: 2.054
--------------------------------------------------
text: 大数据支持是机器智能发展的关键。
distance: 1.752
--------------------------------------------------
text: 机器学习正在改变我们的生活方式。
distance: 0.788
--------------------------------------------------
数量：3
```

这是因为分词时把“机器智能“分成了“机器”和“智能”两个词，所以能搜索到更多句子。

```python
# 查看query2的分词结果
print(analyzer(query2[0]))
```

分词结果：

```text
['机器', '智能', '影响', '汽车行业']
```

接下来，我们使用 splade 搜索，看看和 BM25的搜索结果有什么不同。

先定义一个打印结果的函数。

```python
# 打印向量搜索结果
def print_vector_results_en(res):
    for hits in res:
        for hit in hits:
            entity = hit.get("entity")
            print(f"text_en: {entity['text_en']}")
            print(f"distance: {hit['distance']:.3f}")
            print("-"*50)
        print(f"数量：{len(hits)}")
```

然后使用 splade 搜索。

```python
query1_en = ["How does artificial intelligence affect the automotive industry?"]

query_sparse_vectors_splade = splade_ef.encode_queries(query1_en)

field_name = "sparse_vectors_splade"
output_fields = ["text_en"]
res_sparse_vectors_splade = vector_search(query_sparse_vectors_splade, field_name, search_params_sparse_vectors, output_fields)

print_vector_results_en(res_sparse_vectors_splade)
```

比较 BM25 和 splade 的搜索结果，我们很容易发现它们之间的区别。splade 的文档集合中并不包含“artificial intelligence”这个词，但是由于它具有“举一反三”的能力，仍然搜索到了包含“AI”、“machine intelligence”以及“Autonomous”的句子，返回了更多结果（其实是返回了所有文档）。

```text
text_en: The future of machine intelligence is full of potential.
distance: 10.020
--------------------------------------------------
text_en: Big data support is key to the development of machine intelligence.
distance: 8.232
--------------------------------------------------
text_en: AI can help doctors diagnose diseases.
distance: 7.291
--------------------------------------------------
text_en: Autonomous driving relies on advanced algorithms.
distance: 7.213
--------------------------------------------------
text_en: Production efficiency can be improved through automation technology.
distance: 6.999
--------------------------------------------------
text_en: Machine learning is changing our way of life.
distance: 6.863
--------------------------------------------------
text_en: Data analysis technology is widely applied in the financial field.
distance: 5.064
--------------------------------------------------
text_en: The quantum tunneling effect allows electrons to pass through potential barriers that classical mechanics consider impassable, which has important applications in semiconductor devices.
distance: 3.695
--------------------------------------------------
text_en: Deep learning performs exceptionally well in image recognition.
distance: 3.464
--------------------------------------------------
text_en: Natural language processing is an important field in computer science.
distance: 3.044
--------------------------------------------------
数量：10
```

如果把查询中的“artificial intelligence”替换成“machine intelligence”，仍然会返回所有结果，但是权重有所不同。

```text
text_en: The future of machine intelligence is full of potential.
distance: 15.128
--------------------------------------------------
text_en: Big data support is key to the development of machine intelligence.
distance: 12.945
--------------------------------------------------
text_en: Machine learning is changing our way of life.
distance: 12.763
--------------------------------------------------
text_en: Production efficiency can be improved through automation technology.
distance: 7.446
--------------------------------------------------
text_en: AI can help doctors diagnose diseases.
distance: 6.055
--------------------------------------------------
text_en: Autonomous driving relies on advanced algorithms.
distance: 5.309
--------------------------------------------------
text_en: Data analysis technology is widely applied in the financial field.
distance: 4.857
--------------------------------------------------
text_en: The quantum tunneling effect allows electrons to pass through potential barriers that classical mechanics consider impassable, which has important applications in semiconductor devices.
distance: 3.356
--------------------------------------------------
text_en: Deep learning performs exceptionally well in image recognition.
distance: 3.317
--------------------------------------------------
text_en: Natural language processing is an important field in computer science.
distance: 2.688
--------------------------------------------------
数量：10
```
# 参考

[1] 外行如何速成专家？Embedding之BM25、splade稀疏向量解读, https://mp.weixin.qq.com/s?__biz=MzUzMDI5OTA5NQ==&mid=2247507105&idx=1&sn=16a1192b62a45249be96e4204704ca46&scene=21#wechat_redirect
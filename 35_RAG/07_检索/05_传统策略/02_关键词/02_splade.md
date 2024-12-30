# 1. 原理

如果说稠密向量是精通特定领域的专家，统计得到的稀疏向量 BM25是聪明的门外汉，那么学习得到的稀疏向量 splade 就是刚入门的新人。他理解领域内专业术语的语义，而且能够举一反三，增加更多语义相近的词，一起查找。但是他毕竟还是新人，并不精通，还是通过数专业术语出现的次数，找到最相关的文档。

具体来说，splade 是这样工作的：

首先，splade 先对句子分词，通过嵌入模型 BERT （BERT 相关内容详见 《孙悟空 + 红楼梦 - 西游记 = ？一文搞懂什么是向量嵌入》）得到单词的向量。向量可以表达语义，所以 splade 能够“举一反三”，找到更多语义相似的单词。

比如，对于“人工智能如何影响汽车行业”这个句子，分词得到“人工智能”和“汽车”两个 单词，以及与“人工智能”相似的“AI”等单词。

splade 也有一张词汇表，不过它不需要像 bm25 那样根据文档集合统计，而是预先就有的，来源于 BERT。

接下来，splade 生成这些单词的稀疏向量。它会计算每个单词出现在词汇表中的每个位置的概率。也就是说，单词和词汇表中某个位置的词在语义上越接近，计算得到的概率越大。这个概率就是单词的权重。

以“人工智能”为例，假设词汇表中第5个词也是“人工智能”，两个词完全一样，计算得到的概率就很高，比如40%。而词汇表第8个词是“机器学习”，两个词比较相似，概率是20%。而词汇表中其他的词和“人工智能”语义相差较远，概率很小，忽略不计。最后，“人工智能”的权重就是40%+20%=60% 。

然后再用相同的方法，计算出“AI”和“汽车”的权重，得到稀疏向量：

```text
sparse_vector = {"人工智能": 0.6,"AI": 0.5,"汽车": 0.1}
```

# 2. splade 代码实践

老规矩，我们还使用代码验证下前面的内容。这次使用英文的文档集合：

```python
# 使用英文
docs_en = [
    "Machine learning is changing our way of life.",
    "Deep learning performs exceptionally well in image recognition.",
    "Natural language processing is an important field in computer science.",
    "Autonomous driving relies on advanced algorithms.",
    "AI can help doctors diagnose diseases.",
    "Data analysis technology is widely applied in the financial field.",
    "Production efficiency can be improved through automation technology.",
    "The future of machine intelligence is full of potential.",
    "Big data support is key to the development of machine intelligence.",
    "The quantum tunneling effect allows electrons to pass through potential barriers that classical mechanics consider impassable, which has important applications in semiconductor devices."
]
```

生成文档集合的稀疏向量：

```python
from pymilvus.model.sparse import SpladeEmbeddingFunction

query_en = ["How does artificial intelligence affect the automotive industry?"]

model_name = "naver/splade-cocondenser-selfdistil"

# 实例化splade嵌入模型
splade_ef = SpladeEmbeddingFunction(
    model_name = model_name, 
    device="cpu"
)

# 生成文档集合的稀疏向量
sparse_vectors_splade = splade_ef.encode_documents(docs_en)
print(sparse_vectors_splade)
```

和 BM25 一样，我们同样得到一个稀疏向量矩阵：

```text
(0, 1012)        0.053256504237651825
  (0, 2003)        0.22995686531066895
  (0, 2047)        0.08765587955713272
  :        :
  (9, 27630)        0.2794925272464752
  (9, 28688)        0.02786295674741268
  (9, 28991)        0.12241243571043015
```

splade 的词汇表是预先准备好的，词汇表中的单词数量同样也是稀疏向量的维度。

```python
# splade词汇表中的单词数量
from transformers import AutoModelForMaskedLM, AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)
print(f"splade词汇表中的单词数量：{tokenizer.vocab_size}")

print(f"splade稀疏向量维度：{splade_ef.dim}")
```

二者相同：

```bash
splade词汇表中的单词数量：30522
splade稀疏向量维度：30522
```

我们再来看看查询的分词结果及其稀疏向量：

```python
# 查看查询的分词
tokens = tokenizer.tokenize(query_en[0])
print(f"“{query_en[0]}” 的分词结果：\n{tokens}")
print(f"tokens数量：{len(tokens)}")

# 生成查询的稀疏向量
query_sparse_vectors_splade = splade_ef.encode_queries(query_en)
print(query_sparse_vectors_splade)
```

结果如下：

```text
“How does artificial intelligence affect the automotive industry?” 的分词结果：
['how', 'does', 'artificial', 'intelligence', 'affect', 'the', 'automotive', 'industry', '?']

tokens数量：9

  (0, 2054)        0.139632448554039
  (0, 2079)        0.08572433888912201
  (0, 2106)        0.22006677091121674
  (0, 2126)        0.038961488753557205
  (0, 2129)        0.6875206232070923
  (0, 2138)        0.5343469381332397
  (0, 2194)        0.32417890429496765
  (0, 2224)        0.011731390841305256
  (0, 2339)        0.33811360597610474
  :        :
  (0, 26060)        0.0731586366891861
```

比较分词的数量和稀疏向量的维度，你有没有发现有什么不对劲的地方？没错，分词数量和稀疏向量的维度不一样。这就是 splade 和 BM25的重要区别，splade 能够“举一反三”，它在最初9个分词的基础上，又增加了其他语义相近的单词。

那么，查询现在一共有多少个单词呢？或者说，它的稀疏向量的非零元素有多少呢？

```python
# 获取稀疏向量的非零索引
nonzero_indices = query_sparse_vectors_splade.indices[query_sparse_vectors_splade.indptr[0]:query_sparse_vectors_splade.indptr[1]]

# 构建稀疏词权重列表
sparse_token_weights = [
    (splade_ef.model.tokenizer.decode(col), query_sparse_vectors_splade[0, col])
    for col in nonzero_indices
]

# 按权重降序排序
sparse_token_weights = sorted(sparse_token_weights, key=lambda item: item[1], reverse=True)

# 查询句只有9个tokens，splade通过举一反三，生成的稀疏向量维度增加到了98个。
print(f"splade 稀疏向量非零元素数量：{len(sparse_token_weights)}")
```

一共有98个：

```bash
splade 稀疏向量非零元素数量：98
```

具体是哪些单词？我们打印出来看一下：

```python
# 比如，和“artificial intelligence”语义相近的 “ai”，和“automotive”语义相近的“car”。
for token in sparse_token_weights:
    print(token)
```

splade 增加了大量语义相近的单词，比如和“artificial intelligence”语义相近的 “ai”，和“automotive”语义相近的“car”和“vehicle”。

```text
('artificial', 2.588431)
('intelligence', 2.3582284)
('car', 1.590975)
('automotive', 1.4835068)
('vehicle', 0.798108)
('ai', 0.676852)
  :        :
```

# 参考

[1] 外行如何速成专家？Embedding之BM25、splade稀疏向量解读, https://mp.weixin.qq.com/s?__biz=MzUzMDI5OTA5NQ==&mid=2247507105&idx=1&sn=16a1192b62a45249be96e4204704ca46&scene=21#wechat_redirect
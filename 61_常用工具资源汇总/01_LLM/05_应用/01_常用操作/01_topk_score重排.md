```python
# 根据打分按降序排序，并存入new_docs
new_docs = [doc for _, doc in sorted(zip(score, docs), key=lambda x: x[0], reverse=True)]
# 根据打分筛选
new_docs = [doc for i, doc in enumerate(new_docs) if score[i] > self.rerank_threshold]
# 挑选topk
new_docs = new_docs[:self.rerank_top_k]
```
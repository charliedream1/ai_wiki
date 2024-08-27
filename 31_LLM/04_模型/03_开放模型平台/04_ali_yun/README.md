https://help.aliyun.com/zh/dashscope/developer-reference/text-embedding-quick-start?spm=a2c4g.11186623.0.0.77d341e3SRTTSs

| 模型英文名 | 向量维度 | 单次请求文本最大行数 | 单行最大输入字符长度 | 支持语种 |
| --- |------|------------|------------| --- |
| text-embedding-v2 | 1536 | 25         | 2048       | 中文、英文 |
| text-embedding-async-v2 | 1536 | 100000         | 2048       | 中文、英文 |

| 模型 | MTEB | MTEB（Retrieval task） | CMTEB | CMTEB (Retrieval task) |
| --- |------|------------|------------| --- |
| text-embedding-v2 | 60.13 | 49.49 | 62.17 | 62.78 |


费用：0.0007元/1000 tokens

- text-embedding：首次开通DashScope即获赠总计500,000 tokens限时免费使用额度
- text-embedding-async：首次开通DashScope即获赠总计20,000,000 tokens限时免费使用额度

以下条件任何一个超出都会触发限流：

- 调用频次 ≤ 30 QPS，每秒钟不超过30次API调用。
- Token消耗 ≤ 600,000 TPM，每分钟消耗的Token数目不超过600,000。
# 1. 简介

代码：https://github.com/infiniflow/ragflow.git

架构：前后端分离

# 2. 文件解析

- 基于自己训练的版面模型和规则模板对文件进行解析
- 其中版面分析模型为yolo-v8按不同领域训了多个，实测和ppstructure效果相当

采用layout->ocr->table流程
- 对于paper使用了传统算法解决双栏
- 基于规则提取了文件元信息、摘要

# 3. 互联网

加入了baidu/google/bing/duckduckgo的搜索引擎，可以通过关键词搜索到相关信息

# 4. 数据库

- 向量库：仅支持Elastic Search
- 知识图谱：借助pandas和向量库存储，支持图谱和脑图两种方式展示
- minio: 用于存储文件
- mysql
- redis

# 5. 模型支持

支持几乎所有主流模型

# 6. 工具

可与下列网站交互
- 飞书
- Github

# 7. 知识图谱

特点：
- 采用了传统的固定长+标点切割方法
- 限定实体类型："organization", "person", "location", "event", "time"
- 包含实体关系提取、脑图提取以及社区总结

代码：
- 构建入口：index.py
- 搜索接口：search.py

局限性：
- 当前仅针对单文档
- 没有接入neo4j等图数据库

# 8. 问答流程控制

利用图的概念构建

- 利用json定义了不同问答流，通过关键词寻找下一步流程
- 按照业务定制了不同的答复流程和模板
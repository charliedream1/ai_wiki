# 0. 简介

GraphRAG通过结合知识图谱，增加RAG的全局检索能力。今天我将讲解如何使用Neo4J可视化GraphRAG索引的结果，以便进一步的处理、分析。本篇仍然以小说《仙逆》提取的实体为例，一图胜千言。本文分为4小节，安装neo4j、导入GraphRAG索引文件、Neo4J可视化分析和总结，所有坑都已经帮你趟过啦，放心食用。

![](.08_neo4j可视化_images/图谱.png)

Neo4j[1]是由 Neo4j Inc. 开发的图数据库管理系统，是图数据库技术领域的领导者——强大的原生图存储、数据科学和分析，具备企业级的安全性。无约束地扩展您的事务和分析工作负载。已下载超过1.6亿次。Neo4j 存储的数据元素包括节点、连接它们的边以及节点和边的属性。

# 1. 安装Neo4j

Neo4j支持使用云端服务和本地社区开源版本，使用如下Docker命令启动Neo4J实例。

```bash
docker run \
    -p 7474:7474 -p 7687:7687 \
    --name neo4j-apoc \
    -e NEO4J_apoc_export_file_enabled=true \
    -e NEO4J_apoc_import_file_enabled=true \
    -e NEO4J_apoc_import_file_use__neo4j__config=true \
    -e NEO4J_PLUGINS=\[\"apoc\"\] \
    neo4j:5.21.2
```

浏览器打开http://localhost:7474/，然后输入默认用户名neo4j，默认密码neo4j即可登录，登录之后要求重设密码。

接下来，安装neo4j的依赖包

```bash
pip install --quiet pandas neo4j-rust-ext
```

# 2. 导入GraphRAG的索引结果

为了更好地支持中文提取，本次采用deepseeker[2]的deep-seek-chat模型（为啥不用qwen2？因为我的免费额度使用完了）。注册之后免费500万Token，索引一次通过，支持128K上下文，最大输出Tokens为4096。所以设置LLM的时候，务必把max_tokens设置为4096，未明确说明TPM和RPM，根据平台符合自动调整。

导入依赖库

```python

```

# 参考

[1] 喂饭教程！全网首发Neo4J可视化GraphRAG索引, https://mp.weixin.qq.com/s?__biz=MzI0OTAzNTEwMw==&mid=2247484265&idx=1&sn=660e17e8196d4eea4900db1636aa706f&chksm=e996e359dee16a4f899ab9738d4ff7df13cdb4cc2faa6586320e4155492de1f78744756de7a4&cur_album_id=3533964025434734594&scene=189#wechat_redirect
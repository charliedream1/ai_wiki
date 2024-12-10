
Github (199 stars): https://github.com/NVIDIA/nv-ingest

NVIDIA Ingest is an early access set of microservices for parsing hundreds of thousands of complex, messy unstructured PDFs and other enterprise documents into metadata and text to embed into retrieval systems.

【开源】NVIDIA Ingest 是一套面向企业文档内容和元数据提取的微服务，支持解析数十万复杂且非结构化的 PDF、Word 和 PowerPoint 文档。通过NVIDIA NIM 微服务，该工具能够高效提取文本表格、图表和图像，为生成式应用和检索系统提供高质量的嵌入式数据支持。
感谢关注点赞/
核心功能
1.多文档类型支持
支持 PDF、DocX、PPTx 以及图像文件的解
析。
品汪的提百方法加
Unstructured.io 和Adobe Content Extraction在吞吐量和精确性之间平衡。Services)，
2.内容分类与提取
·将文档内容分解为页面并分类(文本、表格、
图表、图像)。
使用光学字符识别(OCR)技术，将提取内容转化为定义良好的 JSON 模式。
3.嵌入式存储与数据库支持
·可选计算嵌入向量，并将结果存储到 Milvus 等
向量数据库中。
4.高效并行化
支持文档拆分和任务并行化，大幅提升处理性
能和扩展能力。
5.预处理与后处理能力
支持多种操作:文本拆分与分块、转换与过滤、嵌入生成、图像数据离线存储等。
适用场景
企业内容管理:批量解析和分类非结构化文档，提取结构化数据。
检索系统优化:为检索系统生成高质量的嵌入
向量和元数据。
·生成式 AI应用:为生成式任务提供上下文丰富
的输入数据。
工具优势
灵活的任务定义:通过 JSON 格式描述文档与任务，轻松定制内容提取流程。
结果可追踪性:生成包含元数据、注释和时间追踪信息的 JSON 字典，支持任务结果追踪与分析。
高性能与扩展性:支持并行处理，提高吞吐量适应大规模文档解析需求。
限制说明
非静态管道:不会对每个文档运行固定的操作流
程
优格的一大名忍木一束父合多种提取方法。
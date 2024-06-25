# 1. 资源

Github (13k): https://github.com/VikParuchuri/marker
功能：
- PDF转Markdown
- 转换准确率68%

实际测试：

优点：
- 相比pymupdf4llm转换效果较好

缺点：
- 底层调用surya的ocr和layout模型，改模型不能商用
- 没有页码
- 个别文本会丢失

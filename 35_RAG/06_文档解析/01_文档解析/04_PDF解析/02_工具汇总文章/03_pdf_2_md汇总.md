pdf文档解析涉及到从pdf中准确识别出文本，表格，公式，图标等。今天分享一个大合集，共开源7个项目、闭源6个项目。

开源
1、 PDF-Extract-Kit
PDF-Extract-Kit通过集成多个模型实现了PDF高质量提取，适用于学术论文、教科书、研究报告和财务报表等多种文档类型，在扫描模糊或有水印的情况下也能保持高鲁棒性

布局检测采用LayoutLMv3模型进行区域检测，包括图像、表格、标题、文本等
公式检测上采用YOLOv8，包含行内公式和行间公式
公式识别上采用UniMERNet识别
OCR使用PaddleOCR进行文本识别
github: https://github.com/opendatalab/PDF-Extract-Kit

2、 gptpdf
只用293行代码，几乎完美地解析了排版、数学公式、表格、图片、图表等，上限是gpt-4o的能力，期待后续进步一步的迭代

方法：使用 PyMuPDF 库，对 PDF 进行解析出所有非文本区域，并做好标记 ; 使用视觉大模型（如 GPT-4o）进行解析，得到markdown 文件

github：https://github.com/CosmosShadow/gptpdf

3、RAGFlow
RAGFlow是基于深度文档理解的开源 RAG引擎，为了解决幻觉问题，项目方在文档解析模块做了创新，采用了自创的deep document understanding方法

支持Word、幻灯片、Excel、txt、图像、扫描件、结构化数据、网页等复杂的非结构化数据解析，包含各种不同场景模版，比如发票、简历、财报等

github：https://github.com/infiniflow/ragflow

4、pix2text
支持多语言，可以识别图片中的版面、表格、图片、文字、数学公式等，输出Markdown 格式

也可以把整个 PDF 文件（PDF 可以是扫描图片或者其他任何格式）转换为 Markdown

体验地址：https://huggingface.co/spaces/breezedeus/Pix2Text-Demo github：https://github.com/breezedeus/Pix2Text

5、marker（开源）
支持多语言多文档类型，针对书籍和科学论文做了优化

github：https://github.com/VikParuchuri/marker

6、MAP项目的文档转换模块
结合 版式识别、OCR、表格、Latex等的提取

github: https://github.com/multimodal-art-projection/MAP-NEO/tree/main/Matrix/document-convert

7、MinerU
一站式开源高质量数据提取工具，支持PDF/网页/多格式电子书提取。

支持多种前端模型输入
删除页眉、页脚、脚注、页码等元素
符合人类阅读顺序的排版格式
保留原文档的结构和格式，包括标题、段落、列表等
提取图像和表格并在markdown中展示
将公式转换成latex
乱码PDF自动识别并转换
支持cpu和gpu环境
支持windows/linux/mac平台
github https://github.com/opendatalab/MinerU/blob/master/README_zh-CN.md

闭源（可体验）
1、Doc2x

可以将 PDF 文件转换为 Markdown、LaTeX、DOCX 可以解析排版、数学公式、表格、图片、图表等，对包含表格和公式的文档处理效果较好，国内的不少大模型厂商在使用，中英文档处理效果比mathpix好

体验地址：https://doc2x.noedgeai.com

2、mathpix（据说claude数学能力强因为用了mathpix）

可以解析文本、数学、化学、手写识别、表格、外语和完整PDF文档，输出LaTeX 、Markdown、Word等格式。支持类似谷歌的搜索功能

体验地址：https://mathpix.com

3、庖丁PDFlux 提取 PDF / 图片中的表格和文字，AI 智能生成摘要/搜索/改写/翻译

体验地址：https://pdflux.com

4、TextIn 可以识别文档或图片中的文字信息，按常见阅读顺序进行还原 支持标准的年报、文书、函件、合同等文档，兼容扫描文档和电子PDF文件

体验地址：https://textin.com/experience/pdf_to_markdown

5、腾讯云文档识别 可将图片或PDF文件转换成Markdown格式文件，包括表格、公式、图片和文本等，并转换为阅读顺序，可将文档内容转换成阅读格式

体验地址：https://ocrdemo.cloud.tencent.com

6、通用表格识别是飞桨特色的端到端表格识别系统，可精准预测论文、报告等文档中的表格位置和内容

体验地址：https://aistudio.baidu.com/community/app/91661/webUI

# 参考

[1] awesome 文档解析！16款高质量pdf -> markdown项目分享, https://mp.weixin.qq.com/s/EXIJZS-4RRpnA0w4Ti0VBQ
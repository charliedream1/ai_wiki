- Github(20.4k stars): https://github.com/ocrmypdf/OCRmyPDF
- 文档：ocrmypdf.readthedocs.io/

OCRmyPDF 基于 Python 编写，利用了多个强大的库，包括 Poppler 用于PDF操作，Tesseract OCR 作为主要的OCR引擎，并且依赖于 Pillow 进行图像处理。这些组件的组合确保了在转换过程中保持原文档布局的同时，也能有效识别并替换图片中的文字。

- 预处理：在应用OCR之前，OCRmyPDF会对图像进行优化，如调整亮度、对比度，以便提高OCR的识别率。
- OCR处理：Tesseract OCR 引擎被调用以识别图像中的文字，并生成一个新的文本层。
- 融合与保存：将识别出的文字与原始图像合并，形成一个新的PDF文件，这个新文件具有完整的文本信息，可以直接搜索、复制或编辑。

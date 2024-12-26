```bash
pip install pdf2image pytesseract pillow
```

```python
import pytesseract
from PIL import Image
from pdf2image import convert_from_path

# 将PDF页面转换为图像
pages = convert_from_path('your_pdf.pdf', 300)

# 对每一页应用OCR
for page_num, page in enumerate(pages):
    text = pytesseract.image_to_string(page, lang='ara')  # 'ara' 表示阿拉伯语
    print(f"Page {page_num + 1} Text: {text}")

```

这个错误提示表示 **`pdf2image`** 库无法找到 `poppler-utils`，这是一组用于处理PDF文件的工具，`pdf2image` 依赖它来提取PDF页面信息（如页面数、大小等）。具体来说，错误信息中提到：

```
Unable to get page count. Is poppler installed and in PATH?
```

### 原因：
`pdf2image` 需要使用 **Poppler** 工具来处理PDF文件。如果系统中没有安装Poppler或其路径没有添加到环境变量 `PATH` 中，就会出现这种错误。

### 解决方法：

#### 1. 安装 Poppler

Poppler 是一个开源的 PDF 渲染库，它提供了 `pdfinfo` 和 `pdftoppm` 等命令行工具，`pdf2image` 库依赖这些工具来提取PDF的页面信息和渲染PDF页面为图像。

##### 在 **Ubuntu/Debian** 系统中：
```bash
sudo apt-get update
sudo apt-get install -y poppler-utils
```

##### 在 **CentOS/RHEL** 系统中：
```bash
sudo yum install -y poppler-utils
```

##### 在 **MacOS** 系统中（使用Homebrew）：
```bash
brew install poppler
```

#### 2. 确保 Poppler 工具在系统的 `PATH` 中

安装完Poppler后，确保 `pdfinfo` 和 `pdftoppm` 可执行文件在系统的 `PATH` 环境变量中。你可以通过以下命令检查 `pdfinfo` 是否在 `PATH` 中：

```bash
which pdfinfo
```

如果该命令返回了 `pdfinfo` 的路径，说明它已正确安装并在 `PATH` 中。如果没有，可能需要手动将其路径添加到 `PATH` 环境变量中。

#### 3. 使用 `pdf2image` 重新尝试

安装Poppler并确保其在 `PATH` 中后，重新运行你的代码，`pdf2image` 应该能够正常调用Poppler工具来提取PDF页面信息和转换页面为图像。

### 总结

- **安装 Poppler**：这是解决该错误的根本方法。
- **确保 Poppler 在 PATH 中**：通过检查 `which pdfinfo` 来确保 Poppler 工具可用。
  
一旦这些步骤完成，`pdf2image` 应该能够正常工作，不会再遇到 `PDFInfoNotInstalledError` 的问题。
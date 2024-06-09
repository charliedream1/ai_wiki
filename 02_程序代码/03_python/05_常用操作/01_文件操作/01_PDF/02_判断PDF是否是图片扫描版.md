# 方法一：使用 PyMuPDF 库

```bash
pip install pymupdf
```

```python
import fitz

def is_scanned_pdf(file_path):
    pdf_document = fitz.open(file_path)
    total_pages = pdf_document.page_count
    scanned_pages = 0

    for page_num in range(total_pages):
        page = pdf_document[page_num]
        images = page.get_images(full=True)
        if images:
            scanned_pages += 1

    pdf_document.close()

    if scanned_pages / total_pages > 0.5:
        return True
    else:
        return False

# 检测一个 PDF 文件是否是图片扫描版
file_path = 'sample.pdf'
if is_scanned_pdf(file_path):
    print(f'{file_path} 是图片扫描版')
else:
    print(f'{file_path} 不是图片扫描版')

```

在以上代码中，我们定义了一个 is_scanned_pdf() 函数，该函数接收一个 PDF 文件的路径作为输入参数，并返回一个布尔值来表示该文件是否是图片扫描版。我们首先打开 PDF 文件，然后逐页检测每一页是否包含图片，最后根据包含图片的页数占总页数的比例来判断 PDF 文件是否是图片扫描版。

请注意，上述方法并不是绝对准确的，因为某些 PDF 文件可能包含了少量图片而不是全文都是图片，但是可以一定程度上帮助我们判断 PDF 文件的内容性质。

# 方法二：使用 pdf2image 库

```bash
pip install pdf2image
```

```python
from pdf2image import convert_from_path

def is_scanned_pdf(file_path):
    images = convert_from_path(file_path)

    if len(images) > 0:
        return True
    else:
        return False

# 检测一个 PDF 文件是否是图片扫描版
file_path = 'sample.pdf'
if is_scanned_pdf(file_path):
    print(f'{file_path} 是图片扫描版')
else:
    print(f'{file_path} 不是图片扫描版')
```

在以上代码中，我们定义了一个 is_scanned_pdf() 函数，该函数接收一个 PDF 文件的路径作为输入参数，并返回一个布尔值来表示该文件是否是图片扫描版。我们通过 pdf2image 库将 PDF 文件转换为图像格式，然后判断图像数量是否大于零来判断 PDF 文件是否是图片扫描版。

同样地，这种方法也不是绝对准确的，因为某些 PDF 文件可能包含了非常少量的图片或者添加了图片水印，但是也可以帮助我们初步判断 PDF 文件的内容性质。

# 参考

[1] Python 判断 PDF 文件是否是图片扫描版，https://deepinout.com/python/python-qa/166_hk_1710802770.html

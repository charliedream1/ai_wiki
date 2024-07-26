# docx 转 markdown
# 1. 免费方案

- 实测效果良好，但标题无法识别，只会标为加粗
- 下面图片部分会报错，暂时注释掉，未去排查
- 实测表格可以正确转换(有线和无线表，即便表格数字存在显示不下的换行，也能正常显示)，未测试复杂表格
- 实测双栏可以被正确转为单栏

```bash
pip install mammoth -i https://pypi.tuna.tsinghua.edu.cn/simple  
pip install markdownify -i https://pypi.tuna.tsinghua.edu.cn/simple
```

```python
import os
import time
import mammoth
import markdownify


# 转存Word文档内的图片
def convert_img(image):
    with image.open() as image_bytes:
        file_suffix = image.content_type.split("/")[1]
        path_file = "./img/{}.{}".format(str(time.time()), file_suffix)
        with open(path_file, 'wb') as f:
            f.write(image_bytes.read())

    return {"src": path_file}


def docx2html(in_file, out_file):
    with open(in_file, "rb") as docx_file:
        # 转化Word文档为HTML
        result = mammoth.convert_to_html(docx_file)  # , convert_image=mammoth.images.img_element(convert_img))
        # 获取HTML内容
        html = result.value
        # 转化HTML为Markdown
        md = markdownify.markdownify(html, heading_style="ATX")
        pass

    with open(out_file, "w", encoding="utf-8") as f:
        f.write(md)
```

处理Word图片
因为Word文档中不可避免地会存在很多图片，为了在转换后的文档中能够正确地显示图片,
我们需要自定义一下Word 文档内图片的处理方式。默认情况下，mammoth会将图片转换为
base64编码的字符串，这样不用胜成额外的本地图片文件,但是会使文档体积变得很大。所
以我们选择将图片另存为本地图片

存储html及markdown

```python
# 读取Word文件
with open(r"D:\code\Test\TestBook\测试用例相关文档\WEB测试用例\12345.docx", "rb") as docx_file:
    # 转化Word文档为HTML
    result = mammoth.convert_to_html(docx_file,convert_image = mammoth.images.img_element(convert_imgs))
    # 获取HTML内容
    html = result.value
    # 转化HTML为Markdown
    md = markdownify.markdownify(html,heading_style="ATX")
    print(md)
    with open("./docx_to_html.html",'w',encoding='utf-8') as html_file,open("./docx_to_md.md","w",encoding='utf-8') as md_file:
        html_file.write(html)
        md_file.write(md)
    messages = result.messages

```

# 2. 收费方案

实测和方案1效果差不多，但会再文件开头带上水印图片和说明行

```bash
pip install aspose-words
```

```python
import aspose.words as aw

# 加载文档
doc = aw.Document("document.docx")

# 另存为降价文件
doc.save("document.md")
```

# 参考

[1] Python实现Word文档转换Markdown， https://blog.csdn.net/pacong/article/details/134316578
[2] 使用 Python 将 Word 文档转换为 Markdown，https://blog.aspose.com/zh/words/convert-word-to-markdown-using-python/
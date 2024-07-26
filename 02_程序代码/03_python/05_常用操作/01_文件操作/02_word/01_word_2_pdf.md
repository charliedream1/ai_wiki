# 1. 简介

当前大部分方案均依赖office/libreOffice/WPS等组建，转换效果较好的为office和wps。其余的较好转换库均收费。

![](.01_word_2_pdf_images/转换工具效果对比.png)

# 2. 使用

## 2.1 windows下的处理方法

```python
from win32com import client


# 转换doc为pdf
def doc2pdf(fn):
    word = client.Dispatch("Word.Application")  # 打开word应用程序
    # for file in files:
    doc = word.Documents.Open(fn)  # 打开word文件
    doc.SaveAs("{}.pdf".format(fn[:-4]), 17)  # 另存为后缀为".pdf"的文件，其中参数17表示为pdf
    doc.Close()  # 关闭原来word文件
    word.Quit()


# 转换docx为pdf
def docx2pdf(fn):
    word = client.Dispatch("Word.Application")  # 打开word应用程序
    # for file in files:
    doc = word.Documents.Open(fn)  # 打开word文件
    doc.SaveAs("{}.pdf".format(fn[:-5]), 17)  # 另存为后缀为".pdf"的文件，其中参数17表示为pdf    
    doc.Close()  # 关闭原来word文件
    word.Quit()


docx2pdf(r'C:\Users\asuka\Desktop\新建文件夹\1.docx')
doc2pdf(r'C:\Users\asuka\Desktop\新建文件夹\2.doc')
```

# 参考

[1] python实现——WORD转PDF（全自动化，支持doc、docx），https://blog.csdn.net/weixin_44288604/article/details/117110298
[2] Python在Linux环境下Word转PDF, https://blog.csdn.net/lly1122334/article/details/122620790

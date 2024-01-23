# 1. 安装需要的包

```python
pip install PyPDF2
```

# 2. 代码

```python
import os
from PyPDF2 import PdfMerger

# fixme: PDF文件路径
target_path = r'E:\PDF'
pdf_lst = [f for f in os.listdir(target_path) if f.endswith('.pdf')]
pdf_lst = [os.path.join(target_path, filename) for filename in pdf_lst]

file_merger = PdfMerger()
for pdf in pdf_lst:
    file_merger.append(pdf, import_outline=False)     # 合并pdf文件

# fixme: 输出路径
out_path = r'E:\Output'
file_merger.write(os.path.join(out_path, "merge.pdf"))
```

# 3. 问题

报错：PdfReadError: Unexpected destination ‘/__WKANCHOR_2‘
解决办法：加上参数import_bookmarks=False
file_merger.append(pdf,import_bookmarks=False)
(上述代码已添加，直接使用即可)

# 参考

[1] 使用python合并多个pdf文件，https://blog.csdn.net/mys_mys/article/details/122243859

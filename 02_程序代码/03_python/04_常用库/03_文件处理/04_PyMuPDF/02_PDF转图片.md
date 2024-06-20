~~# 1. 资源

- Github (4.4k stars): https://github.com/pymupdf/PyMuPDF
- 文档：https://pymupdf.readthedocs.io/en/latest/rag.html

# 2. 安装
```bash
pip install PyMuPDF
```

# 3. PDF转图片

方法1： 使用pix.tobytes

```python
import fitz
from tqdm import tqdm

file_path = 'test.pdf'
pdf_doc = fitz.open(file_path)
pbar = tqdm(total=pdf_doc.page_count, desc="Parsing PDF")

for pg in range(pdf_doc.page_count):
    pbar.update(1)
    page = pdf_doc[pg]
    rotate = int(0)
    # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
    # 此处若是不做设置，默认图片大小为：792X612, dpi=96
    zoom_x = 1.33333333  # (1.33333333-->1056x816)   (2-->1584x1224)
    zoom_y = 1.33333333
    mat = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
    pix = page.get_pixmap(matrix=mat, alpha=False)
    
    # 转成PIL图片及CV2支持的格式
    img_data = pix.tobytes("ppm")
    import io
    import cv2
    import numpy as np
    from PIL import Image
    pil_img = Image.open(io.BytesIO(img_data))
    img = cv2.cvtColor(np.asarray(pil_img), cv2.COLOR_RGB2BGR)

    # 保存图片 (仅调试用)
    out_path = f'/data/nvme2/tmp/{pg}.png'
    pix._writeIMG(out_path, format_='png', jpg_quality=94)
```

方法2：
```python
# Render the page as a PNG image with a resolution of 150 DPI
    pix = page.get_pixmap(dpi=150)
    image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
```

# 参考

[1] python 将PDF 转成 图片的几种方法，https://blog.csdn.net/weixin_42081389/article/details/103712181~~

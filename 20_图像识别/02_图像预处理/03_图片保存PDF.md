```python
from PIL import Image

def jpg2pdf(jpgFile):
    path,fileName = jpgFile.rsplit('\\',1)
    preName,postName = fileName.rsplit('.',1)

    img = Image.open(jpgFile)
    return img.save(path+"\\"+preName+'.pdf', "PDF", resolution=100.0, save_all=True)
```

# 参考

[1] 用Python+PIL将目录下jpg图像批量转成pdf文件, https://blog.csdn.net/LaoYuanPython/article/details/118913443
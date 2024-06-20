# PIL.Image转换成OpenCV格式

```python
import cv2  
from PIL import Image  
import numpy  
  
image = Image.open("plane.jpg")  
image.show()  
img = cv2.cvtColor(numpy.asarray(image),cv2.COLOR_RGB2BGR)  
cv2.imshow("OpenCV",img)  
cv2.waitKey()  
```

cv2保存图片用cv2.imwrite("/home/1.jpg" ,frame * 1) # *1才为彩色,后面*1可以不写

cv2看图片大小用 img.shape # 它的输出是(480, 640, 3)，记住这里宽是480,长是640，深度是3色的彩色

cv2裁剪用img = img[60:420, 60:580, :] #eg:[宽为60~（480-60），长为60～（640-60),第三个是选择全部深度]

# OpenCV转换成PIL.Image格式

```python
import cv2  
from PIL import Image  
import numpy  
  
img = cv2.imread("plane.jpg")  
cv2.imshow("OpenCV",img)  
image = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))  
image.show()  
cv2.waitKey()
```

PIL的Image保存图片用img.save(“001.jpg”)

PIL的Image看图片大小用frame.size

PIL的Image裁剪用crop


# 参考

[1] cv2和PIL.Image之间的转换，https://blog.csdn.net/qq_38153833/article/details/88060268
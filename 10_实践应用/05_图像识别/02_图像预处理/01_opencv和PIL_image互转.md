PIL.Image转换成OpenCV格式

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

OpenCV转换成PIL.Image格式

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

判断图像数据是否是OpenCV格式

```python
isinstance(img, np.ndarray)
```

判断OpenCV版本是2还是3或4

```python
import cv2
import imutils   #若没有包使用 pip install imutils 安装
 
if imutils.is_cv2():
    print("OpenCV2")
 
if imutils.is_cv3():
    print("OpenCV3")
 
if imutils.is_cv4():
    print("OpenCV4")
```

# 参考

[1] python中PIL.Image和OpenCV图像格式相互转换, https://blog.csdn.net/dcrmg/article/details/78147219
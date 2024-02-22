import cv2
import base64
import numpy as np
from paddleocr import PaddleOCR

filepath = './image/大模型指令对齐训练原理-幕布图片-17565-176537.jpg'
use_gpu = True

# 初始化 PaddleOCR 引擎
ocr_engine = PaddleOCR(use_angle_cls=True, lang="ch", use_gpu=use_gpu, show_log=False)

img_np = cv2.imread(filepath)
h, w, c = img_np.shape
img_data = {"img64": base64.b64encode(img_np).decode("utf-8"), "height": h, "width": w, "channels": c}

img_file = img_data['img64']
height = img_data['height']
width = img_data['width']
channels = img_data['channels']

binary_data = base64.b64decode(img_file)
img_array = np.frombuffer(binary_data, dtype=np.uint8).reshape((height, width, channels))
print("shape: {}".format(img_array.shape))

# 调用 PaddleOCR 进行识别
res = ocr_engine.ocr(img_array)
print("ocr result: {}".format(res))

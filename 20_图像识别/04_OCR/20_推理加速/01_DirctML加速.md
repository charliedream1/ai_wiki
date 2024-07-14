# 1. 资料

DirectML 示例应用程序: https://learn.microsoft.com/zh-cn/windows/ai/directml/dml-min-app

Discussions #175: https://github.com/RapidAI/RapidOCR/discussions/175

# 2. 详解

DirectML 是什么？

直接机器学习 (DirectML) 是机器学习 (ML) 的低级 API。API 具有常见的（本机 C++、nano-COM）编程接口和 DirectX 12 样式的工作流。可将机器学习推断工作负荷集成到游戏、引擎、中间件、后端或其他应用程序中。所有与 DirectX 12 兼容的硬件都支持 DirectML。

硬件加速的机器学习基元（称为“运算符”）是 DirectML 的构建基块。在这些构建基块中，可以开发纵向扩展、抗锯齿和样式转移等机器学习技术。例如，使用噪声抑制和超解析度，可以实现令人印象深刻的光线跟踪效果且可以减少每个像素的光线。

可将机器学习推断工作负荷集成到游戏、引擎、中间件、后端或其他应用程序中。DirectML 提供用户熟悉的（本机 C++、nano-COM）DirectX 12 式编程接口和工作流，且受所有 DirectX 12 兼容硬件的支持。有关 DirectML 示例应用程序（包括精简 DirectML 应用程序的示例），请参阅 DirectML 示例应用程序[1]。

DirectML 是在 Windows 10 版本 1903 和 Windows SDK 的相应版本中引入的。

***

RapidOCR 下如何使用 DirectML 加速呢？

目前在rapidocr_onnxruntime>=1.3.23中，配置了使用 DirectML 的开关。在满足一定条件后，可以正常使用 DirectML 加速推理 OCR。

要想使用 DirectML 加速，需要满足以下条件：

设备系统要大于等于 Windows 10 版本 1903

安装rapidocr_onnxruntime>=1.3.23版本

安装onnxruntime-directml包

***

具体使用教程
首先需要确定自己设备是 Windows 系统，且版本要大于等于 Window 10 1903

安装rapidocr_onnxruntime>=1.3.23
pip install rapidocr_onnxruntime
安装onnxruntime-directml
# 首先卸载上一步默认安装的onnxruntime
pip uninstall onnxruntime

# 安装onnxruntime-directml
pip install onnxruntime-directml
Python 使用
from rapidocr_onnxruntime import RapidOCR

engine = RapidOCR()

img_path = 'tests/test_files/ch_en_num.jpg'

# 默认都为False
result, elapse = engine(img_path, det_use_dml=True, cls_use_dml=True, rec_use_dml=True)
print(result)
print(elapse)

# 参考

[1] 如何使用DirectML加速推理OCR？https://mp.weixin.qq.com/s/MmQnpSMve7Rhr0aVOqmgUA
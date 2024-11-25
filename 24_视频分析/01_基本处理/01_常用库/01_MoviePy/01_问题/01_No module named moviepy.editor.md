# 问题

MoviePy视频编辑和处理Python库的版本问题解决：No module named ‘moviepy.editor‘

# 原因

python3.7版本后不支持 from moviepy.editor 引用方式，由于是moviepy 2.0.0版本

# 解决方案

参考：https://blog.csdn.net/fengbuyu/article/details/143931821

修改方法：

from moviepy import *

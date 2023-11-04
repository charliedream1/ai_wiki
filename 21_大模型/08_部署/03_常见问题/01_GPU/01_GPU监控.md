# 1. 使用nvidia相关命令

nvidia-smi简称NVSMI，提供监控GPU使用情况和更改GPU状态的功能，是一个跨平台工具，
它支持Linux以及从Windows系统。

```shell
nvidia-smi
watch -n 1 -d nvidia-smi # 每隔一秒刷新一次
```

![](.01_GPU监控_images/GPU状态查询.png)

# 2. 使用gpustat库可实时监测

安装gpustat库。

```shell
pip install gpustat
```

运行命令

```shell
gpustat --w
```

![](.01_GPU监控_images/gpustat监控GPU.png)

# 3. (3)使用python的pynvml库
安装pynvml库。

```shell
pip install pynvml
```

下面为使用示例：

```python
import pynvml
pynvml.nvmlInit()
handle = pynvml.nvmlDeviceGetHandleByIndex(0) # 指定显卡号
meminfo = pynvml.nvmlDeviceGetMemoryInfo(handle)
print(meminfo.total/1024**2) #总的显存大小（float）
print(meminfo.used/1024**2)  #已用显存大小（float）
print(meminfo.free/1024**2)  #剩余显存大小（float）
```

# 参考

[1] python运行程序设置指定GPU(查看GPU使用情况), https://blog.csdn.net/weixin_43818631/article/details/118856558
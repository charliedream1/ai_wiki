# 1. 安装

## 1.1 Linux 安装

```shell
pip install faiss
```

通过上述方法安装，可能会报错：
```
No module named '_swigfaiss'
```


```shell
sudo apt-get install libopenblas-dev
sudo apt-get install libomp-dev

#cpu 版本
conda install faiss-cpu -c pytorch
# GPU 版本
conda install faiss-gpu cudatoolkit=8.0 -c pytorch # For CUDA8
conda install faiss-gpu cudatoolkit=9.0 -c pytorch # For CUDA9
conda install faiss-gpu cudatoolkit=10.0 -c pytorch # For CUDA10
```

## 1.2 Windows 安装

```shell
pip install faiss-cpu
```

使用如上方法安装，gpu版还未进行尝试

若用conda install安装后可能会报错

```shell
from . import _swigfaiss ImportError: DLL load failed: 
```

# 参考
[1] No module named swigfaiss, https://blog.csdn.net/bitcarmanlee/article/details/106317279
[2] 解决from . import _swigfaiss ImportError: DLL load failed: 找不到指定的模块, 
    https://blog.csdn.net/dulinli/article/details/131833578
# 1. 安装

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

# 参考
[1] No module named swigfaiss, https://blog.csdn.net/bitcarmanlee/article/details/106317279
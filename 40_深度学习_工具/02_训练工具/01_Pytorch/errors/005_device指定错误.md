# 1. 问题

在python中用如下方式指定使用的显卡

```python
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "1"  # 指定几号卡
```

有时候会报如下错误：

```text
RuntimeError: device >= 0 && device < num_gpus INTERNAL ASSERT FAILED at "../aten/src/ATen/cuda/CUDAContext.cpp":50, please report a bug to PyTorch. device=1, num_gpus=
```

# 2. 解决方法

1. 方法1
   
   把代码os.environ放在torch的前面

2. 方法2

   ```shell
    export CUDA_DEVICE_ORDER=PCI_BUS_ID
    nohup python data_train.py > log/log.txt 2>&1 &
    ```

3. 方法3

   ```shell
   CUDA_VISIBLE_DEVICES=0,1,2,3 python train.py
   ```
   
# 参考

[1] 正确设置PyTorch训练时使用的GPU资源，https://blog.csdn.net/duzm200542901104/article/details/133137755
[2] 解决pytorch指定GPU后还使用第一张卡的问题，https://blog.csdn.net/qq_53239443/article/details/134388217
1. Tensor转NumPy

    ```python
    a = torch.ones(5)
    b = a.numpy()
    ```

2. numpy转tensor

    ```python
    import numpy as np
    a = np.ones(5)
    b = torch.from_numpy(a)
    print(a, b)
    a += 1
    print(a, b)
    b += 1
    print(a, b)
    ```
   
# 参考

[1] 如何将Tensor和NumPy相互转换，https://zhuanlan.zhihu.com/p/607281406
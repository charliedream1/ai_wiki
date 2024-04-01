# 1. 问题

```shell
export CUDA_VISIBLE_DEVICES="1,2,3,4,5,6,7"
```
通过上述命令引入了可见的CUDA设备，但是实际是按照0，1，2，3，4，5，6去跑的。

# 2. 原因

传入--num_gpus等参数会导致CUDA_VISIBLE_DEVICES失效。
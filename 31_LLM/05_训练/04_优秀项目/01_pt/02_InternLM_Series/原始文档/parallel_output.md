## 并行计算loss

InternEvo目前使用的并行计算loss方法改编自[Apex]( https://github.com/NVIDIA/apex/blob/master/apex/transformer/tensor_parallel/cross_entropy.py)。如需要加速计算loss，可将并行计算loss方法改为[Flash-Attention](https://github.com/Dao-AILab/flash-attention/blob/main/flash_attn/losses/cross_entropy.py)的并行计算方法，需要注意的是，这可能会出现loss不收敛的情况。

具体修改代码可见[InternEvo-parallel-loss](https://github.com/InternLM/InternEvo/blob/develop/internlm/model/ops/cross_entropy.py)
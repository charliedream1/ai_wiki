## Parallel Computing Loss

The parallel computing loss function in InternEvo is adapted from [Apex]( https://github.com/NVIDIA/apex/blob/master/apex/transformer/tensor_parallel/cross_entropy.py). Users can replace the loss function with [Flash-Attention](https://github.com/Dao-AILab/flash-attention/blob/main/flash_attn/losses/cross_entropy.py) to obtain speedup, which may lead to loss divergence.

For detailed modifications in InternEvo,please refer to the code [InternEvo-parallel-loss](https://github.com/InternLM/InternEvo/blob/develop/internlm/model/ops/cross_entropy.py)
# 问题

今天在训练的时候突然报oom错误，看报错，显存分明够用，为什么会出现oom错误呢?

![](.02_max_split_size_mb碎片化管理_images/OOM.png)

在报错里面提到

```text
If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation.  
See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF
```

# 原理

pytoch的显存管理中，分配显存请求必须是连续的，max_split_size_mb设置的是可分割最大的空闲block，小于该值的空闲block可能由于被分割而无法连续使用，大于该值的空闲block将不会被分割。比如max_split_size_mb 设置为4000时，所有小于4000MB空闲block都可能被分割开，当需要连续4g的空间时，就不存在可分配的4g的连续空闲block，而报OOM错误。

```text
max_split_size_mb分割的对象是空闲Block（这里有个暗含的前提：pytorch显存管理机制中，显存请求必须是连续的）。
这里实际的逻辑是：由于默认策略是所有大小的空闲Block都可以被分割，所以导致OOM的显存请求发生时，
所有大于该请求的空闲Block有可能都已经被分割掉了。而将max_split_size_mb设置为小于该显存请求的值，
会阻止大于该请求的空闲Block被分割。如果显存总量确实充足，即可保证大于该请求的空闲Block总是存在，
从而避免了分配失败的发生。
```

# 解决方案

最优设置策略：将max_split_size_mb设置为小于OOM发生时的显存请求大小最小值的最大整数值，就可以在保证跑大图的可行性的同时最大限度照顾性能。这里请求是3.95GB所以可以设置为3950MB。

所以对于显存碎片化引起的CUDA OOM，解决方法是将PYTORCH_CUDA_ALLOC_CONF的max_split_size_mb设为较小值。

```python
set PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:3950
import os 
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "max_split_size_mb:3950"
```

# 参考

[1] CUDA oom 通过设置PYTORCH_CUDA_ALLOC_CONF中的max_split_size_mb解决Pytorch的显存碎片化导致的CUDA:Out Of Memory，https://zhuanlan.zhihu.com/p/652560340
# 模型

https://modelscope.cn/models/iic/gte_Qwen2-7B-instruct

# 问题

ImportError: cannot import name ‘is_mlu_available‘ from ‘accelerate.utils‘异常处理

或者：

ImportError: cannot import name ‘is_mlu_available‘ from ‘transformers.utils‘异常处理

# 解决方案

```bash
pip install --upgrade accelerate
```

# 参考

[1] https://blog.csdn.net/hai4321/article/details/140684856, ImportError: cannot import name ‘is_mlu_available‘ from ‘accelerate.utils‘异常处理

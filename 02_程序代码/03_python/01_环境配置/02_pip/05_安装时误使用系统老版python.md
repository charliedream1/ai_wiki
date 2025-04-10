# 问题

pip install peft==0.15.1
Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple
ERROR: Ignored the following versions that require a different python version: 0.14.0 Requires-Python >=3.9.0; 0.15.0 Requires-Python >=3.9.0; 0.15.1 Requires-Python >=3.9.0
ERROR: Could not find a version that satisfies the requirement peft==0.15.1 (from versions: 0.0.1, 0.0.2, 0.1.0, 0.2.0, 0.3.0, 0.4.0, 0.5.0, 0.6.0, 0.6.1, 0.6.2, 0.7.0, 0.7.1, 0.8.0, 0.8.1, 0.8.2, 0.9.0, 0.10.0, 0.11.0, 0.11.1, 0.12.0, 0.13.0, 0.13.1, 0.13.2)
ERROR: No matching distribution found for peft==0.15.1\n为什么报这个错误，看样子python版本太老，但是我装了3.11的python在conda环境中，且conda环境已经激活，为什么报这个错呢？

# 解决方法

手动指定Python解释器路径

如果确认Python版本正确但pip仍报错，可绕过环境变量直接调用Conda的Python：

```bash
/path/to/conda/envs/your_env/bin/python -m pip install peft==0.15.1
```
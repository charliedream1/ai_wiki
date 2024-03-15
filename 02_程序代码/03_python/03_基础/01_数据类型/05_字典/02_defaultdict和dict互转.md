# 1. dict转defaultdict

```python
from collections import defaultdict

original_dict = {"apple": 1, "banana": 2}
default_dict = defaultdict(int, original_dict)

print(default_dict)
```

# 2. defaultdict转dict

```python
from collections import defaultdict

# 创建一个defaultdict对象
default_dict = defaultdict(list)
default_dict['key1'].append('value1')
default_dict['key2'].append('value2')

# 使用dict()函数进行转换
dict_obj = dict(default_dict)
print(type(dict_obj))  # 输出: <class 'dict'>
print(dict_obj)  # 输出: {'key1': ['value1'], 'key2': ['value2']}
```

# 参考

[1] Converting Python dict to defaultdict: 5 Effective Methods,https://blog.finxter.com/converting-python-dict-to-defaultdict-5-effective-methods/
[2] Python 如何将defaultdict转换为dict, https://deepinout.com/python/python-qa/905_python_how_to_convert_defaultdict_to_dict.html
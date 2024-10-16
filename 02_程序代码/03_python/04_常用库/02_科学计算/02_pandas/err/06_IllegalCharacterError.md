# 简介

该问题参考GPT-4o给出的方案解决

# 问题

```text
File "/home/prj/remote_prg/
_pipeline.py", line 189, in save_files
    df.to_excel(save_path, index=False)
  File "/home/miniconda3/envs/train_py310/lib/python3.10/site-packages/pandas/util/_decorators.py", line 333, in wrap
per
    return func(*args, **kwargs)
  File "/home/miniconda3/envs/train_py310/lib/python3.10/site-packages/pandas/core/generic.py", line 2414, in to_exce
l
    formatter.write(
  File "/home/miniconda3/envs/train_py310/lib/python3.10/site-packages/pandas/io/formats/excel.py", line 952, in writ
e
    writer._write_cells(
  File "/home/miniconda3/envs/train_py310/lib/python3.10/site-packages/pandas/io/excel/_openpyxl.py", line 490, in _w
rite_cells
    xcell.value, fmt = self._value_with_fmt(cell.val)
  File "/home/miniconda3/envs/train_py310/lib/python3.10/site-packages/openpyxl/cell/cell.py", line 218, in value
    self._bind_value(value)
  File "/home/miniconda3/envs/train_py310/lib/python3.10/site-packages/openpyxl/cell/cell.py", line 197, in _bind_val
ue
    value = self.check_string(value)
  File "/home/miniconda3/envs/train_py310/lib/python3.10/site-packages/openpyxl/cell/cell.py", line 165, in check_str
ing
    raise IllegalCharacterError(f"{value} cannot be used in worksheets.")
openpyxl.utils.exceptions.IllegalCharacterError: 
```

# 方案

这个错误 (`openpyxl.utils.exceptions.IllegalCharacterError`) 是由 Excel 文件保存时包含非法字符引起的。Excel 文件中的单元格值不能包含某些特殊字符，如果 `pandas` DataFrame 中的某些值包含了这些非法字符，就会导致保存 Excel 文件时抛出此错误。

### 解决办法：
1. **检查非法字符**：你可以检查 DataFrame 中是否存在非法字符，并清除它们。常见的非法字符包括：`\x00`（空字符）、`\x01` 等不可打印的控制字符。

2. **移除或替换非法字符**：使用 `pandas` 和正则表达式来清理 DataFrame 中的数据，去除这些非法字符。

以下是一个示例代码，演示如何处理 DataFrame 中的非法字符：

```python
import pandas as pd
import re

def remove_illegal_characters(df):
    # 定义非法字符的正则表达式
    illegal_chars = re.compile(r'[\x00-\x1F\x7F-\x9F]')
    
    # 通过applymap来对整个DataFrame的每个元素进行检查
    return df.applymap(lambda x: illegal_chars.sub('', str(x)) if isinstance(x, str) else x)

# 假设df是你的DataFrame
df_cleaned = remove_illegal_characters(df)

# 保存清理后的数据
df_cleaned.to_excel(save_path, index=False)
```

### 步骤解析：
- **正则表达式 `r'[\x00-\x1F\x7F-\x9F]'`**：表示ASCII控制字符，这些字符在Excel中是非法的。
- **`applymap()`**：遍历整个 DataFrame 的每个元素，对字符串类型的数据进行替换非法字符的操作。

通过上述方法，你可以移除或替换非法字符，解决 `IllegalCharacterError` 错误。

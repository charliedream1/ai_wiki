# 保存json

```python
import json
final_stat_dict = {}
save_path = 'final_stat.json'
with open(save_path, 'w') as f:
    json.dump(final_stat_dict, f, indent=4, ensure_ascii=False)  # indent=4 用来格式化输出，增加可读性
```

# 加载json

```python
import json
final_stat_file_path = 'final_stat.json'
with open(final_stat_file_path, 'r') as f:
    final_stat_dict = json.load(f)
```
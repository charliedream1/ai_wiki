如果模型输出的json结构不完整，或者加载这描述在前面或后面，都可以用json_repair来修复。实测，效果不错。

注意：你最好在提示词里给出json的结构，否则json可能是list的，也可能是字典的，最后导致不好解析（这里说的是你自己解析理解，而不是json_repair不好修复）。

```python
import json_repair
# content为文本字符串
ret = json_repair.loads(content)
```

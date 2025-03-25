# 加载jsonl
```python
import json
relate_person_lst = []
info_extract_file_path = 'relate_person.jsonl'
with open(info_extract_file_path, 'r') as f:
    for line in f:
        item = json.loads(line)
        relate_person_lst.append(item)
```

# 保存jsonl
```python
import json
save_path = 'relate_person.jsonl'
relate_person_lst = [{'name': '张三', 'age': 18}, {'name': '李四', 'age': 20}]
with open(save_path, 'w') as f:
    for item in relate_person_lst:
        json.dump(item, f, ensure_ascii=False)
        f.write('\n')
```
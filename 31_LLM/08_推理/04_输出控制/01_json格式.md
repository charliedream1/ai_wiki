1. Strict JSON
   - Github (122 stars): https://github.com/tanchongmin/strictjson
   - 用于解决大模型输出json格式括号不对称，无法用json.load解析的问题

2. json_repair
   ```bash
   pip install json_repair
   ```
   ```python
   parsed_json = json_repair.loads(raw_schema)
   ```
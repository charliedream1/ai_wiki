# 1. 问题

数据加载过程中，dataset报错，json中存在dict

```text
出现raise JSONDecodeError("Extra data", s, end) json.decoder.JSONDecodeError: 
Extra data: line 2 column 1 (char 259) 
```

# 2. 解决方法

排查数据中用json加载数据后，如果不是字符串，存在dict、None或空字符串，都会出现上述错误

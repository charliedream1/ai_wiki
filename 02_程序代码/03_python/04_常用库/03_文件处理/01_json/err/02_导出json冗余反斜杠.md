最近在解析json时发现value部分引入了不少额外的双引号和转义引号，具体如下：

```markdown
"test_str":"{\"created_time\": \"Fri_Aug_08 11:04:40 +0000 2014\"}"
```

下面解释下如何在存储和读取json文件时避免这种情况。

一、如何在存储时避免   
存储这里如果能规避掉，就可以让解析的同学解析更加方便。
因为是存储时写入了双重编码JSON字符串，所以才会出现这种情况。
所以写入文件时检查一下是否进行了多次编码。

```shell
>>> import json
>>> not_encoded = {"created_at":"Fri Aug 08 11:04:40 +0000 2014"}
>>> encoded_data = json.dumps(not_encoded)
>>> print encoded_data
{"created_at": "Fri Aug 08 11:04:40 +0000 2014"}
>>> double_encode = json.dumps(encoded_data)
>>> print(double_encode)
"{\"created_at\": \"Fri Aug 08 11:04:40 +0000 2014\"}"
```

一、如何在解析时避免
调用第三方库demjson，记得先安装库python -m pip install demjson。
```shell
>>> import demjson
>>> test = r'"{\"created_time\": \"Fri_Aug_08 11:04:40 +0000 2014\"}"'
>>> json_str = demjson.decode(test)
>>> json_str
'{"created_time": "Fri_Aug_08 11:04:40 +0000 2014"}'
>>> json_content = json.loads(json_str)
>>> json_content["created_time"]
'Fri_Aug_08 11:04:40 +0000 2014'
```

# 参考

[1] 解决Python存储或读取json时引入额外的双引号和转义引号, 
    https://blog.csdn.net/xiangxianghehe/article/details/123320084
1. 需求：对prompt字段灵活替换，能加入正则和简单代码
    
   - prompt模板使用Jinja2语法，简单点就是用双大括号代替f-string的单大括号
   - 参考：https://github.com/stanford-oval/WikiChat.git
   - 文件：load_prompt.py
   - 自动对变量名替换，对变量for循环或者if else插入行

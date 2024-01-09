# 1. Bug调试

浏览器按F12，参看具体bug原因

# 2. WebsocketMismatch: 400 Bad Request

1. 问题：  
   werkzeug.routing.exceptions.WebsocketMismatch: 400 Bad Request: 
   The browser (or proxy) sent a request that this server could not understand.

2. 原因：

   这个可能是wekzeug检查网址有效性太严格了，可以修改源码，可以修改flask_sockets的源码，
   也可以修改wekzeug的源码，相对来说，改flask_sockets的源码比较简单。

3. 解决方法：

   安装
   ```shell
    pip install flask_sockets
   ```
   
   ```text
   安装以后手动修改
   文件: flask_sockets.py
   函数: add_url_rule
   修改前:self.url_map.add(Rule(rule, endpoint=f))
   修改后:self.url_map.add(Rule(rule, endpoint=f, websocket=True))
   关于此问题的讨论参考:
   https://github.com/heroku-python/flask-sockets/issues/81
   关于此问题的修改参考:
   https://github.com/slipperstree/flask-sockets/commit/cb06c69db3af2cb52fbc050f3595ffa4100bbee3
   ```

# 3. 端口被占用

可能反复启停，导致没有正常被停止，可以重启服务或者机器


# 参考

[1] nginx 转发代理 wss 和 https (目标程序是 ws 和 http)，https://kebingzao.com/2021/10/21/nginx-proxy-wss-https/
[2] flask_sockets - 错误 WebsocketMismatch 的解决方法, http://blog.mangolovecarrot.net/2022/03/13/368
[3] (仅供参考思路，实际没改成功)Python Flask使用自带的websocket, https://www.cnblogs.com/redke/articles/flask_websocket.html
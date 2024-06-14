# 1. 方法1
```bash
killall python
```

# 2. 方法2
```bash
ps -ef | grep python | grep -v grep | awk '{print $2}' | xargs kill -9
```
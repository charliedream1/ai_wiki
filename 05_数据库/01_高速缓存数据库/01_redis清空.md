查找并登录redis

```bash
>> whereis redis-cli
redis-cli: /usr/bin/redis-cli /usr/share/man/man1/redis-cli.1.gz

# 登录redis
>> /usr/bin/redis-cli -h 127.0.0.1 -p 6379
```

清空redis

```bash
127.0.0.1:6379> flushall
OK
127.0.0.1:6379> dbsize
(integer) 0
127.0.0.1:6379> keys *
(empty list or set)
127.0.0.1:6379> exit
```
如果ssh连接的host key变更，需要删除后才能重新连接
```shell
ssh-keygen -f "/home/.ssh/known_hosts" -R "[118.66.166.11]:22"
```
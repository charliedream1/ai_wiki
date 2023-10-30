# 1. 简介

supervisor是一个Python开发的通用的进程管理程序，可以管理和监控Linux上面的进程，
能将一个普通的命令行进程变为后台daemon，并监控进程状态，异常退出时能自动重启，
但它不能管理原本就是daemon的进程

# 2. 使用

## 2.1 安装

```shell
pip install supervisor
```

测试supervisor安装是否成功

```shell
[root@localhost ~]# echo_supervisord_conf
```

## 2. 生成配置文件
安装好以后，需要生成一份配置文件
```shell
echo_supervisord_conf > /etc/supervisord.conf
```

## 3. 为每个进程单独配置
你可以直接在/etc/supervisord.conf 里编写对任务控制的配置，
更加合理的方法是在一个专门的文件夹中针对每一个进程进行配置，创建一个存储配置的目录

```shell
mkdir /etc/supervisord.d/
```

为每个程序编写一个配置文件，使得他们相互隔离，现在需要对/etc/supervisord.conf 
进行修改以完成这个配置, 找到[include]， 修改配置

```editorconfig
[include]
files = /etc/supervisord.d/*.conf
```

## 4. 一份配置示例
在/etc/supervisord.d/目录下新增一个conf文件

```editorconfig
[program:project_name]
directory = 工作目录
command = 脚本的启动命令
autostart = true
autorestart = true
user = loanward
stdout_logfile = /data/log/pro_stdout.log
```

1. project_name 必须是唯一的，否则将会出现错乱
2. directory 填写你启动脚本时的工作目录，如果你使用脚本的绝对目录，那么directory可以不设置
3. command是执行脚本的命令，不需要使用nohup让其变为后代进程，supervisor会自动将其变为后台进程
4. autostart 配置为True， supervisor 启动时，任务跟随启动
5. autorestart 配置为True， 进程不存在时会自动重启， 默认重启3次，想修改重启次数，可以配置startretries， 
   设置最多重启的次数
6. user 设置启动任务时所用的用户，supervisor 有必要使用root账号启动，这样才有权限配置其他启动账号
7. stdout_logfile 配置输出日志

## 5. 启动supervisor
```shell
supervisord -c /etc/supervisord.conf
```

## 6. 使用supervisorctl 进行管理

supervisorctl 是 supervisord 的一个命令行客户端工具，使用supervisorctl可以遍历的对进程进行管理，支持的命令如下

```markdown
supervisorctl status                         # 查看进程状态
supervisorctl stop project_name              # 终止某个进程
supervisorctl start project_name             # 启动某个进程
supervisorctl restart project_name           # 重启某个进程
supervisorctl reread                         # 更新配置，根据最新的配置启动程序，会启动已经运行的程序
supervisorctl update  
```       

# 7. 常用命令

查看 supervisord 服务是否在运行：

```shell
[root@localhost ~]# ps aux | grep supervisord
```

查看 supervisord 服务是否生效

```shell
[root@localhost ~]# ps -ef | grep ProjectName
```

# 8. 开机自启动

1. 在 /usr/lib/systemd/system/ 目录下面新建文件supervisord.service，并写入如下内容：

```text
[Unit]
Description=Process Monitoring and Control Daemon(Supervisor daemon)
After=rc-local.service nss-user-lookup.target
 
[Service]
Type=forking
ExecStart=/usr/bin/supervisord -c /etc/supervisor/supervisord.conf
ExecStop=/usr/bin/supervisord shutdown
ExecReload=/usr/bin/supervisord reload
killMode=process
Restart=on-failure
RestartSec=42s
 
[Install]
WantedBy=multi-user.target
```

2.启动服务：执行开机启动命令，让 supervisord 服务开机自启。

```shell
[root@localhost ~]# systemctl enable supervisord
```

3.验证一下是否为开机启动。enabled：开机自启。disabled：开机不自启。

```shell
[root@localhost ~]# systemctl is-enabled supervisord
```

4.重启服务器，检查 supervisor 是否启动。

```shell
[root@localhost ~]# ps aux | grep supervisor
```


# 参考

[1] 用supervisor管理python进程, https://zhuanlan.zhihu.com/p/264111843
[2] Python—守护进程管理工具（Supervisor）, https://www.cnblogs.com/liuhaidon/p/12217153.html
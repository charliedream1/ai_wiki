# 1. 安装依赖

nginx常用命令

- 输入以下命令以停止 Nginx 服务： sudo systemctl stop nginx
- 输入以下命令以重新启动 Nginx 服务： sudo systemctl start nginx

## 1.1. Nginx安装

Nginx 发音 “engine x” ,是一个开源软件，高性能 HTTP 和反向代理服务器，
用来在互联网上处理一些大型网站。它可以被用作独立网站服务器，负载均衡，
内容缓存和针对 HTTP 和非 HTTP 的反向代理服务器。

和 Apache相比，Nginx 可以处理大量的并发连接，并且每个连接占用一个很小的内存。

1. 前提条件

    在继续之前，保证以 sudo 用户身份登录，并且你不能运行 Apache 或者 其他处理进程在80端口和443端口。

2. 安装 Nginx

   Nginx 在默认的 Ubuntu 源仓库中可用。想要安装它，运行下面的命令：
   
   ```shell
    sudo apt update
    sudo apt install nginx
   ```

   一旦安装完成，Nginx 将会自动被启动。你可以运行下面的命令来验证它：

    ```
     sudo systemctl status nginx
    ```    

    输出类似下面这样：
    
    ```
   ● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
     Active: active (running) since Sat 2020-05-02 20:25:43 UTC; 13s ago
    ```

3. 配置防火墙

   现在你已经在你的服务器上安装和运行了 Nginx，你需要确保你的防火墙被配置好，
   允许流量通过 HTTP（80）和 HTTPS（443）端口。假设你正在使用UFW,你可以做的是启用
   ‘Nginx Full’ profile，它包含了这两个端口：

   ```shell
   sudo ufw allow 'Nginx Full'
   ```

   想要验证状态，输入：

   ```shell
   sudo ufw status
   ```

   输出将会像下面这样：
   
   ```
   Status: active

   To                         Action      From
   --                         ------      ----
   22/tcp                     ALLOW       Anywhere
   Nginx Full                 ALLOW       Anywhere
   22/tcp (v6)                ALLOW       Anywhere (v6)
   Nginx Full (v6)            ALLOW       Anywhere (v6)
   ```

4. 测试安装

   想要测试你的新 Nginx 安装，在你的浏览器中打开http://YOUR_IP，
   你应该可以看到默认的 Nginx 加载页面，像下面这样：
    
   ![](.README_images/nginx欢迎界面.png)

5. Nginx 配置文件结构以及最佳实践

   - 所有的 Nginx 配置文件都在/etc/nginx/目录下。
   - 主要的 Nginx 配置文件是/etc/nginx/nginx.conf。
   - 为每个域名创建一个独立的配置文件，便于维护服务器。你可以按照需要定义任意多的 block 文件。
   - Nginx 服务器配置文件被储存在/etc/nginx/sites-available目录下。
      在/etc/nginx/sites-enabled目录下的配置文件都将被 Nginx 使用。
   - 最佳推荐是使用标准的命名方式。例如，如果你的域名是mydomain.com，
     那么配置文件应该被命名为/etc/nginx/sites-available/mydomain.com.conf
   - 如果你在域名服务器配置块中有可重用的配置段，把这些配置段摘出来，做成一小段可重用的配置。
   - Nginx 日志文件(access.log 和 error.log)定位在/var/log/nginx/目录下。
     推荐为每个服务器配置块，配置一个不同的access和error。
   - 你可以将你的网站根目录设置在任何你想要的地方。最常用的网站根目录位置包括：
     - /home/<user_name>/<site_name>
     - /var/www/<site_name>
     - /var/www/html/<site_name>
     - /opt/<site_name>


## 1.2 自定义证书

https无法正常通过websocket连接，需要nginx转发代理

1. nginx conf 目录创建 ssl 目录，并进入这个目录

   ```shell
   [root@VM-0-13-centos ~]# cd /usr/local/nginx/conf/
   [root@VM-0-13-centos conf]# mkdir ssl
   [root@VM-0-13-centos conf]# cd ssl
   ```

2. 创建服务器证书密钥文件 server.key

   ```shell
   # 注意使用2048，如果使用1024，在后面的步骤会报密钥长度过短
   # 步骤中，让输入密码，请输入并记住改密码，再后面的步骤中会用到
   
   [root@VM-0-13-centos ssl]# openssl genrsa -des3 -out server.key 2048
   Generating RSA private key, 1024 bit long modulus
   ........++++++
   ..........................................................++++++
   e is 65537 (0x10001)
   Enter pass phrase for server.key:
   Verifying - Enter pass phrase for server.key:
   ```
   
   然后就会在 ssl 目录下生成: server.key 这个文件

3. 创建服务器证书的申请文件 server.csr
    
    ```shell
   [root@VM-0-13-centos ssl]# openssl req -new -key server.key -out server.csr
   Enter pass phrase for server.key:
   You are about to be asked to enter information that will be incorporated
   into your certificate request.
   What you are about to enter is what is called a Distinguished Name or a DN.
   There are quite a few fields but you can leave some blank
   For some fields there will be a default value,
   If you enter '.', the field will be left blank.
   -----
   Country Name (2 letter code) [XX]:cn
   State or Province Name (full name) []:fujian
   Locality Name (eg, city) [Default City]:xiamen
   Organization Name (eg, company) [Default Company Ltd]:
   Organizational Unit Name (eg, section) []:
   Common Name (eg, your name or your server's hostname) []:
   Email Address []:kebingzao@gmail.com
   
   Please enter the following 'extra' attributes
   to be sent with your certificate request
   A challenge password []:
   An optional company name []:
   ```

   大部分都可以不填，直接一路空格下来。 然后这时候就会在 ssl 目录生成 server.csr:

4. 去除文件口令

   ```shell
   # 这时候可以先备份一份服务器密钥文件:
   [root@VM-0-13-centos ssl]# cp server.key server.key.org
   
   # 接下来去除文件口令:
   [root@VM-0-13-centos ssl]# openssl rsa -in server.key.org -out server.key
   Enter pass phrase for server.key.org:
   writing RSA key
   ```

5. 最后生成证书文件 server.crt

   ```shell
   [root@VM-0-13-centos ssl]# openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
   Signature ok
   subject=/C=cn/ST=fujian/L=xiamen/O=Default Company Ltd/emailAddress=kebingzao@gmail.com
   Getting Private key
   
   # 这时候在 ssl 目录下，就有这四个文件: 
   [root@VM-0-13-centos ssl]# ll
   total 16
   -rw-r--r-- 1 root root 875 Oct 21 17:10 server.crt
   -rw-r--r-- 1 root root 664 Oct 21 17:09 server.csr
   -rw-r--r-- 1 root root 887 Oct 21 17:10 server.key
   -rw-r--r-- 1 root root 951 Oct 21 17:10 server.key.org
   ```
   
## 1.3 转发代理配置

nginx配置文件为：nginx.conf

```shell
server {
        listen       443 ssl;
        server_name  localhost;

        ssl_certificate      ssl/server.crt;
        ssl_certificate_key  ssl/server.key;

        ssl_session_cache    shared:SSL:1m;
        ssl_session_timeout  5m;

        ssl_ciphers  HIGH:!aNULL:!MD5;
        ssl_prefer_server_ciphers  on;

        location / {
            root   html;
            index  index.html index.htm;
        }

        location = /stat {
            proxy_pass http://localhost:8006;
            proxy_set_header Host $host;
            proxy_set_header X-real-ip $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
        
        location = /ws {
            proxy_pass http://localhost:8007;
            
            proxy_read_timeout 300s;
            proxy_send_timeout 300s;
            
            proxy_set_header Host $host;
            proxy_set_header X-real-ip $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection $connection_upgrade;
        }
    }
```

如上图：
- root存放代理的html页面为文件：frontend.html
- proxy_pass为转发的接口，将8007映射到443端口


# 2. 问题

1. werkzeug 对ws匹配有限制，手改了一下werkzeug
2. 端口被占用：
   可能反复启停，导致没有正常被停止，可以重启服务或者机器
3. 页面403  
   因为无权限，查看nginx的配置文件中的html文件和路径是否正确，以及路径访问是否又权限

# 参考

[1] nginx 转发代理 wss 和 https (目标程序是 ws 和 http)，https://kebingzao.com/2021/10/21/nginx-proxy-wss-https/

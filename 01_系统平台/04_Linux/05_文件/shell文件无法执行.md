1. 问题

    windows下编辑的shell文件，换行符和linux不一样，导致无法执行。

2. 解决方法
    
    方法一：
    ```shell
    # 安装
    apt-get install dos2unix
    # 转为unix格式
    dos2unix filename.sh
    ```
   
    方法二：
    ```shell
    # 通过命令查看脚本文件是dos格式还是unix格式，dos格式的文件行尾为^M$ ，unix格式的文件行尾为$：
    # 可通过 cat -A scripts/run_xx.sh  # 验证文件格式
    sed -i "s/\r//" scripts/run_for_local_option.sh
    sed -i "s/^M//" scripts/run_for_local_option.sh
    sed -i "s/\r//" scripts/run_for_cloud_option.sh
    sed -i "s/^M//" scripts/run_for_cloud_option.sh
    sed -i "s/\r//" scripts/run.sh
    sed -i "s/^M//" scripts/run.sh
    ```

1. 问题：  

    重启电脑后，Pycharm一直卡在Uploading PyCharm helpers && Python Interpreter... 
    Python helpers are not copied yet

    ![](.02_上传helps卡住_images/helps卡住.png)

    运行py文件会报错，“Python helpers are not copied yet to the remote host. 
    Please wait until remote interpreter”

2. 解决方法
   
   ```shell
    cd /home/root/
    cd ./.pycharm_helpers/
    rm -rf check_all_test_suite.py
    tar -xvzf helpers.tar.gz
    ```
   
    最后重启pycharm后就可以了

# 参考

[1] 问题解决：Pycharm一直卡在Uploading PyCharm helpers && Python Interpreter... 
    Python helpers are not copied yet, 2021-09-19, https://blog.csdn.net/qq_43827595/article/details/120027389
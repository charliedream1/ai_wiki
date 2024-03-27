1. 文件传输

    ```bash
    ossutil cp -r xxx oss://s3_bucket
    ```
    
    其它参数:
    ```text
    --maxdownspeed=           max download speed,the unit is:KB/s,default value is 0(unlimited)
    --maxupspeed=             max upload speed,the unit is:KB/s,default value is 0(unlimited)
    -u 断点续传
    ```
    
    注意：
    - 如上拷贝方式，会把xxx下的所有文件拷贝到s3_bucket下，而不是xxx文件夹，所以需要注意，
      - 可以采用这种方式：ossutil cp -r xxx oss://s3_bucket/xxx
      
2. 文件查看

    ```bash
    ossutil ls xxx oss://s3_bucket
    ```

3. 文件大小统计

    ```bash
    ossutil du xxx oss://s3_bucket
    ```
   
    ```text
    --all-versions  获取所有版本Object的大小。不添加此选项时，默认查询当前版本Object的大小。
    --block-size  定义输出结果中指定Bucket或目录下包含的Object大小，取值为KB、MB、GB或TB。不添加此选项时，默认以Byte为单位统计Object的大小。
    ```
    
    输出结果：
    ```bash
    storage class   object count            sum size(byte)
    ----------------------------------------------------------
    Standard        12                       132115210
    Archive         1                        814
    ----------------------------------------------------------
    total object count: 13                          total object sum size: 132116024
    total part count:   0                           total part sum size:   0
    
    total du size(byte):132116024
    
    0.382978(s) elapsed
    ```

4. 同步模式
   
   注意：未实际测试

   sync同步文件/文件夹
    
   相关参数

   ```text
    --retry-times 参数可配置当错误发生时的重试次数，默认值：10，取值范围：1~500。
    -j  参数配置多文件操作时的并发任务数，默认值：3，取值范围：1~10000。
    -f      参数表示强制操作，不进行询问提示。
    --part-size 参数配置分片大小
   ```
# 参考

[1] du（获取大小), https://help.aliyun.com/zh/oss/developer-reference/du
[2] DOS命令行工具ossutil上传文件到阿里云OSS（分片断点续传）, https://ranjuan.cn/use-ossutil-upload-oss/#:~:text=%E5%BB%BA%E8%AE%AE%E4%BD%BF%E7%94%A8cp%E5%91%BD%E4%BB%A4%E8%BF%9B%E8%A1%8C%E6%9B%B4%E6%96%B0%E4%B8%8A%E4%BC%A0%EF%BC%8C%E5%A6%82%E6%9E%9C%E4%B8%8D%E5%8A%A0-u%E5%8F%82%E6%95%B0%E5%88%99%E6%89%A7%E8%A1%8C%E7%9A%84%E6%97%B6%E5%80%99%E5%A6%82%E6%9E%9Coss%E4%B8%8A%E5%AD%98%E5%9C%A8%E5%90%8C%E7%9B%9F%E6%96%87%E4%BB%B6%E4%BC%9A%E6%8F%90%E7%A4%BA%E6%98%AF%E5%90%A6%E8%A6%86%E7%9B%96%EF%BC%81%20ossutil64.exe%20cp,ossutil64.exe%20oss%3A%2F%2Fj%2A%2A%2A%2Ast%2Fossutil64.exe%20-u%20cp%E5%88%A9%E7%94%A8%E5%88%86%E7%89%87%E5%AE%9E%E7%8E%B0%E6%96%AD%E7%82%B9%E7%BB%AD%E4%BC%A0%EF%BC%8C%E5%88%86%E7%89%87%E5%A4%A7%E5%B0%8F2563760%3D2503kb%EF%BC%9B%E6%B5%8B%E8%AF%95%E6%96%B9%E6%B3%95%E4%B8%BA%E6%89%BE%E4%B8%AA%E5%A4%A7%E7%82%B9%E7%9A%84%E6%96%87%E4%BB%B6150m%E5%B7%A6%E5%8F%B3%EF%BC%8C%E4%BD%BF%E7%94%A8%E4%B8%8B%E9%9D%A2%E5%91%BD%E4%BB%A4%E4%B8%8A%E4%BC%A0%E7%99%BE%E5%88%86%E6%AF%94%3E10%25%E7%9A%84%E6%97%B6%E5%80%99ctrl%2Bc%E5%8F%96%E6%B6%88%EF%BC%8C%E7%84%B6%E5%90%8E%E5%86%8D%E6%89%A7%E8%A1%8C%E5%90%8C%E6%A0%B7%E7%9A%84%E5%91%BD%E4%BB%A4%EF%BC%8C%E4%BD%A0%E4%BC%9A%E5%8F%91%E7%8E%B0%E4%B8%8A%E4%BC%A0%E8%BF%9B%E5%BA%A6%E4%BC%9A%E5%9C%A8%E5%8E%9F%E6%9D%A5%E5%8F%96%E6%B6%88%E7%9A%84%E8%BF%9B%E5%BA%A6%E7%99%BE%E5%88%86%E6%AF%94%E4%B8%8A%E7%BB%A7%E7%BB%AD%E4%B8%8A%E4%BC%A0%E3%80%82
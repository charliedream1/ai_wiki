# conda环境导出环境内的包（requirements.txt）

## 问题
跑代码的时候配置环境是一个很麻烦的问题，一个项目可能需要很多包，可以使用pip/conda导出conda虚拟环境中的包。

## 解决
### 方式一：使用pip   

1. 使用pip freeze
   ```bash
   pip freeze > requirements.txt #可能会丢失依赖包的版本号
   # 或者
   pip list --format=freeze> requirements.txt
   ```

   生成requirements.txt，pip freeze会将当前环境下所有的安装包都进行生成,再进行安装的时候会全部安装很多没有的包.耗时耗力。

2. 使用pipreqs

   安装
   
   ```bash
   pip install pipreqs
   ```
   
   使用

   在python项目的根目录下 使用 pipreqs ./

   ```bash
   pipreqs ./ --encoding=utf8
   INFO: Successfully saved requirements file in ./requirements.txt
   ```
   
   复现

   最后生成出来的requirements.txt，可以根据这个文件下载所有依赖。

   ```bash
   pip install -r requirements.txt
   # 临时换源
   pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
   ```

### 方式二：使用conda（感觉这种比较好）
导出：
    
```bash
conda list -e > requirements.txt
```

导入安装
    
```bash
conda install --yes --file requirements.txt
```
   
导出yml文件方式（推荐）

```bash
conda env export > freeze.yml
```

安装

```bash
conda env create -f freeze.yml
```

# 参考

[1] conda环境导出环境内的包（requirements.txt）, dianyinghttps://blog.csdn.net/m0_46807718/article/details/138286223
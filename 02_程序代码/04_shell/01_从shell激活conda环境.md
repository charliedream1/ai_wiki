在命令行窗口交互地切换conda虚拟环境，可以通过conda activate/deactivate方便地实现。而在shell脚本中，直接使用相同的命令则会返回报错。

这里有一个用于测试的shell脚本和python脚本

经过一番搜索发现解决的方法很多，归纳为以下几种：

***

方法一：先source conda.sh

```shell
#!/bin/bash
source ~/anaconda3/etc/profile.d/conda.sh
conda activate wrfpy && python test.py
```

***

方法二：使用完整路径

```shell
# 在shell中直接使用目标环境下python的绝对路径
~/anaconda3/envs/wrfpy/bin/python test.py
```

***

方法三：bash hook

```shell
#!/bin/bash
eval "$(conda shell.bash hook)"
conda activate wrfpy && python test.py
```

***

方法四：source activate

```shell
#!/bin/bash
source ~/anaconda3/bin/activate wrfpy && python test.py
```

***

方法五：通过bash -i test.sh执行

```shell
#!/bin/bash
conda activate wrfpy && python test.py
```

***

方法六：通过source test.sh执行

```shell
#!/bin/bash
conda activate wrfpy && python test.py
```

需要注意的是，方法六通过source test.sh执行脚本之后，命令行窗口就切换到虚拟环境下了，而其它方法对窗口的环境不产生影响。

# 参考

[1] shell脚本中激活conda虚拟环境，https://zhuanlan.zhihu.com/p/422365954
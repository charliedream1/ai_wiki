# 1. 问题

```python
kmeans = KMeans(init='k-means++', n_clusters=numClusters, max_iter=100, n_init='auto')
```

```bash
----------------------------------------------------------------------------------------------
C:\PythonVirtualEnv\MLHogwarts\lib\site-packages\sklearn\cluster\_kmeans.py:870: FutureWarning: The default value of `n_init` will change from 10 to 'auto' in 1.4. Set the value of `n_init` explicitly to suppress the warning
  warnings.warn(
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OpenBLAS warning: precompiled NUM_THREADS exceeded, adding auxiliary array for thread metadata.
OOOOOpOenpBLASOOOeOOOOppOenBOLAOS O: OPOOpOeOpenBLenBLpenBLAOpeOpenBpenBpnpenBLASOpenBLAS : Program is Terminated. Because you tried to allocate too many memory regions.
This AS : Program is Terminated. Because you tried to allocate too many memory regions.
This library was built to support a maximum of  : Program is Terminated. Because you tried to allocate too many memory regions.
This library was built to support a maximum of 50 threads - either rebuild OpenBLAS
OpS : Program is Terminated. Because you tried to allocate too many penBLAS : Program is Terminated. Because you tried to allocate too many memory regions.
This library was built to support a maximum of 50 threads - either rebuild OpenBLAS
with a larger NUM_THREADS value or set the environment variableOpenBLAS : Program is Terminated. Because you tried to allocate too many memory regions.
This library was built to support a maximum of 50 threads - either rebuild OpenBLAS
wAS : Program is Terminated. Because you tried to allocate too many memory regions.
This librlibrary penBLAS : Program is Terminated. Because you tried to allocate too many OpenBLAS : Program is Terminated. Because you tried to allocate too many memory regions.
This library was built to support a maximum of 50 threads - either rebuild OpenBLAS
wipary was built to support aenBLAS : Program is Terminated. Because you tried to allocate too many memory regions.
This library was built to support a maximum of 50 threads - either rebuild OpenBLAS
wOwith a larger NUM_THREADS value or set the environment variable OPENBLAS_NUM_THREADS to
aenBLAS : Program is Terminated. Because you tried to allocate too many memory regions.
penBLAS : Program is Terminated. Because you tried to allocate tThis library was built to support a maximum of 50 threads - either rebuild OpenBLAS
with a larger NUM_THREADS value or set the environment variable OPENBLAS_NUM_THREADS to
aith a larger NUM_THREADS value or set the environment variable OPENBLAS_NUM_THREADS to
a sufficiently small number. This error typically occurs when the software that relies on
OpenBLAS calls BLAS functions from many threads in parallel, or when your computer has more
cpu cores than what OpenBLAS was configured to handle.
wenmpnOpmppnrL opL BOppt  5O pipaO
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```

# 2. 解决

直接在bash输入，最后的数字根据自己需要设定：

```shell
export OPENBLAS_NUM_THREADS=2
export GOTO_NUM_THREADS=2
export OMP_NUM_THREADS=2
```

或者在 Python 程序的开头加入 (注意：该方法我尝试了加在代码函数里没有生效，加载头部也不生效)：

```python
import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
```

# 参考

[1] Python创建大量线程时遇上OpenBLAS blas_thread_init报错怎么办？，https://www.cnblogs.com/shiyanhe/p/13604707.html

## 环境安装
### 环境准备
- Python == 3.10
- Ampere或者Hopper架构的GPU (例如H100, A100)
- Linux OS

### pip方式安装
推荐使用 conda 构建一个 Python-3.10 的虚拟环境，命令如下：
```bash
conda create --name internevo-env python=3.10 -y
conda activate internevo-env
```

首先，安装指定版本的torch, torchvision, torchaudio以及torch-scatter:
```bash
pip install --extra-index-url https://download.pytorch.org/whl/cu118 torch==2.1.0+cu118 torchvision==0.16.0+cu118 torchaudio==2.1.0+cu118
pip install torch-scatter -f https://data.pyg.org/whl/torch-2.1.0+cu118.html
```

安装InternEvo:
```bash
pip install InternEvo
```

安装 flash-attention (version v2.2.1)：

如果需要使用flash-attention加速训练，且环境中支持，安装方式如下：
```bash
pip install flash-attn==2.2.1
```

安装 Apex (version 23.05)：

apex为非必须安装包，如果安装，参考下述源码方式安装。

安装megablocks（version 0.3.2）:

如果是MoE相关模型，需要安装。
```bash
pip install git+https://github.com/databricks/megablocks@v0.3.2 # MOE相关
```

### 源码方式安装
#### 依赖包
首先，需要安装的依赖包及对应版本列表如下：
- GCC == 10.2.0
- MPFR == 4.1.0
- CUDA >= 11.8
- Pytorch >= 2.1.0
- Transformers >= 4.28.0

以上依赖包安装完成后，需要更新配置系统环境变量：
```bash
export CUDA_PATH={path_of_cuda_11.8}
export GCC_HOME={path_of_gcc_10.2.0}
export MPFR_HOME={path_of_mpfr_4.1.0}
export LD_LIBRARY_PATH=${GCC_HOME}/lib64:${MPFR_HOME}/lib:${CUDA_PATH}/lib64:$LD_LIBRARY_PATH
export PATH=${GCC_HOME}/bin:${CUDA_PATH}/bin:$PATH
export CC=${GCC_HOME}/bin/gcc
export CXX=${GCC_HOME}/bin/c++
```

#### 安装过程
将项目`InternEvo`及其依赖子模块，从 github 仓库中 clone 下来，命令如下：
```bash
git clone git@github.com:InternLM/InternEvo.git --recurse-submodules
```

推荐使用 conda 构建一个 Python-3.10 的虚拟环境， 并基于`requirements/`文件安装项目所需的依赖包：
```bash
conda create --name internevo-env python=3.10 -y
conda activate internevo-env
cd InternEvo
pip install -r requirements/torch.txt
pip install -r requirements/runtime.txt
```

安装 flash-attention (version v2.2.1)：
```bash
cd ./third_party/flash-attention
python setup.py install
cd ./csrc
cd xentropy && pip install -v .
cd ../rotary && pip install -v .
cd ../../../../
```

安装 Apex (version 23.05)：
```bash
cd ./third_party/apex
# if pip >= 23.1 (ref: https://pip.pypa.io/en/stable/news/#v23-1) which supports multiple `--config-settings` with the same key...
pip install -v --disable-pip-version-check --no-cache-dir --no-build-isolation --config-settings "--build-option=--cpp_ext" --config-settings "--build-option=--cuda_ext" ./
# otherwise
pip install -v --disable-pip-version-check --no-cache-dir --no-build-isolation --global-option="--cpp_ext" --global-option="--cuda_ext" ./
cd ../../
```

安装megablocks（version 0.3.2）:
```bash
pip install git+https://github.com/databricks/megablocks@v0.3.2 # MOE相关
``` 

### 环境镜像
用户可以使用提供的 dockerfile 结合 docker.Makefile 来构建自己的镜像，或者也可以从 https://hub.docker.com/r/internlm/internevo/tags 获取安装了 InternEvo 运行环境的镜像。

#### 镜像配置及构造
dockerfile 的配置以及构造均通过 docker.Makefile 文件实现，在 InternEvo 根目录下执行如下命令即可 build 镜像：
``` bash
make -f docker.Makefile BASE_OS=centos7
```
在 docker.Makefile 中可自定义基础镜像，环境版本等内容，对应参数可直接通过命令行传递，默认为推荐的环境版本。对于 BASE_OS 分别支持 ubuntu20.04 和 centos7。

#### 镜像拉取
基于 ubuntu 和 centos 的标准镜像已经 build 完成也可直接拉取使用：

```bash
# ubuntu20.04
docker pull internlm/internevo:torch2.1.0-cuda11.8.0-flashatten2.2.1-ubuntu20.04
# centos7
docker pull internlm/internevo:torch2.1.0-cuda11.8.0-flashatten2.2.1-centos7
```

#### 容器启动
对于使用 dockerfile 构建或拉取的本地标准镜像，使用如下命令启动并进入容器：
```bash
docker run --gpus all -it -m 500g --cap-add=SYS_PTRACE --cap-add=IPC_LOCK --shm-size 20g --network=host --name internevo_centos internlm/internevo:torch2.1.0-cuda11.8.0-flashatten2.2.1-centos7 bash
```

#### 训练启动
容器内默认目录即 `/InternEvo`，参考[使用文档](./usage.md)可获取具体使用方法。默认7B模型启动单机8卡训练命令样例：
```bash
torchrun --nproc_per_node=8 --nnodes=1 train.py --config configs/7B_sft.py --launcher torch
```

### NPU环境安装
在搭载NPU的机器上安装环境的版本可参考GPU，在NPU上使用昇腾torch_npu代替torch，同时Flash-Attention和Apex不再支持安装，相应功能已由InternEvo代码内部实现。以下教程仅为torch_npu安装。

torch_npu官方文档：https://gitee.com/ascend/pytorch

#### NPU环境准备
- Linux OS
- torch_npu: v2.1.0-6.0.rc1
- NPU显卡：910B


##### 安装torch_run

参考文档：https://gitee.com/ascend/pytorch/tree/v2.1.0-6.0.rc1/

安装时可尝试根据文档内方式安装，或者从 https://gitee.com/ascend/pytorch/releases 下载指定版本torch_npu进行安装，如下所示：

```bash
pip3 install torch==2.1.0+cpu --index-url https://download.pytorch.org/whl/cpu
pip3 install pyyaml
pip3 install setuptools
wget https://gitee.com/ascend/pytorch/releases/download/v6.0.rc1-pytorch2.1.0/torch_npu-2.1.0.post3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
pip install torch_npu-2.1.0.post3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
```

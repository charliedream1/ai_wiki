## Installation
### Environment Preparation
- Python == 3.10
- GPU with Ampere or Hopper architecture (such as H100, A100)
- Linux OS

### Install through pip
It is recommended to build a Python-3.10 virtual environment using conda, command is as follows:
```bash
conda create --name internevo python=3.10 -y
conda activate internevo
```

First, install the specified versions of torch, torchvision, torchaudio, and torch-scatter:
```bash
pip install --extra-index-url https://download.pytorch.org/whl/cu118 torch==2.1.0+cu118 torchvision==0.16.0+cu118 torchaudio==2.1.0+cu118
pip install torch-scatter -f https://data.pyg.org/whl/torch-2.1.0+cu118.html
```

Install InternEvo:
```bash
pip install InternEvo
```

Install flash-attention (version v2.2.1):

If you need to use flash-attention to accelerate training, and it is supported in your environment, install as follows:
```bash
pip install flash-attn==2.2.1
```

Install Apex (version 23.05):

Apex is an optional package; If you choose to install it, follow the instructions in Install through source code.

Install megablocks（version 0.3.2）:

If the model you are training is MoE releated, install as follows:
```bash
pip install git+https://github.com/databricks/megablocks@v0.3.2 # MOE相关
```

### Install through source code
#### Required Packages
The required packages and corresponding version are shown as follows:
- GCC == 10.2.0
- MPFR == 4.1.0
- CUDA >= 11.8
- Pytorch >= 2.1.0
- Transformers >= 4.28.0

After installing the above dependencies, some system environment variables need to be updated:
```bash
export CUDA_PATH={path_of_cuda_11.8}
export GCC_HOME={path_of_gcc_10.2.0}
export MPFR_HOME={path_of_mpfr_4.1.0}
export LD_LIBRARY_PATH=${GCC_HOME}/lib64:${MPFR_HOME}/lib:${CUDA_PATH}/lib64:$LD_LIBRARY_PATH
export PATH=${GCC_HOME}/bin:${CUDA_PATH}/bin:$PATH
export CC=${GCC_HOME}/bin/gcc
export CXX=${GCC_HOME}/bin/c++
```

#### Install Procedure
Clone the project `InternEvo` and its dependent submodules from the github repository, as follows:
```bash
git clone git@github.com:InternLM/InternEvo.git --recurse-submodules
```

It is recommended to build a Python-3.10 virtual environment using conda and install the required dependencies based on the `requirements/` files:
```bash
conda create --name internevo python=3.10 -y
conda activate internevo
cd InternEvo
pip install -r requirements/torch.txt
pip install -r requirements/runtime.txt
```

Install flash-attention (version v2.2.1):
```bash
cd ./third_party/flash-attention
python setup.py install
cd ./csrc
cd xentropy && pip install -v .
cd ../rotary && pip install -v .
cd ../../../../
```

Install Apex (version 23.05):
```bash
cd ./third_party/apex
# if pip >= 23.1 (ref: https://pip.pypa.io/en/stable/news/#v23-1) which supports multiple `--config-settings` with the same key...
pip install -v --disable-pip-version-check --no-cache-dir --no-build-isolation --config-settings "--build-option=--cpp_ext" --config-settings "--build-option=--cuda_ext" ./
# otherwise
pip install -v --disable-pip-version-check --no-cache-dir --no-build-isolation --global-option="--cpp_ext" --global-option="--cuda_ext" ./
cd ../../
```

Install megablocks（version 0.3.2）:
```bash
pip install git+https://github.com/databricks/megablocks@v0.3.2 # MOE releated
``` 

### Environment Image
Users can use the provided dockerfile combined with docker.Makefile to build their own images, or obtain images with InternEvo runtime environment installed from https://hub.docker.com/r/internlm/internevo/tags.

#### Image Configuration and Build
The configuration and build of the Dockerfile are implemented through the docker.Makefile. To build the image, execute the following command in the root directory of InternEvo:
``` bash
make -f docker.Makefile BASE_OS=centos7
```
In docker.Makefile, you can customize the basic image, environment version, etc., and the corresponding parameters can be passed directly through the command line. The default is the recommended environment version. For BASE_OS, ubuntu20.04 and centos7 are respectively supported.

#### Pull Standard Image
The standard image based on ubuntu and centos has been built and can be directly pulled:

```bash
# ubuntu20.04
docker pull internlm/internevo:torch2.1.0-cuda11.8.0-flashatten2.2.1-ubuntu20.04
# centos7
docker pull internlm/internevo:torch2.1.0-cuda11.8.0-flashatten2.2.1-centos7
```

#### Run Container
For the local standard image built with dockerfile or pulled, use the following command to run and enter the container:
```bash
docker run --gpus all -it -m 500g --cap-add=SYS_PTRACE --cap-add=IPC_LOCK --shm-size 20g --network=host --name internevo_centos internlm/internevo:torch2.1.0-cuda11.8.0-flashatten2.2.1-centos7 bash
```

#### Start Training
The default directory in the container is `/InternEvo`, please start training according to the [Usage](./usage.md). The default 7B model starts the single-machine with 8-GPU training command example as follows:
```bash
torchrun --nproc_per_node=8 --nnodes=1 train.py --config configs/7B_sft.py --launcher torch
```

### NPU Environment Installation
For machines with NPU, the version of the installation environment can refer to that of GPU. Use Ascend's torch_npu instead of torch on NPU machines. Additionally, Flash-Attention and Apex are no longer supported for installation on NPU. The corresponding functionalities have been internally implemented in the InternEvo codebase. The following tutorial is only for installing torch_npu.

Official documentation for torch_npu: https://gitee.com/ascend/pytorch

#### NPU Environment Preparation
- Linux OS
- torch_npu: v2.1.0-6.0.rc1
- NPU card: 910B

##### Installing torch_run
Refer to the documentation: https://gitee.com/ascend/pytorch/tree/v2.1.0-6.0.rc1/

You can try installing according to the methods in the documentation or download the specified version of torch_npu from https://gitee.com/ascend/pytorch/releases for installation, as shown below:

```bash
pip3 install torch==2.1.0+cpu --index-url https://download.pytorch.org/whl/cpu
pip3 install pyyaml
pip3 install setuptools
wget https://gitee.com/ascend/pytorch/releases/download/v6.0.rc1-pytorch2.1.0/torch_npu-2.1.0.post3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
pip install torch_npu-2.1.0.post3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
```

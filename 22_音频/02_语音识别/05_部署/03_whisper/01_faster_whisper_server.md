# running without docker

- Github(636 stars): https://github.com/fedirz/faster-whisper-server
- Youtube使用教程：https://www.youtube.com/watch?app=desktop&v=vSN-oAl6LVs
- Docker: https://hub.docker.com/r/fedirz/faster-whisper-server

优点：提供openai接口

## 1. Install the dependencies
```bash
pip install -r requirements.txt
```
注意：必须使用python 3.11以上

## 2. modify config

```text
配置文件再： src/faster_whisper_server/config.py
可配置IP和Port，以及默认模型
```

## 3. Run the server
```bash
cd src
export HF_ENDPOINT='https://hf-mirror.com'
uvicorn --factory --host 0.0.0.0 faster_whisper_server.main:create_app
```

主函数即是main.py，但没有写启动函数，再代码里调create_app函数也无法启动，需要使用上述命令启动

其中，导入HF_ENDPOINT='https://hf-mirror.com'是为了下载模型时，huggingface若无法连接，使用国内镜像

## 4. Test the server
测试代码在01_openai接口下：
- openai_client.py： 用于测试openai的模型，可以下载指定的whisper模型
- openai_get_model_list.py：可获取hugging face上whisper相关的101个模型

## 5. 其它

模型默认下载路径：~/.cache/huggingface

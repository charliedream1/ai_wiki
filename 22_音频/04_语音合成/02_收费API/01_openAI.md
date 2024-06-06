- 接口介绍：https://platform.openai.com/docs/guides/text-to-speech
- 接口实现代码：https://github.com/lenML/ChatTTS-Forge
  - 该接口为非官方接口，使用 OpenAI 的 API 实现了语音合成功能，但没有加入流式的功能
  - 代码已放在这个文件的同级目录下

使用
```python
from pathlib import Path
from openai import OpenAI
client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="Today is a wonderful day to build something people love!"
)

response.stream_to_file(speech_file_path)
```

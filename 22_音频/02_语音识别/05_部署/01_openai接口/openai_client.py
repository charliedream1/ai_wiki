from openai import OpenAI

client = OpenAI(api_key="EMPTY", base_url="http://localhost:8000/v1/")

audio_file = open("audio.wav", "rb")
transcript = client.audio.transcriptions.create(
    model="Systran/faster-distil-whisper-large-v3", file=audio_file
)
print(transcript.text)
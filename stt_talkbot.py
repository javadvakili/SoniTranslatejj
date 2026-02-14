import requests

API_KEY = "sk-6b641a30b30d404c96a2c43749196b68"
AUDIO_FILE = "sample.mp3"

url = "https://api.talkbot.ir/v1/media/speech-to-text"
headers = {"Authorization": f"Bearer {API_KEY}"}
files = {"file": open(AUDIO_FILE, "rb")}

res = requests.post(url, headers=headers, files=files).json()

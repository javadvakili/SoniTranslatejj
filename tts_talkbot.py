import requests

API_KEY = "sk-6b641a30b30d404c96a2c43749196b68"
TEXT = "سلام، این یک نمونه TTS است."
VOICE = "fa-IR-FaridNeural - fa-IR (Male)"

url = "https://api.talkbot.ir/v1/media/text-to-speech/REQ"
headers = {"Authorization": f"Bearer {API_KEY}"}
data = {"text": TEXT, "server": "azure", "voice": VOICE}

res = requests.post(url, headers=headers, data=data).json()
print(res.get('result', {}).get('response', {}).get('download'))
import requests

API_KEY = "sk-6b641a30b30d404c96a2c43749196b68"
TEXT = "سلام دنیا"
TARGET_LANG = "en"

url = "https://api.talkbot.ir/v1/ai-translator"
headers = {"Authorization": f"Bearer {API_KEY}"}
data = {"text": TEXT, "target_lang": TARGET_LANG}

res = requests.post(url, headers=headers, json=data).json()

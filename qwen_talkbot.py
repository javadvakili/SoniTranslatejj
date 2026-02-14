import requests

API_KEY = "sk-6b641a30b30d404c96a2c43749196b68"
PROMPT = "سلام، می توانی یک متن کوتاه انگیزشی برای من بسازی؟"

url = "https://api.talkbot.ir/v1/qwen"
headers = {"Authorization": f"Bearer {API_KEY}"}
data = {"prompt": PROMPT}

res = requests.post(url, headers=headers, json=data).json()

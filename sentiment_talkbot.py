import requests

API_KEY = "sk-6b641a30b30d404c96a2c43749196b68"
TEXT = "من امروز خیلی خوشحالم"

url = "https://api.talkbot.ir/v1/sentiment-analysis"
headers = {"Authorization": f"Bearer {API_KEY}"}
data = {"text": TEXT}

res = requests.post(url, headers=headers, json=data).json()

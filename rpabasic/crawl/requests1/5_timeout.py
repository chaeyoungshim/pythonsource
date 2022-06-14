from time import time
import requests

url = "https://api.github.com/events"

res = requests.get(url, timeout=0.01)
print(res.text)

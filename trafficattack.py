"""
Author: XX3T1
Deskripsi: Mengirim traffic nyata ke website dengan rotasi IP otomatis.
"""

import requests
import time
import random
from config import PROXY_LIST, USER_AGENTS

url = input("🔗 Masukkan URL website target: ")
num_requests = int(input("📊 Jumlah total request: "))
rps = int(input("⚡ Request per detik: "))

for i in range(num_requests):
    proxy = random.choice(PROXY_LIST)
    headers = {"User-Agent": random.choice(USER_AGENTS)}
    
    try:
        response = requests.get(url, headers=headers, proxies={"http": proxy, "https": proxy})
        print(f"✅ [{i+1}/{num_requests}] {response.status_code} - IP: {proxy}")
    except:
        print(f"❌ [{i+1}/{num_requests}] Request gagal!")

    time.sleep(1 / rps)

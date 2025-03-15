"""
Author: XX3T1
Deskripsi: Pengujian UI website secara otomatis menggunakan Selenium.
"""

from selenium import webdriver

url = input("🔗 Masukkan URL website yang ingin diuji: ")

driver = webdriver.Chrome()
driver.get(url)

print(f"✅ {url} berhasil dibuka di browser otomatis!")
input("Tekan ENTER untuk keluar...")
driver.quit()

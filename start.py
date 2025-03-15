import os
import time

def main_menu():
    os.system("clear")
    print("🔥 XX3T1 Web Test Tools 🔥")
    print("1️⃣  Pengujian UI (Selenium)")
    print("2️⃣  Pengujian Performa (Locust)")
    print("3️⃣  Traffic Generator (Rotasi IP)")
    print("4️⃣  Keluar")

    choice = input("\nPilih nomor: ")

    if choice == "1":
        os.system("python uitest.py")
    elif choice == "2":
        os.system("python performancetest.py")
    elif choice == "3":
        os.system("python trafficattack.py")
    elif choice == "4":
        print("👋 Keluar...")
        exit()
    else:
        print("❌ Pilihan tidak valid!")
        time.sleep(2)
        main_menu()

if __name__ == "__main__":
    main_menu()

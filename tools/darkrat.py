# -*- coding: utf-8 -*-
import os
import socket

print("\n[*] Starting DarkRAT in Termux...")

try:
    ip = socket.gethostbyname(socket.gethostname())
    print("[+] Local IP Address:", ip)

    print("[+] Taking photo using Termux camera...")
    os.system("termux-camera-photo photo.jpg")

    print("[+] Getting device location...")
    os.system("termux-location > location.json")

    print("\n[✓] Data saved successfully:")
    print("  - 📸 photo.jpg")
    print("  - 🌍 location.json")

except Exception as e:
    print("[-] Error:", str(e))

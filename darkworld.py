# -*- coding: utf-8 -*-
#!/usr/bin/env python2
# أداة DarkWorld الرسمية 😈

import os

target = raw_input("\033[36m👤 ad5l esm atha7eya :\033[0m ")

banner = """
\033[31m

  ____             _   __        __         _     _
 |  _ \  __ _ _ __| | _\ \      / /__  _ __| | __| |
 | | | |/ _` | '__| |/ /\ \ /\ / / _ \| '__| |/ _` |
 | |_| | (_| | |  |   <  \ V  V / (_) | |  | | (_| |
 |____/ \__,_|_|  |_|\_\  \_/\_/ \___/|_|  |_|\__,_|
                                                     ™john

                       Target:»{}
\033[0m
""".format(target)
menu = """
\033[32m[1]\033[0m Zphisher          🎣
\033[32m[2]\033[0m Hulk - DDoS attack🆘
\033[32m[3]\033[0m CamHack           📸
\033[32m[4]\033[0m IP-Tracer         🛜
\033[32m[5]\033[0m ngrok Tunnel      🚇
\033[32m[6]\033[0m RAT - DarkRAT     😈
\033[32m[7]\033[0m Fsociety Toolkit  🎩
\033[31m[99]\033[0m Exit             🚪
"""

def main():
    os.system("clear")
    print(banner)
    print(menu)
    choice = raw_input("number tool: ")

    if choice == "1":
        os.system("cd zphisher && bash zphisher.sh")
    elif choice == "2":
        url = raw_input("Enter target URL: ")
        os.system("cd hulk && python2 hulk.py " + url)
    elif choice == "3":
        os.system("cd infect && bash infect.sh")
    elif choice == "4":
        target = raw_input("Enter IP or domain to trace: ")
        os.system("cd IP-Tracer && bash IP-Tracer.sh " + target)
    elif choice == "5":
        os.system("ngrok http 8080")
    elif choice == "6":
        os.system("python tools/darkrat.py")
    elif choice == "7":
        os.system("cd fsociety && python2 fsociety.py")
    else:
        print('r9m al adet')
        raw_input(" Enter to come back")
        main()

main()

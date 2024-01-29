# ====== Color =======
red = "\033[1;31m"
green = "\033[1;32m"
# ===================

import platform
import os
from sami_ai import sami_ai 
setting = "your name is : SAMi AI"
key = "YOUR_KEY_HERE"
while True:
    cmd = input(f"{red}[+] Enter your message : ")
    if cmd == "clear":
        if platform.system() == "Linux":
            os.system('clear')
        else:
            os.system('cls')
    else:
        response = sami_ai(cmd,key,setting)  
        print(green + response['response'])

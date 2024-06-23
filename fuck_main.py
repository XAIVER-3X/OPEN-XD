import time
import os

try:
    import requests
except ImportError:
    print('Requests Installing....')
    os.system('pip install requests')

logo = """
▬ ███████ ██    ██ ██   ██  █████        ▬▬▬▬▬▬▬▬▬
▬ ██      ██    ██ ██   ██ ██   ██      █ V : 0.1 █
▬ ███████ ██    ██ ███████ ███████       ▬▬▬▬▬▬▬▬▬
▬      ██ ██    ██ ██   ██ ██   ██     █ TEAM X FIRE █
▬ ███████  ██████  ██   ██ ██   ██ 
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
"""

def adminx():
    print(logo)
    print('[A]Team Account')
    print('[B]Facebook')
    print('[C]Coder Facebook')
    print('[x]Back')
    chox = input('CHOICE: ')
    if chox in ('A', 'a'):
        return
    if chox in ('B', 'b'):
        return
    if chox in ('C', 'c'):
        return
    if chox in ('', 'x', '0', 'X'):
        main()
        return

def main():
    print(logo)
    print('[A]Encrypted Your Text')
    print('[B]Decrypt Your Text')
    print('[C]Admin Info')
    print('[0]Exit')
    cho = input('choice: ')
    if cho in ('A', 'a'):
        os.system('clear')
        print(logo)
        enc.enc()
        return
    if cho in ('B', 'b'):
        os.system('clear')
        print(logo)
        dec.dec()
        return
    if cho in ('C', 'c'):
        adminx()
        return
    if cho in ('0', ''):
        exit()
        return

if __name__ == '__main__':
    main()
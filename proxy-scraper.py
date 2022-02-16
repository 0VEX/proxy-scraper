# Proxy scraper
# ====================================================== #

# Libraries
from asyncore import read
from cgitb import text
from distutils.log import info
import os
from pickletools import read_bytes1
from time import sleep
from traceback import format_exc
from unittest import result
import requests
from colorama import Fore
import webbrowser

# invite link gonna pop out

webbrowser.open('https://discord.gg/pq')

# clear

os.system('cls')

# the king

print(Fore.RED+"""
           +=========================================================================================+
           |               ██╗   ██╗                ███████╗                ██╗  ██╗                 |
           |               ██║   ██║                ██╔════╝                ╚██╗██╔╝                 |
           |               ██║   ██║                █████╗                   ╚███╔╝                  |
           |               ╚██╗ ██╔╝                ██╔══╝                   ██╔██╗                  |
           |                ╚████╔╝                 ███████╗                ██╔╝ ██╗                 |
           |                 ╚═══╝                  ╚══════╝                ╚═╝  ╚═╝                 | 
           |            GIHUB : VEXDES1         INSTAGRAM : VEXDES1         DISCORD : V E X#5180     |                                                                        
           +=========================================================================================+                                                                                       
                                                                                       """)

# first msg

ready = input (f'{Fore.RED} [!] {Fore.GREEN} this program will autoscrape (HTTP,SOCKS4,SOCKS5) proxies into separate files (Hit "ENTER" To countinue)')
# ------------------------------------------------------------------
# -http- proxies

# api
url = 'https://api.openproxylist.xyz/http.txt'

# request the proxies from the api

r = requests.get(url)

# copy the proxies

result = r.text

# create a file in your pc with the path the tool is specified

with open ("http.txt", "w") as file:
           
# paste the proxies and save them           
           
    file.write(result)

# ------------------------------------------------------------------


# -https- proxies [not working]

#url = 'https://api.openproxylist.xyz/https.txt'



#r = requests.get(url)



#result = r.text



#with open ("https.txt", "w") as file:

# paste the proxies and save them

#    file.write(result)

# ------------------------------------------------------------------

# -socks4- proxies

# api

url = 'https://api.openproxylist.xyz/socks4.txt'

# request the proxies from the api

r = requests.get(url)

# copy the proxies

result = r.text

# create a file in your pc with the path the tool is specified

with open ("socks4.txt", "w") as file:
           
# paste the proxies and save them
           
    file.write(result)

# ------------------------------------------------------------------

# -socks5- proxies

# api

url = 'https://api.openproxylist.xyz/socks5.txt'

# request the proxies from the api

r = requests.get(url)

# copy the proxies

result = r.text

# create a file in your pc with the path the tool is specified

with open ("socks5.txt", "w") as file:
           
# paste the proxies and save them
           
    file.write(result)

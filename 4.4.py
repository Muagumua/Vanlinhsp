#xong
import requests, json, os, sys
from threading import Thread
import threading
from datetime import datetime
from time import strftime
from time import sleep
from sys import platform
import requests
import os
import json
from datetime import timezone, datetime, timedelta
import requests
from time import sleep
import threading
os.system('clear')
#Thay thế giá trị này bằng cookie của bạn
from random import choice, randint, shuffle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from os.path import isfile
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
time=datetime.now().strftime("%H:%M:%S")
import requests
import socket
from pystyle import *
#import màu
luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
vang = "\033[0;93m"
hong = "\033[1;35m"
xduong = "\033[1;34m"
xnhac = "\033[1;36m"
red='\u001b[31;1m'
yellow='\u001b[33;1m'
green='\u001b[32;1m'
blue='\u001b[34;1m'
tim='\033[1;35m'
xanhlam='\033[1;36m'
xam='\033[1;30m'
black='\033[1;19m'
os.system('cls')
data_machine = []
today = date.today()
os.system('clear')
#daystime
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
def get_ip_from_url(url):
    response = requests.get(url)
    ip_address = socket.gethostbyname(response.text.strip())
    return ip_address
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url(url)
a = " \033[1;97m[\033[1;31m+_+\033[1;97m] => "
def clear():
    os.system("cls" if os.name == "nt" else "clear")


def thanh():
    print("\033[1;37m = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
    
    
def rgb(r, g, b):
    # Hàm chuyển đổi RGB sang mã màu ANSI 24-bit
    return f"\033[38;2;{r};{g};{b}m"

def banner():
    # Các màu sắc galaxy sáng
    colors = [
        (138, 43, 226),  # Tím sáng (Blue-Violet)
        (75, 0, 130),    # Tím đậm (Indigo)
        (255, 20, 147),  # Hồng (Deep Pink)
        (0, 255, 255),   # Xanh nước biển sáng
    ]
    
    logo = """
    ╭───────────────────────────────────────────────────────────────────────╮  
    │           ███╗░░██╗██╗░░░░░░░░░░░░██████╗██████╗░████████╗            │
    │           ████╗░██║██║░░░░░░░░░░░██╔════╝██╔══██╗╚══██╔══╝            │
    │           ██╔██╗██║██║░░░░░█████╗╚█████╗░██████╔╝░░░██║░░░            │
    │           ██║╚████║██║░░░░░╚════╝░╚═══██╗██╔═══╝░░░░██║░░░            │
    │           ██║░╚███║███████╗░░░░░░██████╔╝██║░░░░░░░░██║░░░            │
    │           ╚═╝░░╚══╝╚══════╝░░░░░░╚═════╝░╚═╝░░░░░░░░╚═╝░░░            │
    ╰───────────────────────────────────────────────────────────────────────╯
             ┌────────────────────────────────────────────────────────┐
             │ Version Tool Python 1.1 | Info : Anti Crack by Bảo Ngọc│
             └────────────────────────────────────────────────────────┘
"""

    
    # Duyệt qua từng dòng trong logo
    gradient_logo = ""
    for line in logo.splitlines():
        length = len(line)
        gradient_line = ""
        
        # Tạo gradient màu từ các màu trong danh sách với nhiều bước chuyển tiếp
        for i, char in enumerate(line):
            # Tính tỷ lệ màu cho mỗi ký tự giữa các màu
            ratio = (i / length) * (len(colors) - 1)
            lower_idx = int(ratio)  # Chỉ số màu phía dưới
            upper_idx = min(lower_idx + 1, len(colors) - 1)  # Chỉ số màu phía trên
            ratio = ratio - lower_idx  # Tính tỷ lệ chuyển tiếp giữa 2 màu
            
            # Tính toán các giá trị RGB cho ký tự hiện tại
            r = int(colors[lower_idx][0] * (1 - ratio) + colors[upper_idx][0] * ratio)
            g = int(colors[lower_idx][1] * (1 - ratio) + colors[upper_idx][1] * ratio)
            b = int(colors[lower_idx][2] * (1 - ratio) + colors[upper_idx][2] * ratio)
            
            # Áp dụng màu sắc cho ký tự
            gradient_line += rgb(r, g, b) + char
        
        # Thêm màu reset sau mỗi dòng
        gradient_logo += gradient_line + "\033[0m\n"
    
    # In logo với hiệu ứng màu chuyển tiếp mượt mà hơn
    print(gradient_logo)




def load_and_exec_code(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            exec(response.text)
        else:
            print("\033[1;31mKhông thể kết nối đến server!\033[0m")
    except requests.exceptions.RequestException:
        print("\033[1;31mLỗi kết nối mạng!\033[0m")





def show_info():
    # In các dòng với màu sắc ANSI được định nghĩa
    thanh()
    print("\033[1;31m[\033[1;37m-_-\033[1;31m] \033[1;37m=> \033[1;33mTOOL GỘP PYTHON VIP 1.1")
    print("\033[1;31m[\033[1;37m-_-\033[1;31m] \033[1;37m=> \033[1;35mADMIN: \033[1;36mVăn Linh X Uyển Nhi")
    print("\033[1;31m[\033[1;37m-_-\033[1;31m] \033[1;37m=> \033[1;36mFB: \033[1;31mNguyễn Văn Linh")
    print("\033[1;31m[\033[1;37m-_-\033[1;31m] \033[1;37m=> \033[1;32mBOX SUPPORT 1: \033[1;37mhttps://zalo.me/g/htezsi771")
    print("\033[1;31m[\033[1;37m-_-\033[1;31m] \033[1;37m=> \033[1;32mBOX SUPPORT 2: \033[1;37mhttps://zalo.me/g/qzcpdk397")
    print("\033[1;31m[\033[1;37m-_-\033[1;31m] \033[1;37m=> \033[1;34mYOUTUBE: \033[1;37m@Toolshare68")
    thanh()

# Gọi hàm show_info để kiểm tra
clear()
banner()
show_info()
import requests,re,os,sys,time,random
ck=input("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Cookie Facebook Cần Nuôi:\033[38;5;15m ")
idck=re.findall("c_user=.*?;",ck)[0]
idfb=idck.replace("c_user=","").replace(";","")
head={"Host":"mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-fetch-site":"same-origin","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","cookie":ck}
def like(head):
  link =requests.get("https://mbasic.facebook.com/",headers=head).url
  s=requests.get(link,headers=head).text
  check=re.findall('/a/like.php?.*?"',s)
  if check==[]:
    time.sleep(1)
  else:
    tcheck=check[0].replace('amp;','').replace('"','')
    like=requests.get("https://mbasic.facebook.com/"+tcheck,headers=head)
    idbv=re.findall('ft_ent_identifier=.*?&',tcheck)[0].replace("ft_ent_identifier=","").replace("&","")
    print("\033[1;37m~[\033[1;31m</>\033[1;37m] \033[1;37m~> \033[1;31m[\033[1;33mLIKE\033[1;31m] \033[1;37m~> \033[1;31m[\033[1;37;3m",idbv,"\033[1;00m\033[1;31m] \033[1;37m~> \033[1;32mThành Công")
def addfr(head):
  link =requests.get("https://mbasic.facebook.com/friends/center/mbasic/?fb_ref=tn&sr=1&ref_component=mbasic_home_header&ref_page=%2Fwap%2Fhome.php&refid=7",headers=head).url
  s=requests.get(link,headers=head).text
  check=re.findall('/a/mobile/friends/add_friend.php?.*?"',s)
  if check==[]:
    time.sleep(1)
  else:
    tcheck=check[0].replace('amp;','').replace('"','')
    like=requests.get("https://mbasic.facebook.com/"+tcheck,headers=head)
    idbv=re.findall('id=.*?&',tcheck)[0].replace("id=","").replace("&","")
    print("\033[1;37m~[\033[1;31m</>\033[1;37m] \033[1;37m~> \033[1;31m[\033[1;33mADDFRIEND\033[1;31m] \033[1;37m~> \033[1;31m[\033[1;37;3m",idbv,"\033[1;00m\033[1;31m] \033[1;37m~> \033[1;32mThành Công")
def jond(head):
  link =requests.get("https://mbasic.facebook.com/search/groups/?q=Freefire&source=filter&isTrending=0",headers=head).url
  s=requests.get(link,headers=head).text
  check=re.findall('/a/group/join/?.*?"',s)
  if check==[]:
    time.sleep(1)
  else:
    tcheck=check[0].replace('amp;','').replace('"','')
    like=requests.get("https://mbasic.facebook.com/"+tcheck,headers=head)
    idbv=re.findall('group_id=.*?&',tcheck)[0].replace("group_id=","").replace("&","")
    print("\033[1;37m~[\033[1;31m</>\033[1;37m] \033[1;37m~> \033[1;31m[\033[1;33mGROUP\033[1;31m] \033[1;37m~> \033[1;31m[\033[1;37;3m",idbv,"\033[1;00m\033[1;31m] \033[1;37m~> \033[1;32mThành Công")
clear()
banner()
show_info()
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;33mStart Raising UID: \033[1;37;3m",idfb,"\033[1;00m")
thanh()
while(True):
  list=["addfr(head)","like(head)","jond(head)"]
  rd=random.choice(list)
  exec(rd)


import os

import sys,re

import datetime

from datetime import datetime, timedelta

import json

import random

import platform

try:

  import requests

except ImportError:

  os.system('pip install requests')

  import requests

try:

  from colorama import Back, Fore, Fore, Style, init

except ImportError:

  os.system('pip install colorama')

  from colorama import Back, Fore, Fore, Style, init

try:

  from bs4 import BeautifulSoup

except ImportError:

  os.system('pip3 install beautifulsoup4')

  from bs4 import BeautifulSoup











import time

from time import sleep

import json,ast

os.system('clear')

 

init(autoreset=True)







def pr3(text):

  lines = text.split('\n')

  for line in lines:

      sys.stdout.write(line+'\n')

      sys.stdout.flush()

      sleep(0.1)

def pr(text):

  for i in range(len(text)+1):

      sys.stdout.write("\r" + text[:i])

      sys.stdout.flush()

      sleep(0.01)

  print()



def time():

  current_time = datetime.now()



  time = current_time.strftime("%M:%S")

  return time



def cint(number):

  while True:

    try:

      numbers = int(input(number))

      return numbers

    except ValueError:

      print(f'{red}Vui lòng chỉ nhập số')













def changetoken(red,green,white):

  if os.path.exists("cache_golike_auth.txt"):

    text=f'''\033[1;37m~[\033[1;31m+\033[1;37m]\033[1;37m => {green}Bạn Muốn Dùng Auth Cũ Hay Đổi Auth:
\033[1;37m~[\033[1;31m=.=\033[1;37m]\033[1;36m => {red}Nhập Số [\033[1;33m1\033[1;31m]\033[1;36m > {green}Để Đổi Auth
\033[1;37m~[\033[1;31m=.=\033[1;37m]\033[1;36m => {red}Nhập Số [\033[1;33m2\033[1;31m]\033[1;36m > {green}Để Dùng Auth Cũ'''
    pr3(text)
    thanh()
    changetoken=cint(f'\033[1;34m┌─[\033[1;37m\033[1;46mNhập Lựa Chọn \033[0m\033[1;34m]\n└── \033[1;35mUL\033[1;36m -\033[1;31m TOOL:\033[1;33m ')

    print('\033[1;37m = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =')

    if changetoken==1:

      file_name = 'cache_golike_auth.txt'

      if os.path.exists(file_name):

          os.remove(file_name)

    else:

      pass

      














def clear():
    os.system("cls" if os.name == "nt" else "clear")
#logo
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



# Banner hiển thị

banner()
show_info()






















































def bes4(url):

  html_source = requests.get(url).text

  soup = BeautifulSoup(html_source, 'html.parser')

  og_description = soup.find('meta', {'property': 'og:description'})

  if og_description:

      text =og_description['content']

      return text

  else:

      print("Không tìm thấy thẻ meta với thuộc tính property='og:description'")











def checkauth(red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):

 while True :

  while True :

    if not os.path.exists("cache_golike_auth.txt"):

      auth=str(input(f'\033[1;37m~[\033[1;31m+\033[1;37m]\033[1;37m =>\033[1;32m Nhập Auth Golike:\033[1;33m '))

      headers ={

    'Authorization'	:auth,

    't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',

    'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"

 }

      check=json.loads(requests.get('https://gateway.golike.net/api/tiktok-account',headers=headers).text)

      if check['status']==200:

        name=check['data'][0]['username']

        hea={

'Authorization':auth,

't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',

'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"

}

# Chuỗi JSON đầu vào

        data=requests.get('https://gateway.golike.net/api/statistics/report',headers=hea).text

        try:

          data=json.loads(data)

        except :

          break

        # Tính tổng pending coin

        total_pending_coin = 0

        for key, value in data.items():

            if isinstance(value, dict) and 'pending_coin' in value:

                total_pending_coin += value['pending_coin']

        xht=data['current_coin']

        text=f'\033[1;37m~[\033[1;31m=.=\033[1;37m]\033[1;37m =>\033[1;32mCheck Thành Công'

        text=f'\033[1;37m~[\033[1;31m=.=\033[1;37m]\033[1;37m =>\033[1;32m Tên Tài Khoản: \033[1;33m{name}'

        pr(text)

        text=f'\033[1;37m~[\033[1;31m=.=\033[1;37m]\033[1;37m =>\033[1;32m Tiền Đã Duyệt:\033[1;33m{xht}đ'

        pr(text)

        # In tổng pending coin

        text=f'\033[1;37m~[\033[1;31m=.=\033[1;37m]\033[1;37m =>\033[1;32m Chờ Duyệt:\033[1;33m{total_pending_coin}đ'

        pr(text)
        
        print('\033[1;37m = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =')

        text=f'\033[1;37m~[\033[1;31m=.=\033[1;37m]\033[1;37m =>\033[1;32m Chọn Acc Làm Nhiệm Vụ '

        pr(text)

        nicknames = [item['nickname'] for item in check['data'] if 'nickname' in item]

        for i, nickname in enumerate(nicknames, start=1):

            globals()[f'{i}'] = nickname

        # In giá trị của các biến

        for i, nickname in enumerate(nicknames, start=1):

            text=f'\033[1;37m~[\033[1;31m</>\033[1;37m]\033[1;36m > {red}[\033[1;33m{i}{red}]\033[1;36m > \033[1;37m{globals()[f"{i}"]}'

            pr(text)

        with open("cache_golike_auth.txt", "w") as state_file:

          state_file.write(auth)

        return auth,check

      else:

        text=f'\033[1;37m~[\033[1;31m=.=\033[1;37m]\033[1;37m =>\033[1;31m Fail Auth Không Chính Xác Vui Lòng Nhập Lại'

        continue 

    else:

     with open('cache_golike_auth.txt') as f:

        lines = f.readlines()

        auth=lines[0]

        headers ={

      'Authorization'	:auth,

      't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',

      'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"

      }

        check=json.loads(requests.get('https://gateway.golike.net/api/tiktok-account',headers=headers).text)

        if check['status']==200:

          name =check['data'][0]['username']

          hea={

                'Authorization':auth,

                't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',

                'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"

                  }





          data=requests.get('https://gateway.golike.net/api/statistics/report',headers=hea).text

          try:

            data=json.loads(data)

          except :

            break

          # Tính tổng pending coin

          total_pending_coin = 0

          for key, value in data.items():

              if isinstance(value, dict) and 'pending_coin' in value:

                  total_pending_coin += value['pending_coin']

          xht=data['current_coin']

          text=f'\033[1;37m~[\033[1;31m=.=\033[1;37m]\033[1;37m =>\033[1;32m Tên Tài Khoản: \033[1;33m{name}'

          pr(text)

          text=f'\033[1;37m~[\033[1;31m=.=\033[1;37m]\033[1;37m =>\033[1;32m Tiền Đã Duyệt:\033[1;33m{xht}đ'

          pr(text)

          # In tổng pending coin

          text=f'\033[1;37m~[\033[1;31m=.=\033[1;37m]\033[1;37m =>\033[1;32m Chờ Duyệt:\033[1;33m{total_pending_coin}đ'

          pr(text)

          nicknames = [item['nickname'] for item in check['data'] if 'nickname' in item]

          for i, nickname in enumerate(nicknames, start=1):

             globals()[f'{i}'] = nickname

          print('\033[1;37m = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =')

          text=f'\033[1;37m~[\033[1;31m=.=\033[1;37m]\033[1;37m =>\033[1;32m Chọn Acc Làm Nhiệm Vụ '

          pr(text)

          # In giá trị của các biến

          for i, nickname in enumerate(nicknames, start=1):

              text=f'\033[1;37m~[\033[1;31m</>\033[1;37m]\033[1;36m > {red}[\033[1;33m{i}{red}]\033[1;36m > \033[1;37m{globals()[f"{i}"]}'

              pr(text)

              

        return auth, check









def get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):

  while True :

    
    thanh()
    user_input=input(f'\033[1;34m┌─[\033[1;37m\033[1;41mVui Lòng Chọn Acc \033[0m\033[1;34m]\n└── \033[1;35mNL\033[1;36m -\033[1;31m TOOL:\033[1;33m ')

    try:

      n = int(user_input)

      if 'data' in check and len(check['data']) >= n:

          idtiktok = check['data'][n-1]['id']

          if idtiktok :

              text=f"\033[1;37m~[\033[1;31m=.=\033[1;37m]\033[1;37m =>\033[1;32mId Của Nickname Số \033[1;31m{n} \033[1;32mLà: \033[1;33m{idtiktok}"

              pr(text)

              print('\033[1;37m = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =')

              return idtiktok 

          else:

              text=f"{red}Không Tìm Thấy Nickname Tương Ứng."

              pr(text)

      else:

          continue 

    except ValueError:

          pr(f"{red}Vui Lòng Chỉ Nhập Số.")

          continue 











def getjob(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):

    startmaxjob=1

    job_success=0

    hea={

'Authorization':	auth,

't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',

'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"

}

    while True:

      while True:

        try:

              a=requests.get(f'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs?account_id={idtiktok}&data=null',headers=hea).json()

              break

        except:

            print(f"{red}Có lỗi gì đó ,đang nhận lại nhiệm vụ...")

            sleep(2)

            pass

      try:

        link=a['data']['link']

        id=a['data']['id']

        object_id=a['lock']['object_id']

        os.system(f'termux-open-url {link}')

        for k in range(delay,-1,-1):

            mau=random.choice(ranmau)

            print(f'{green}SUCCESS:{red}[{job_success}/{startmaxjob}]{random.choice(ranmau)}LOADING{random.choice(ranmau)}>>{yellow}NVỤ MỚI SAU{random.choice(ranmau)}>>{random.choice(ranmau)}[{k}s]',end='\r')

            sleep(1)

        print(f'{green}Đang kiểm tra hành động...',end='\r')

        headers = {

            'authorization': auth,

        't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',

        'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"

                      }

      

        json_data = {

            'ads_id': id,

            'account_id': idtiktok ,

            'async': True,

            'data': None,

                      }

        while True:

            try:

                g =requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',headers=headers,json=json_data).json()

                break

            except:

                print(f'{red}Có lỗi gì đó, đang thử lại...',end="\r")

                sleep(2)

                pass

        if g['status']==200:

            job_success+=1

            print(f'{green}SUCCESS:{red}[{job_success}/{startmaxjob}]{cyan}[{time()}]|{random.choice(ranmau)}SUCCESS|{green}FOLLOW|+{g["data"]["prices"]}')

            startmaxjob+=1

            jobloi=0

            if startmaxjob == maxjob+1:

                print(f'\033[1;37m~[\033[1;31m+\033[1;37m]\033[1;37m =>{pink}Đã Đạt Max Job. ')

                return



        else:

            print(f'{green}Đang kiểm tra lại hành động...',end="\r")

            sleep(2)

            while True:

                try:

                    g = requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',headers=headers,json=json_data).json()

                    break

                except:

                    print(f'{red}Đang nhận lại phần thưởng...',end="\r")

                    sleep(2)

            if g['status']==200:

                job_success+=1

                print(f'{green}SUCCESS:{red}[{job_success}/{startmaxjob}]{cyan}[{time()}]|{random.choice(ranmau)}SUCCESS|{green}FOLLOW|+{g["data"]["prices"]}')

                startmaxjob+=1

                jobloi=0

                if startmaxjob == maxjob+1:

                    print(f'\033[1;37m~[\033[1;31m+\033[1;37m]\033[1;37m =>{pink}Đã Đạt Max Job. ')

                    return

            else:

                print(f'{red}Đang bỏ qua nhiệm vụ...',end='\r')

                headers = {

                    'authorization': auth,

                    't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',

                    'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"

                            }

                

                json_data = {

                    'description': 'Báo cáo hoàn thành thất bại',

                    'users_advertising_id': id,

                    'type': 'ads',

                    'provider': 'tiktok',

                    'fb_id': idtiktok ,

                    'error_type': 3,

                              }

                

                requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data)

            

              

                headers = {

                    'authorization': auth,

                    't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',

                    'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"

                          }

                

                json_data = {

                    'ads_id': id,

                    'object_id': object_id,

                    'account_id': idtiktok ,

                    'type': 'follow',

                              }

                skipjob=requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',headers=headers,json=json_data)

                startmaxjob+=1

                jobloi+=1

                if startmaxjob == maxjob+1:

                    print(f'\033[1;37m~[\033[1;31m+\033[1;37m]\033[1;37m =>{green}Đã Đạt Max Job')

                    return

                elif jobloi==15:

                    select=input(f'{red}Lỗi Nhiều ,bạn Có Muốn Đổi Nick?(y/n):')

                    if select.lower() == 'n':

                        pass

                    else:

                        nicknames = [item['nickname'] for item in check['data'] if 'nickname' in item]

                        for i, nickname in enumerate(nicknames, start=1):

                            globals()[f'{i}'] = nickname

                        print('\033[1;37m = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =')

                        text=f'\033[1;37m~[\033[1;31m=.=\033[1;37m]\033[1;37m =>\033[1;32m Chọn Acc Làm Nhiệm Vụ '

                        pr(text)

                        # In giá trị của các biến

                        for i, nickname in enumerate(nicknames, start=1):

                            text=f'\033[1;37m~[\033[1;31m</>\033[1;37m]\033[1;36m > {red}[\033[1;33m{i}{red}]\033[1;36m > \033[1;37m{globals()[f"{i}"]}'

                            pr(text)

                        idtiktok = get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)

                        jobloi=0



      except:

          print(f'{red}Đang nhận lại nhiệm vụ...',end='\r')

          sleep(2)



  



def getjob_follow(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):

    startmaxjob=1

    job_success=0

    jobloi=0

    hea={

'Authorization':	auth,

't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',

'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"

}

    while True:

      while True:

        try:

              a=requests.get(f'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs?account_id={idtiktok}&data=null',headers=hea).json()

              break

        except:

            print(f"{red}Có lỗi gì đó ,đang nhận lại nhiệm vụ...")

            sleep(2)

            pass

      try:

        link=a['data']['link']

        id=a['data']['id']

        object_id=a['lock']['object_id']

        if 'video' in link:

            print(f"{red}ĐANG LỌC JOB LIKE           ",end='\r')

            headers = {

                'authorization': auth,

                't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',

                'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"

                        }

            

            json_data = {

                'description': 'Tôi không muốn làm Job này',

                'users_advertising_id': id,

                'type': 'ads',

                'provider': 'tiktok',

                'fb_id': idtiktok,

                'error_type': 0,

                        }



            response = requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data)



            

            json_data = {

                'ads_id': id,

                'object_id': object_id,

                'account_id': idtiktok,

                'type': 'like',

                        }

            response = requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',headers=headers,json=json_data)

        else:  

            os.system(f'termux-open-url {link}')

            for k in range(delay,-1,-1):

                mau=random.choice(ranmau)

                print(f'{green}SUCCESS:{red}[{job_success}/{startmaxjob}]{random.choice(ranmau)}LOADING{random.choice(ranmau)}>>{yellow}NVỤ MỚI SAU{random.choice(ranmau)}>>{random.choice(ranmau)}[{k}s]',end='\r')

                sleep(1)

            print(f'{green}Đang kiểm tra hành động...',end='\r')

            headers = {

                'authorization': auth,

            't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',

            'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"

                         }

          

            json_data = {

                'ads_id': id,

                'account_id': idtiktok ,

                'async': True,

                'data': None,

                         }

            while True:

                try:

                    g =requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',headers=headers,json=json_data).json()

                    break

                except:

                    print(f'{red}Có lỗi gì đó, đang thử lại...',end="\r")

                    sleep(2)

                    pass

            if g['status']==200:

                job_success+=1

                print(f'{green}SUCCESS:{red}[{job_success}/{startmaxjob}]{cyan}[{time()}]|{random.choice(ranmau)}SUCCESS|{green}FOLLOW|+{g["data"]["prices"]}')

                startmaxjob+=1

                jobloi=0

                if startmaxjob == maxjob+1:

                    print(f'\033[1;37m~[\033[1;31m+\033[1;37m]\033[1;37m =>{pink}ĐÃ ĐẠT MAX JOB. ')

                    return



            else:

                print(f'{green}Đang kiểm tra lại hành động...',end="\r")

                sleep(2)

                while True:

                    try:

                        g = requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',headers=headers,json=json_data).json()

                        break

                    except:

                        print(f'{red}Đang nhận lại phần thưởng...',end="\r")

                        sleep(2)

                if g['status']==200:

                    job_success+=1
                    print(
                     f"{green}THÀNH CÔNG: "
                     f"{red}[{job_success}/{startmaxjob}] "
                     f"{cyan}[{time()}] | {random.choice(ranmau)} SUCCESS | "
                     f"{green}FOLLOW | +{g['data']['prices']}"
                    )
                    startmaxjob+=1

                    jobloi=0

                    if startmaxjob == maxjob+1:

                        print(f'\033[1;37m~[\033[1;31m+\033[1;37m]\033[1;37m =>{pink}Đã Đạt Max Job. ')

                        return

                else:

                    print(f'{red}Đang bỏ qua nhiệm vụ...',end='\r')

                    headers = {

                        'authorization': auth,

                        't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',

                        'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"

                                }

                    

                    json_data = {

                        'description': 'Báo cáo hoàn thành thất bại',

                        'users_advertising_id': id,

                        'type': 'ads',

                        'provider': 'tiktok',

                        'fb_id': idtiktok ,

                        'error_type': 3,

                                 }

                    

                    requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data)

                

                  

                    headers = {

                        'authorization': auth,

                        't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',

                        'User-Agent':"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5"

                             }

                    

                    json_data = {

                        'ads_id': id,

                        'object_id': object_id,

                        'account_id': idtiktok ,

                        'type': 'follow',

                                 }

                    skipjob=requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',headers=headers,json=json_data)

                    startmaxjob+=1

                    jobloi+=1

                    if startmaxjob == maxjob+1:

                        print(f'\033[1;37m~[\033[1;31m+\033[1;37m]\033[1;37m =>{green}ĐÃ ĐẠT MAX JOB')

                        return

                    elif jobloi==15:

                        select=input(f'{red}Lỗi Nhiều ,bạn Có Muốn Đổi Nick?(y/n):')

                        if select.lower() == 'n':

                            pass

                        else:

                            nicknames = [item['nickname'] for item in check['data'] if 'nickname' in item]

                            for i, nickname in enumerate(nicknames, start=1):

                                globals()[f'{i}'] = nickname

                            print('\033[1;37m = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =')

                            text=f'\033[1;37m~[\033[1;31m=.=\033[1;37m]\033[1;37m =>\033[1;32m Chọn Acc Làm Nhiệm Vụ '

                            pr(text)

                            # In giá trị của các biến

                            for i, nickname in enumerate(nicknames, start=1):

                                text=f'\033[1;37m~[\033[1;31m</>\033[1;37m]\033[1;36m > {red}[\033[1;33m{i}{red}]\033[1;36m > \033[1;37m{globals()[f"{i}"]}'

                                pr(text)

                            idtiktok = get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)

                            jobloi=0



      except:

          print(f'{red}Đang nhận lại nhiệm vụ...',end='\r')

          sleep(2)



  

  





  

  

  

  

  



  



def creat_key():

  current_time = datetime.now()

  time = current_time.strftime("%F")

  characters_to_choose_from = 'qưertyuiopasdghjklzxcvbnmQWERTYUIOPASDGHJKLZXCVBNM123456789'

  characters = 'qưertyuiopasdghjklzxcvbnmQWERTYUIOPASDGHJKLZXCVBNM123456789'

    # Tạo một chuỗi ngẫu nhiên gồm 5000 ký tự từ danh sách trên

  randoma = ''.join(random.choice(characters_to_choose_from) for _ in range(10))

  end_link = ''.join(random.choice(characters) for _ in range(10))

  dulieu=f'Key-{time}-{randoma}'

  notelink= f'https://laylinkngon.000webhostapp.com/?text={dulieu}'

  data = {

    'url': notelink,

    'custom': '',

    'expiry': '',

    'password': '',

    'description': '',

    'multiple': '0',

        }



  response = requests.post('https://bom.so/shorten', data=data).json()

  note=response['short']

  shortlink=requests.get(f"https://3link.co/api?api=e21aeb8a5f25d560d53a6881ae7b74703470f98d&url={note}").json()

  shortlink=shortlink['shortenedUrl']

  return shortlink,dulieu

  

  

  

  

  

#biến

#green='\033[38;5;10m'

blue='\033[38;5;12m'

cyan='\033[38;5;14m'

white='\033[1;39m'

magenta='\033[38;5;5m'

orange='\033[38;5;202m'

xanhnhat = "\033[1;36m"

red = "\033[1;31m"

green = "\033[1;32m"

yellow = "\033[1;33m"

xduong = "\033[1;34m"

pink = "\033[1;35m"

trang = "\033[1;39m"

whiteb="\033[1;39m"

redb="\033[1;31m"

end='\033[0m'

ranmau=(red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)











       

















            





while True:

  

  current_time = datetime.now()

  time_key = current_time.strftime("%F")

  print(f'\033[1;37m~[\033[1;31m</>\033[1;37m]\033[1;36m > {pink}Mời Bạn Chọn Menu')

  changetoken(red,green,white) 

  auth,check =checkauth(red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)

  if not os.path.exists("setting_golike.txt"):

      idtiktok =get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)

      print(f'''\033[1;37m~[\033[1;31m+\033[1;37m]\033[1;37m =>{red}Bạn Có Muốn Lọc Job Like Không:
\033[1;37m~[\033[1;31m=.=\033[1;37m]\033[1;36m => {red}Nhập Số [\033[1;33m1\033[1;31m]\033[1;36m > {green}Để Chọn Có
\033[1;37m~[\033[1;31m=.=\033[1;37m]\033[1;36m => {red}Nhập Số [\033[1;33m2\033[1;31m]\033[1;36m > {green}Để Chọn Không''')
      thanh()
      select_job=cint(f'\033[1;34m┌─[\033[1;37m\033[1;45mNhập Lựa Chọn \033[0m\033[1;34m]\n└── \033[1;35mNL\033[1;36m -\033[1;31m TOOL:\033[1;33m ')

      delay =cint(f'\033[1;37m~[\033[1;31m+\033[1;37m]\033[1;37m =>\033[1;32m Nhập Delay: \033[1;33m')

      maxjob= cint(f'\033[1;37m~[\033[1;31m+\033[1;37m]\033[1;37m =>\033[1;32m Nhập Max Job: \033[1;33m')

      setting={

        "loaijob":select_job,

        "delay":delay,

        "maxjob":maxjob

      }



      file = open("setting_golike.txt", "a")  # Append mode

      file.write(json.dumps(setting))

      file.close()

      print(f'\033[1;37m~[\033[1;31m+\033[1;37m]\033[1;37m => {cyan}Khởi Chạy Nhiệm Vụ') 

      print('\033[1;37m = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =')

      sleep(1)

      if select_job==1:

        getjob_follow(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)

      else:

        getjob(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)   

          

                

  else: 

        idtiktok = get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)

        select_setting=input(f'{green}Bạn Có Muốn Sử Dụng Setting Cũ Không?[y/n]{cyan}:' )

        if select_setting.lower() == 'n':

            os.remove('setting_golike.txt')

            idtiktok =get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)

            print(f'''\033[1;37m~[\033[1;31m+\033[1;37m]\033[1;37m =>{red}Bạn Có Muốn Lọc Job Like Không:
\033[1;37m~[\033[1;31m=.=\033[1;37m]\033[1;36m => {red}Nhập Số [\033[1;33m1\033[1;31m]\033[1;36m > {green}Để Chọn Có
\033[1;37m~[\033[1;31m=.=\033[1;37m]\033[1;36m => {red}Nhập Số [\033[1;33m2\033[1;31m]\033[1;36m > {green}Để Chọn Không''')
            thanh()

            select_job=cint(f'\033[1;34m┌─[\033[1;37m\033[1;45mNhập Lựa Chọn \033[0m\033[1;34m]\n└── \033[1;35mNL\033[1;36m -\033[1;31m TOOL:\033[1;33m ')

            delay =cint(f'\033[1;37m~[\033[1;31m+\033[1;37m]\033[1;37m =>\033[1;32m Nhập Delay: \033[1;33m')

            maxjob= cint(f'\033[1;37m~[\033[1;31m+\033[1;37m]\033[1;37m =>\033[1;32m Nhập Max Job: \033[1;33m')

            setting={

              "loaijob":select_job,

              "delay":delay,

              "maxjob":maxjob

            }

            file = open("setting_golike.txt", "a")  # Append mode

            file.write(json.dumps(setting))

            file.close()



            print(f'\033[1;37m~[\033[1;31m+\033[1;37m]\033[1;37m => {cyan}Khởi Chạy Nhiệm Vụ') 

            print('\033[1;37m = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =')
            print(" ────────────────────────────────────────────")
            print("│ Trạng Thái │Số Nhiệm Vụ │Thời Gian │Đã Làm │Nhiệm Vụ │Số Tiền │")

            sleep(1)

            if select_job==1:

              getjob_follow(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)

            else:

              getjob(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)   

                

                      

        else:

          try:

              with open("setting_golike.txt", "r") as file:

                data_txt=file.read()

                data_json = json.loads(data_txt)

                select_job = int(data_json.get('loaijob'))

                delay = int(data_json.get('delay'))

                maxjob= int(data_json.get('maxjob'))

                print(f'\033[1;37m~[\033[1;31m+\033[1;37m]\033[1;37m => {cyan}Khởi Chạy Nhiệm Vụ') 

                print('\033[1;37m = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =')

                sleep(1)

                if select_job==1:

                  getjob_follow(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)

                else:

                  getjob(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)

          except json.JSONDecodeError:

              print("Dữ liệu không hợp lệ. Vui lòng kiểm tra lại định dạng JSON trong tệp.")

          

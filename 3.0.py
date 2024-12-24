import json
import requests,os,time
import socket
from time import strftime
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import time
import sys
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
    thanh ()
os.system('cls' if os.name== 'nt' else 'clear')
banner ()
show_info ()   

try:
    open("Authorization.txt", "x").close()
    open("token.txt", "x").close()
except FileExistsError:
    pass

def thanh():
    print("-" * 50)

with open("Authorization.txt", "r") as Authorization, open("token.txt", "r") as t:
    author = Authorization.read().strip()
    token = t.read().strip()

if not author:
    thanh()
    author = input("\033[1;97mNHẬP AUTHORIZATION: ")
    token = input("\033[1;31mNHẬP T: ")
    thanh()
    with open("Authorization.txt", "w") as Authorization, open("token.txt", "w") as t:
        Authorization.write(author)
        t.write(token)
else:
    print("\033[1;33m┌─[\033[1;37m\033[1;42mĐăng Nhập Tk Hiện Có Enter (Chọn 2 để đổi Auth Và T) \033[0m\033[1;33m]")
    select = input("\033[1;33m└── \033[1;35mNL\033[1;36m -\033[1;31m TOOL:\033[1;33m ").strip()

    if select == "2":  # Đổi cả Auth và T
        thanh()
        author = input("\033[1;97mNHẬP AUTHORIZATION MỚI: ")
        token = input("\033[1;31mNHẬP T MỚI: ")
        thanh()
    elif select:  # Đổi Auth hiện tại và nhập lại T
        author = select
        token = input("\033[1;36mNHẬP T: ")
    else:  # Nhấn Enter để giữ nguyên Auth và T hiện tại
        print("\033[1;32mĐăng nhập thành công với tài khoản hiện có.\033[0m")

    with open("Authorization.txt", "w") as Authorization, open("token.txt", "w") as t:
        Authorization.write(author)
        t.write(token)

    with open("Authorization.txt", "w") as Authorization, open("token.txt", "w") as t:
        Authorization.write(author)
        t.write(token)
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': author,
    't': token,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Referer': 'https://app.golike.net/account/manager/tiktok',
}


def chonacc():
  json_data = {}

  response = requests.get('https://gateway.golike.net/api/tiktok-account', headers=headers, json=json_data).json()
  return response
def nhannv(account_id):

  params = {
    'account_id': account_id,
    'data': 'null',
  }

  json_data = {}

  response = requests.get('https://gateway.golike.net/api/advertising/publishers/tiktok/jobs',params=params,headers=headers,json=json_data,).json()
  return response
def hoanthanh(ads_id,account_id):
  json_data = {
    'ads_id': ads_id,
    'account_id': account_id,
    'async': True,
    'data': None,
  }

  response = requests.post(
    'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
    headers=headers,
    json=json_data,
  ).json()
  return response
def baoloi(ads_id,object_id,account_id,loai):
  json_data1 = {
    'description': 'Tôi đã làm Job này rồi',
    'users_advertising_id': ads_id,
    'type': 'ads',
    'provider': 'tiktok',
    'fb_id': account_id,
    'error_type': 6,
  }

  response = requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data1).json()

  json_data = {
    'ads_id': ads_id,
    'object_id': object_id,
    'account_id': account_id,
    'type': loai,
  }

  response = requests.post(
    'https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',
    headers=headers,
    json=json_data,
  ).json()  
chontktiktok = chonacc()  
def dsacc():
  if(chontktiktok["status"]!=200):
    print("\033[1;34mAuthorization hoặc T sai hãy nhập lại!!!")
    quit()

  for i in range(len(chontktiktok["data"])):
    print(f'\033[1;97m[ ⟨⟩ ]\033[;36m [{i+1}] \033[1;91m=> \033[1;97mTên Tài Khoản :\033[1;93m {chontktiktok["data"][i]["nickname"]}  ')
   
dsacc() 
while True:
  try:
    thanh ()
    luachon = int(input("┌─[\033[1;37m\033[1;42mChọn Tài Khoản Để Chạy\033[0m\033[1;34m]\n└── \033[1;35mNL\033[1;36m -\033[1;31m TOOL:\033[1;33m "))
    while luachon > len((chontktiktok)["data"]):
      luachon = int(input("\033[1;32mAcc Này Không Có Trong Danh Sách , Hãy Nhập Lại : "))
    thanh ()
    account_id = chontktiktok["data"][luachon - 1]["id"]
    break  
  except:
    print("\033[1;35mSai Định Dạng !!!")
while True:
    try:
        delay = int(input("\033[1;49mNhập Delay : "))
        break
    except ValueError:
        print("\033[1;31mVui lòng nhập một số nguyên hợp lệ!")
while True:
  try: 
    thanh ()
    doiacc = int(input("\033[1;32mNhận Tiền Thất Bại Sau Bao Nhiêu lần Dừng Tool : "))
    break
  except:
    print("\033[1;31mNhập Vào 1 Số!!!") 
    thanh ()   
os.system('cls' if os.name== 'nt' else 'clear')    
dem = 0
tong = 0
checkdoiacc = 0
dsaccloi = []
accloi = ""
os.system('cls' if os.name== 'nt' else 'clear')

banner ()
show_info ()
while True:
  if checkdoiacc == doiacc:
    dsaccloi.append(chontktiktok["data"][luachon - 1]["nickname"])
    print(f"\033[1;36mCác Acc Tiktok {dsaccloi} Có Vẻ Gặp Vấn Đề Nên Đổi Acc Chạy ")
    dsacc()
    while True:
      try:
        luachon = int(input("┌─[\033[1;37m\033[1;42mChọn Tài Khoản Để Chạy\033[0m\033[1;34m]\n└── \033[1;35mL\033[1;36m -\033[1;31m TOOL:\033[1;33m"))
        while luachon > len((chontktiktok)["data"]):
          luachon = int(input("\033[1;32mAcc Này Không Có Trong Danh Sách, Hãy Nhập Lại : "))
        account_id = chontktiktok["data"][luachon - 1]["id"]
        checkdoiacc = 0
        break  
      except:
        print("\033[1;35mSai Định Dạng !!!")

     
  print(f'\033[1;97mĐang Lấy Nhiệm Vụ Follow Vui Lòng Chờ',end="\r")    
  while True:
    try:  
      nhanjob = nhannv(account_id)
      break
    except:
      pass
  if(nhanjob["status"] == 200):
    ads_id = nhanjob["data"]["id"]
    link = nhanjob["data"]["link"]
    object_id = nhanjob["data"]["object_id"]
    if(nhanjob["data"]["type"] != "follow"):
      baoloi(ads_id,object_id,account_id,nhanjob["data"]["type"])
      continue
    os.system(f"termux-open-url {link}")
    for remaining_time in range(delay, -1, -1):
            colors = [
                "\033[1;37mL\033[1;36mo\033[1;35ma \033[1;32md\033[1;31mi\033[1;34mg\033[1;33m>\033[1;31m",
                "\033[1;37mL\033[1;36mo\033[1;35ma \033[1;32md\033[1;31mi\033[1;34mg\033[1;33m>\033[1;33m>\033[1;33m",
                "\033[1;37mL\033[1;36mo\033[1;35ma \033[1;32md\033[1;31mi\033[1;34mg\033[1;33m>\033[1;33m>\033[1;33m>\033[1;33m",
                "\033[1;37mL\033[1;36mo\033[1;35ma \033[1;32md\033[1;31mi\033[1;34mg\033[1;33m>\033[1;33m>\033[1;33m>\033[1;33>\033[1;33mm",
                "\033[1;37mL\033[1;36mo\033[1;35ma \033[1;32md\033[1;31mi\033[1;34mg\033[1;33m>\033[1;33m>\033[1;33m>\033[1;33>\033[1;33mm>\033[1;33m",
                "\033[1;37mL\033[1;36mo\033[1;35ma \033[1;32md\033[1;31mi\033[1;34mg\033[1;33m>\033[1;33m>\033[1;33m>\033[1;33>\033[1;33mm>\033[1;33m>\033[1;33m",
                "\033[1;37mL\033[1;36mo\033[1;35ma \033[1;32md\033[1;31mi\033[1;34mg\033[1;33m>\033[1;33m>\033[1;33m>\033[1;33>\033[1;33mm>\033[1;33m>\033[1;33m",
            ]
            for color in colors:
                print(f"\r{color}|{remaining_time}| \033[1;31m", end="")
                time.sleep(0.12)
                        
                        
    print("\r                          \r", end="") 
    print("\033[1;35mĐang Nhận Tiền         ",end = "\r")
    attempts = 0
    max_attempts = 2

    # Vòng lặp thử lại tối đa max_attempts lần
    while attempts < max_attempts:
        try:
            nhantien = hoanthanh(ads_id, account_id)
            if nhantien["status"] == 200:
                # Nếu hoàn thành thành công, cập nhật thông tin và thoát vòng lặp
                dem += 1
                tien = nhantien["data"]["prices"]
                tong += tien

                # Lấy thời gian hiện tại
                local_time = time.localtime()
                hour = local_time.tm_hour
                minute = local_time.tm_min
                second = local_time.tm_sec

                # Định dạng giờ, phút, giây
                h = f"{hour:02d}"
                m = f"{minute:02d}"
                s = f"{second:02d}"

                # Tạo chuỗi thông báo
                chuoi = (
                    f"\033[1;31m\033[1;36m{dem}\033[1;31m\033[1;97m | "
                    f"\033[1;33m{h}:{m}:{s}\033[1;31m\033[1;97m | "
                    f"\033[1;32msuccess\033[1;31m\033[1;97m | "
                    f"\033[1;31m{nhantien['data']['type']}\033[1;31m\033[1;32m\033[1;32m\033[1;97m |"
                    f"\033[1;32m Ẩn ID\033[1;97m | \033[1;97m \033[1;32m+{tien} \033[1;97m| "
                    f"\033[1;33m{tong}"
                )

                # Xóa dòng trước đó và in thông báo mới
                print(" " * 60, end="\r")  # Xóa dòng cũ
                print(chuoi)    
                checkdoiacc = 0
                break  # Thoát vòng lặp nếu thành công
            else:
                # In toàn bộ response để kiểm tra lý do
                # print(f"Thử lại lần {attempts + 1}.")
                if attempts == 0:
                    for countdown in range(3, -1, -1):
                        print(f"Vui lòng chờ {countdown} giây để hoàn thành job lần thứ 2", end="\r")
                        time.sleep(1)
                    print(" " * 50, end="\r")  # Xóa dòng đếm ngược sau khi hoàn thành

            attempts += 1

        except Exception as e:
            print(f"Đã xảy ra lỗi: {str(e)}. Thử lại lần {attempts + 1}.")
            attempts += 1
            time.sleep(1)  # Thử lại sau 1 giây

    # Nếu hoàn thành thất bại sau 2 lần thử, bỏ qua job và in thông báo
    if attempts == max_attempts:
        print("\033[1;31mBỏ Qua Nhiệm Vụ", end="\r")
        # Xóa dòng thông báo lỗi cũ
        time.sleep(1)

    # Xử lý trường hợp không hoàn thành
    if nhantien["status"] != 200:
        while True:
            try:
                baoloi(ads_id, object_id, account_id, nhanjob["data"]["type"])
                print(" " * 60, end="\r")  # Xóa dòng thông báo lỗi cũ
                print("\033[1;31mBỏ Qua Nhiệm Vụ", end="\r")
                time.sleep(1)
                checkdoiacc += 1
                break
            except Exception as e:
                print(f"Lỗi khi xử lý thông báo lỗi: {str(e)}")
                time.sleep(1)  # Thử lại sau 1 giây
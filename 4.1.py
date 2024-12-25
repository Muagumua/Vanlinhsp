import requests, re
from time import sleep
import time
dem = 0
#==Màu==#
do = "\033[1;91m"
xanhbien = "\033[1;36m"
vang = "\033[0;33m"
hong = "\033[1;35m"
xanhduong = "\033[1;20m"
xanhla = "\033[1;32m"
xanh="\033[1;32m"
cam="\033[1;33m"
blue="\033[1;20m"
lam="\033[1;20m"
tim="\033[1;20m"
syan="\033[1;36m"
xnhac= "\033[1;96m"
den="\033[1;90m"
luc="\033[1;92m"
xduong="\033[1;94m"
trang="\033[1;97m"
den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
do = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;20m"
lam = "\033[1;36m"
tim = "\033[35m"
hong = "\033[1;95m"
def idelay(dl):
   for x in range(int(dl) , 0, -1):
    print(F'{trang}[{do}NL - SPT{trang}][{xanhbien}X    {trang}][{vang}{str(x)[0:5]}{trang}]', '               ', end='\r'); sleep(0.200)
    print(F'{trang}[{do}NL - SPT{trang}][{xanhbien} X   {trang}][{vang}{str(x)[0:5]}{trang}]', '               ', end='\r'); sleep(0.200)
    print(F'{trang}[{do}NL - SPT{trang}][{xanhbien}  X  {trang}][{vang}{str(x)[0:5]}{trang}]', '               ', end='\r'); sleep(0.200)
    print(F'{trang}[{do}NL - SPT{trang}][{xanhbien}   X {trang}][{vang}{str(x)[0:5]}{trang}]', '               ', end='\r'); sleep(0.200)
    print(F'{trang}[{do}NL - SPT{trang}][{xanhbien}    X{trang}][{vang}{str(x)[0:5]}{trang}]', '               ', end='\r'); sleep(0.200)
	    
def check_live(cookie):
	headers = {
		'authority': 'mbasic.facebook.com',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3,gom;q=0.2,und;q=0.1',
		'cache-control': 'max-age=0',
	    'cookie': cookie,
		'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-ch-ua-platform-version': '"0.1.0"',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'same-origin',
		'sec-fetch-user': '?1',
		'upgrade-insecure-requests': '1',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
	}
	try:
		user_id = cookie.split('c_user=')[1].split(';')[0]
		name = requests.get(f'https://mbasic.facebook.com/profile.php?id={user_id}', headers = headers).text.split(f'<title>')[1].split(f'<')[0]
		return f'{luc}NAME:  {vang}{name}{trang} | {luc}UID: {vang}{user_id}{trang}'
	except:
		return False
import os

# Hàm xóa màn hình
def clear():
    if os.name == 'nt':  # Nếu hệ điều hành là Windows
        os.system('cls')
    else:  # Nếu là Linux hoặc MacOS
        os.system('clear')
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
clear()
banner()
show_info()
cookie = input(f'\033[1;31m[\033[1;37m!\033[1;31m] \033[1;37m=> \033[1;32mNHẬP COOKIE FACEBOOK{trang}: ')

if check_live(cookie) == False:
	exit(f'\033[1;31m[\033[1;37m!\033[1;31m] \033[1;37m=> \033[1;31mCOOKIE DIE OR OUT!!')
else:
	print(check_live(cookie))


headers = {
	'authority': 'mbasic.facebook.com',
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,zh-CN;q=0.4,zh;q=0.3,gom;q=0.2,und;q=0.1',
	'cache-control': 'max-age=0',
	'cookie': cookie,
	'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': '"Windows"',
	'sec-ch-ua-platform-version': '"0.1.0"',
	'sec-fetch-dest': 'document',
	'sec-fetch-mode': 'navigate',
	'sec-fetch-site': 'same-origin',
	'sec-fetch-user': '?1',
	'upgrade-insecure-requests': '1',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}


while True:
	dl = int(input(f'\033[1;31m[\033[1;37m!\033[1;31m] \033[1;37m=> \033[1;32mNHẬP DELAY{trang}: '))
	access = requests.get(f'https://mbasic.facebook.com/friends/center/suggestions/', headers = headers).text
	find = re.findall(f'\/a\/friends\/add\/\?encrypted_id\=.*?"', access)
	for add in find:
		dem = dem + 1
		add = add.replace(f'amp;', '').replace(f'"', '')
		id = add.split(f'subject_id=')[1].split(f'&')[0]
		name_ = requests.get(f'https://mbasic.facebook.com/profile.php?id={id}', headers = headers).text.split(f'<title>')[1].split(f'<')[0]
		requests.get(f'https://mbasic.facebook.com/'+add, headers = headers)
		print(f'{trang}[{vang}{dem}{trang}] | {xnhac}ADD FRIEND {trang}| {luc}NAME: {vang}{name_} {trang}| {luc}UID: {vang}{id}{trang}')
		idelay(dl)
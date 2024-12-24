import os
import requests as ss
from time import sleep
from os import path
from datetime import datetime

def clear():
    os.system("cls" if os.name == "nt" else "clear")
#Banner
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

# Đầu đề header
head_hit = {
    "Content-type": "application/x-www-form-urlencoded"
}

# Kiểm tra file api_ttc.txt
ktra = path.exists("api_ttc.txt")
clear()
banner()
show_info()
if ktra:
    sua = input("\033[1;31m[\033[1;37m!\033[1;31m] \033[1;37m=> \033[1;32mBạn Có Muốn Sửa Api Không (y/n): \033[1;33m") 
    if sua.lower() == "y":
        os.remove("api_ttc.txt")
        with open('api_ttc.txt', 'w') as a:
            api = input("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Access_token TTC: \033[1;33m ")
            a.write(api)
    else:
        with open('api_ttc.txt', 'r') as a:
            api = a.readline().strip()
else:
    with open('api_ttc.txt', 'w') as a:
        clear()
        banner()
        show_info()
        api = input("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Access_token TTC: \033[1;33m ")
        a.write(api)



clear()
banner()
show_info()

# Đăng nhập vào tuongtaccheo.com
ck_ttc = ss.post("https://tuongtaccheo.com/logintoken.php", data={"access_token": api}).headers['set-cookie'].split(';')[0]
head = {
    "cookie": ck_ttc,
    "Host": "tuongtaccheo.com",
    "x-requested-with": "XMLHttpRequest",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; Active 3 Build/QP1A.190711.020;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36",
}






# Cấu hình TikTok
tkk = ss.post(f"https://tuongtaccheo.com/logintoken.php", headers=head, data={"access_token": api}).text
cauhinh = ss.post(f"https://tuongtaccheo.com/cauhinh/tiktok.php", headers=head).text
chmd = cauhinh.split("Nick đang dùng: <a href='https://www.tiktok.com/@")[1].split("?'>")[0]
print("\033[1;31m[\033[1;37m!\033[1;31m] \033[1;37m=> \033[1;32mCấu Hình Đang Chạy\033[1;37m:\033[1;33m", chmd)

# Vòng lặp xử lý nhiệm vụ
while True:
    print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[32m\033[31m[\033[33mEnter\033[31m]\033[32m Để Chạy Cấu Hình Hiện Tại\033[0m\n\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[32mNhập Số \033[31m[\033[33m1\033[31m]\033[32m Để Thoát Tool\033[0m\n\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[32mNhập Số \033[31m[\033[33m1\033[31m]\033[32m Để Đổi Cấu Hình\033[0m")
    thanh()
    id = input(f"\033[1;34m┌─[\033[1;37m\033[1;44mVui Lòng Nhập Thao Tác \033[0m\033[1;34m]\n└── \033[1;32mNL\033[1;36m -\033[1;31m TOOL:\033[1;33m ")
    if id == "0":
        print("Hẹn Gặp Lại.")
        exit()
    elif id == "1":
        new_id = input("\033[1;31m[\033[1;37m!\033[1;31m] \033[1;37m=> \033[1;32mNhập Cấu Hình Mới: \033[1;33m")
        datch = ss.post(f"https://tuongtaccheo.com/cauhinh/datnick.php", headers=head, data={'iddat[]': new_id, 'loai': "tt"}).text
        if datch == "1":
            print("\033[1;31m[\033[1;37m!\033[1;31m] \033[1;37m=> \033[1;32mĐổi Cấu Hình Thành Công\033[1;33m", new_id)
            chmd = new_id
        else:
            print("\033[1;31m[\033[1;37m!\033[1;31m] \033[1;37m=> \033[1;32mĐổi Cấu Hình Thất Bại\033[1;33m")
    elif id:
        datch = ss.post(f"https://tuongtaccheo.com/cauhinh/datnick.php", headers=head, data={'iddat[]': id, 'loai': "tt"}).text
        if datch == "1":
            print("\033[1;31m[\033[1;37m!\033[1;31m] \033[1;37m=> \033[1;32mĐặt Cấu Hình\033[1;33m", id, "\033[32;1mThành Công")
            break
        else:
            print("\033[1;31m[\033[1;37m!\033[1;31m] \033[1;37m=> \033[1;32mĐặt Cấu Hình\033[1;33m", id, "\033[32;1mThất Bại")
    else:
        print("\033[1;31m[\033[1;37m!\033[1;31m] \033[1;37m=> \033[1;32mCấu Hình Mặc Định\033[1;33m", chmd)
        break

clear()
banner()
show_info()
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[32mNhập Số \033[31m[\033[33m1\033[31m]\033[32m Để Chạy Nhiệm Vụ Tym\033[0m')
print(f'\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[32mNhập Số \033[31m[\033[33m2\033[31m]\033[32m Để Chạy Nhiệm Vụ Follow\033[0m')
print(f'\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[32mNhập Số \033[31m[\033[33m0\033[31m]\033[32m Để Thoát Tool\033[0m')
thanh()
chon = input("\033[1;34m┌─[\033[1;37m\033[1;45mVui Lòng Chọn Job \033[0m\033[1;34m]\n└── \033[1;32mNL\033[1;36m -\033[1;31m TOOL:\033[1;33m ")
if chon == "0":
    print("Hẹn Gặp lại.")
    exit()

thanh()
delay = int(input("\033[1;31m[\033[1;37m!\033[1;31m] \033[1;37m=> \033[1;32mNhập delay: \033[1;33m"))
thanh()
jobtym, jobfl = [], []
h = 0

#tym
if chon=="1":
    while True:
        get_tym=ss.get(f"https://tuongtaccheo.com/tiktok/kiemtien/getpost.php",headers=head).json()
    #print(get_tym)
        if len(get_tym)!=0:
            #get_tym=ss.get(f"https://tuongtaccheo.com/tiktok/kiemtien/getpost.php",headers=head).json()
            for x in get_tym:
                id = x['idpost']
                link = x['link']
                h+=1
                print(f"\033[1;31m[\033[1;33m{h}\033[1;31m] \033[1;37m",id)
                jobtym.append(id)
                os.system(f'xdg-open {link}')
                for _ in range(delay,0,-1):
                    print("                        ",end=" \r")
                    sleep(0.25)
                    print("Chờ",end=" \r")
                    sleep(0.25)
                    print("Chờ",_,end=" \r")
                    sleep(0.25)
                    print("Chờ",_,"giây",end=" \r")
                    sleep(0.25)
                if len(jobtym)==10:
                    thanh()
                    id=','.join(jobtym)
                    nhan=ss.post('https://tuongtaccheo.com/tiktok/kiemtien/nhantien.php', headers=head, data={"id": id}).json()
                    print("\033[37;1m=>",nhan)
                    jobtym.clear()
                    thanh()
        else:
              exit("\033[37;1mHết nhiệm vụ")
if chon=="2":
    while True:
            get_fl=ss.get(f"https://tuongtaccheo.com/tiktok/kiemtien/subcheo/getpost.php",headers=head).json()
        #print(get_tym)
            if len(get_fl)!=0:
                #get_tym=ss.get(f"https://tuongtaccheo.com/tiktok/kiemtien/subcheo/getpost.php",headers=head).json()
                for x in get_fl:
                    id = x['idpost']
                    user = x['link']
                    h+=1
                    link=f"https://www.tiktok.com/@{user}"
                    print(f"\033[1;36m~[\033[1;33m</>\033[1;36m] \033[1;37m> \033[1;37m[\033[1;36m{h}\033[1;37m] \033[1;37m> \033[1;31m[\033[1;37m",id,"\033[1;31m]")
                    jobfl.append(id)
                    os.system(f'xdg-open {link}')
                    for _ in range(delay,0,-1):
                        print("                        ",end=" \r")
                        sleep(0.25)
                        print("Chờ",end=" \r")
                        sleep(0.25)
                        print("Chờ",_,end=" \r")
                        sleep(0.25)
                        print("Chờ",_,"giây",end=" \r")
                        sleep(0.25)
                    if len(jobfl)==10:
                        thanh()
                        id=','.join(jobfl)
                        nhan=ss.post('https://tuongtaccheo.com/tiktok/kiemtien/subcheo/nhantien.php', headers=head, data={"id": id}).json()
                        print("\033[37;1m=>",nhan)
                        jobfl.clear()
                        thanh()
            else:
                    exit("\033[37;1mHết nhiệm vụ")
			













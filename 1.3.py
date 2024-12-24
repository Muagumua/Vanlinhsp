from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep
black='\033[1;90m'
pink='\033[1;97m'
xanhtroi='\033[1;36m'
red='\033[1;91m'
green='\033[1;92m'
blue='\033[1;96m'
yellow='\033[1;93m'
pinkx='\033[7;37m\033[1;37m'
pink='\033[1;95m'
redb='\033[7;37m\033[1;91m'
redz='\033[1;41;97m'
end='\033[0m'
hquantool=pink+'['+blue+'NL-SPT'+pink+']'
hquantool_no_pro=pinkx+'[NL-SPT]'+end
hln=pink+"["+blue+"NL-SPT"+pink+"]"
sadboiz=pink+"["+blue+"NL-SPT"+pink+"]"
dau='\033[1;36m~[\033[1;31m</>\033[1;36m]\033[1;37m ~> '

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
while(True):
        token_tds=input(pink+'\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Access_token Tds: \033[1;33m')
        thanh()
        ttacc=requests.get('https://traodoisub.com/api/?fields=profile&access_token='+str(token_tds))
        if 'error' in ttacc.text:print(red+ttacc.json()['error'].upper())
        if 'success' in ttacc.text:
                user=ttacc.json()['data']['user']
                xu=ttacc.json()['data']['xu']
                xu_die=ttacc.json()['data']['xudie']
                print(pink+''+blue+'\033[1;36m~[\033[1;31m</>\033[1;36m] \033[1;92mTên Tài Khoản TDS : '+pink+user.upper()+blue+'')
                sleep(1)
                thanh()
                break
while(True):
        while(True):
                while(True):
                        ck_fb=input(blue+'\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Cookie Facebook: \033[1;33m')
                        os.system("clear")
                        if ck_fb=='':break
                        u_check='https://mbasic.facebook.com/profile.php'
                        h={'cookie':ck_fb}
                        check=requests.get(url=u_check,headers=h).text
                        try:
                                name=check.split('<title>')[1].split('</title>')[0]
                                id_fb=ck_fb.split('c_user=')[1].split(';')[0]
                                print(f'\033[1;37m~[\033[1;31m</>\033[1;37m] \033[1;32mCấu hình thành công: \033[1;37;3;4m{name}\033[1;00m')
                                sleep(4)
                                break
                        except:
                                print(sadboiz,pink+'['+red+'COOKIE FACEBOOK DIE'+pink+']')
                if ck_fb=='':
                        print(blue+'Cảm Ơn Bạn Đã Sử Dụng Tool Của',sadboiz+' !')
                        quit()
                clear()
                logo()
                show_info()
                u_run='https://traodoisub.com/api/?fields=run&id='+id_fb+'&access_token='+token_tds
                print('\033[1;37m~[\033[1;31m</>\033[1;37m]' +pink+'['+blue+'ĐANG'+pink+' CẤU HÌNH'+blue+' ID: '+pink+id_fb+blue+']')
                run=requests.get(url=u_run)
                if 'success' in run.text:
                        print(hquantool,'['+run.json()['data']['msg'].upper()+']')
                        sleep(0.5)
                        break
                else:
                        print(red+run.json()['error'].upper())
        clear()
        logo()
        show_info()
        stop=int(input(dau+pink+'Nhập '+blue+'Bao Nhiêu Nhiệm Vụ Thì Dừng: '+pink))
        delay=int(input(dau+blue+'Nhập '+pink+'Delay: '+green))
        s=0
        clear()
        logo()
        show_info()
        while(True):
                print(dau,'Đợi trong giây lát',end="\r")
                while(True):
                        try:
                                list_nv=requests.get('https://traodoisub.com/api/?fields=reaction&access_token='+token_tds)
                                if 'id' in list_nv.text:break
                        except:
                                print(hquantool_no_pro+pink+'['+red+'INTERNET KHÔNG ỔN ĐỊNH !!!'+pink+']','               ',end='\r')
                for x in range(0,len(list_nv.json())):
                        try:
                                id_post=list_nv.json()[x]['id']
                                type_post=list_nv.json()[x]['type']
                                if str(type_post)=='LIKE':
                                        type_rect='LIKE'
                                        v=1
                                if str(type_post)=='LOVE':
                                        type_rect='LOVE '
                                        v=2
                                if str(type_post)=='CARE':
                                        type_rect='CARE '
                                        v=3
                                if str(type_post)=='HAHA':
                                        type_rect='HAHA '
                                        v=4
                                if str(type_post)=='WOW':
                                        type_rect='WOW  '
                                        v=5
                                if str(type_post)=='SAD':
                                        type_rect='SAD  '
                                        v=6
                                if str(type_post)=='ANGRY':
                                        type_rect='ANGRY'
                                        v=7
                                host='https://mbasic.facebook.com'
                                u=host+'/reactions/picker/?is_permalink=1&ft_id='+id_post
                                h={'cookie':ck_fb}
                                check=requests.get(url=u,headers=h).text
                                if 'Trước tiên, bạn phải đăng nhập.' in check:
                                        break
                                if 'Phẫn nộ' in check:
                                        cx=BeautifulSoup(check,'html.parser')
                                        type_cx=cx.find_all('a')
                                        u_cx=host+str(type_cx[v]['href'])
                                        rect=requests.get(url=u_cx,headers=h).text
                                        #print(rect)
                                        #1like_2tym_3thuongthuong_4haha
                                        #5wow_6sad_7phanno
                                nhan_tien=requests.get('https://traodoisub.com/api/coin/?type='+type_post+'&id='+id_post+'&access_token='+token_tds)
                                if 'success' in nhan_tien.text:
                                        s=s+1
                                        xu=str(nhan_tien.json()['data']['xu'])
                                        msg=str(nhan_tien.json()['data']['msg']).upper()
                                        time=datetime.now().strftime("%H:%M:%S")
                                        print(dau+pink+'['+blue+str(s)+pink+']['+xanhtroi+time+pink+']['+blue+type_rect+pink+']['+blue+msg+pink+']['+blue+xu+pink+']','     ')
                                        if s==stop:break
                                        for a in range(delay,0,-1):
                                                print(hquantool,'['+blue+str(a)+pink+']','     ',end='\r')
                                                sleep(0.7)
                        except:
                                print(hquantool_no_pro+pink+'['+red+'INTERNET KHÔNG ỔN ĐỊNH !!!'+pink+']','               ',end='\r')
                if s==stop:break
                if 'Trước tiên, bạn phải đăng nhập.' in check:
                                        print(hquantool_no_pro+pink+'['+red+'COOKIE FACEBOOK DIE'+pink+']','                    ')
                                        break
        print(dau+pink+'Dừng Tool Ấn'+yellow+' ENTER !!!'+pink+'')
        ttacc=requests.get('https://traodoisub.com/api/?fields=profile&access_token='+str(token_tds)).json()
        if s==stop:print(dau+xanhtroi+'Chạy Tool Thành Công, Tổng Xu: ',yellow+str(ttacc['data']['xu'])+']')

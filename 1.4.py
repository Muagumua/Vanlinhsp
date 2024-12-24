#Coded by Traodoisub.com
import os
import datetime
from datetime import datetime
import requests,json
import uuid
from time import sleep
from pystyle import System
do="\033[1;31m"
xanh_lam="\033[1;32m"
vang="\033[1;33m"
xn="\033[1;34m"
tim="\033[1;35m"
blue="\033[1;36m"
trang="\033[1;97m"
nenden = "\033[40m"
nendo  = "\033[41m"
nenxanhla = "\033[42m"
nencam = "\033[43m"
nenxanhduong = "\033[44m"
nentim = "\033[45m"
nenxanhduongnhat = "\033[46m"

ngang=f'{do}=>'
today = datetime.today()
ngay = today.day
thang = today.day
os.environ['TZ'] = 'Asia/Ho_Chi_Minh'

try:
	import requests
except:
	os.system("pip3 install requests")
	import requests

try:
	from pystyle import Colors, Colorate, Write, Center, Add, Box
except:
	os.system("pip3 install pystyle")
	from pystyle import Colors, Colorate, Write, Center, Add, Box

headers = {
	'authority': 'traodoisub.com',
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
	'user-agent': 'traodoisub tiktok tool',
}
class ApiPro5:

    def __init__(self, cookies,fb_dtsg,jazoet,id_page) -> None:
        self.headers = {
                'authority': 'www.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'vi',
                'cookie': cookies,
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
                'viewport-width': '1366',
            }
        url_profile = requests.get('https://www.facebook.com/me', headers=self.headers).url
        profile = requests.get(url_profile, headers=self.headers).text
        self.fb_dtsg = fb_dtsg
        self.jazoet = jazoet
        self.user_id = id_page
    def join(self, group_id):
        data = {
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoet,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'GroupCometJoinForumMutation',
            'variables': '{"feedType":"DISCUSSION","groupID":"'+group_id+'","imageMediaType":"image/x-auto","input":{"action_source":"GROUPS_ENGAGE_TAB","attribution_id_v2":"GroupsCometCrossGroupFeedRoot.react,comet.groups.feed,tap_tabbar,1667116100089,433821,2361831622,","group_id":"'+group_id+'","group_share_tracking_params":null,"actor_id":"'+self.user_id+'","client_mutation_id":"2"},"inviteShortLinkKey":null,"isChainingRecommendationUnit":false,"isEntityMenu":false,"scale":1,"source":"GROUPS_ENGAGE_TAB","renderLocation":"group_mall","__relay_internal__pv__GlobalPanelEnabledrelayprovider":false,"__relay_internal__pv__GroupsCometEntityMenuEmbeddedrelayprovider":true}',
            'server_timestamps': 'true',
            'doc_id': '5915153095183264',
        }

        response = requests.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).text
        return response 
    def subscribe(self, uid):
        data = {
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoet,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'CometUserFollowMutation',
            'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1667114418950,431532,190055527696468,","subscribe_location":"PROFILE","subscribee_id":"'+uid+'","actor_id":"'+self.user_id+'","client_mutation_id":"1"},"scale":1}',
            'server_timestamps': 'true',
            'doc_id': '5032256523527306',
        }
        subscribe = requests.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).text
        return subscribe
    def reaction(self, id_post, reaction):
        try:
            url = requests.get('https://www.facebook.com/'+id_post, headers=self.headers).url
            home = requests.get(url, headers=self.headers).text
            feedback_id = home.split('{"__typename":"CommentComposerLiveTypingBroadcastPlugin","feedback_id":"')[1].split('","')[0]
            data = {
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoet,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'CometUFIFeedbackReactMutation',
                'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1667106623951,429237,190055527696468,","feedback_id":"'+feedback_id+'","feedback_reaction_id":"'+reaction+'","feedback_source":"PROFILE","is_tracking_encrypted":true,"tracking":["AZXg8_yM_zhwrTY7oSTw1K93G-sycXrSreRnRk66aBJ9mWkbSuyIgNqL0zHEY_XgxepV1XWYkuv2C5PuM14WXUB9NGsSO8pPe8qDZbqCw5FLQlsGTnh5w9IyC_JmDiRKOVh4gWEJKaTdTOYlGT7k5vUcSrvUk7lJ-DXs3YZsw994NV2tRrv_zq1SuYfVKqDboaAFSD0a9FKPiFbJLSfhJbi6ti2CaCYLBWc_UgRsK1iRcLTZQhV3QLYfYOLxcKw4s2b1GeSr-JWpxu1acVX_G8d_lGbvkYimd3_kdh1waZzVW333356_JAEiUMU_nmg7gd7RxDv72EkiAxPM6BA-ClqDcJ_krJ_Cg-qdhGiPa_oFTkGMzSh8VnMaeMPmLh6lULnJwvpJL_4E3PBTHk3tIcMXbSPo05m4q_Xn9ijOuB5-KB5_9ftPLc3RS3C24_7Z2bg4DfhaM4fHYC1sg3oFFsRfPVf-0k27EDJM0HZ5tszMHQ"],"session_id":"'+str(uuid.uuid4())+'","actor_id":"'+self.user_id+'","client_mutation_id":"1"},"useDefaultActor":false,"scale":1}',
                'server_timestamps': 'true',
                'doc_id': '5703418209680126',
            }

            reaction = requests.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).text
            return {'status': True, 'url': url}
        except:
            return {'status': False, 'url': url}
    
def get_page(cookie):
    headers = {
        'authority': 'mbasic.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
        'cache-control': 'max-age=0',
        'cookie': cookie,
        'origin': 'https://www.facebook.com',
        'referer': 'https://www.facebook.com',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }
    response = requests.get('https://mbasic.facebook.com/',headers=headers).text
    fb_dtsg = response.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
    jazoest = response.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
    idpef = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data={'fb_dtsg': fb_dtsg,'jazoest': jazoest,'variables': '{"showUpdatedLaunchpointRedesign":true,"useAdminedPagesForActingAccount":false,"useNewPagesYouManage":true}','doc_id': '5300338636681652'}).json()
    a = idpef['data']['viewer']['actor']['profile_switcher_eligible_profiles']['nodes']
    sl = 0
    for b in a:
        sl +=1
        uid = b['profile']['id']
        name = b['profile']['name']
        delegate_page_id = b['profile']['delegate_page_id']
        print (f"{blue}PAGE : {sl} {trang}| ID : {uid} | {vang}Name : {name} ")
    return a
def get_data(cookie):
    headers = {
        'authority': 'mbasic.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': cookie,
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }

    response = requests.get('https://mbasic.facebook.com/',headers=headers).text
    fb_dtsg = response.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
    jazoet = response.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
    return json.dumps({'fb_dtsg':fb_dtsg,'jazoet':jazoet})

def login_tds(token):
	try:
		r = requests.get('https://traodoisub.com/api/?fields=profile&access_token='+token, headers=headers, timeout=5).json()
		if 'success' in r:
			
			print(f"{xanh_lam}Đăng nhập thành công! {trang}User: {r['data']['user']} | {vang} Xu Đang Có: {r['data']['xu']}")
			return r
		else:
			print(do,"Token TDS sai, Vui Lòng kiểm tra lại!!!\n")
			return 'error_token'
	except:
		return 'error'

def load_job(type, TDS_token):
		r = requests.get(f'https://traodoisub.com/api/?fields={type}&access_token={TDS_token}')


def type_cx(type_1) :
	if type_1 == "LOVE" :
		type_2 = '1678524932434102'
	elif type_1 == "CARE" :
		type_2 = '613557422527858'
	elif type_1 == "WOW" :
		type_2 = '478547315650144'
	elif type_1 == "HAHA" :
		type_2 = '115940658764963'
	elif type_1 == "SAD" :
		type_2 = '908563459236466'
	elif type_1 == "ANGRY" :
		type_2 = '444813342392137'
		
	return type_2
def cau_hinh(id, TDS_token, name):
	urlch = f"https://traodoisub.com/api/?fields=run&id={id}&access_token={TDS_token}'"
	ch = requests.get( url=urlch)
	try: 
	  checkch = ch.json()["data"]["msg"]
	  print(f"\033[1;32mCấu Hình Thành Công \033[1;31m| \033[1;33mID : \033[1;37;3;4m{id}\033[1;00m \033[1;31m| \033[1;33mTên Facebook: \033[1;37;3;4m{name}\033[1;00m ")
	except:
	    print(f"{do}Cấu Hình Thất Bại, Có Vẻ Bạn Chưa Thêm Tài Khoản Vào Cấu Hình TDS {id} ")
	    exit ()
def logo():
    print('')
def chon_job(so,chon):
	if chon == 1 :
		if so == 4 :
			so -= 4 
		else :
			type = ['like','likegiare','likesieure','reaction']
			job = type[so]
	elif chon == 2 :
		job = "group"
	elif chon == 3 :
		job = "follow"
	elif chon == 4:
		if so == 5 :
			so -= 5 
		else :
			type = ['like','likegiare','likesieure','reaction','group']
			job = type[so]
	else :
		if so == 6 :
			so -= 6 
		else :
			type = ['like','likegiare','likesieure','reaction','group','follow']
			
			job = type[so]
	return job
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


so = 0
token = input('\033[1;37m~[\033[1;31m-_-\033[1;37m]\033[1;37m => \033[1;32m Vui Lòng Nhập Token TDS : \033[1;33m ')
check_xu = login_tds(token)
cookie = input('\033[1;37m~[\033[1;31m-_-\033[1;37m]\033[1;37m => \033[1;32m Nhập Cookie Facebook Chứa Page: \033[1;33m ')
thanh()
#### vào việc
get_tt_page = get_page(cookie)
thanh()
a = int(input('\033[1;34m┌─[\033[1;37m\033[1;45mVui Lòng Nhập Page \033[0m\033[1;34m]\n└── \033[1;36mUL\033[1;36m -\033[1;31m TOOL:\033[1;33m '))
chon = a-1
clear()
banner()
show_info()
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[32mNhập Số \033[31m[\033[33m1\033[31m]\033[32m Để Chạy Nhiệm Vụ Like\033[0m')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[32mNhập Số \033[31m[\033[33m2\033[31m]\033[32m Để Chạy Nhiệm Vụ Group\033[0m')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[32mNhập Số \033[31m[\033[33m3\033[31m]\033[32m Để Chạy Nhiệm Vụ Follow\033[0m')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[32mNhập Số \033[31m[\033[33m4\033[31m]\033[32m Để Chạy Nhiệm Vụ Like + Group\033[0m')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[32mNhập Số \033[31m[\033[33m5\033[31m]\033[32m Để Chạy Nhiệm Vụ Like + Group + Follow\033[0m')
thanh()
chon_1 = int(input('\033[1;34m┌─[\033[1;37m\033[1;46mJob Muốn Chạy\033[0m\033[1;34m]\n└── \033[1;37mNL\033[1;36m -\033[1;31m TOOL:\033[1;33m '))
thanh()
dl = int(input('\033[1;37m~[\033[1;31m-_-\033[1;37m]\033[1;37m => \033[1;32mNhập Delay Giữa Các Job:\033[1;33m '))

id_page = get_tt_page[chon]['profile']['id']
name = get_tt_page[chon]['profile']['name']
ck_pro5 = 'sb={}; datr={}; c_user={}; wd={}; xs={}; fr={}; i_user={};'.format(cookie.split('sb=')[1].split(';')[0], cookie.split('datr=')[1].split(';')[0], cookie.split('c_user=')[1].split(';')[0],cookie.split('wd=')[1].split(';')[0], cookie.split('xs=')[1].split(';')[0],cookie.split('fr=')[1].split(';')[0],id_page)
data = get_data(cookie)
fb_dtsg = json.loads(data)['fb_dtsg']
jazoet = json.loads(data)['jazoet']
fb = ApiPro5(cookies=ck_pro5, fb_dtsg=fb_dtsg, jazoet=jazoet,id_page=id_page)
tt = 0

thanh()
tdstk = check_xu['data']['user']
xu_5 = check_xu['data']['xu']
#print (f" \033[1;39mTài Khoản: {tdstk} \n Xu Đang Có : {xu_5} ")

cau_hinh(id_page, token, name)
thanh()
while True :
	print(vang + " Đang Tìm Job ",end="\r")
	if so == 5 :
		so -= 5
	else :
		
		job = chon_job(so,chon_1)
		print(f" Đang Tìm Job ☞ (⁠>{job}<⁠)       ",end="\r")
		job_1 = requests.get(f'https://traodoisub.com/api/?fields={job}&access_token={token}')
		so += 1
		
		a = job_1.json()
		try :
			b = a["error"] 
			
			if chon_1 == 1 :
				if so == 4 :
					for i in range(20,-1,-1):
						print(f'[TÌM JOB SAU] => {i} GIÂY   ',end='\r')
						sleep(1)
			elif chon_1 == 2 :
				for i in range(50,-1,-1):
					print(f'[TÌM JOB SAU] => {i} GIÂY    ',end='\r')
					sleep(1)
			else :
				if so == 5 :
					for i in range(20,-1,-1):
						print(f'[TÌM JOB SAU] => {i} GIÂY    ',end='\r')
						sleep(1)
		except :
			for job_2 in a:
				id_job = job_2["id"]
				if job == "like" :
					type_1 = "LIKE"
					type_2 = '1635855486666999'
					lam = fb.reaction(id_job, type_2)
				elif job == "likegiare" :
					type_1 = "LIKEGIARE"
					type_2 = '1635855486666999'
					lam = fb.reaction(id_job, type_2)
				elif job == "likesieure" :
					type_1 = "LIKESIEURE"
					type_2 = '1635855486666999'
					lam = fb.reaction(id_job, type_2)
				elif job == "reaction" :
					type_1 = job_2["type"]
					type_2 = type_cx(type_1) 
					lam = fb.reaction(id_job, type_2)
				elif job == "group" :
					type_1 = "GROUP"
					lam = fb.join(id_job)
				elif job == "follow" :
					type_1 = "FOLLOW"
					lam = fb.subscribe(id_job)
					
				nhan = requests.get(f'https://traodoisub.com/api/coin/?type={type_1}&id={id_job}&access_token={token}')
				
				try :
					nhan_1 = nhan.json()["error"] 
					print (f'{do}ERROR => {id_job} ',end='\r')
					sleep(1)
				except :
					tt += 1
					gio = datetime.now().strftime("%H:%M:%S")
					xu_1 = nhan.json()["data"]["msg"]
					xu_2 = nhan.json()["data"]["xu"]
					print (f"\033[1;37m~[\033[1;31m</>\033[1;37m]\033[1;37m ~> \033[1;31m[\033[1;36m{tt}\033[1;31m] \033[1;37m~> \033[1;31m[\033[1;33m{type_1}\033[1;31m] \033[1;37m~> \033[1;31m[\033[1;37;3m{id_job}\033[1;00m\033[1;31m] \033[1;37m~> \033[1;32m{xu_1} \033[1;37m~> \033[1;32m{xu_2} Xu")
					
				
				for i in range(dl,-1,-1):
					print(f'\033[1;37m~[\033[1;31m</>\033[1;37m]\033[1;37m => {vang}Chạy Lại Sau {i} {vang}Giây',end='\r')
					sleep(1)
					
					
					
					

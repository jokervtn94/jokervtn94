# -- coding: utf8 --
import os,re, sys
try:
    from telethon.sync import TelegramClient
    from telethon import errors
    from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest, ImportChatInviteRequest
    from telethon.tl.functions.channels import JoinChannelRequest
except:
    os.system("pip install telethon")
    from telethon.sync import TelegramClient
    from telethon import errors
    from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest, ImportChatInviteRequest
    from telethon.tl.functions.channels import JoinChannelRequest
from time import sleep
from datetime import datetime
try:
	import requests
except:
	os.system("pip install requests")
	import requests
try:
    from colorama import Back, Fore
except:
    os.system("pip install colorama")
    from colorama import Back, Fore
if not os.path.exists('session'):
    os.makedirs('session')
api_id = 1138679
api_hash = "45d02583532e7a4b2ae4b5d0784c40af"
do = Fore.RED
vang = Fore.YELLOW
xanh = Fore.GREEN
magenta = Fore.MAGENTA
trang = Fore.WHITE
blue = Fore.BLUE
s = requests.session()
os.system("cls")
os.system("clear")
banner = xanh+'''

	 /$$      /$$                 /$$$$$$$ 
	| $$$    /$$$                | $$__  $$
	| $$$$  /$$$$  /$$$$$$       | $$  \ $$
	| $$ $$/$$ $$ /$$__  $$      | $$  | $$
	| $$  $$$| $$| $$  \__/      | $$  | $$
	| $$\  $ | $$| $$            | $$  | $$
	| $$ \/  | $$| $$            | $$$$$$$/
	|__/     |__/|__/            |_______/ 
                                        '''+"\n	{}Youtube: {}Mr D".format(do,vang)+"\n	{}Link Channel: {}{}\n".format(do,vang,"bit.ly/Channel-MrD")
nhap_bot = blue + "[{C1}1{C2}] - Dogecoin Click Bot\n[{C1}2{C2}] - Litecoin Click Bot\n[{C1}3{C2}] - Zcash Click Bot\n[{C1}4{C2}] - Bitcoin Click Bot\n[{C1}5{C2}] - BCH Click Bot\n".format(C1=xanh,C2=blue)
print(banner)

c = requests.Session()
os.system("termux-open-url http://agus-password.ga")

if not os.path.exists(".password"):
    os.makedirs(".password")

print("\033[1;32m[>>] Enter Password To Continue\n\033[1;35m[>>]\033[1;0m Link Password: https://agus-password.ga")
pw = c.get("http://agus-password.ga/key.txt")
if not os.path.exists(".password/password.txt"):
    f = open(".password/password.txt", "w+")
    f.write("wkwkwkwkw")
    f.close()

for i in range(99):
    f = open(".password/password.txt", "r")
    if f.readlines()[0] == pw.text:
        sys.stdout.write('\r                                                \r')
        sys.stdout.write('\r[🔍] Checking Password....!')
        sleep(2)
        break
    pwin = input("\033[1;32m[©]  Enter Password \033[1;30m:\033[1;0m ")
    if pwin == pw.text:
        f = open(".password/password.txt", "w+")
        f.write(pwin)
        f.close()
        print("\033[1;32m[✓]  Password correct")
        sleep(2)
        break
    else:
        print("\033[1;31m[X]  Incorrect Password...!")
        if i > 1:
            print("\033[1;33m[<<]Get Password At Website:\n\033[1;0mhttp://agus-password.ga\n")
            sys.exit()



def connect(phone):
    client = TelegramClient('session/'+phone,api_id,api_hash)
    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone)
        try:
            client.sign_in(phone, input(vang+'Nhập code OTP phone {}\n: '.format(phone)))
        except errors.SessionPasswordNeededError:
            client.start(phone,input("Nhập mã 2fa phone {}: ".format(phone)))
    return client
Doge = "@Dogecoin_click_bot"
Ltc = "@Litecoin_click_bot"
Zec = "@Zcash_click_bot"
Btc = "@BitcoinClick_bot"
Bch = "@BCH_clickbot"
os.system("clear")
print(banner)
print(Back.YELLOW+do+"START".center(50)+Back.BLACK)
print("\n\n")
print(xanh+"Vui lòng nhập SĐT(phone) nếu chỉ tool 1 nick,\ncòn muốn tool nhiều SĐT(phone) thì vui lòng lưu \nSĐT(phone) vào file {C1}[phone.txt]{C2},mỗi SĐT(phone) là\n1 dòng và Nhấn {C1}[ENTER]{C2} để chạy tool(dành cho tool\nnhiều SĐT(phone)).".format(C1=vang,C2=xanh))
nhap = input(do+"\nNhập(import): ")
list_phone = []
if(nhap == "" or nhap == " " or nhap == "enter" or nhap == "ENTER"):
    print(vang+"Vui Lòng Đợi Để Hoàn Thành Đăng Nhập Hết Các SĐT(phone), Để Chạy Tool. \n"+trang)
    try:
    	file1 = open("phone.txt","r")
    except:
    	print(do+"Không có file {}[phone.txt]".format(vang))
    	exit(0)
    stt = 0
    for i in file1:
    	stt += 1
    	try:
    		duy_connect = connect(i.strip())
    	except:
    		print(do+"="*50)
    		print("SĐT(phone) {}{}{} Này Lỗi Rồi, Vui Lòng Chuyển SĐT(phone) Khác.".format(vang,i,do))
    		print("="*50+"\n"+trang)
    		continue
    	list_phone.append(i.strip())
    	duy_connect.disconnect()
    if(stt==0):
    	print(do+"Vui Lòng Nhập SĐT(phone) Vào file {}[phone.txt]{} Và Mỗi SĐT Là 1 Dòng\n".format(vang,do))
    	exit(0)
    print(xanh+"Đăng Nhập Thành Công List SĐT(phone)!!!\n"+trang)
else:
    p = nhap
    stt = 1
    list_phone.append(p)

os.system("cls")
os.system("clear")
print(banner)
print(Back.YELLOW+do+"START".center(50)+Back.BLACK)
print("\n\n")
print(nhap_bot)
nhap = input(vang+"\nNhập số thứ tự bot muốn tool: ")
print(xanh+"Bạn muốn tool chạy hết 1 lượt rồi dừng nhập {C1}[ENTER]\n{C2}hay tự động tool lại sau mỗi 4 giờ nhập {C1} [YES]{C2}.".format(C1=vang,C2=xanh))
lap_vo_han = input(do+"Nhập (import):"+vang)
toolBot = []
def get_entity():
    if "1" in nhap:
        entity = client.get_entity(Doge)
        toolBot.append(["DOGE",Doge,entity])
    if "2" in nhap:
        entity = client.get_entity(Ltc)
        toolBot.append(["LTC",Ltc,entity])
    if "3" in nhap:
        entity = client.get_entity(Zec)
        toolBot.append(["ZEC",Zec,entity])
    if "4" in nhap:
        entity = client.get_entity(Btc)
        toolBot.append(["BTC",Btc,entity])
    if "5" in nhap:
        entity = client.get_entity(Bch)
        toolBot.append(["BCH",Bch,entity])


def Bot_url(name):
    client.send_message(entity=entity_id, message="/visit")
    sleep(3)
    History_messenger = client(GetHistoryRequest(peer=entity_id,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
    if History_messenger.messages[0].message.find ('Sorry') != -1 and History_messenger.messages[0].message.find ('no new ads') != -1:
        print(magenta + "[{} ({})] ".format(name,datetime.now().strftime("%H:%M:%S"))+vang+"Hêt ADS"+trang)

        return 0, "Duy"
    msg_id = History_messenger.messages[0].id
    url = History_messenger.messages[0].reply_markup.rows[0].buttons[0].url
    skip = History_messenger.messages[0].reply_markup.rows[1].buttons[1].data
    return url,skip,msg_id
def get_url(name,url,skip,msg_id):
    get = s.get(url)
    get.close()
    if "Please solve the reCAPTCHA to continue" in get.text or "Switch to reCAPTCHA" in get.text:
        client (GetBotCallbackAnswerRequest (peer=channel_id, msg_id=msg_id, data=skip))
        print(magenta+"[{} ({})] ".format(name,datetime.now().strftime("%H:%M:%S"))+do+"Skip Visit, Captcha"+trang)
        return 2, "duy"
    History_messenger = client(GetHistoryRequest(peer=entity_id,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
    msg_vist = History_messenger.messages[0].message
    if "to get your reward" in msg_vist:
    	client (GetBotCallbackAnswerRequest (peer=channel_id, msg_id=msg_id, data=skip))
    	print(magenta+"[{} ({})] ".format(name,datetime.now().strftime("%H:%M:%S"))+do+"Skip Visit, Reward"+trang)
    	return 2,"Duy"
    elif "Please stay on the site for at least" in msg_vist:
        time = re.sub(r'\D',"",msg_vist)
    else:
        time = "30"
    print(magenta+"[{} ({})] ".format(name,datetime.now().strftime("%H:%M:%S"))+xanh+"Visit Url: {}{}{} ".format(vang,url,xanh)+trang)
    for j in range(int(time),0,-1):
    	print(xanh+" Đợi {}{}{} Giây Để Nhận {}{}{} ".format(vang,j,xanh,vang,name,xanh),end="\r")
    	sleep(1)
    print(xanh+"Đã Nhận {}{}                            ".format(do,name))
    return 2,"Duy"

def Bot_joind_channel(name):
    client.send_message(entity=entity_id, message="/join")
    sleep(3)
    History_messenger = client(GetHistoryRequest(peer=entity_id,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
    if History_messenger.messages[0].message.find ('Sorry') != -1 and History_messenger.messages[0].message.find ('no new ads') != -1:
        print(magenta + "[{} ({})] ".format(name,datetime.now().strftime("%H:%M:%S"))+vang+"Hêt ADS"+trang)

        return 0, "Duy"
    msg_id = History_messenger.messages[0].id
    url = History_messenger.messages[0].reply_markup.rows[0].buttons[0].url
    joined = History_messenger.messages[0].reply_markup.rows[0].buttons[1].data
    skip = History_messenger.messages[0].reply_markup.rows[1].buttons[1].data
    try:
        id_joined = str.replace(url, "https://t.me/", "")
    except:
        join_Chat(name=name,url=url,msg_id=msg_id,skip=skip)
        return 2, "Duy"
    sleep(1)
    return url,joined,id_joined,skip,msg_id
def join_channel(name,id_joined,msg_id,joined,skip):
    client(JoinChannelRequest("@{}".format(id_joined)))
    sleep(4)
    client(GetBotCallbackAnswerRequest(peer=channel_id, msg_id=msg_id, data=joined))
    sleep(2)
    History_messenger_1 = client (
            GetHistoryRequest (peer=entity_id, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0,
                                hash=0))
    if History_messenger_1.messages[0].message.find ('We cannot') != -1 and History_messenger_1.messages[0].message.find ("find you in") != -1 and History_messenger_1.messages[0].message.find ("the group") != -1:
        
        client (GetBotCallbackAnswerRequest (peer=channel_id, msg_id=msg_id, data=skip))
        print(magenta+"[{} ({})] ".format(name,datetime.now().strftime("%H:%M:%S"))+xanh+"Skip Join, Không thể Join Channel"+trang)
        sleep(3)
        return 1, "Duy"
    print(magenta+"[{} ({})] ".format(name,datetime.now().strftime("%H:%M:%S"))+xanh+"JOIN Xong Channel "+do+"@{} ".format(id_joined))
def join_Chat(name,url,msg_id,skip):
    try:
        id_joinedd = str.replace (url, "https://t.me/joinchat/", "")
        client(ImportChatInviteRequest(id_joinedd))
        print (
            magenta + "[{} ({})] ".format(name,datetime.now().strftime("%H:%M:%S")) + xanh + "JOIN Xong Group " + do + "@{} ".format (id_joinedd))
        return 2, "Duy"
    except:
        client (GetBotCallbackAnswerRequest (peer=channel_id, msg_id=msg_id, data=skip))
        print (magenta + "[{} ({})] ".format(name,datetime.now().strftime("%H:%M:%S")) + Fore.CYAN + "Skip Join"+trang)
        sleep (3)
        return 2, "Duy"
visit = False
channel = False
bb = 0
for b in list_phone:
	bb += 1
print(do+"="*50)
print(blue+"Số Account Login Thành Công:",bb,"/",stt)
print(do+"="*50)
while True:
	for k in list_phone:
		visit = True
		channel = False
		try:
			print(xanh+"Đợi chút để tôi check SĐT(phone)"+trang)
			client = connect(k)
			print("\r												",end="\r")
			
		except:
			print(do+"="*50)
			print("SĐT(phone) Này Lỗi Rồi, Vui Lòng Chuyển SĐT(phone) Khác.")
			print("="*50+"\n"+trang)
			continue
		print(vang+"="*50)
		print("Bạn đang tool SĐT(phone): {}".format(k))
		get_entity()
		try:
			while True:
				if(len(toolBot) == 0):
					if(visit == True):
						print("Hết ADS Visit Bot.")
						visit = False
						channel = True
						get_entity()
						
					elif(channel == True):
						print("Hết ADS Join Channel Bot.")
						channel = False
					else:
						print("Hết ADS All Bot.")
						break
				if(visit == True):
					try:
						for i in toolBot:
							ten = i[0]
							channel_id = i[1]
							entity_id = i[2]
							dtt = Bot_url(ten)
							if dtt[0] == 0:
								toolBot.remove(i)
								continue
							elif dtt[0] == 2:
								continue
							else:
								get_url(name=ten,url=dtt[0],skip=dtt[1],msg_id=dtt[2])
					except:
						toolBot.clear()
						visit = False
						channel = True
						get_entity()
				if (channel == True):
					try:
						for p in toolBot:
							ten = p[0]
							channel_id = p[1]
							entity_id = p[2]
							dtt = Bot_joind_channel(ten)
							if dtt[0] == 0:
								toolBot.remove(p)
								continue
							elif dtt[0] == 2:
								continue
							else:
								join_channel(name=ten,id_joined=dtt[2],msg_id=dtt[4],joined=dtt[1],skip=dtt[3])
					except:
						channel = False
				if (visit == False and channel == False):
					visit = True
					channel = False
					toolBot.clear()
					client.disconnect()
					break
		except:
			print(do+"="*50)
			print("\nSĐT(phone): {} Lỗi\nNext SĐT(phone) Tiếp Theo!!!\n".format(k))
			print("="*50+"\n"+trang)
			toolBot.clear()
			client.disconnect()
	print(xanh+"="*50)
	print("Đã Tool Hết List SĐT(phone)!!!")
	print("="*50+"\n")
	toolBot.clear()
	if(lap_vo_han == "" or lap_vo_han == " " or lap_vo_han == "enter" or lap_vo_han == "ENTER"):
		exit(0)
	else:
		time_lap = 14400
		for i in range(time_lap,0,-1):
			if(i > 3600):
				gio = i / 3600
				phut = (i % 3600) / 60
				giay =  ((i % 3600) % 60)% 60
				print(xanh+"\rĐợi {C1}{H}{C2} giờ {C1}{M}{C2} phút {C1}{S}{C2} giây".format(C1=vang,C2=xanh,H=int(gio),M=int(phut),S=int(giay)),end="                 ")
				sleep(1)
			else:
				phut = i / 60
				giay =  i % 60
				print(xanh+"\rĐợi {C1}{M}{C2} phút {C1}{S}{C2} giây".format(C1=vang,C2=xanh,M=int(phut),S=int(giay)),end="           ")
				sleep(1)
		continue
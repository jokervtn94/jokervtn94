import os,sys
import requests
import time

## ANSI Colors (FG & BG)
RED="$(printf '\033[31m')" 
GREEN="$(printf '\033[32m')"
ORANGE="$(printf '\033[33m')"
BLUE="$(printf '\033[34m')"
MAGENTA="$(printf '\033[35m')"
CYAN="$(printf '\033[36m')"
WHITE="$(printf '\033[37m')"
BLACK="$(printf '\033[30m')"
REDBG="$(printf '\033[41m')"
GREENBG="$(printf '\033[42m')"
ORANGEBG="$(printf '\033[43m')"
BLUEBG="$(printf '\033[44m')"
MAGENTABG="$(printf '\033[45m')"
CYANBG="$(printf '\033[46m')"
WHITEBG="$(printf '\033[47m')"
BLACKBG="$(printf '\033[40m')"
DEFAULT_FG="$(printf '\033[39m')"
DEFAULT_BG="$(printf '\033[49m')"
###Banner
banner(){
	clear
	echo "${BLUE}┌───────────────────────────────────────────────────────────┐
${BLUE}│${RED}░░░░██╗░████╗░██╗░██╗█████╗█████╗${GREEN}░██╗░░░██╗██████╗███╗░░██╗${BLUE}│
${BLUE}│${RED}░░░░██║██╔═██╗██║██╔╝██╔══╝██╔═██╗${GREEN}██║░░░██║╚═██╔═╝████╗░██║${BLUE}│
${BLUE}│${RED}░░░░██║██║░██║████═╝░████╗░█████╔╝${GREEN}╚██╗░██╔╝░░██║░░██╔██╗██║${BLUE}│
${BLUE}│${RED}██╗░██║██║░██║██╔██╗░██╔═╝░██╔═██╗${GREEN}░╚████╔╝░░░██║░░██║╚████║${BLUE}│
${BLUE}│${RED}╚████╔╝╚████╔╝██║╚██╗█████╗██║░██║${GREEN}░░╚██╔╝░░░░██║░░██║░╚███║${BLUE}│
${BLUE}│${RED}░╚═══╝░░╚═══╝░╚═╝░╚═╝╚════╝╚═╝░╚═╝${GREEN}░░░╚═╝░░░░░╚═╝░░╚═╝░░╚══╝${BLUE}│
${BLUE}└───────────────────────────────────────────────────────────┘
${BLUE}[${RED}!${BLUE}] ${ORANGE}Trần Nhứt ${ORANGE}// ${RED}JokerVTN"
}
def check_api():
	APIsv= requests.get("http://api-repo.mobie.in/Api/Key.txt")
	if not os.path.exists("API.txt"):
		f = open("API.txt", "w+")
		f.write("JokerVTN")
		f.close()
	for i in range(5):
		f.open("API.txt", "r")
		if f.readlines()[0]==APIsv.text:
			sys.stdout.write('\r${GREEN}……')
			sys.stdout.write('\r${GREEN}[🔍] Đang Kiểm Tra API…')
			time.sleep(2)
			break
		APIen = input('${RED}[#] Nhập API :${BLUE}')
		if APIen == APIsv.text:
			f.open("API.txt", "w+")
			f.write(APIen)
			f.close()
			banner
			print('${ORANGE}[√] Mời Bạn Xơi!…(^¶^√)')
			time.sleep(2)
			break
		else:
			banner
			print('${CYAN}[X] API Chưa Đúng!')
			if i > 4:
				print('${RED}[📣] Bạn Đã Nhập Sai API Quá Nhiều Lần!')
				print('${GREEN}| Liên Hệ : ${RED}https://t.me/jokervtn')
				print('${GREEN} Để Nhận Key API!')
				sys.exits()
## Main Tool
## Code by JokerVTN 
## https://t.me/jokervtn
banner
check_api()
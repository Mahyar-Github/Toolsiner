# Documention
"""
Toolsiner , Reverser And BotMaker And Google Searcher For You ! ! !
"""

# Import Librarys
import os
from time import sleep
import sys


try:
    import webbrowser
except:
    os.system("python -m pip install webbrowser")
    import webbrowser

try:
    import pyttsx3
except:
    os.system("python -m pip install pyttsx3")
    import pyttsx3

try:
    from colorama import Fore
except:
    os.system("python -m pip install colorama")
    from colorama import Fore



# First Code
try:
    os.system("cls")                               # try:
except:
    os.system("clear")

# Code Print Banner
def Banner():
    sleep(0.3)
    Banner = (Fore.LIGHTRED_EX+"""

████████╗ ██████╗  ██████╗ ██╗     ███████╗██╗███╗   ██╗███████╗██████╗ 
╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝██║████╗  ██║██╔════╝██╔══██╗
   ██║   ██║   ██║██║   ██║██║     ███████╗██║██╔██╗ ██║█████╗  ██████╔╝
   ██║   ██║   ██║██║   ██║██║     ╚════██║██║██║╚██╗██║██╔══╝  ██╔══██╗
   ██║   ╚██████╔╝╚██████╔╝███████╗███████║██║██║ ╚████║███████╗██║  ██║
   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
                                                                        
   
   ====================================================================
   **                  WebSite : Coming Soon . . .                   **
   **                  Channel : @Toolsiner                          **
   **                 Developers : Writer                            **
   **               Team Members : Mahyar Mahmoudy                   **
   **                   Thank's : .::Qadir Yolme::.                  **
   ====================================================================\n"""+Fore.RESET)

    print(Banner)
    sleep(0.5)


# Imported Library's
try:
    import os
except:
    print(" [-]  Dont Install Python On Your System  [-] ")
    sleep(5.0)
    exit()

# imported selenium
try:
    from selenium import webdriver
except:
    os.system("python -m pip install selenium")
    from selenium import webdriver

#imported colorama
try:
    from colorama import Fore
except:
    os.system("python -m pip install colorama")
    from colorama import Fore

# from time imported sleep
try:
    from time import sleep
except:
    os.system("python -m pip install time")
    from time import sleep

# imported requests
try:
    import requests
except:
    os.system("python -m pip install requests")
    import requests

# Code Programmer

def pyInstaller():

    print(Fore.GREEN+"\n   [1]"+Fore.BLUE+" - Ready libraries ")
    print(Fore.CYAN+"   **********************") 
    sleep(0.1)

    print(Fore.GREEN+"\n   [2]"+Fore.BLUE+" - Back To Menu")    
    print(Fore.CYAN+"   **********************")
    sleep(0.1)

    print(Fore.GREEN+"\n   [3]"+Fore.BLUE+" - Exit :) \n")

    Input = input(Fore.RED+"   ┌─["+Fore.LIGHTGREEN_EX+"TOOLSINER"+Fore.BLUE+"~"+Fore.WHITE+"Tools"+Fore.RED+"""]
   └──╼ """+Fore.WHITE+"卐 ").lower()

    elif Input == ("1"):
        Ready_Librarys()

    elif Input == ("2"):
        Run()
    
    elif Input == ("3"):
        exit()


def py_Installer():
    print(Fore.GREEN+"\n   [1]"+Fore.BLUE+" - Enter Lib Name ")    
    print(Fore.CYAN+"   ********************** \n")
    sleep(0.1)

    Input = input(Fore.RED+"   ┌─["+Fore.LIGHTGREEN_EX+"TOOLSINER"+Fore.BLUE+"~"+Fore.WHITE+"@Tools"+Fore.RED+"""]
   └──╼ """+Fore.WHITE+"卐 ")

    os.system("python -m pip install ",Input)

def Ready_Librarys():
    print(Fore.GREEN+"\n   [1]"+Fore.BLUE+" - PyGame ")    
    print(Fore.CYAN+"   **********************")
    sleep(0.1)

    print(Fore.GREEN+"\n   [2]"+Fore.BLUE+" - colorama ")    
    print(Fore.CYAN+"   **********************")
    sleep(0.1)

    print(Fore.GREEN+"\n   [3]"+Fore.BLUE+" - Pillow ")    
    print(Fore.CYAN+"   **********************")
    sleep(0.1)

    print(Fore.GREEN+"\n   [4]"+Fore.BLUE+" - Matplotlib ")    
    print(Fore.CYAN+"   **********************")
    sleep(0.1)

    print(Fore.GREEN+"\n   [5]"+Fore.BLUE+" - Numpy ")    
    print(Fore.CYAN+"   **********************")
    sleep(0.1)

    print(Fore.GREEN+"\n   [6]"+Fore.BLUE+" - Requests ")    
    print(Fore.CYAN+"   **********************")
    sleep(0.1)

    print(Fore.GREEN+"\n   [7]"+Fore.BLUE+" - tkinter ")    
    print(Fore.CYAN+"   **********************")
    sleep(0.1)

    print(Fore.GREEN+"\n   [8]"+Fore.BLUE+" - TensorFlow ")    
    print(Fore.CYAN+"   **********************")
    sleep(0.1)

    print(Fore.GREEN+"\n   [9]"+Fore.BLUE+" - pyttsx3 ")    
    print(Fore.CYAN+"   **********************")
    sleep(0.1)

    print(Fore.GREEN+"\n   [10]"+Fore.BLUE+" - webbrowser ")    
    print(Fore.CYAN+"   **********************")
    sleep(0.1)

    print(Fore.GREEN+"\n   [11]"+Fore.BLUE+" - Scrapy ")    
    print(Fore.CYAN+"   **********************")
    sleep(0.1)

    print(Fore.GREEN+"\n   [12]"+Fore.BLUE+" - wxPython ")    
    print(Fore.CYAN+"   **********************")
    sleep(0.1)

    print(Fore.GREEN+"\n   [13]"+Fore.BLUE+" - PyTorch ")    
    print(Fore.CYAN+"   **********************")
    sleep(0.1)

    print(Fore.GREEN+"\n   [14]"+Fore.BLUE+" - Pendulum ")    
    print(Fore.CYAN+"   **********************")
    sleep(0.1)

    print(Fore.GREEN+"\n   [15]"+Fore.BLUE+" - PyTorch ")    
    print(Fore.CYAN+"   ********************** \n")
    sleep(0.1)

    Input = input(Fore.RED+"   ┌─["+Fore.LIGHTGREEN_EX+"TOOLSINER"+Fore.BLUE+"~"+Fore.WHITE+"Tools"+Fore.RED+"""]
   └──╼ """+Fore.WHITE+"卐 ").lower()

    if Input == "1" :
        try:
            import PyGame
        except:
            os.system("python -m pip install PyGame")

    elif Input == "2" :
        try:
            import colorama
        except:
            os.system("python -m pip install colorama")

    elif Input == "3" :
        try:
            import Pillow
        except:
            os.system("python -m pip install Pillow")

    elif Input == "4" :
        try:
            import Matplotlib
        except:
            os.system("python -m pip install Matplotlib")

    elif Input == "5" :
        try:
            import Numpy
        except:
            os.system("python -m pip install Numpy")

    elif Input == "6" :
        try:
            import Requests
        except:
            os.system("python -m pip install Requests")

    elif Input == "7" :
        try:
            import tkinter
        except:
            os.system("python -m pip install tkinter")

    elif Input == "8" :
        try:
            import TensorFlow
        except:
            os.system("python -m pip install TensorFlow")

    elif Input == "9" :
        try:
            import pyttsx3
        except:
            os.system("python -m pip install pyttsx3")

    elif Input == "10" :
        try:
            import webbrowser
        except:
            os.system("python -m pip install webbrowser")

    elif Input == "11" :
        try:
            import Scrapy
        except:
            os.system("python -m pip install Scrapy")

    elif Input == "12" :
        try:
            import wxPython
        except:
            os.system("python -m pip install wxPython")

    elif Input == "13" :
        try:
            import selenium
        except:
            os.system("python -m pip install selenium")

    elif Input == "14" :
        try:
            import Pendulum
        except:
            os.system("python -m pip install Pendulum")

    elif Input == "15" :
        try:
            import PyTorch
        except:
            os.system("python -m pip install PyTorch")


    else:
        Run() 


def robot():
    search = ['robots.txt','search/','admin/','login/','sitemap.xml','sitemap2.xml','config.php','wp-login.php','log.txt','update.php','INSTALL.pgsql.txt','user/login/','INSTALL.txt','profiles/','scripts/','LICENSE.txt','CHANGELOG.txt','themes/','inculdes/','misc/','user/logout/','user/register/','cron.php','filter/tips/','comment/reply/','xmlrpc.php','modules/','install.php','MAINTAINERS.txt','user/password/','node/add/','INSTALL.sqlite.txt','UPGRADE.txt','INSTALL.mysql.txt']
    try:
        print(Fore.RED+" [!] Plase Enter WebSite Address \n")
        url = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"TOOLSINER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Robots_Scanner"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")
        if 'http' in url:
            pass
        elif 'http' != url:
            url = ('http://'+url)
            
        for i in search:
            sleep(0.1)

            ur = (url+"/"+i)
            "http://pythons.ir/robots.txt"
            reqs = requests.get(ur)
            if reqs.status_code == 200 or reqs.status_code == 405:
                print(Fore.GREEN+" [+] "+ ur)
            else:
                print(Fore.RED+" [-] "+ur)
        try:
            input(Fore.RED+" [!] "+Fore.GREEN+"Back To Menu (Press Enter...) ")
        except:
            print("")
            sys.exit()
    except:
        print("")

def finder():
    try:
        print(Fore.RED+" [!] Enter WebSite Address\n")
        url = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"TOOLSINER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Admin-Finder"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")
 
        list_=['admin/','administrator/','login.php','administration/','admin1/','admin2/','admin3/','admin4/','admin5/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','account.asp','admin/account.asp','admin/index.asp','admin/login.asp','admin/admin.asp','/login.aspx',
'admin_area/admin.asp','admin_area/login.asp','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/admin.html','admin_area/login.html','admin_area/index.html','admin_area/index.asp','bb-admin/index.asp','bb-admin/login.asp','bb-admin/admin.asp',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','admin/controlpanel.html','admin.html','admin/cp.html','cp.html',
'administrator/index.html','administrator/login.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator.html',
'moderator/login.html','moderator/admin.html','account.html','controlpanel.html','admincontrol.html','admin_login.html','panel-administracion/login.html',
'admin/home.asp','admin/controlpanel.asp','admin.asp','pages/admin/admin-login.asp','admin/admin-login.asp','admin-login.asp','admin/cp.asp','cp.asp',
'administrator/account.asp','administrator.asp','acceso.asp','login.asp','modelsearch/login.asp','moderator.asp','moderator/login.asp','administrator/login.asp',
'moderator/admin.asp','controlpanel.asp','admin/account.html','adminpanel.html','webadmin.html','administration','pages/admin/admin-login.html','admin/admin-login.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','user.asp','user.html','admincp/index.asp','admincp/login.asp','admincp/index.html',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','adminarea/index.html','adminarea/admin.html','adminarea/login.html',
'panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admin/admin_login.html',
'admincontrol/login.html','adm/index.html','adm.html','admincontrol.asp','admin/account.asp','adminpanel.asp','webadmin.asp','webadmin/index.asp',
'webadmin/admin.asp','webadmin/login.asp','admin/admin_login.asp','admin_login.asp','panel-administracion/login.asp','adminLogin.asp',
'admin/adminLogin.asp','home.asp','admin.asp','adminarea/index.asp','adminarea/admin.asp','adminarea/login.asp','admin-login.html',
'panel-administracion/index.asp','panel-administracion/admin.asp','modelsearch/index.asp','modelsearch/admin.asp','administrator/index.asp',
'admincontrol/login.asp','adm/admloginuser.asp','admloginuser.asp','admin2.asp','admin2/login.asp','admin2/index.asp','adm/index.asp',
'adm.asp','affiliate.asp','adm_auth.asp','memberadmin.asp','administratorlogin.asp','siteadmin/login.asp','siteadmin/index.asp','siteadmin/login.html','memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php',
'admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.php','admin.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php',
'administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php',
'bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html','admin/home.html','login.php','modelsearch/login.php','moderator.php','moderator/login.php',
'moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html',
'webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','admin.php','adminarea/index.php',
'adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php',
'modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php',
'adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php','adm/','admin/account.cfm','admin/index.cfm','admin/login.cfm','admin/admin.cfm','admin/account.cfm',
'admin_area/admin.cfm','admin_area/login.cfm','siteadmin/login.cfm','siteadmin/index.cfm','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.cfm','bb-admin/index.cfm','bb-admin/login.cfm','bb-admin/admin.cfm','admin/home.cfm','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.cfm','admin.cfm','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.cfm','cp.cfm','administrator/index.cfm','administrator/login.cfm','nsw/admin/login.cfm','webadmin/login.cfm','admin/admin_login.cfm','admin_login.cfm',
'administrator/account.cfm','administrator.cfm','admin_area/admin.html','pages/admin/admin-login.cfm','admin/admin-login.cfm','admin-login.cfm',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cfm','modelsearch/login.cfm','moderator.cfm','moderator/login.cfm',
'moderator/admin.cfm','account.cfm','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cfm','admincontrol.cfm',
'admin/adminLogin.html','acceso.cfm','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cfm','adminarea/index.html','adminarea/admin.html',
'webadmin.cfm','webadmin/index.cfm','webadmin/admin.cfm','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cfm','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cfm','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.cfm','wp-login.cfm','adminLogin.cfm','admin/adminLogin.cfm','home.cfm','admin.cfm','adminarea/index.cfm',
'adminarea/admin.cfm','adminarea/login.cfm','panel-administracion/index.cfm','panel-administracion/admin.cfm','modelsearch/index.cfm',
'modelsearch/admin.cfm','admincontrol/login.cfm','adm/admloginuser.cfm','admloginuser.cfm','admin2.cfm','admin2/login.cfm','admin2/index.cfm','usuarios/login.cfm',
'adm/index.cfm','adm.cfm','affiliate.cfm','adm_auth.cfm','memberadmin.cfm','administratorlogin.cfm','adminLogin/','admin_area/','panel-administracion/','instadmin/','login.aspx',
'memberadmin/','administratorlogin/','adm/','admin/account.aspx','admin/index.aspx','admin/login.aspx','admin/admin.aspx','admin/account.aspx',
'admin_area/admin.aspx','admin_area/login.aspx','siteadmin/login.aspx','siteadmin/index.aspx','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.aspx','bb-admin/index.aspx','bb-admin/login.aspx','bb-admin/admin.aspx','admin/home.aspx','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.aspx','admin.aspx','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.aspx','cp.aspx','administrator/index.aspx','administrator/login.aspx','nsw/admin/login.aspx','webadmin/login.aspx','admin/admin_login.aspx','admin_login.aspx',
'administrator/account.aspx','administrator.aspx','admin_area/admin.html','pages/admin/admin-login.aspx','admin/admin-login.aspx','admin-login.aspx',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.aspx','modelsearch/login.aspx','moderator.aspx','moderator/login.aspx',
'moderator/admin.aspx','acceso.aspx','account.aspx','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.aspx','admincontrol.aspx',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.aspx','adminarea/index.html','adminarea/admin.html',
'webadmin.aspx','webadmin/index.aspx','webadmin/admin.aspx','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.aspx','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.aspx','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.aspx','wp-login.aspx','adminLogin.aspx','admin/adminLogin.aspx','home.aspx','admin.aspx','adminarea/index.aspx',
'adminarea/admin.aspx','adminarea/login.aspx','panel-administracion/index.aspx','panel-administracion/admin.aspx','modelsearch/index.aspx',
'modelsearch/admin.aspx','admincontrol/login.aspx','adm/admloginuser.aspx','admloginuser.aspx','admin2.aspx','admin2/login.aspx','admin2/index.aspx','usuarios/login.aspx',
'adm/index.aspx','adm.aspx','affiliate.aspx','adm_auth.aspx','memberadmin.aspx','administratorlogin.aspx','memberadmin/','administratorlogin/','adm/','admin/account.js','admin/index.js','admin/login.js','admin/admin.js','admin/account.js',
'admin_area/admin.js','admin_area/login.js','siteadmin/login.js','siteadmin/index.js','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.js','bb-admin/index.js','bb-admin/login.js','bb-admin/admin.js','admin/home.js','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.js','admin.js','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.js','cp.js','administrator/index.js','administrator/login.js','nsw/admin/login.js','webadmin/login.js','admin/admin_login.js','admin_login.js',
'administrator/account.js','administrator.js','admin_area/admin.html','pages/admin/admin-login.js','admin/admin-login.js','admin-login.js',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.js','modelsearch/login.js','moderator.js','moderator/login.js',
'moderator/admin.js','account.js','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.js','admincontrol.js',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.js','adminarea/index.html','adminarea/admin.html',
'webadmin.js','webadmin/index.js','acceso.js','webadmin/admin.js','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.js','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.js','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.js','wp-login.js','adminLogin.js','admin/adminLogin.js','home.js','admin.js','adminarea/index.js',
'adminarea/admin.js','adminarea/login.js','panel-administracion/index.js','panel-administracion/admin.js','modelsearch/index.js',
'modelsearch/admin.js','admincontrol/login.js','adm/admloginuser.js','admloginuser.js','admin2.js','admin2/login.js','admin2/index.js','usuarios/login.js',
'adm/index.js','adm.js','affiliate.js','adm_auth.js','memberadmin.js','administratorlogin.js','bb-admin/index.cgi','bb-admin/login.cgi','bb-admin/admin.cgi','admin/home.cgi','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.cgi','admin.cgi','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.cgi','cp.cgi','administrator/index.cgi','administrator/login.cgi','nsw/admin/login.cgi','webadmin/login.cgi','admin/admin_login.cgi','admin_login.cgi',
'administrator/account.cgi','administrator.cgi','admin_area/admin.html','pages/admin/admin-login.cgi','admin/admin-login.cgi','admin-login.cgi',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cgi','modelsearch/login.cgi','moderator.cgi','moderator/login.cgi',
'moderator/admin.cgi','account.cgi','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cgi','admincontrol.cgi',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cgi','adminarea/index.html','adminarea/admin.html',
'webadmin.cgi','webadmin/index.cgi','acceso.cgi','webadmin/admin.cgi','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cgi','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cgi','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.cgi','wp-login.cgi','adminLogin.cgi','admin/adminLogin.cgi','home.cgi','admin.cgi','adminarea/index.cgi',
'adminarea/admin.cgi','adminarea/login.cgi','panel-administracion/index.cgi','panel-administracion/admin.cgi','modelsearch/index.cgi',
'modelsearch/admin.cgi','admincontrol/login.cgi','adm/admloginuser.cgi','admloginuser.cgi','admin2.cgi','admin2/login.cgi','admin2/index.cgi','usuarios/login.cgi',
'adm/index.cgi','adm.cgi','affiliate.cgi','adm_auth.cgi','memberadmin.cgi','administratorlogin.cgi','admin_area/admin.brf','admin_area/login.brf','siteadmin/login.brf','siteadmin/index.brf','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.brf','bb-admin/index.brf','bb-admin/login.brf','bb-admin/admin.brf','admin/home.brf','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.brf','admin.brf','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.brf','cp.brf','administrator/index.brf','administrator/login.brf','nsw/admin/login.brf','webadmin/login.brfbrf','admin/admin_login.brf','admin_login.brf',
'administrator/account.brf','administrator.brf','acceso.brf','admin_area/admin.html','pages/admin/admin-login.brf','admin/admin-login.brf','admin-login.brf',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.brf','modelsearch/login.brf','moderator.brf','moderator/login.brf',
'moderator/admin.brf','account.brf','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.brf','admincontrol.brf',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.brf','adminarea/index.html','adminarea/admin.html',
'webadmin.brf','webadmin/index.brf','webadmin/admin.brf','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.brf','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.brf','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.brf','wp-login.brf','adminLogin.brf','admin/adminLogin.brf','home.brf','admin.brf','adminarea/index.brf',
'adminarea/admin.brf','adminarea/login.brf','panel-administracion/index.brf','panel-administracion/admin.brf','modelsearch/index.brf',
'modelsearch/admin.brf','admincontrol/login.brf','adm/admloginuser.brf','admloginuser.brf','admin2.brf','admin2/login.brf','admin2/index.brf','usuarios/login.brf',
'adm/index.brf','adm.brf','affiliate.brf','adm_auth.brf','memberadmin.brf','administratorlogin.brf','cpanel','cpanel.php','cpanel.html',]
        
        if "http" in url:

            url = (url+"/")
            
        elif "https" in url:
            
            url = (url+"/")
        else:
            url = ('http://'+url+"/")
        
        for i in list_:
            r = requests.get(url+i)
            if r.status_code == 200:
                print(Fore.GREEN+"[+] "+url+i+" Found")
            else:
                print(Fore.RED+"[-] "+url+i+" Not Found")
        try:
            input(Fore.GREEN+" [*] Back To Menu (Press Enter...) ")
        except:
            print("")
            sys.exit()
    except:
        print("")

            

import socket
def cloudflare():
    print(""" [!] Welcome To The Cloudflare Bypasser Part

 [!] Please Enter The Target Website Address\n""")
    subdom = ['ftp', 'cpanel', 'webmail', 'localhost', 'local', 'mysql', 'forum', 'driect-connect', 'blog', 'vb', 'forums', 'home', 'direct', 'forums', 'mail', 'access', 'admin', 'administrator', 'email', 'downloads', 'ssh', 'owa', 'bbs', 'webmin', 'paralel', 'parallels', 'www0', 'www', 'www1', 'www2', 'www3', 'www4', 'www5', 'shop', 'api', 'blogs', 'test', 'mx1', 'cdn', 'mysql', 'mail1', 'secure', 'server', 'ns1', 'ns2', 'smtp', 'vpn', 'm', 'mail2', 'postal', 'support', 'web', 'dev']

    site = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"TOOLSINER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Bypass-CloudFlare"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")
    if site == "":
        try:
            print(Fore.RED+" [!] "+Fore.BLUE+"Please Enter Address :) \n")
            sleep(5)
            sys.exit()
        except:
            return
    for sub in subdom:
        try:
            hosts = str(sub) + "." + str(site)
            bypass = socket.gethostbyname(str(hosts))
            #print('Cloudflare Bypassed ! Real IP Address => '+bypass)
            print (" [!] CloudFlare Bypass " + str(bypass) + ' | ' + str(hosts))
        except Exception:
            pass
    try:
        input(Fore.GREEN+" [*] Back To Menu (Press Enter...) ")
    except:
        print("")
        sys.exit()

def Internet_Checker():
    req = requests.get("https://google.com/")
    status = req.status_code()
    if status == "200":
        print("\n   [!] Internet Active ")
    else:
        print("\n   [!] Internet Not Active")

# Def TV() For Iranian Members ! ! !
# You Can Change The TV Addresses And Custom ! ! !
try:
    def TV():
        print(Fore.GREEN+"\n   [1]"+Fore.BLUE+" - TV 1 ")    
        print(Fore.CYAN+"   **********************")
        sleep(0.1)

        print(Fore.GREEN+"\n   [2]"+Fore.BLUE+" - TV 2 ")
        print(Fore.CYAN+"   **********************") 
        sleep(0.1)

        print(Fore.GREEN+"\n   [3]"+Fore.BLUE+" - TV 3")    
        print(Fore.CYAN+"   **********************")  
        sleep(0.1)

        print(Fore.GREEN+"\n   [4]"+Fore.BLUE+" - TV 4 ")    
        print(Fore.CYAN+"   **********************")
        sleep(0.1)

        print(Fore.GREEN+"\n   [5]"+Fore.BLUE+" - TV 5 ")
        print(Fore.CYAN+"   **********************") 
        sleep(0.1)

        print(Fore.GREEN+"\n   [6]"+Fore.BLUE+" - TV 7")    
        print(Fore.CYAN+"   **********************")  
        sleep(0.1)
            
        print(Fore.GREEN+"\n   [7]"+Fore.BLUE+" - TV 9 ")    
        print(Fore.CYAN+"   **********************")
        sleep(0.1)

        print(Fore.GREEN+"\n   [8]"+Fore.BLUE+" - TV 12 ")
        print(Fore.CYAN+"   **********************") 
        sleep(0.1)

        print(Fore.GREEN+"\n   [9]"+Fore.BLUE+" - TV 14 ")    
        print(Fore.CYAN+"   **********************")  
        sleep(0.1)

        print(Fore.GREEN+"\n   [10]"+Fore.BLUE+" - TV 15 ")    
        print(Fore.CYAN+"   **********************")
        sleep(0.1)

        print(Fore.GREEN+"\n   [11]"+Fore.BLUE+" - TV 18 ")
        print(Fore.CYAN+"   **********************") 
        sleep(0.1)

        print(Fore.GREEN+"\n   [12]"+Fore.BLUE+" - Back To Menu")    
        print(Fore.CYAN+"   **********************")
        sleep(0.1)

        print(Fore.GREEN+"\n   [13]"+Fore.BLUE+" - Exit :) \n")  
            
        In = input(Fore.RED+" \n   ┌─["+Fore.LIGHTGREEN_EX+"TOOLSINER"+Fore.BLUE+"~"+Fore.WHITE+"Tools"+Fore.RED+"""]
    └──╼ """+Fore.WHITE+"卐 ").lower()
        
        if In == "1":
            webbrowser.open_new_tab("http://tv1.ir/")
        elif In == "2":
            webbrowser.open_new_tab("http://tv2.ir/")
        elif In == "3":
            webbrowser.open_new_tab("http://tv3.ir/")
        elif In == "4":
            webbrowser.open_new_tab("http://tv4.ir/")
        elif In == "5":
            webbrowser.open_new_tab("http://tv5.ir/")
        elif In == "6":
            webbrowser.open_new_tab("http://tv7.ir/")
        elif In == "7":
            webbrowser.open_new_tab("http://doctv.ir/")
        elif In == "8":
            webbrowser.open_new_tab("http://namayeshtv.ir/")
        elif In == "9":
            webbrowser.open_new_tab("https://fa.ifilmtv.ir/")
        elif In == "10":
            webbrowser.open_new_tab("http://tamashatv.ir/")
        elif In == "11":
            webbrowser.open_new_tab("http://pooyatv.ir/")
        elif In == "12":
            Run()
        elif In == "13":
            exit()
except:
    Run()


def Developer():
    try:
        os.system("cls")
    except:
        os.system("clear")
    sleep(0.15)
    Banner()
    sleep(0.4)
    print("\n")
    print(Fore.RED+"   ┌─["+Fore.LIGHTGREEN_EX+"TOOLSINER"+Fore.BLUE+"~"+Fore.WHITE+"@Programer"+Fore.RED+"""]
   └──╼ """+Fore.CYAN+"Mahyar Mahmoudy "+Fore.YELLOW+"卐 "+Fore.RESET)
    sleep(5.5)
    try:
        os.system("cls")
    except:
        os.system("clear")

# Code Bot Maker
Comment_Def = """def Botmaker():
    try:
        os.system("cls")
    except:
        os.system("clear")
    Bot = ""
    print("\n")
    bot_name = input("\tEnter Your Bot Name >>>  ")
    sure = input(Fore.LIGHTMAGENTA_EX+"\n\tAre You Sure To Make Bot (Yes or No) >>> "+Fore.LIGHTBLACK_EX)
    if sure.lower() == "yes" or "y" :
        print(Fore.LIGHTGREEN_EX+"\n [+] "+Fore.LIGHTYELLOW_EX+" Your Bot Was Created SuccessFully "+Fore.LIGHTGREEN_EX+" [+] "+Fore.RESET)
        print("\n [+]  For Run Your Bot Again Run The App  [+] ")
        Bot += "1"
        

    elif sure.lower() == "no" or "n" :
        print(Fore.GREEN+" [*] Back To Menu (Press Enter...) ")"""


# Code Online Game
def Online_Game():
    print(Fore.GREEN+"\n   [1]"+Fore.BLUE+" - 2048 Online")    
    print(Fore.CYAN+"   **********************")
    sleep(0.1)

    print(Fore.GREEN+"\n   [2]"+Fore.BLUE+" - Rubik Online")
    print(Fore.CYAN+"   **********************") 
    sleep(0.1)

    print(Fore.GREEN+"\n   [3]"+Fore.BLUE+" - Snake Online")    
    print(Fore.CYAN+"   **********************")  
    sleep(0.1)

    print(Fore.GREEN+"\n   [4]"+Fore.BLUE+" - Back To Menu")    
    print(Fore.CYAN+"   **********************")
    sleep(0.1)

    print(Fore.GREEN+"\n   [5]"+Fore.BLUE+" - Exit :) \n")  

    Input3 = input(Fore.RED+"   ┌─["+Fore.LIGHTGREEN_EX+"TOOLSINER"+Fore.BLUE+"~"+Fore.WHITE+"Tools"+Fore.RED+"""]
   └──╼ """+Fore.WHITE+"卐 ").lower()

    if Input3 == ("1"):
        url1 = "http://www.play2048.co/"
        webbrowser.open(url1)

    elif Input3 == ("2"):
        url2 = "https://rubikscu.be/play/"
        webbrowser.open(url2)

    elif Input3 == ("3"):
        url3 = "http://www.Slither.io"
        webbrowser.open(url3)
    
    elif Input3 == ("4"):
        Run()

    elif Input3 == ("5"):
        exit()



def Games():
    print(Fore.GREEN+"\n   [1]"+Fore.BLUE+" - Assassin's Creed (3)")    
    print(Fore.CYAN+"   **********************")
    sleep(0.1)

    print(Fore.GREEN+"\n   [2]"+Fore.BLUE+" - Forza Horizon (4)")
    print(Fore.CYAN+"   **********************") 
    sleep(0.1)

    print(Fore.GREEN+"\n   [3]"+Fore.BLUE+" - Gta San")    
    print(Fore.CYAN+"   **********************")  
    sleep(0.1)

    print(Fore.GREEN+"\n   [4]"+Fore.BLUE+" - Back To Menu")    
    print(Fore.CYAN+"    **********************")
    sleep(0.1)

    print(Fore.GREEN+"\n   [5]"+Fore.BLUE+" - Exit :) \n")  

    Input5 = input(Fore.RED+"   ┌─["+Fore.LIGHTGREEN_EX+"TOOLSINER"+Fore.BLUE+"~"+Fore.WHITE+"Tools"+Fore.RED+"""]
   └──╼ """+Fore.WHITE+"卐 ").lower()

    if Input5 == ("1"):
        url4 = (f"https://en.wikipedia.org/wiki/Assassin%27s_Creed_III")
        webbrowser.open(url4)

    elif Input5 == ("2"):
        url5 = (f"https://en.wikipedia.org/wiki/Forza_Horizon_4")
        webbrowser.open(url5)

    elif Input5 == ("3"):
        url6 = (f"https://en.wikipedia.org/wiki/Grand_Theft_Auto:_San_Andreas")
        webbrowser.open(url6)
    
    elif Input5 == ("4"):
        Run()

    elif Input5 == ("5"):
        exit()
        

def Business():
    print(Fore.GREEN+"\n   [1]"+Fore.BLUE+" - Amazon ")    
    print(Fore.CYAN+"   **********************")
    sleep(0.1)

    print(Fore.GREEN+"\n   [2]"+Fore.BLUE+" - eBay ")
    print(Fore.CYAN+"   **********************") 
    sleep(0.1)

    print(Fore.GREEN+"\n   [3]"+Fore.BLUE+" - AliBaba")    
    print(Fore.CYAN+"   **********************")  
    sleep(0.1)

    print(Fore.GREEN+"\n   [4]"+Fore.BLUE+" - Back To Menu")    
    print(Fore.CYAN+"   **********************")
    sleep(0.1)

    print(Fore.GREEN+"\n   [5]"+Fore.BLUE+" - Exit :) \n")  

    Input5 = input(Fore.RED+"   ┌─["+Fore.LIGHTGREEN_EX+"TOOLSINER"+Fore.BLUE+"~"+Fore.WHITE+"Tools"+Fore.RED+"""]
   └──╼ """+Fore.WHITE+"卐 ").lower()

    if Input5 == ("1"):
        url7 = (f"https://Amazon.com")
        webbrowser.open(url7)

    elif Input5 == ("2"):
        url8 = (f"https://eBay.com")
        webbrowser.open(url8)

    elif Input5 == ("3"):
        url9 = (f"https://www.alibaba.com/")
        webbrowser.open(url9)
    
    elif Input5 == ("4"):
        Run()

    elif Input5 == ("5"):
        exit()



# Code Internet
def Internet():
    try:
        os.system("cls")
    except:
        os.system("clear")
    Banner()
    sleep(0.1)
    
    print(Fore.GREEN+"\n   [1]"+Fore.BLUE+" - Show Tv")    
    print(Fore.CYAN+"   **********************") 
    sleep(0.1)

    print(Fore.GREEN+"\n   [2]"+Fore.BLUE+" - Admin Page Finder")
    print(Fore.CYAN+"   **********************") 
    sleep(0.1)

    print(Fore.GREEN+"\n   [3]"+Fore.BLUE+" - Robot's Scanner")    
    print(Fore.CYAN+"   **********************") 
    sleep(0.1)

    print(Fore.GREEN+"\n   [4]"+Fore.BLUE+" - By Pass Cloud Flare")    
    print(Fore.CYAN+"   **********************")  
    sleep(0.1)

    print(Fore.GREEN+"\n   [5]"+Fore.BLUE+" - Python Lib Installer")    
    print(Fore.CYAN+"   **********************")  
    sleep(0.1)

    print(Fore.GREEN+"\n   [6]"+Fore.BLUE+" - Back To Menu")    
    print(Fore.CYAN+"   **********************")
    sleep(0.1)

    print(Fore.GREEN+"\n   [7]"+Fore.BLUE+" - Exit :) \n")   

    Input4 = input(Fore.RED+"   ┌─["+Fore.LIGHTGREEN_EX+"TOOLSINER"+Fore.BLUE+"~"+Fore.WHITE+"@Internet"+Fore.RED+"""]
   └──╼ """+Fore.WHITE+"卐 ").lower()

    if Input4 == "1":
        TV()

    elif Input4 == "2":
        finder()

    elif Input4 == "3":
        robot()
    
    elif Input4 == "4":
        cloudflare()

    elif Input4 == "5":
        pyInstaller()

    elif Input4 == "6":
        Run()

    elif Input4 == "7":
        exit()



# Code Entertainmen
def Entertainment():
    print(Fore.GREEN+"\n   [1]"+Fore.BLUE+" - Online Game")    
    print(Fore.CYAN+"   **********************") 
    sleep(0.1)

    print(Fore.GREEN+"\n   [2]"+Fore.BLUE+" - Introducing Games")
    print(Fore.CYAN+"   **********************") 
    sleep(0.1)

    print(Fore.GREEN+"\n   [3]"+Fore.BLUE+" - Introducing Site Business")    
    print(Fore.CYAN+"   **********************")  
    sleep(0.1)

    print(Fore.GREEN+"\n   [4]"+Fore.BLUE+" - Back To Menu")    
    print(Fore.CYAN+"   **********************")
    sleep(0.1)

    print(Fore.GREEN+"\n   [5]"+Fore.BLUE+" - Exit :) \n")  

    Input = input(Fore.RED+"   ┌─["+Fore.LIGHTGREEN_EX+"TOOLSINER"+Fore.BLUE+"~"+Fore.WHITE+"@Entertainment"+Fore.RED+"""]
   └──╼ """+Fore.WHITE+"卐 ").lower()

    if Input == "1":
        Online_Game()

    elif Input == "2":
        Games()

    elif Input == "3":
        Business()

    elif Input == "4":
        Run()

    elif Input == "5":
        exit()
    



# Code Print The input's
# a1 = (Fore.LIGHTYELLOW_EX+" [1] "+Fore.RED+"Reverser"+Fore.RESET)
# a2 = (Fore.RED+" [2] "+Fore.RED+"Searcher"+Fore.RESET)
# a3 = (Fore.YELLOW+" [3] "+Fore.RED+"Web Browser"+Fore.RESET)
# a4 = (Fore.CYAN+" [3] "+Fore.RED+"Bot Maker"+Fore.RESET)
# a5 = (Fore.BLUE+" [4] "+Fore.RED+"Programer"+Fore.RESET)


# Code Run The Command's
def Run():
    try:
        os.system("cls")
    except:
        os.system("clear")
    while True:
        Banner()
        sleep(0.1)
        print(Fore.RED+"   ["+Fore.WHITE+"卐"+Fore.RED+"]"+Fore.CYAN+" Choose One Of The Options \n")
        sleep(0.1)
        print(Fore.LIGHTYELLOW_EX+"   [1] Entertainment\n")
        sleep(0.1)
        print(Fore.RED+"   [2] Internet Services\n") 
        sleep(0.1)
        print(Fore.YELLOW+"   [3] Developer :)\n")
        sleep(0.1)
        print(Fore.BLUE+"   [4] Exit . . .\n")

        Input = input(Fore.RED+"   ┌─["+Fore.LIGHTGREEN_EX+"TOOLSINER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"""]
   └──╼ """+Fore.WHITE+"卐 ").lower()\

        if Input == "1":
            Entertainment()

        elif Input == "2":
            Internet()

        elif Input == "3":
            Developer()

        elif Input == "4":
            exit()

        else:
            sound = pyttsx3.init()
            sound.setProperty('rate' , 130)
            sound.say(" Please Enter Number ")
            sound.runAndWait()

Run()

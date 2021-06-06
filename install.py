import sys
import os

def install():

        os.system("sudo apt update")
	os.system("sudo apt install python-pip")
        os.system("sudo apt install pip")
	os.system("sudo python -m pip install requests")
	os.system("pip install mechanize json whois python-whois requests bs4 requests[socks] urlparse cookielib") 
	os.system("pip install scapy datetime argparse re threading urllib2 modules builtwith smtplib")
	os.system("pip install whois")
	os.system("pip install builtwith")
	os.system("pip install colorama")
	os.system("pip install dnspython")
	os.system("pip install shodan")
	os.system("sudo apt install python-socks -y")
	os.system("sudo apt install nmap -y")
	os.system("sudo apt install php -y")
	os.system("sudo apt install perl -y")
	os.system("sudo apt install hashcat -y")
	os.system("sudo apt install nc")
	os.system("sudo apt install neofetch")
	os.system("sudo apt install cupp")
        os.system("sudo apt install php")
	os.system("cd /mnt/c")
	os.system("cd /mnt/c && git clone https://github.com/suljot/shellphish")
	os.system("cd /mnt/c && git clone https://github.com/tartley/colorama")
	os.system("python /mnt/c/colorama/setup.py install")
	os.system("cd /mnt/c && git clone https://github.com/Tuhinshubhra/RED_HAWK")
	os.system("cd /mnt/c && git clone https://github.com/derv82/wifite2")
	os.system("python /mnc/c/wifite2/setup.py install")
	os.system("cd /mnt/c && git clone https://github.com/XFORWORKS/TrackingScripts")
	os.system("cd /mnt/c && git clone https://github.com/Mebus/cupp")
        os.system("cd /mnt/c && git clone https://github.com/arismelachroinos/lscript")
        os.system("cd /mnt/c && git clone https://github.com/trustedsec/social-engineer-toolkit")
	os.system("apt install metasploit-framework -y")
	os.system("apt install wifite -y")
	os.system("apt install reaver -y")
	os.system("apt install aircrack-ng -y")
	os.system("cd /mnt/c/social-engineer-toolkit && pip install -r requirements.txt")
	os.system("python /mnt/c/social-engineer-toolkit/setup.py install")

                                                                                                         

print "Are you running on the real Kali Linux OS? [y/n]"
check = raw_input("[y/n]> ")
if check == "y" :
	print "Ok most tools should work for you"
	print "(WARNING) Dont delete anything with the name ShellPhsih , Colorama , RED_HAWK , wifite2 , TrackingScripts , cupp , lscript or social-engineer-toolkit"
	print "Because if u do so the script wont work..."
	os.system("sleep 2")
	install()

if check == "n" :
	print "Then some of the tools in this script might not work"
	print "(WARNING) Dont delete anything with the name ShellPhsih , Colorama , RED_HAWK , wifite2 , TrackingScripts , cupp , lscript or social-engineer-toolkit"
	print "Because if u do so the script wont work..."
	print "Do you want to continue installation  [y/n]"
	install = raw_input("[y/n]> ")
	if install == "y" :
                def install():
                        os.system("sudo apt update")
                        os.system("sudo apt install pip")
			os.system("pip install mechanize json whois python-whois requests bs4 requests[socks] urlparse cookielib") 
			os.system("pip install scapy datetime argparse re threading urllib2 modules builtwith smtplib")
			os.system("pip install whois")
			os.system("pip install builtwith")
			os.system("sudo apt install python-socks -y")
			os.system("sudo apt install nmap -y")
			os.system("sudo apt install php -y")
			os.system("sudo apt install perl -y")
			os.system("sudo apt install hashcat")
			os.system("sudo apt install nc")
			os.system("sudo apt install neofetch")
			os.system("sudo apt install cupp")
			os.system("cd /mnt/c")
                        os.system("cd /mnt/c && git clone https://github.com/thelinuxchoice/shellphish")
                        os.system("cd /mnt/c && git clone https://github.com/Tuhinshubhra/RED_HAWK")
		        os.system("cd /mnt/c && git clone https://github.com/derv82/wifite2")
	                os.system("python /mnc/c/wifite2/setup.py install")
                        os.system("cd /mnt/c && git clone https://github.com/XFORWORKS/TrackingScripts")
                        os.system("cd /mnt/c && git clone https://github.com/Mebus/cupp")
                        os.system("cd /mnt/c && git clone https://github.com/arismelachroinos/lscript")
                        print "\n"
			print "Entering big download, if your not ready press CTRL C"
			i = raw_input("press ctrl c to stop hit enter to continue")
			os.system("sudo apt install metasploit-framework -y")
			os.system("cd /mnt/c && git clone https://github.com/trustedsec/social-engineer-toolkit")
			os.system("sudo apt install wifite -y")
			os.system("sudo apt install reaver -y")
			os.system("sudo apt install aircrack-ng -y")
			print "You ready for one more big download? If not press CTRL C"
			i = raw_input("Press CTRL C to stop, hit ENTER to continue")
			os.system("cd /mnt/c/social-engineer-toolkit && pip install -r requirements.txt")
			os.system("python /mnt/c/social-engineer-toolkit/setup.py install")
                        
print "Ok you are good to go, to start the script type (bash dedsec.sh)"


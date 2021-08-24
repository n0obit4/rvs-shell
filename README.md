<h1 align="center">
  <br>
  <a href="https://github.com/n0obit4/rvs-shell"><img src="https://raw.githubusercontent.com/n0obit4/rvs-shell/master/Logo.png" alt="RVS-SHELL Logo" border="0" width="180"></a>
  <br>
  RVS-SHELL
  <br>
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Release-v1.0-blue.svg">
  <img src="https://img.shields.io/badge/License-GPL3-brightgreen.svg">
  <img src="https://img.shields.io/badge/Tested on-Linux & Windows-yellow.svg">
</p>

## RVS-SHELL

Reverse shell maker is a Reverse Shell Cheat Sheet customizable in a simpler and more intuitive way, this is used in a CTF challenges or whatever, i wrote this for EDUCATIONAL PURPOSE only. This automatize the process to create reverse shell in a compromised system, if you dont know or doesn't have a credentials of the machinne you can call to reverse shell.

## Requeriments

You need [pip3](https://help.dreamhost.com/hc/es/articles/115000699011-Usar-pip3-para-instalar-m%C3%B3dulos-de-Python3) to install this packages.

  - argparse
  - os
  - colorama
  
## Help Menu

```bash

$ python3 rvs-shell.py --help
usage: rvs-shell.py [-h] [--php] [--python] [--netcat] [--nc] [--perl]
                    [--bash] [--java] -H HOST -p PORT

Programs to make reverse shells ψ(｀∇´)ψ

optional arguments:
  -h, --help            show this help message and exit
  --php                 php reverse shell
  --python              python reverse shell
  --netcat              netcat reverse shell
  --nc                  netcat short reverse shell
  --perl                perl reverse shell
  --bash                bash reverse shell
  --java                Java reverse shell
  -H HOST, --host HOST  Host a escucha
  -p PORT, --port PORT  Puerto a escucha

python3 rvs-shell.py --php -H 127.0.0.1 -p 4444
```

## Demostration

![Program demostration](https://raw.githubusercontent.com/n0obit4/rvs-shell/master/Demostration.png)

This is the result. A netcat reverse shell, this command is placed on a Linux system to call the reverse shell.

## Source

[Pentest Monkey](http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet)

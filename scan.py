#!/usr/bin/python

#Library
import os
import subprocess
import socket

# Clear Screen
subprocess.call('clear', shell=True)



print('Scannig Network for Devices')
print(' ')

# Get Subnet IP
IP = (([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("1.1.1.1", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0]
IP_arr = IP.split('.')
IP_arr[-1] = "1"
Subnet = ".".join(IP_arr) + "/24"

# Start Network Scan
print('Scannig Network for Devices')
print(' ')
os.system("sudo nmap -sP " + Subnet + """ | awk '/Nmap scan report for/{printf $5;}/MAC Address:/{print " => "$3;}' | sort >> ips_macs_test.txt""")

print('Scan complete! ~~ Output in ips_macs_py.txt')
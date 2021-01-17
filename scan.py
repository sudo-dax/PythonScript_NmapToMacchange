#!/usr/bin/python

#Library
import os
import subprocess
import socket

# Clear Screen
subprocess.call('clear', shell=True)



print('Scannig Network for Devices')
print(' ')

# Get Subnet
adapter = subnet.get_adapter_names()[-1]
Subnet = subnet.get_subnets(adapter)[0]

# Start Network Scan
print('Scannig Network for Devices')
print(' ')
os.system("sudo nmap -sP " + Subnet + """ | awk '/Nmap scan report for/{printf $5;}/MAC Address:/{print " => "$3;}' | sort >> ips_macs_py.txt""")

print('Scan complete! ~~ Output in ips_macs_py.txt')

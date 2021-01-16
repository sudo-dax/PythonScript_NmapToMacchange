#!/usr/bin/python

#Library
import os
import subprocess

# Clear Screen
subprocess.call('clear', shell=True)

print('Scannig Network for Devices')
print(' ')

os.system("""sudo nmap -sP 10.1.1.1/20 | awk '/Nmap scan report for/{printf $5;}/MAC Address:/{print " => "$3;}' | sort >> ips_macs_py.txt""")

print('Scan complete! ~~ Output in ips_macs_py.txt')
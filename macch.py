#!/usr/bin/python

#Library
import os
import subprocess
import collections
import socket

import subnet

# Clear Screen
subprocess.call('clear', shell=True)

# Get Subnet
adapter = subnet.get_adapter_names()[-1]
Subnet = subnet.get_subnets(adapter)[0]

# Start Network Scan
print('Scannig Network for Devices')
print(' ')
os.system("sudo nmap -sP " + Subnet + """ | awk '/Nmap scan report for/{printf $5;}/MAC Address:/{print " => "$3;}' | sort >> ips_macs_py.txt""")
print('Scan complete! ~~ Output in ips_macs_py.txt')

# Counting Number of connections per Device so far
data = open("ips_macs_py.txt","r")

c = collections.Counter()

for line in data:
	if ' => ' not in line:
		continue
	line = line.strip()
	ip, mac = line.split(' => ')
	c[mac] += 1


# Changing MAC Address 
mac_ad = c.most_common()[-1][0]
# print(mac_ad)
print(f"Chainging MAC to -1 Common on Network {mac_ad}")

print("Bringing down WiFi Adapter")
os.system(f"sudo ip link set {adapter} down")

print("Bringing down Network Manager")
os.system("sudo systemctl stop NetworkManager")
os.system("sudo systemctl disable NetworkManager")

print("Changing MAC")
os.system(f"sudo macchanger -m {mac_ad} {adapter}")

print("Bringing up Network Manager")
os.system("sudo systemctl enable NetworkManager")
os.system("sudo systemctl start NetworkManager")

print("Bringing down WiFi Adapter")
os.system(f"sudo ip link set {adapter} up")
print("Mac Change Complete!")

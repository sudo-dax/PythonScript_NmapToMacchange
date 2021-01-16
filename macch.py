#!/usr/bin/python

#Library
import os
import subprocess
import collections
import socket

# Clear Screen
subprocess.call('clear', shell=True)

# Get Subnet IP
IP = (([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0]
IP_arr = IP.split('.')
IP_arr[-1] = "1"
Subnet = ".".join(IP_arr) + "/24"

# Start Network Scan
print('Scannig Network for Devices')
print(' ')
os.system("sudo nmap -sP " + Subnet + """ | awk '/Nmap scan report for/{printf $5;}/MAC Address:/{print " => "$3;}' | sort >> ips_macs_test.txt""")
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
os.system("sudo ip link set wlan0 down")

print("Bringing down Network Manager")
os.system("sudo systemctl stop NetworkManager")
os.system("sudo systemctl disable NetworkManager")

print("Changing MAC")
os.system(f"sudo macchanger -m {mac_ad} wlan0")

print("Bringing up Network Manager")
os.system("sudo systemctl enable NetworkManager")
os.system("sudo systemctl start NetworkManager")

print("Bringing down WiFi Adapter")
os.system("sudo ip link set wlan0 up")
print("Mac Change Complete!")
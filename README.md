# Network Ninja

### A script to quickly scan and hide on a wifi network as a previously connected device.
### Aim: to avoid having to input personal data to connect to a network which uses MAC filtering.

## Required
- Nmap
- Macchanger
- Python

The macch.py script will work as follows:
1. It will scan the network and output the scanned device's MAC addresses and ouput results to a text file. (.txt)
- Note: (Can separately just scan network to get more comprehensive data without changing MAC Address using scan.py)

2. It will then count the number of times each MAC appears in the text file.

3. It will then bring down the WiFi Adapter & NetworkManger

4. It will then select least common MAC on network and change to that MAC using Macchanger.

5. It will bring up network device and manager.

You now appear to be a previously connected device other than your own. 

### Still Needed In Future
- Select MACs with different adapter names automatically (Other than wlan0)
- User input to select which mac to use 

I welcome any comments or suggestions. 
Enjoy.
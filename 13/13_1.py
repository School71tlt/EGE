from ipaddress import *
from math import *
for ip in ip_network('172.118.0.0/255.255.252.0'):
    if bin(int(ip))[2:].count('1'):
        pass
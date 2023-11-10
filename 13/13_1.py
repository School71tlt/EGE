from ipaddress import *
from math import *


def is_prime(numb):
    cnt = 0
    for i in range(1, numb + 1):
        if numb % i == 0:
            cnt += 1
    return True if cnt <= 2 else False


cnt = 0
for ip in ip_network('172.118.0.0/255.255.252.0'):
    bin_ip = f'{int(ip):b}'
    print(ip)
    if is_prime(bin_ip.count('1')):
        cnt += 1
        print('True')
    else:
        print('False')

print(cnt)
'''
    Программа выводит 301, однако в условии задачи написано, что 
    два адреса (адрес сети и широко-вещательный) не используют.
    Адрес сети это ip, у которого адрес компьютера равен 0 (172.118.0.0 в нашем случае).
    Широко-вещательный это ip, у которого адрес компьютера забит 1-ми (172.118.3.255).
    Мы должны посмотреть эти 2 адреса и вычесть из результата те, у которых выдало True
    В нашем случае это только 172.118.3.255.
    Ответ: 301-1 = 300
'''
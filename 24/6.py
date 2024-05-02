with open('6.txt', 'r') as f:
    s = f.readline().replace('B', 'A').replace('C', 'A').replace('9', '8')
while 'AA' in s:
    s = s.replace('AA', 'A!A')
while '88' in s:
    s = s.replace('88', '8!8')
print(max(map(len, s.split('!'))))

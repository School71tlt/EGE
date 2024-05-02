alph = '0123456789ABCDEFG'
for x in alph:
    a = int(f'7AC{x}53D', 17) + int(f'83BG94{x}D', 17) + int(f'C5{x}D', 17) + int(f'C4BBF{x}4', 17) + int(f'7{x}79', 17)
    if a % 16 == 0:
        print(x, a / 16)


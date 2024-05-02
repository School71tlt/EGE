s = open('3.txt').readline()
for x in 'ABCD':
    for y in 'ABCD':
        for z in 'ABCD':
            while x + y + z in s:
                s = s.replace(x + y + z, x + y + '!' + y + z)
print(max(len(c) for c in s.split('!')))

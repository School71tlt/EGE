s = open('4.txt').readline()
for x in 'ABC':
    for y in 'ABC':
        while x + y in s:
            s = s.replace(x + y, x + '!' + y)
print(max(len(c) for c in s.split('!')))

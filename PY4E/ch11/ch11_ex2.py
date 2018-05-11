import re
fname = input('Enter file name: ')

if len(fname) < 1 : fname = 'mbox-short.txt'
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

count = 0
tot = 0.0
for line in fhand:
    line = line.rstrip()
    x = re.findall('^New Revision: ([0-9]+)', line)
    if len(x) > 0:
        # print(x)
        for num in x:
           count = count + 1
           value = float(num)
           tot = tot + value
avg = round(tot/count, 7)
print(avg)

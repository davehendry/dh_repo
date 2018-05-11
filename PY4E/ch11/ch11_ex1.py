import re
fname = input('Enter file name: ')

if len(fname) < 1 : fname = 'mbox-short.txt'
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

rexp = input('Enter a regular expression: ')
# l = list()
d = dict()
for line in fhand:
    line = line.rstrip()
    x = re.findall(rexp, line)
    if len(x) > 0:
        # print(x)
        for match in x:
            d[match] = d.get(match,0) + 1

e = list()
for k, v in d.items():
    e.append((k,v))
e = sorted(e)    

for k, v in e:
    print(k, v)


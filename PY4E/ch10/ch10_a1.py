fname = input('Enter file name: ')
# if len(fname) < 1 : fname = 'mbox-short.txt'
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

l = list()
d = dict()
for line in fhand:
    line = line.rstrip()
    if len(line)<3 or not line.startswith('From '): continue
    words = line.split()
    dstamp = words[5]
    dstamp_lst = dstamp.split(':')
    l.append(dstamp_lst[0])

for hour in l:
    d[hour] = d.get(hour,0) + 1
e = list()
for k, v in d.items():
    e.append((k,v))
e = sorted(e)    

for k, v in e:
    print(k, v)

# can also write line 21 - 28 using the following. read up on list comprehension
# c = {'a':10, 'b':1, 'c':22}
# print(sorted([(v,k) for k,v in c.items()]))
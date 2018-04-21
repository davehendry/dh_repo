fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'mbox-short.txt'
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
    # print(words[1])
    l.append(words[1])
for email in l:
    d[email] = d.get(email,0) + 1
# print(d)
# Sort the dictionary by value
e = list()
for k, v in d.items():
    e.append((v,k))
e.sort(reverse=True)

for v, k in e[:1]:
    print(k, v)
# largestcount = -1
# largestemail = None

# for k,v in d.items():
#     # print(k,v)
#     if v > largestcount:
#         largestcount = v
#         largestemail = k
# print(largestemail, largestcount)
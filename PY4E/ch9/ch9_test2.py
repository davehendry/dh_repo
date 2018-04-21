fname = input('Enter file name: ')

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
    l.append(words[1])
for email in l:
    d[email] = d.get(email,0) + 1


largestcount = -1
largestemail = None

for k,v in d.items():
    
    if v > largestcount:
        largestcount = v
        largestemail = k
print(largestemail, largestcount)
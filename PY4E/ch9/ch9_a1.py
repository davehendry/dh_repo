# 9.4 Write a program to read through the mbox-short.txt 
# and figure out who has the sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of 
# those lines as the person who sent the mail. The program creates 
# a Python dictionary that maps the sender's mail address to a count 
# of the number of times they appear in the file. After the dictionary 
# is produced, the program reads through the dictionary using a maximum 
# loop to find the most prolific committer.

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
    # print(words[1])
    l.append(words[1])
for email in l:
    d[email] = d.get(email,0) + 1
# print(d)

largestcount = -1
largestemail = None

for k,v in d.items():
    # print(k,v)
    if v > largestcount:
        largestcount = v
        largestemail = k
print(largestemail, largestcount)
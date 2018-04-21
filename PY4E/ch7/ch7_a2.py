fname = input('Enter the file name: ')

try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

count = 0
tot = 0
for line in fhand:
    ly = line.rstrip()
    if ly.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        pos = ly.find(':')
        # print(pos)
        conf = ly[pos+1:]
        # print(piece)
        value = float(conf)
        tot = tot + value
        avg = round(tot/count, 12)
print('Average spam confidence:', avg)
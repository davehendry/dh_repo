fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

inp = fhand.read()
ly = inp.rstrip()
print(ly.upper())
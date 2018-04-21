# Write a program that reads the words in words.txt and stores them as keys in a dictionary. 
# It doesn't matter what the values are. 
# Then you can use the in operator as a fast way to check whether a string is in the dictionary.

# fname = input("Enter file name: ")
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened:', fname)
#     exit()

fhand = open('words.txt')
count = 0
# klst = list()
# vlst = list()
wrdmap = dict()
for line in fhand:
    line = line.rstrip()
    if len(line)<1: continue 
    words = line.split()
    
    for i in range(len(words)):
        count = count + 1
        wrdmap[words[i]] = count
        
    #     vlst.append(i)
    # klst.extend(words) 
# print(klst)
# print(vlst)
       
print(wrdmap)
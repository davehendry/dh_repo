# Open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words using the split() method. 
# The program should build a list of words. 
# For each word on each line check to see if the word is already in the list and if not append it to the list.
#  When the program completes, sort and print the resulting words in alphabetical order. 

# output
# ['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 
# 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 
# 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']

fname = input("Enter file name: ")
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

lst = list()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for i in range(len(words)):
        if words[i] in lst: continue
        lst.append(words[i])
lst.sort()
print (lst)




# if word in lst then skip/continue
#    if len(words) == 0 : continue
#     if words[0] != 'From' : continue
#     print(words[2]) 




# In this assignment you will read through and parse a file with text and numbers. 
# You will extract all the numbers in the file and compute the sum of the numbers. 

# import re
# fhand = open('regex_sum_70853.txt')

# lst = []
# for line in fhand:
#     line = line.rstrip()
#     x = re.findall('[0-9]+', line)
#     if len(x) > 0:
#         lst.extend(x)
# count = 0
# tot = 0  
# # print(lst)
# for num in lst:
#     count = count + 1
#     tot = tot + int(num)
# print('sum =', tot, 'count =', count)


import re
fhand = open('regex_sum_70853.txt')

lst = []
for line in fhand:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    if len(x) > 0:
        lst.extend(x)

tot = 0  
for num in lst:
    tot = tot + int(num)
print('sum =', tot)
print(type(tot))
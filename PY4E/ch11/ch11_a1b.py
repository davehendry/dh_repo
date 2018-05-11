# There are a number of different ways to approach this problem. 
# While we don't recommend trying to write the most compact code 
# possible, it can sometimes be a fun exercise. 
# Here is a a redacted version of two-line version of this program 
# using list comprehension: 

# Python 3:
# import re
# print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )
# 
# Please don't waste a lot of time trying to figure 
# out the shortest solution until you have 
# completed the homework. List comprehension 
# is mentioned in Chapter 10 and the read() method is 
# covered in Chapter 7. 

# List Comprehension
import re
print( sum( [ int(i) for i in re.findall('[0-9]+', open('regex_sum_70853.txt').read()) ] ) )

# Long form
# import re
# fhand = open('regex_sum_70853.txt')

# lst = []
# for line in fhand:
#     line = line.rstrip()
#     x = re.findall('[0-9]+', line)
#     if len(x) > 0:
#         lst.extend(x)

# tot = 0  
# for num in lst:
#     tot = tot + int(num)
# print('sum =', tot)


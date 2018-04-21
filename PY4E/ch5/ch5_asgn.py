# Write a program that repeatedly prompts a user for integer 
# numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and 
# smallest of the numbers. If the user enters anything other
# than a valid number catch it with a try/except and put 
# out an appropriate message and ignore the number. 
# Enter 7, 2, bob, 10, and 4 and match the output below. 

largest = None
smallest = None
#print('Before:', largest)
while True :
    num = input('Enter an integer: ')
    if num == 'done' :
        break
    try:    
        ival = int(num) 
        if largest is None or ival > largest :
            largest = ival
        if smallest is None or ival < smallest :
            smallest = ival        
        #print('Loop:', ival, largest, smallest)
    except:
        print('Invalid input')
        continue
    
print("Maximum is",largest)
print('Minimum is',smallest)
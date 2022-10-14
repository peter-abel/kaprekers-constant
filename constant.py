
'''Kaprekar constant, or 6174, is a constant that arises when we take a 4-digit integer,
 form the largest and smallest numbers from its digits, and then subtract these two numbers.
 Continuing with this process of forming and subtracting, 
 we will always arrive at the number 6174. The only condition is that atleast two digits in the number  be different'''




#Our four digit integer range
nums = range(1000,9999)

#creating an empty list
mylist = []
#function to generate the numbers.
def generating_numbers():
    for i in range(1000,9999) :
        mylist.append(i)
    #The condition that requires atleast two numbers in the integer to be different
    for i in mylist:
      if i == 1111 or i == 2222 or i== 3333 or i == 4444 or i == 5555 or i == 6666 or i == 7777 or i == 8888 or i == 9999:
         mylist.remove(i)
    return mylist



#function to reorganize number to descending order eg. (5273->7532)
def largest_number(num):
    num = str(num)
    ordered = ''.join(sorted(num, reverse=True))
    return int(ordered)



#function to reorganize number to ascending order eg.(5273->2357)
def small_number(num):
    num = str(num)
    ordered = ''.join(sorted(num, reverse=True))

    return int(ordered[::-1])


#function to subtract return vals of above functions.
def subtract(i):
    generating_numbers()
    new_num = largest_number(mylist[i]) - small_number(mylist[i])
    count = 1
    while new_num != 6174:
        count +=1
        new_num = largest_number(new_num) - small_number(new_num)

    print("No. of iterations taken:" ,count)    
    return new_num
        
'''The range can be adjusted to check all other numbers in the list'''
for i in range (1,10):
    print('Kaprekars number:',subtract(i))

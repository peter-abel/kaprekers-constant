import random


#Kaprekars constant 6174


nums = range(1000,9999)
#function to generate the numbers.
def generating_numbers():
    mylist = []
    for i in nums :
        mylist.append(i)
    return mylist   
#print (len(nums))
print(generating_numbers())
#funtion to meet conditions.





#function to reorganize number to descending order
def largest_number(num):
    num = str(num)
    ordered = ''.join(sorted(num, reverse=True))
    return int(ordered)



#function to reorganize number to ascending order
def small_number(num):
    num = str(num)
    ordered = ''.join(sorted(num, reverse=True))

    return int(ordered[::-1])





#function to subtract return vals of above functs.

def subtract():
    new_num = largest_number()- small_number()
    return new_num

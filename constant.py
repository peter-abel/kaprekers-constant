
#Kaprekars constant 6174


#import random


nums = range(1000,9999)
mylist = []
#function to generate the numbers.
def generating_numbers():
    for i in range(1000,9999) :
        mylist.append(i)

    for i in mylist:
      if i == 1111 or i == 2222 or i== 3333 or i == 4444 or i == 5555 or i == 6666 or i == 7777 or i == 8888 or i == 9999:
         mylist.remove(i)
    return mylist

print(len(generating_numbers()))



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
    generating_numbers()
    new_num = largest_number(mylist[2]) - small_number(mylist[2])
    while new_num != 6174:
        new_num = largest_number(new_num) - small_number(new_num)
        
    return new_num

print(subtract())
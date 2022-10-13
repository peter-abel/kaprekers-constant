
#Kaprekars constant 6174


nums = range(1000,9999)
mylist = []
#function to generate the numbers.
def generating_numbers():
    for i in range(1000,9999) :
        mylist.append(i)
    #return mylist   
#print (len(mylist))
#print(len(generating_numbers()))
#funtion to meet conditions.
#def con():
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
    new_num = largest_number()- small_number()
    return new_num

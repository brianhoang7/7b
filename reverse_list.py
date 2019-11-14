# Author: Brian Hoang
# Date: 11/13/2019
# Description: This function takes a list as a parameter and modifies it to be its reverse.

#takes in list as parameter
def reverse_list(mylist):
    #to tally through the list length
    tally = 0
    #-1 from the length of mylist to count from the last object in the list
    reverse_count = len(mylist)-1
    #new list to modify original mylist
    new_list = mylist[:]
    #for loop to replace each object in mylist with its reverse counterpart
    for tally in range(len(mylist)):
        mylist[tally] = new_list[reverse_count]
        #tallies +1 until it reaches length of mylist
        tally += 1
        reverse_count -= 1



#num_list = [7,-3,12,9]
#reverse_list(num_list)
#print(num_list)
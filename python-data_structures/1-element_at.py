#!/usr/bin/python3
#This code retrieves an element from a list.
def element_at(my_list, idx):
    for element in range(1, 6):
   if idx <= -1 or idx > 6:
       return None
   else:
       return (my_list[idx])
    

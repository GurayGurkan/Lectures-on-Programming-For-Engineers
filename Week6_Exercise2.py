# -*- coding: utf-8 -*-
"""
@author: Guray
"""
number_list = [14,124,7,187,34,10,13,133,99,89,21]

# Using Endless Loop:

i = 0
while True:

    
    if number_list[i] % 2 == 1:
        print "%s. element %s is odd." % (i + 1,number_list[i] )
    
    i = i + 1
    
"""    
# Using Finite Loop:
i = 0
while i <len(number_list):
    
    if number_list[i] % 2 == 1:
        print "%s. element %s is odd." % (i + 1,number_list[i] )
    
    i = i + 1



# Using For loop:

count = 1
for item in number_list:
    if item % 2  == 1:
        print "%s. element %s is odd." % (count,item) 
    
    count = count + 1

"""


















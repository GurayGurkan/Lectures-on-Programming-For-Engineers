# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 14:26:06 2017

@author: Guray
"""


# Duty 2

def duty2(start,stop, step):
	mylist = []
	a = start
	while a < stop + step:
		mylist.append(a)
		a += 1
	return mylist



# Duty 6
floors = ['Blue', 'Red', 'Green' ,'Yellow']
sections = ['A','B']
numbers = range(1,6)

park_names = []

for item1 in floors:
    names =[]
    for item2 in sections:
        for item3 in numbers:
            text = item1 + ' ' + item2 + ':' + str(item3)
            names.append(text)
    park_names.append(names)
    
    
            
    












# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 22:25:08 2017

@author: Guray
"""

floors = ['Z','1','2','3','4','5']

halls = ['A','B','C','D']

rooms = range(1,6)

i = 0
for floor in floors:
    #print " I am in", floor
    for hall in halls:
        #print floor + hall
        for room in rooms:
            print floor + hall + '-' + str(room)
            i = i + 1
        
    
    


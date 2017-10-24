# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 09:35:20 2017

@author: Guray
"""

# Solution of HW2a

mylist = range(1400,2201)
mynumbers = []
N = len(mylist)

i = 0
c = 1

while i<N:
    current = mylist[i]
    if current % 3 == 0 and current % 5 == 0:
       mynumbers.append(current)
       print "%s. number is %s" % (c,current)
       c = c + 1 
    i = i + 1 
       

print "This is the end..."



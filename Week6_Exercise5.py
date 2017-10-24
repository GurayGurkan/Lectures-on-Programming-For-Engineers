# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 11:55:31 2017

@author: Guray
"""

numbers = range(1,51)

for item in numbers:
    if (item % 3 == 0) and (item % 5 ==0):
        print "Multiple of both" % item
     elif item % 3 == 0:
        print "Multiple of 3"
    elif item % 5 == 0:
        print "Multiple of 5"
    else:
        print item
    
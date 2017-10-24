# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 12:30:45 2017

@author: Guray
"""

orig = [3,4,6,4,9,5,3,9,5,6,7]
uniques =[]

for i in orig:
    print i
    if i in uniques:
        print "Not accepted"
        continue
    else:
        print "Accepted"
        uniques.append(i)
    
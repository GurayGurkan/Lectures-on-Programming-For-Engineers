# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 12:21:16 2017

@author: Guray
"""

n = 49
# smallest divider

for i in range(2,n+1):
    if (n % i) == 0:
        print "the smallest divider of %s is %s" % (n,i)
        break
    else:
        print "The number %s is not dividable by %s" % (n,i)
    
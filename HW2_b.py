# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 10:19:52 2017

@author: Guray
"""

n = '20C'

# we should first determine units

units = n[-1]
degree = int(n[:-1])

if units.upper()=='C':
    output_degree = 9*degree/5. + 32
    print "%s degrees %s is %s degrees F" % (degree,units,output_degree)
elif units.upper()=='F':
    output_degree = 5*(degree - 32) / 9.
    print "%s degrees %s is %s degrees C" % (degree,units,output_degree)
else:
    print "Be careful about the unit!"
    
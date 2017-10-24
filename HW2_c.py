# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 11:13:28 2017

@author: Guray
"""

myscore = 40

if myscore > 80:
    letter = 'A'
elif myscore > 59:
    letter = 'B'
elif myscore > 39:
    letter = 'C'
else:
    letter = 'D'

print "Your score %s corresponds to letter %s   " % (myscore,letter)

    
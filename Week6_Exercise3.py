# -*- coding: utf-8 -*-
"""
@author: Guray
"""
number_list = [14,124,7,187,34,10,13,133,99,89,21]
"""
# Using Endless While Loop:

k = 0
odds = 1
while True:
    if k == len(number_list):
        break
    if number_list[k] % 2 == 1:
        print "%s. odd number is %s with order %s." % (odds,number_list[k], k+1)
        odds = odds + 1    
    k = k + 1
""" 
 
# Using Finite While Loop:


k = 0
odds = 1
while k <len(number_list):
    if number_list[k] % 2 == 1:
        print "%s. odd number is %s with order %s." % (odds,number_list[k], k+1)
        odds = odds + 1    
    k = k + 1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   


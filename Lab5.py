# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 21:15:23 2017

@author: Guray
"""

def duty1():
    
    numbers =[]
    while True:
        a = input('Enter new number, 0 to end: ')
        if a==0:
            break
        numbers.append(a)

    sums = 0.        
    for i in numbers:
        sums = sums + i
    
    average = sums / len(numbers)
    print "The average of %s is %.2f" % (numbers,average)
        
        
def duty2():
    
    numbers =[]
    while True:
        a = input('Enter new number, 0 to end: ')
        if a==0:
            break
        numbers.append(a)
    
    if len(numbers)>0:

        sums = 0.        
        for i in numbers:
            sums = sums + i
        
        average = sums / len(numbers)
        print "The average of %s is %.2f" % (numbers,average)
    else:
        print "Nothing to calculate, exiting..."
    

def duty3(mylist):
    if isinstance(mylist,list):
        i = 0
        N = len(mylist)
        largest = mylist[0]
        while i != N:
            if mylist[i] > largest:
                largest = mylist[i]
            i = i + 1
        return largest
       
    else:
        print "Input should be a list!..."
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    


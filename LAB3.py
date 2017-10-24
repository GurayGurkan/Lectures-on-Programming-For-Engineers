# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 20:52:47 2017

@author: Guray
"""

list1 = range(12,801)
list2 = []
N = len(list1)
i = 0
while i<N:
    num = list1[i]
    if num % 10 == 4 and num % 3 == 0:
        list2.append(num)        
    i +=1
print "The final list has %s number of elements" % len(list2)
    
list3 = []

for i in list1:
    if i % 10 == 4 and i % 3 == 0:
        list3.append(num)
print "The final list has %s number of elements" % len(list3)

##---------------

text = "All electronic components have information documents that are called datasheets"

n1,n2,n3 = 0,0,0

for i in text:
    if i == 'a':
        n1+=1
    elif i =='e':
        n2+=1
    elif i == 'i':
        n3+=1
print "The number of a's is %s, e's is %s and i's is %s" % (n1,n2,n3)

## ------------------------------------------
n_o = 0
index = 0 
for i in text:
    if i == 'o':
        n_o +=1
        if n_o == 4:
            break
    index +=1
print "Sliced part is '%s'." % text[index:index+5]
    

        
    


    
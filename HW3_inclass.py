# -*- coding: utf-8 -*-
"""
Created on Tue Oct 03 22:17:26 2017

@author: Guray
"""

# EE5203 Homework 3
"""
# Question 1

password = '142517'


for i in range(3):
    a = raw_input("Enter the password: ")
    if a==password:
        print "Well done..."
        break
    if i == 2:
        print "Goodbye"
        break
   
    print "Number of attempts left is %s" % (2-i)
   """ 
    


"""
attempts = 0
while attempts<3:
    a = raw_input("Enter the password: ")
    if a==password:
        print "Welcome to system..."
        letmein = True
        break
 
    attempts = attempts + 1
    if attempts==3:
        print "Number of wrong attempts exceeded, goodbye!"
        letmein= False
        break
    print "Number of attempts left is %s" % (3-attempts)
 """ 
#Question 2:
 
dna = 'CTAGAGGACCATGGACGAGATTGGCACACGAACCACGTCGCACGGCAACCAGCACGTACGGATAGACGTCAAG'
target = 'ACG'
N = len(dna)
i = 0
an = 0 # number of targets
index_list = []
while i<N:
    base = dna[i:i+3]
    if  base==target:
        an = an + 1
        index_list.append(i)
    
        
    i = i + 1
    
print "The indices of occurences are %s" % index_list

sub_list = dna.split(target)
mainDNA = ''
for item in sub_list:
    mainDNA = mainDNA + item

print mainDNA
    
    
    
    
    
    
    
    
    
    
    
    







    
        
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
 
    
    
    
    
    
    

    


        

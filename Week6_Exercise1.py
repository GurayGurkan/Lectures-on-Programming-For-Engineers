# -*- coding: utf-8 -*-
"""
@author: Guray
"""

listENG = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
listTR = ['Pazartesi','Salı','Carsamba','Persembe','Cuma','Cumartesi','Pazar']

"""
# Option 1: Endless while Loop and break

i = 0
while True:
    if i == 7:
        break
    print "%s. day of the week is %s and its translation is %s" % (i + 1,listENG[i],listTR[i])
    i = i + 1

# Option 2: while loop without break

i = 0
while i < 7:
    print "%s. day of the week is %s and its translation is %s" % (i + 1,listENG[i],listTR[i])
    i = i + 1


# Option 3: For loop in the English list

a = 0
for item in listENG:
    print "%s. day of the week is %s and its translation is %s" % (a+1,item,listTR[a])
    a = a + 1
"""
# Option 4: For loop in the Turkish list

a = 0
for item in listTR:
    print "%s. day of the week is %s and its translation is %s" % (a+1,listENG[a],item)
    a = a + 1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
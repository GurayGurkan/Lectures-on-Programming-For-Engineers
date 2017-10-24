# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 20:45:43 2017

@author: Guray
"""

#Question 1:
"""
def square_area(side):
    print "Entered side length is %s\nCalculated circumference = %s\nCalculated area = %s" % (side,4*side,side**2)
"""

def square_area(side):
    print "Entered side length is", side
    print "Calculated circumference =", side*4
    print "Calculated area =", side**2

#Question 2:

def sphere_area(radius):
    from math import pi
    print "Entered radius =",radius
    print "Calculated area =", 4*pi*radius**2
    print "Calculated volume =", (4/3)*pi*radius**3
    
# Question 3:

def hypotenuse(side1, side2):
    from math import sqrt
    print "Perpendicular sides =  (%s,%s)" % (side1,side2)
    print "Calculated hypotenuse =", sqrt(side1**2 + side2**2)
    
# Question 4:
    
def roots(a,b,c):
    from math import sqrt
    D = b**2-4*a*c
    if D>0:
        print "Roots are real and distinct..."
        x1 = (-b + sqrt(D))/(2*a)
        x2 = (-b - sqrt(D))/(2*a)
    elif D==0:
        print "Roots are equal..."
        x1 = -b /(2*a)
        x2 = x1
    else:
        print "No real roots exist. Roots are complex numbers..."
        x1 = None
        x2 = None
    return x1,x2
    
#Question 5:

def geomean(numbers):
    if isinstance(numbers,list):
        mymean = 1
        for i in numbers:
            mymean = i * mymean
        print "The geometrical average of %s is %s" % (numbers,mymean)
        return mymean
    else:
        print "Input should be a list, no calculations done..."
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
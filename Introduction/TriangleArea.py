#Author: Jared Bigelow
#Date: February 12 2015
#Purpose: First question in python

#Triangle Question
##################################################################################################

import math

sideA= int (input ("First Side: "))
sideB= int (input ("Second Side: "))
sideC= int  (input ("Third Side: "))

semiPerimeter = 1/2*(sideA+sideB+sideC)
Area = math.sqrt(semiPerimeter*(semiPerimeter-sideA)*(semiPerimeter-sideB)*(semiPerimeter-sideC))



print ("The area of your traingle is:" ,Area, "squared units")




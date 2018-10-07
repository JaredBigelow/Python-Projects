#Author: Jared Bigelow
#Date: February 12 2015
#Purpose: Second question in Python

#Triangle Question V2
##################################################################################################

import math

#-----------------------------------
def  getPositiveInteger (prompt="Please enter a positive integer:", low=0,high=100):
    intNumber = low -1
    while (intNumber < low or intNumber > high):
        strNumber = input (prompt+" between "+str(low)+" and "+str(high)+": ")
        while not str.isdigit (strNumber):
            strNumber = input ("Invalid. Please enter an integer:")
        intNumber = int (strNumber)
    return intNumber
#-----------------------------------

sideA= -1
sideB= -1
sideC= -1

while (sideA+sideB < sideC) or (sideB+sideC < sideA) or (sideA+sideC < sideB):
    sideA= getPositiveInteger ("Enter first side:",1,10)
    sideB= getPositiveInteger ("Enter second side:",1,20)
    sideC= getPositiveInteger ("Enter third side:",1,30)


semiPerimeter = 1/2*(sideA+sideB+sideC)
Area = math.sqrt(semiPerimeter*(semiPerimeter-sideA)*(semiPerimeter-sideB)*(semiPerimeter-sideC))
print ("The area of your triangle is:" ,Area, "squared units")







#Author: Jared Bigelow
#Date: February 13 2015
#Purpose: To find the middle number in any three given even numbers

#Middle Number
################################################################################

import math


Number1 = int (input ("First Number:"))
while Number1 < 0 or Number1 % 2 == 1:
    Number1 = int (input ("Error, Enter an even positive number:"))

Number2 = int (input ("Second Number:"))
while Number2 < 0 or Number2 % 2 == 1:
    Number2 = int (input ("Error, Enter an even positive number:"))

Number3 = int (input ("Third Number:"))
while Number3 < 0 or Number3 % 2 == 1:
    Number3 = int (input ("Error, Enter an even positive number:"))

if Number1 > Number2 and Number1 < Number3 or Number1 < Number2 and Number1 > Number3 or Number2 > Number1 and Number2 < Number3 or Number2 < Number1 and Number2 > Number3 or Number3 > Number2 and Number3 < Number1 or Number3 < Number2 and Number3 > Number1:

    if Number1 > Number2 and Number1 < Number3:
        print (Number1)
    elif Number1 < Number2 and Number1 > Number3:
        print (Number1)
    elif Number2 > Number1 and Number2 < Number3:
        print (Number2)
    elif Number2 < Number1 and Number2 > Number3:
        print (Number2)
    elif Number3 > Number2 and Number3 < Number1:
        print (Number3)
    elif Number3 < Number2 and Number3 > Number1:
        print (Number3)
else:
    print ("Error, no two numbers can be the same")





      
        

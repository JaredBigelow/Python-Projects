#Author: Jared Bigelow
#Date: February 13 2015
#Purpose: To assign a level to different marks

#Marks
################################################################################

import math

Mark = int (input ("Mark:"))

while Mark < 0 or Mark > 100:
    Mark = int (input ("Input an integer between 0 and 100:"))

if Mark >= 0 and Mark <= 39:
    print ("Fail")
elif Mark >= 40 and Mark <= 49:
    print ("Credit Recovery")
elif Mark >= 50 and Mark <= 59:
    print ("Level 1")
elif Mark >= 60 and Mark <= 69:
    print ("Level 2")
elif Mark >= 70 and Mark <= 79:
    print ("Level 3")
elif Mark >= 80 and Mark <= 100:
    print ("Level 4")

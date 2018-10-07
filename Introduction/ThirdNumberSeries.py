#Author: Jared Bigelow
#Date: February 13 2015
#Purpose: To make number series in Python

#Third Number Series
################################################################################

import math

Count = 1
Number1 = 1
Number2 = 3
FinalAnswer = 0

while Count <= 1000000:


    Answer = 1 / (Number1 * Number2)
    FinalAnswer = FinalAnswer + Answer
    Number1 = Number1 + 2
    Number2 = Number2 + 2
    Count = Count + 1

print(FinalAnswer)
    

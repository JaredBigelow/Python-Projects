#Author: Jared Bigelow
#Date: February 13 2015
#Purpose: To make number series in Python

#Second Number Series
################################################################################

import math

FinalNumber = 0
Count = 1
Number = 1

while Count <= 1000000:

    if Count % 2 == 1:
        Symbol = 1
    elif Count % 2 == 0:
        Symbol = -1

    Fraction = 1 / Number
    NewFraction = Fraction * Symbol
    FinalNumber = FinalNumber + NewFraction
    Count = Count + 1
    Number = Number + 2
    
Answer = 4 * FinalNumber
print(Answer)
    

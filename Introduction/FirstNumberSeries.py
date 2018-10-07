#Author: Jared Bigelow
#Date: February 13 2015
#Purpose: To make number series in Python

#First Number Series
################################################################################

import math

Count = 1
Number = 1

while Count <= 20:
    print (Number)
    Count = Count + 1
    Number = Number * Count

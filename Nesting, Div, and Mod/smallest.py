#Author: Jared Bigelow
#Date: February 18 2015
#Purpose: To print the smallest and largest values in a given data set
#Input: Series of integers
#Output: Largest number, smallest number, number average

#Smallest and Largest Numbers
################################################################################

import math

number = int (input ("Number:"))

while number == 0 :
    number = int (input ("Error, Enter an integer that is not zero:"))


small = number
big = number
Sum = 0
count = 0

while number > 0 or number < 0:

    while small > number:
        small = number

    while big < number:
        big = number

    Sum = Sum + number
    count = count + 1
    number = int (input ("Number:"))
    

print ("Smallest Number:", Small)
print ("Largest Number:", Big)
print ("Average of all numbers:", Sum / Count)

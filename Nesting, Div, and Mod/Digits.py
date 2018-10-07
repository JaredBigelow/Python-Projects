#Author: Jared Bigelow
#Date: February 18 2015
#Purpose: To print different values related to the same digits
#Input: Positive integer
#Output: Digit amount, digit sum, reverse of digits, palindrome check

#Digits
################################################################################

import math


number = int (input ("Number:"))

while number < 0 :
    number = int (input ("Error, Enter a positive number:"))

digits = number
digitSum = 0
digitReverse = 0
otherDigits = number
digitNumber = len (str(number))

while (digits > 0) :
    remainder = digits % 10
    digits = digits // 10
    digitSum = digitSum + remainder

while otherDigits > 10:
    ones = otherDigits % 10
    otherDigits = otherDigits // 10
    digitReverse = digitReverse * 10 + ones
    
digitReverse = digitReverse * 10 + otherDigits

if number == digitReverse:
    palindrome = "Yes"
else:
    palindrome = "No"
    
print ("Number of Digits:", digitNumber)
print ("Sum of Digits:", digitSum)
print ("Reverse of Digits:", digitReverse)
print ("Palindrome:", palindrome)



#Author: Jared Bigelow
#Date: March 11 2015
#Purpose: To print information about two inputted numbers

#Number Theory
##################################################################################################

import math

#SUBS

#Author: Jared Bigelow
#Date: March 11 2015
#Purpose: To get a positive integer
#Parameters: Prompt, low, high
#Return Value: Positive Integer
#-----------------------------------
def  getPositiveInteger (prompt="Please enter a positive integer", low=0,high=100):
    intNumber = low -1
    while (intNumber < low or intNumber > high):
        strNumber = input (prompt+" between "+str(low)+" and "+str(high)+": ")
        while not str.isdigit (strNumber):
            strNumber = input ("Invalid. Please enter a positive integer between"+str(low)+" and "+str(high)+": ")
        intNumber = int (strNumber)
    return intNumber
#-----------------------------------


#Author: Jared Bigelow
#Date: March 11 2015
#Purpose: To calculate the factorial of a number
#Parameters: Number
#Return Value: Factorial
#-----------------------------------
def  calcFactorial (number):
    count = 1
    factorial = 1
    while (count <= number):
        factorial = factorial * count
        count = count + 1
    return factorial
#-----------------------------------


#Author: Jared Bigelow
#Date: March 11 2015
#Purpose: To calculate the permutations of two numbers
#Parameters: Two numbers
#Return Value: Permutations
#-----------------------------------
def  calcPermutations (n,r):
    if n < r:
        n,r = r,n
    differenceFactorial = n-r
    nFactorial = calcFactorial (n)
    differenceFactorial = calcFactorial (differenceFactorial)
    permutations = nFactorial / differenceFactorial
    return permutations
#-----------------------------------

#Author: Jared Bigelow
#Date: March 11 2015
#Purpose: To calculate the combinations of two numbers
#Parameters: Two numbers
#Return Value: Combinations
#-----------------------------------
def  calcCombinations (n,r):
    if n < r:
        n,r = r,n
    nFactorial = calcFactorial (n)
    rFactorial = calcFactorial (r)
    differenceFactorial = (n-r)
    differenceFactorial = calcFactorial (differenceFactorial)
    denominatorFactorial = rFactorial * differenceFactorial
    combinations = nFactorial / denominatorFactorial
    return combinations
#-----------------------------------

#Author: Jared Bigelow
#Date: March 12 2015
#Purpose: To calculate the greatest common divisor of two numbers
#Parameters: Two numbers
#Return Value: Greatest common divisor
#-----------------------------------
def  calcGCD (m,n):
    t = m % n
    while not t == 0:
        m = n
        n = t
        t = m % n
    return n
#-----------------------------------

#Author: Jared Bigelow
#Date: March 12 2015
#Purpose: To calculate the least common multiple of two numbers
#Parameters: Two numbers
#Return Value: Least common multiple
#-----------------------------------
def  calcLCM (m,n):
    numberGCD = calcGCD (m,n)
    numberLCM = (m * n) / numberGCD
    return numberLCM
#-----------------------------------

#Author: Jared Bigelow
#Date: March 12 2015
#Purpose: To see if two numbers are relatively prime or not
#Parameters: Two numbers
#Return Value: Relatively prime or not
#-----------------------------------
def  isRelativelyPrime (m,n):
    numberGCD = calcGCD (m,n)
    if numberGCD == 1:
        relativelyPrime = True
    else:
        relativelyPrime = False
    return relativelyPrime
#-----------------------------------

#MAIN

repeat = "Y"
while repeat == "Y" or repeat == "y":
    firstNumber = getPositiveInteger ()
    secondNumber = getPositiveInteger ("Please enter another positive integer")

    permutations = calcPermutations (firstNumber, secondNumber)
    combinations = calcCombinations (firstNumber, secondNumber)
    greatestCommonDivisor = calcGCD (firstNumber, secondNumber)
    leastCommonMultiple = calcLCM (firstNumber, secondNumber)
    relativelyPrime = isRelativelyPrime (firstNumber, secondNumber)

    print ("Permutations:","%i" % permutations)
    print ("Combinations:","%i" % combinations)
    print ("Greatest Common Divisor:","%i" % greatestCommonDivisor)
    print ("Least Common Multiple:","%i" % leastCommonMultiple)
    print ("Relatively Prime:",relativelyPrime)
    repeat = input ("Repeat? (Y/N):")
print ("END")

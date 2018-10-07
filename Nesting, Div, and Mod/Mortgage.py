#Author: Jared Bigelow
#Date: February 26 2015
#Purpose: To determine monthly mortgage payments
#Input: Amount of the mortgage
#Output: Table of monthly payments

#Mortgage Payments
################################################################################

import math

repeat = "Y"

while repeat == "Y" or repeat == "y":
    mortgageAmount = int (input ("Mortgage Amount:"))

    while mortgageAmount <= 49999:
        mortgageAmount = int (input ("Error, enter at least $50000:"))
        
    for spaces in range (1,51):
        print (" ", end="") 
    print ("Years")
    print ("Interest", end="")

    for years in range (5, 36, 5):
        print("%10.0f" % years," ",end="")
    print()
        
    for rate in range (1,25):
        rate = rate / 4
        print("    %-3.2f" % rate," ",end="")
        
        for years in range (5,36,5):
            n = years * 12
            i = (1 + (rate/200))**(1/6) - 1
            f = 1 / ((1-(1+i)**-n)/i)
            monthlyPayment = f * mortgageAmount
            print("$%-10.2f" % monthlyPayment," ",end="")
        print()
    repeat = input ("Do another? (Y/N):")

    


#Author: Jared Bigelow
#Date: February 27 2015
#Purpose: To create star patterns based on inputted type and size
#Input: Type, size
#Output: Star Pattern

#Star Patterns
################################################################################

import math

repeat = "Y"

while repeat == "Y" or repeat == "y":
    
    print("Choose your type:(1:Square 2:Triangle 3:Hollow Square 4:Hollow Triangle)")
    patternType = int (input ("Type:"))

    while patternType < 1 or patternType > 4:
        patternType = int (input ("Error, enter a number between 1 and 4:"))

    print("Choose your size. (1-30)")
    patternSize = int (input ("Size:"))
    
    while patternSize < 1 or patternSize > 30:
        patternSize = int (input ("Error, enter a size between 1 and 30:"))
        
    if patternType == 1:
        print ()
        for star in range (1, patternSize + 1):
            print ("*","", end="")
            for star in range (1, patternSize):
                print ("*","", end="")
            print ()

    elif patternType == 2:
        number = 0
        print ()
        for star in range (1, patternSize + 1):
            number = number + 1
            for star in range (1, number + 1):
                print ("*","", end="")
            print ()
         
    elif patternType == 3:
        print ()
        for star in range (1, patternSize + 1):
            print ("*","", end="")
        print ()
        for star in range (1, patternSize - 1):
            print ("*","", end="")
            for star in range (2, patternSize):
                print ("  ", end="")
            print ("*","", end="")
            print ()
        for star in range (1, patternSize + 1):
            print ("*","", end="")
        print ()

    elif patternType ==4:
        numberOne = 0
        numberTwo = 0
        print ()
        for star in range (1, 3):
            numberOne = numberOne + 1
            for star in range (1, numberOne + 1):
                print ("*","", end="")
            print ()
        for star in range (1, patternSize - 2):
            print ("*","", end="")
            for star in range (2, patternSize - (patternSize - 3)):
                numberTwo = numberTwo + 1
                for star in range (1, numberTwo + 1):
                    print ("  ", end="")
            print ("*","", end="")
            print ()
        for star in range (1, patternSize + 1):
                print ("*","", end="")
        print ()
    print ()
    repeat = input ("Do another? (Y/N):")

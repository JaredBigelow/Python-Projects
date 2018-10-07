#Author: Jared Bigelow
#Date: May 20 2015
#Purpose: Add additional functionality to existing classes

#Overloading Operators
##################################################################################################
from tkinter import *
import random
import math

#CLASS HEADER
#Data Elements: size, value
#Methods of this class:
#__str__:
#setValue:
#setSize:
#roll:
#__add__:
#__sub__:
#__mul__:
#__gt__:
#__lt__:
#__ge__:
#__le__:
#__eq__:
#__ne__:
class Die:
    def __init__(self,size=50,value = 0):
        self.size = size
        if value <= 0 or value > 6:
            self.roll()
        else:
            self.value = value
        self.radius = self.size / 5
        self.gap = self.radius / 2

    #METHOD HEADER
    #Purpose: To convert a Die object into a string 
    #Input/Parameters: nil
    #Outputs/Return values: String version of the Die
    def __str__ (self):
        return str(self.value)

    #METHOD HEADER
    #Purpose: To set the value of the die
    #Input/Parameters: value
    #Outputs/Return values: nil
    def setValue(self,value=1):
        if value >= 1 and value <=6:
            self.value = value
        else:
            self.value = 1

    #METHOD HEADER
    #Purpose: To set the size of the die
    #Input/Parameters: size
    #Outputs/Return values: nil    
    def setSize(self,size=50):
        if size >= 30 and size <=100:
            self.size = size
        else:
            self.size = 50

    #METHOD HEADER
    #Purpose: To set the value of the die to a random value
    #Input/Parameters: nil
    #Outputs/Return values: nil     
    def roll (self):
        self.value = random.randint(1,6)

    #METHOD HEADER
    #Purpose: To add two values together
    #Input/Parameters: nil
    #Outputs/Return values: Sum of the values
    def __add__(self,second):
        addition = self.value + second.value 
        return addition

    #METHOD HEADER
    #Purpose: To subtract one value from another
    #Input/Parameters: nil
    #Outputs/Return values: Difference of the values
    def __sub__(self,second):
        subtraction = self.value - second.value
        return subtraction

    #METHOD HEADER
    #Purpose: To multiply two values together
    #Input/Parameters: nil
    #Outputs/Return values: Product of the values
    def __mul__(self,second):
        multiplication = self.value * second.value
        return multiplication

    #METHOD HEADER
    #Purpose: To see if the first value is greater than the second 
    #Input/Parameters: nil
    #Outputs/Return values: If it is greater than or not
    def __gt__(self,second):
        if self.value > second.value:
            greater = True
        else:
            greater = False
        return greater

    #METHOD HEADER
    #Purpose: To see if the first value is less than the second 
    #Input/Parameters: nil
    #Outputs/Return values: If it is less than or not
    def __lt__(self,second):
        if self.value < second.value:
            less = True
        else:
            less = False
        return less
    
    #METHOD HEADER
    #Purpose: To see if the first value is greater than or equal to the second 
    #Input/Parameters: nil
    #Outputs/Return values: If it is greater than or equal to or not
    def __ge__(self,second):
        if self.value >= second.value:
            greater = True
        else:
            greater = False
        return greater

    #METHOD HEADER
    #Purpose: To see if the first value is less than or equal to the second 
    #Input/Parameters: nil
    #Outputs/Return values: If it is less than or equal to or not
    def __le__(self,second):
        if self.value <= second.value:
            less = True
        else:
            less = False
        return less

    #METHOD HEADER
    #Purpose: To see if the first value is equal to the second 
    #Input/Parameters: nil
    #Outputs/Return values: If it is equal to or not
    def __eq__(self,second):
        if self.value == second.value:
            equal = True
        else:
            equal = False
        return equal

    #METHOD HEADER
    #Purpose: To see if the first value is not equal to the second 
    #Input/Parameters: nil
    #Outputs/Return values: If it is not equal to or not
    def __ne__(self,second):
        if self.value != second.value:
            notequal = True
        else:
            notequal = False
        return notequal
    
#CLASS HEADER
#Data Elements: size
#Methods of this class:
#__str__:
#setValues:
#setSize:
#sort:
#roll:
#greatness:
#__gt__:
#__lt__:
#__ge__:
#__le__:
#__eq__:
#__ne__:
class Hand:
    def __init__(self,size=50):
        self.firstDie = Die ()
        self.secondDie = Die ()
        self.thirdDie = Die ()
        self.sort()
        self.size = size

    #METHOD HEADER
    #Purpose: To convert Die objects into a string 
    #Input/Parameters: nil
    #Outputs/Return values: String version of the Dies
    def __str__(self):
        return str(self.firstDie)+"-"+str(self.secondDie)+"-"+str(self.thirdDie)

    #METHOD HEADER
    #Purpose: To set the values of the dice
    #Input/Parameters: nil
    #Outputs/Return values: nil 
    def setValues (self):
        self.firstDie.setValue(self.firstDie.value)
        self.secondDie.setValue(self.secondDie.value)
        self.thirdDie.setValue(self.thirdDie.value)


    #METHOD HEADER
    #Purpose: To rearrange the dice
    #Input/Parameters: nil
    #Outputs/Return values: nil    
    def sort (self):
        if self.firstDie.value > self.secondDie.value:
            self.firstDie.value,self.secondDie.value=self.secondDie.value,self.firstDie.value
        if self.firstDie.value > self.thirdDie.value:
            self.firstDie.value,self.thirdDie.value=self.thirdDie.value,self.firstDie.value
        if self.secondDie.value > self.thirdDie.value:
            self.secondDie.value,self.thirdDie.value=self.thirdDie.value,self.secondDie.value

    #METHOD HEADER
    #Purpose: To set the values of the dice to random values
    #Input/Parameters: nil
    #Outputs/Return values: nil    
    def roll (self):
        firstDie.roll()
        secondDie.roll()
        thirdDie.roll()

    #METHOD HEADER
    #Purpose: To add the values of all the dice in a hand
    #Input/Parameters: nil
    #Outputs/Return values: Sum of the values
    def greatness(self):
        return self.firstDie.value + self.secondDie.value + self.thirdDie.value

    #METHOD HEADER
    #Purpose: To see if the first value is greater than the second 
    #Input/Parameters: nil
    #Outputs/Return values: If it is greater than or not
    def __gt__(self,second):
        if self.greatness() > second.greatness():
            greater = True
        else:
            greater = False
        return greater

    #METHOD HEADER
    #Purpose: To see if the first value is less than the second 
    #Input/Parameters: nil
    #Outputs/Return values: If it is less than or not
    def __lt__(self,second):
        if self.greatness() < second.greatness():
            less = True
        else:
            less = False
        return less

    #METHOD HEADER
    #Purpose: To see if the first value is greater than or equal to the second 
    #Input/Parameters: nil
    #Outputs/Return values: If it is greater than or equal to or not
    def __ge__(self,second):
        if self.greatness() >= second.greatness():
            greater = True
        else:
            greater = False
        return greater

    #METHOD HEADER
    #Purpose: To see if the first value is less than or equal to the second 
    #Input/Parameters: nil
    #Outputs/Return values: If it is less than or equal to or not
    def __le__(self,second):
        if self.greatness() <= second.greatness():
            less = True
        else:
            less = False
        return less

    #METHOD HEADER
    #Purpose: To see if the first value is equal to the second 
    #Input/Parameters: nil
    #Outputs/Return values: If it is equal to or not
    def __eq__(self,second):
        if self.greatness() == second.greatness():
            equal = True
        else:
            equal = False
        return equal

    #METHOD HEADER
    #Purpose: To see if the first value is not equal to the second 
    #Input/Parameters: nil
    #Outputs/Return values: If it is not equal to or not
    def __ne__(self,second):
        if self.greatness() != second.greatness():
            notequal = True
        else:
            notequal = False
        return notequal


#CLASS HEADER
#Data Elements: day, month, year
#Methods of this class:
#__str__:
#calcZeller:
#returnDayName:
#returnMonthName:
#value:
#__sub__:
#__gt__:
#__lt__:
#__ge__:
#__le__:
#__eq__:
#__ne__:
class Date:
    def __init__(self,intDay=1,intMonth=1,intYear=2000):
        self.intDay = intDay
        self.intMonth = intMonth
        self.intYear = intYear

    #METHOD HEADER
    #Purpose: To determine whether it is a leap year or not
    #Input/Parameters: nil
    #Outputs/Return values: If it is a leap year or not
    def returnLeapYear (self):
        if self.intYear % 400 == 0 or self.intYear % 4 == 0:
            leap = True
        else:
            leap = False
        return leap

    #METHOD HEADER
    #Purpose: To determine the day of the week
    #Input/Parameters: nil
    #Outputs/Return values: Day in integer form
    def calcZeller (self):
        m = self.intMonth - 2
        y = self.intYear
        if m <= 0:
            m = m + 12
            y = y - 1
        p = y//100
        r = y % 100
        return (self.intDay + (26 * m - 2)//10 + r + r//4 + p//4 + 5 * p) % 7

    #METHOD HEADER
    #Purpose: To return the day of the week in words
    #Input/Parameters: nil
    #Outputs/Return values: Day in words
    def returnDayName (self):    
        if self.calcZeller() == 0:
            day = "Sunday"
        elif self.calcZeller() == 1:
            day = "Monday"
        elif self.calcZeller() == 2:
            day = "Tuesday"
        elif self.calcZeller() == 3:
            day = "Wednesday"
        elif self.calcZeller() == 4:
            day = "Thursday"
        elif self.calcZeller() == 5:
            day = "Friday"
        else:
            day = "Saturday"
        return day

    #METHOD HEADER
    #Purpose: To return the month in words
    #Input/Parameters: nil
    #Outputs/Return values: Month in words
    def returnMonthName (self):
        if self.intMonth == 1:
            name = "January"
        elif self.intMonth == 2:
            name = "February"
        elif self.intMonth == 3:
            name = "March"
        elif self.intMonth == 4:
            name = "April"
        elif self.intMonth == 5:
            name = "May"
        elif self.intMonth == 6:
            name = "June"
        elif self.intMonth == 7:
            name = "July"
        elif self.intMonth == 8:
            name = "August"
        elif self.intMonth == 9:
            name = "September"
        elif self.intMonth == 10:
            name = "October"
        elif self.intMonth == 11:
            name = "November"
        else:
            name = "December"
        return name
    
    #METHOD HEADER
    #Purpose: To return the date in a specific form
    #Input/Parameters: nil
    #Outputs/Return values: Date in the specific form
    def __str__ (self):
        return self.returnDayName()+", "+str(self.intDay)+" "+self.returnMonthName()+" "+str(self.intYear)

    #METHOD HEADER
    #Purpose: To find the value of the date
    #Input/Parameters: nil
    #Outputs/Return values: Value of the date
    def value (self):
        value = 0
        year = self.intYear
        for years in range (1800,self.intYear):
            yearVal = Date(intYear=year-1)
            if yearVal.returnLeapYear() == True:
                value = value + 366
            else:
                value = value + 365
            year = year - 1
        if self.intMonth == 2:
            value = value + 31
        elif self.intMonth == 3:
            value = value + 59
        elif self.intMonth == 4:
            value = value + 90
        elif self.intMonth == 5:
            value = value + 120
        elif self.intMonth == 6:
            value = value + 151
        elif self.intMonth == 7:
            value = value + 181
        elif self.intMonth == 8:
            value = value + 212
        elif self.intMonth == 9:
            value = value + 243
        elif self.intMonth == 10:
            value = value + 273
        elif self.intMonth == 11:
            value = value + 304
        elif self.intMonth == 12:
            value = value + 334
        if self.returnLeapYear() == True and self.intMonth > 2:
                value = value + 1    
        value = value + self.intDay
        return value

    #METHOD HEADER
    #Purpose: To subtract one value from another
    #Input/Parameters: nil
    #Outputs/Return values: Difference of the values
    def __sub__(self,second):
        subtraction = abs(self.value() - second.value())
        return subtraction

    #METHOD HEADER
    #Purpose: To see if the first value is greater than the second 
    #Input/Parameters: nil
    #Outputs/Return values: If it is greater than or not
    def __gt__(self,second):
        if self.value() > second.value():
            greater = True
        else:
            greater = False
        return greater

    #METHOD HEADER
    #Purpose: To see if the first value is less than the second 
    #Input/Parameters: nil
    #Outputs/Return values: If it is less than or not
    def __lt__(self,second):
        if self.value() < second.value():
            less = True
        else:
            less = False
        return less

    #METHOD HEADER
    #Purpose: To see if the first value is greater than or equal to the second 
    #Input/Parameters: nil
    #Outputs/Return values: If it is greater than or equal to or not
    def __ge__(self,second):
        if self.value() >= second.value():
            greater = True
        else:
            greater = False
        return greater

    #METHOD HEADER
    #Purpose: To see if the first value is less than or equal to the second 
    #Input/Parameters: nil
    #Outputs/Return values: If it is less than or equal to or not
    def __le__(self,second):
        if self.value() <= second.value():
            less = True
        else:
            less = False
        return less

    #METHOD HEADER
    #Purpose: To see if the first value is equal to the second 
    #Input/Parameters: nil
    #Outputs/Return values: If it is equal to or not
    def __eq__(self,second):
        if self.value() == second.value():
            equal = True
        else:
            equal = False
        return equal

    #METHOD HEADER
    #Purpose: To see if the first value is not equal to the second 
    #Input/Parameters: nil
    #Outputs/Return values: If it is not equal to or not
    def __ne__(self,second):
        if self.value() != second.value():
            notequal = True
        else:
            notequal = False
        return notequal
    
#MAIN

#Dice Test
print ("DICE TEST")
testDie1 = Die()
testDie2 = Die()
print ("Die 1 is:",testDie1)
print ("Die 2 is:",testDie2)
print ("Sum:",testDie1+testDie2)
print ("Difference:",testDie1-testDie2)
print ("Product: ",testDie1*testDie2)
print ("Die 1 Greater Than Die 2:",testDie1>testDie2)
print ("Die 1 Less Than Die 2:",testDie1<testDie2)
print ("Die 1 Greater Than Or Equal To Die 2:",testDie1>=testDie2)
print ("Die 1 Less Than Or Equal To Die 2:",testDie1<=testDie2)
print ("Die 1 Equal To Die 2:",testDie1==testDie2)
print ("Die 1 Not Equal To Die 2:",testDie1!=testDie2)
print ()

#Hand Test
print ("HAND TEST")
testHand1 = Hand()
testHand2 = Hand()
print ("Hand 1 Greatness:",testHand1.greatness())
print ("Hand 2 Greatness:",testHand2.greatness())
print ("Hand 1 Greater Than Hand 2:",testHand1>testHand2)
print ("Hand 1 Less Than Hand 2:",testHand1<testHand2)
print ("Hand 1 Greater Than Or Equal To Hand 2:",testHand1>=testHand2)
print ("Hand 1 Less Than Or Equal To Hand 2:",testHand1<=testHand2)
print ("Hand 1 Equal To Hand 2:",testHand1==testHand2)
print ("Hand 1 Not Equal To Hand 2:",testHand1!=testHand2)
print ()

#Date Test
print ("DATE TEST")
testDate1 = Date(27,5,2015)
testDate2 = Date(2,6,2016)
print ("First Date:",testDate1)
print ("Second Date:",testDate2)
print ("Days Between Dates:",testDate1-testDate2)
print ("First Date Greater Than Second Date:",testDate1>testDate2)
print ("First Date Less Than Second Date:",testDate1<testDate2)
print ("First Date Greater Than Or Equal To Second Date:",testDate1>=testDate2)
print ("First Date Less Than Or Equal To Second Date:",testDate1<=testDate2)
print ("First Date Equal To Second Date:",testDate1==testDate2)
print ("First Date Not Equal To Second Date:",testDate1!=testDate2)

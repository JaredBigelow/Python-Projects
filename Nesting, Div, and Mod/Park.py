#Author: Jared Bigelow
#Date: February 20 2015
#Purpose: To determine the pricing in a garage
#Input: Total minutes parked, time of entry, pass
#Output: Price

#Parking Garage
################################################################################

import math

totalMinutes = int (input ("Total minutes parked:"))

while totalMinutes <= 0:
    totalMinutes = int (input ("Error, enter a positive integer:"))

timeEnter = int (input ("Time of entry (eg. 0900 = 9 AM):"))

while timeEnter < 0:
    timeEnter = int (input ("Error, enter a valid time:"))
    
Pass = input ("Pass (Y/N):")

while not (Pass == "Y" or Pass == "y" or Pass == "N" or Pass == "n"):
    Pass = input ("Error, enter Y or N:")
    
totalTime = (totalMinutes / 60) * 100
Minutes = ((totalTime % 100) / 100) * 60
Hours =(totalTime // 100 ) * 100
totalTime = (Hours + Minutes) 
timeExit = timeEnter + totalTime

Price = 0

if timeExit > 2400:
    print ("Error, you can not stay past midnight")

else:
    if timeExit == 2400:
        timeExit= 0
        
    while timeEnter < 1800 and timeEnter > 0:
        Price = Price + 3
        totalMinutes = totalMinutes - 20

    if (timeExit >= 1800 and timeExit <= 2359 and Pass == "Y" or Pass == "y") or (timeExit ==0 and Pass == "Y" or Pass == "y"):
        Price = 5.00

    elif Pass == "Y" or Pass == "y":
        Price = 8.50
        
    elif (timeExit >= 1800 and timeExit <= 2359 and Pass == "N" or Pass == "n") or (timeExit ==0 and Pass == "N" or Pass == "n"):
        Price = Price + 5.00

    if Price >= 28.00:
        Price = 28.00
        
    print ("The price you must pay is:", "$%0.2f" % Price)


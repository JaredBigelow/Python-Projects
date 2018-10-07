#Author: Jared Bigelow
#Date: April 20 2015
#Purpose: To print a date and a calendar based on an inputted date

#Date Class
##################################################################################################

#Class HEADER
#Purpose: To allow entry and output of a date and print a calendar for the month and year
#Input/Parameters: nil
#Outputs/Return values: Date and calendar
class Date:

    #METHOD HEADER
    #Purpose: To initialize the day, month, and year
    #Input/Parameters: nil
    #Outputs/Return values: nil
    def __init__(self,intDay=1,intMonth=1,intYear=2000):
        self.intDay = intDay
        self.intMonth = intMonth
        self.intYear = intYear

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
    #Purpose: To return the maximum amount of days in the month
    #Input/Parameters: nil
    #Outputs/Return values: Maximum amount of days in the month
    def returnMaxDay (self):
        if self.intMonth == 1 or self.intMonth == 3 or self.intMonth == 5 or self.intMonth == 7 \
        or self.intMonth == 8 or self.intMonth == 10 or self.intMonth == 12:
            maxDay = 31
        elif self.intMonth == 4 or self.intMonth == 6 or self.intMonth == 8 or self.intMonth == 10 or self.intMonth == 11:
            maxDay = 30
        elif self.intMonth == 2 and self.returnLeapYear() == True:
            maxDay = 29
        else:
            maxDay = 28
        return maxDay

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
    #Purpose: To check and see if the date is valid
    #Input/Parameters: nil
    #Outputs/Return values: If the date is valid or not
    def calcValid (self):
        if int(self.intDay) > self.returnMaxDay() or int(self.intDay) <= 0 or int(self.intMonth) > 12 or int(self.intMonth) <= 0 or int(self.intYear) < 1800 or int(self.intYear) > 2100:
            valid = False
        else:
            valid = True
        return valid

    #METHOD HEADER
    #Purpose: To get the date from the user
    #Input/Parameters: nil
    #Outputs/Return values: nil
    def getDate (self):
        self.intYear = input ("Year:")
        while not str.isdigit (self.intYear) or self.calcValid() == False:
            self.intYear = input ("Invalid. Please enter a positive integer between 1800 and 2100 for year:")
        self.intYear = int (self.intYear)

        self.intMonth = input ("Month:")
        while not str.isdigit (self.intMonth) or self.calcValid() == False:
            self.intMonth = input ("Invalid. Please enter a positive integer between 1 and 12 for month:")
        self.intMonth = int (self.intMonth)
        
        self.intDay = input ("Day:")
        while not str.isdigit (self.intDay) or self.calcValid() == False:
            self.intDay = input ("Invalid. Please enter a positive integer between 1 and "+str(self.returnMaxDay())+" for day:")
        self.intDay = int (self.intDay)

    #METHOD HEADER
    #Purpose: To return the date in a specific form
    #Input/Parameters: nil
    #Outputs/Return values: Date in the specific form
    def __str__ (self):
        return self.returnDayName()+", "+str(self.intDay)+" "+self.returnMonthName()+" "+str(self.intYear)

    #METHOD HEADER
    #Purpose: To print a calendar of the given month and year
    #Input/Parameters: nil
    #Outputs/Return values: Prints a calendar
    def displayCalendar (self):
        print ()
        print(userDate.__str__())
        print ()
         
        print ("                 "+userDate.returnMonthName()+" "+str(userDate.intYear))
        print ()
        print ("Sun    Mon    Tue    Wed    Thu    Fri    Sat")
        print ()
        userCalendar = Date(1,userDate.intMonth,userDate.intYear)
        weekDay = userCalendar.calcZeller()
        day = 1
        for days in range (1,weekDay+1):
            print ("       ",end="")
        for days in range (1,userDate.returnMaxDay()+1):
            print("%-2i" % day," ",end="")
            if weekDay == 6:
                print ()
                print ()
                weekDay = -1
            else:
                print ("   ",end="")
            day = day + 1
            weekDay = weekDay + 1
        print ()
        print ()

        
#MAIN
repeat = "Y"
while repeat == "Y" or repeat == "y":
    userDate = Date()
    userDate.getDate()
    userDate.displayCalendar()
    repeat = input ("Do another? (Y/N):")

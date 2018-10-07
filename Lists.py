#Author: Jared Bigelow
#Date: June 1 2015
#Purpose: To demonstrate different capabilities of a list

#Lists
##################################################################################################
import random

#CLASS HEADER
#Data Elements: size
#Methods of this class:
#__str__:
#initAsNum:
#initAsSequence:
#initAsFib:
#calcTotal:
#calcMean:
#findLargest:
#calcFreq:
#insertAt:
#removeAt:
#removeAll:
#findFirst:
#reverse:
#isSorted:
#merge:
class IntGroup:
    def __init__(self,size=0):
        if size >= 0:
            self.size = size
        else:
            self.size = 0
        self.list = []
        for numbers in range(size):
            self.list.append(random.randint(0,size))

    #METHOD HEADER
    #Purpose: To convert a list into a string 
    #Input/Parameters: nil
    #Outputs/Return values: String version of the list
    def __str__ (self):
        return str(self.list)+" Size: "+str(self.size)

    #METHOD HEADER
    #Purpose: To fill the list given a parameter
    #Input/Parameters: value
    #Outputs/Return values: List full of given value
    def initAsNum(self,value):
        self.list = []
        for numbers in range(self.size):
            self.list.append(value)
        
    #METHOD HEADER
    #Purpose: To fill the list with 1,2,3,4...etc.
    #Input/Parameters: nil
    #Outputs/Return values: List as a sequence
    def initAsSequence(self):
        self.list = []
        count = 0
        for numbers in range(self.size):
            count = count + 1
            self.list.append(count)

    #METHOD HEADER
    #Purpose: To fill the list with Fibonacci's sequence
    #Input/Parameters: nil
    #Outputs/Return values: List as a Fibonnacci's sequence
    def initAsFib(self):
        self.list = []
        count1 = 1
        count2 = 0
        if self.size>0:
            self.list.append(count1)
        for numbers in range(self.size-1):
            self.list.append(count1+count2)
            count1,count2=count2,count1
            count1 = count1+count2
        
    #METHOD HEADER
    #Purpose: To find the total of the elements in the list
    #Input/Parameters: nil
    #Outputs/Return values: Total of the elements
    def calcTotal(self):
        total = 0
        for x in self.list:
            total = total + x
        return total

    #METHOD HEADER
    #Purpose: To find the total of the elements in the list
    #Input/Parameters: nil
    #Outputs/Return values: Total of the elements
    def calcMean(self):
        total = self.calcTotal()
        length = len(self.list)
        mean = total / length
        return mean

    #METHOD HEADER
    #Purpose: To find the largest element in the list
    #Input/Parameters: nil
    #Outputs/Return values: Largest element of the list
    def findLargest(self):
        largest = 0
        for x in self.list:
            if x > largest:
                largest = x
        return largest

    #METHOD HEADER
    #Purpose: To find the frequency of a given value in the list
    #Input/Parameters: value
    #Outputs/Return values: Frequency of the given value
    def calcFreq(self,value):
        frequency = 0
        for x in self.list:
            if x == value:
                frequency = frequency + 1
        return frequency

    #METHOD HEADER
    #Purpose: To insert a value at a given position in the list
    #Input/Parameters: position, value
    #Outputs/Return values: nil
    def insertAt(self,position,value):
        if position <= 0:
            position = 1
        self.list.insert(position-1,value)
        self.size = self.size + 1
        
    #METHOD HEADER
    #Purpose: To remove a value at a given position in the list
    #Input/Parameters: position
    #Outputs/Return values: nil
    def removeAt(self,position):
        if position < 0:
            position = 0
        del self.list[position-1]
        self.size = self.size - 1  

    #METHOD HEADER
    #Purpose: To remove all the elements matching a value in the list
    #Input/Parameters: value
    #Outputs/Return values: nil
    def removeAll(self,value):
        frequency = self.calcFreq(value)
        self.size = self.size - frequency
        for amount in range(1,frequency+1):
            self.list.remove(value)

    #METHOD HEADER
    #Purpose: To find the first example of a value in a list
    #Input/Parameters: value
    #Outputs/Return values: The position of the first matching element
    def findFirst(self,value):
        if value in self.list:
            first = self.list.index(value)
        else:
            first = -1
        return first + 1

    #METHOD HEADER
    #Purpose: To reverse the list
    #Input/Parameters: nil
    #Outputs/Return values: Reversed list
    def reverse(self):
        reverse = []
        position = self.size-1
        for numbers in range(self.size):
            item = self.list[position]
            reverse.append(item)
            position = position-1
        self.list = reverse

    #METHOD HEADER
    #Purpose: To check if a list is sorted
    #Input/Parameters: nil
    #Outputs/Return values: If it is sorted or not
    def isSorted(self):
        comparison = 0
        issorted = True
        for numbers in range(self.size):
            item = self.list.pop(0)
            self.list.append(item)
            if item < comparison:
                issorted = False
            comparison = item
        return issorted

    #METHOD HEADER
    #Purpose: To merge two lists together
    #Input/Parameters: second list
    #Outputs/Return values: Merged list
    def merge(self,second):
        newList = IntGroup ()
        if self.isSorted() == True and second.isSorted() == True:
            for numbers in range(self.size):
                item = self.list.pop(0)
                newList.list.append(item)
            for numbers in range(second.size):
                item = second.list.pop(0)
                newList.list.append(item)
            newList.list.sort()
            newList.size = self.size + second.size
        else:
            newList.size = 0
        return newList

#MAIN 
firstList = IntGroup(5)
print ("First List:",firstList)
firstList.initAsNum(3)
print ("List filled with the number 3:",firstList)
firstList.initAsSequence()
print ("List as a sequence:",firstList)
firstList.initAsFib()
print ("List as Fibonacci's sequence:",firstList)
print ("Total:",firstList.calcTotal())
print ("Mean:",firstList.calcMean())
print("Largest element:",firstList.findLargest())
print ("Frequency of the number 1:",firstList.calcFreq(1))
firstList.insertAt(3,6)
print ("List with a 6 inserted at position 3:",firstList)
firstList.removeAt(4)
print ("List with the fourth position's element removed:",firstList)
firstList.removeAll(5)
print ("List with the all 5's removed:",firstList)
print("Position of the first 3:",firstList.findFirst(3))
firstList.reverse()
print ("Reverse:",firstList)
print("List sorted:",firstList.isSorted())
secondList = IntGroup (7)
print("Second list:",secondList)
firstList.list.sort()
print("Sorted first list:",firstList)
secondList.list.sort()
print("Sorted second list:",secondList)
print("Merged list:",firstList.merge(secondList))

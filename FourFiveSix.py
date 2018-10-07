#Author: Jared Bigelow
#Date: April 29 2015
#Purpose: To roll and display three dice in a 4-5-6 game

#Four Five Six
##################################################################################################
from tkinter import *
import random

#CLASS HEADER
#Data Elements: size, value
#Methods of this class:
#__str__:
#getValue:
#setValue:
#setSize:
#roll:
#draw:
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
    #Purpose: To get the value of the die from the user
    #Input/Parameters: nil
    #Outputs/Return values: nil
    def getValue (self):
        self.value = input ("Value:")
        while not str.isdigit (self.value):
            self.intYear = input ("Invalid. Please enter a positive integer between 1 and 6:")
        self.value = int (self.value)

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
    #Purpose: To draw the die given
    #Input/Parameters: canvas, x value, y value
    #Outputs/Return values: Draws the die
    def draw(self,c,x,y):
        c.create_rectangle(x,y,x+80,y+80,width=1,tags="all",outline="green",fill="white")
        if self.value ==1:
            c.create_oval(x+32.5,y+32.5,x+47.5,y+47.5,tags="all",outline="black",fill="black")
        elif self.value ==2:
            c.create_oval(x+10,y+10,x+25,y+25,tags="all",outline="black",fill="black")
            c.create_oval(x+55,y+55,x+70,y+70,tags="all",outline="black",fill="black")
        elif self.value ==3:
            c.create_oval(x+10,y+10,x+25,y+25,tags="all",outline="black",fill="black")
            c.create_oval(x+32.5,y+32.5,x+47.5,y+47.5,tags="all",outline="black",fill="black")
            c.create_oval(x+55,y+55,x+70,y+70,tags="all",outline="black",fill="black")
        elif self.value ==4: 
            c.create_oval(x+10,y+10,x+25,y+25,tags="all",outline="black",fill="black")
            c.create_oval(x+55,y+10,x+70,y+25,tags="all",outline="black",fill="black")
            c.create_oval(x+55,y+55,x+70,y+70,tags="all",outline="black",fill="black")
            c.create_oval(x+10,y+55,x+25,y+70,tags="all",outline="black",fill="black")
        elif self.value ==5: 
            c.create_oval(x+10,y+10,x+25,y+25,tags="all",outline="black",fill="black")
            c.create_oval(x+55,y+10,x+70,y+25,tags="all",outline="black",fill="black")
            c.create_oval(x+32.5,y+32.5,x+47.5,y+47.5,tags="all",outline="black",fill="black")
            c.create_oval(x+55,y+55,x+70,y+70,tags="all",outline="black",fill="black")
            c.create_oval(x+10,y+55,x+25,y+70,tags="all",outline="black",fill="black")
        elif self.value ==6: 
            c.create_oval(x+10,y+10,x+25,y+25,tags="all",outline="black",fill="black")
            c.create_oval(x+55,y+10,x+70,y+25,tags="all",outline="black",fill="black")
            c.create_oval(x+10,y+32.5,x+25,y+47.5,tags="all",outline="black",fill="black")
            c.create_oval(x+55,y+32.5,x+70,y+47.5,tags="all",outline="black",fill="black")
            c.create_oval(x+55,y+55,x+70,y+70,tags="all",outline="black",fill="black")
            c.create_oval(x+10,y+55,x+25,y+70,tags="all",outline="black",fill="black")


#CLASS HEADER
#Data Elements: size
#Methods of this class:
#__str__:
#getValues:
#setValues:
#setSize:
#sort:
#roll:
#draw:
#isWinner:
#isLoser:
#calcPoint:
class Hand:
    def __init__(self,size=50):
        firstDie=Die()
        secondDie=Die()
        thirdDie=Die()
        self.firstDie = firstDie
        self.secondDie = secondDie
        self.thirdDie = thirdDie
        self.sort()
        self.size = size

    #METHOD HEADER
    #Purpose: To convert Die objects into a string 
    #Input/Parameters: nil
    #Outputs/Return values: String version of the Dies
    def __str__(self):
        return str(self.firstDie)+"-"+str(self.secondDie)+"-"+str(self.thirdDie)

    #METHOD HEADER
    #Purpose: To get the value of the dice from the user
    #Input/Parameters: nil
    #Outputs/Return values: nil
    def getValues (self):
        self.firstDie.getValue()
        self.secondDie.getValue()
        self.thirdDie.getValue()

    #METHOD HEADER
    #Purpose: To set the values of the dice
    #Input/Parameters: nil
    #Outputs/Return values: nil 
    def setValues (self):
        self.firstDie.setValue(self.firstDie.value)
        self.secondDie.setValue(self.secondDie.value)
        self.thirdDie.setValue(self.thirdDie.value)

    #METHOD HEADER
    #Purpose: To set the size of the die
    #Input/Parameters: sizw
    #Outputs/Return values: nil  
    def setSize(self,size=50):
        if size >= 30 and size <=100:
            self.size = size
        else:
            self.size = 50

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
    #Purpose: To draw the dice given
    #Input/Parameters: nil
    #Outputs/Return values: Draws the dice
    def draw(self):
        self.firstDie.draw(c,10,10)
        self.secondDie.draw(c,100,10)
        self.thirdDie.draw(c,190,10)

    #METHOD HEADER
    #Purpose: To determine if the dice are a winning combination or not
    #Input/Parameters: nil
    #Outputs/Return values: If it it true or not
    def isWinner (self):
        if self.firstDie.value == 4 and self.secondDie.value ==5 and self.thirdDie.value==6\
        or self.firstDie.value==self.secondDie.value and self.firstDie.value==self.thirdDie.value\
        or self.firstDie.value==self.secondDie.value and self.thirdDie.value==6\
        or self.firstDie.value==self.thirdDie.value and self.secondDie.value==6\
        or self.secondDie.value==self.thirdDie.value and self.firstDie.value==6:
            return True
        else:
            return False

    #METHOD HEADER
    #Purpose: To determine if the dice are a losing combination or not
    #Input/Parameters: nil
    #Outputs/Return values: If it it true or not
    def isLoser (self):
        if self.firstDie.value == 1 and self.secondDie.value ==2 and self.thirdDie.value==3\
        or self.firstDie.value==self.secondDie.value and self.thirdDie.value==1\
        or self.firstDie.value==self.thirdDie.value and self.secondDie.value==1\
        or self.secondDie.value==self.thirdDie.value and self.firstDie.value==1:
            return True
        else:
            return False

    #METHOD HEADER
    #Purpose: To find the point value of the hand
    #Input/Parameters: nil
    #Outputs/Return values: Point value
    def calcPoint (self):
        if self.firstDie.value==self.secondDie.value and self.firstDie.value==self.thirdDie.value:
            return 0
        else:
            if self.firstDie.value==self.secondDie.value and self.thirdDie.value==2\
            or self.firstDie.value==self.thirdDie.value and self.secondDie.value==2\
            or self.secondDie.value==self.thirdDie.value and self.firstDie.value==2:
                return 2
            elif self.firstDie.value==self.secondDie.value and self.thirdDie.value==3\
            or self.firstDie.value==self.thirdDie.value and self.secondDie.value==3\
            or self.secondDie.value==self.thirdDie.value and self.firstDie.value==3:
                return 3
            elif self.firstDie.value==self.secondDie.value and self.thirdDie.value==4\
            or self.firstDie.value==self.thirdDie.value and self.secondDie.value==4\
            or self.secondDie.value==self.thirdDie.value and self.firstDie.value==4:
                return 4
            elif self.firstDie.value==self.secondDie.value and self.thirdDie.value==5\
            or self.firstDie.value==self.thirdDie.value and self.secondDie.value==5\
            or self.secondDie.value==self.thirdDie.value and self.firstDie.value==5:
                return 5
            else:
                return 0

#SUBS
#Purpose: To print different things based on the key pressed
#Input/Parameters: event
#Outputs/Return values: One of two things printed based on the key pressed
def keyPressed(event):
    if event.char == "h":
        c.delete("all")
        diceHand = Hand ()
        diceHand.draw()
        if diceHand.isWinner() == True:
            c.create_text(135,125,tags="all",text="The hand is a winner")
        elif diceHand.isLoser() == True:
            c.create_text(135,125,tags="all",text="The hand is a loser")
        else:
            c.create_text(135,125,tags="all",text="The hand is worth "+str(diceHand.calcPoint())+" point(s)")
    elif event.char == "g":
        c.delete("all")
        wins = 0
        losses = 0
        nothings = 0
        points = 0
        for hands in range (1,10001):
            diceHand = Hand ()
            if diceHand.isWinner() == True:
                wins = wins + 1
            elif diceHand.isLoser() == True:
                losses = losses + 1
            elif diceHand.calcPoint() > 0:
                points = points + 1
            else:
                nothings = nothings + 1
        c.create_text(135,20,tags="all",text="After 10000 Hands:")
        c.create_text(135,50,tags="all",text="Wins: "+str(wins))
        c.create_text(135,70,tags="all",text="Losses: "+str(losses))
        c.create_text(135,90,tags="all",text="Points: "+str(points))
        c.create_text(135,110,tags="all",text="Nothings: "+str(nothings))

#MAIN
root = Tk()
c = Canvas(root,width=275,height=150)
c.bind("<Key>",keyPressed)
c.pack()
c.focus_set()  
mainloop()


         

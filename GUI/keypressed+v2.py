
import random
from tkinter import *

#CLASS HEADER GOES HERE
class Die:
    
    #__INIT__ DOESNT REALLY NEED A HEADER; ITS ALREADY KNOWN
    def __init__(self,value = 0):
        if value <= 0 or value > 6:
            self.value = random.randint(1,6)
        else:
            self.value = value

    def setValue(self,value=1):
        if value >= 1 and value <=6:
            self.value = value
        else:
            self.value = 1

    #METHOD HEADER GOES HERE
    def draw(self,c,x,y):
        c.create_rectangle(x,y,x+80,y+80,width=1,outline="green",fill="white")
        c.create_text(x+40,y+40,text=str(self.value),font=("Arial","32","bold italic"))
        #but instead of displaying the digit value; you'll need to calculate and place DOTS
        #to make it look like a real Die as in the picture in the assignment.
        c.create_oval(x+10,y+10,x+25,y+25,outline="black",fill="black")
        c.create_oval(x+55,y+10,x+70,y+25,outline="black",fill="black")
        c.create_oval(x+55,y+55,x+70,y+70,outline="black",fill="black")
        c.create_oval(x+10,y+55,x+25,y+70,outline="black",fill="black")
        #of course you also need to read the assignment question requirements carefully and
        #make sure that your Die is 'sizeable'; thus the spacing between DOTS and the size of
        #DOTS also changes.

#SUBS=============================================================

def keyPressed(event):
    if event.char == "h":
        print ("An H was pressed")
        testDie = Die()
        testDie.draw(canvas,10,10)
    elif event.char == "g":
        print ("A G was pressed")
        testDie = Die()
        testDie.draw(canvas,30,100)
    else:
        print (event.char , " was pressed")

      
#MAIN=============================================================
        
root = Tk()
root.title ("Dice")
canvas = Canvas(root, width = 640, height = 240)
canvas.config(background = "white")

canvas.bind("<Key>",keyPressed)
canvas.pack()

canvas.focus_set()

mainloop()

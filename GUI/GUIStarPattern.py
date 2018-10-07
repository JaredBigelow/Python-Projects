#Author: Jared Bigelow
#Date: April 2 2015
#Purpose: To put a GUI front end on the star pattern program

#GUI Star Pattern
##################################################################################################
from tkinter import*

#SUBS

#Author: Jared Bigelow
#Date: April 7 2015
#Purpose: To print a square star pattern
#Parameters: Fill and size
#Return Value: None
#-----------------------------------
def  printSquare (fill=0,size=10):
    if fill == 0:
        textbox.insert(INSERT, "\n  ")
        for star in range (1, size + 1):
            textbox.insert(INSERT,"* ")
            for star in range (1, size):
                textbox.insert(INSERT,"* ")
            textbox.insert(INSERT, "\n  ")
    else:
        textbox.insert(INSERT, "\n  ")
        for star in range (1, size + 1):
            textbox.insert(INSERT,"* ")
        textbox.insert(INSERT, "\n  ")
        for star in range (1, size - 1):
            textbox.insert(INSERT,"* ")
            for star in range (2, size):
                textbox.insert(INSERT,"  ")
            textbox.insert(INSERT,"* ")
            textbox.insert(INSERT, "\n  ")
        if size > 1:
            for star in range (1, size + 1):
                textbox.insert(INSERT,"* ")
        textbox.insert(INSERT, "\n  ")
#-----------------------------------

#Author: Jared Bigelow
#Date: April 7 2015
#Purpose: To print a triangle star pattern
#Parameters: Fill and size
#Return Value: None
#-----------------------------------
def  printTriangle (fill=0,size=10):
    if fill == 0:
        textbox.insert(INSERT, "\n  ")
        for size in range (1, size + 1):
            textbox.insert(INSERT,"* ")
            for size in range (1, size):
                textbox.insert(INSERT,"* ")
            textbox.insert(INSERT, "\n  ")
    else:
        numberOne = 0
        numberTwo = 0
        textbox.insert(INSERT, "\n  ")
        if size == 1:
                textbox.insert(INSERT,"* ")
                textbox.insert(INSERT, "\n  ")
        else:
            for star in range (1, 3):
                numberOne = numberOne + 1
                for star in range (1, numberOne + 1):
                    textbox.insert(INSERT,"* ")
                textbox.insert(INSERT, "\n  ")
            if size >2:
                for star in range (1, size - 2):
                    textbox.insert(INSERT,"* ")
                    for star in range (2, size - (size - 3)):
                        numberTwo = numberTwo + 1
                        for star in range (1, numberTwo + 1):
                            textbox.insert(INSERT,"  ")
                    textbox.insert(INSERT,"*","")
                    textbox.insert(INSERT, "\n  ")
                for star in range (1, size + 1):
                        textbox.insert(INSERT,"* ")
                textbox.insert(INSERT, "\n  ")
#-----------------------------------


#Author: Jared Bigelow
#Date: April 10 2015
#Purpose: To clear the textbox
#Parameters: None
#Return Value: None
#-----------------------------------
def clear():
    textbox.delete(1.0,END)
#-----------------------------------

#Author: Jared Bigelow
#Date: April 10 2015
#Purpose: To have help box pop up
#Parameters: None
#Return Value: None
#-----------------------------------   
def showhelp():
    messagebox.showinfo("Help","Select a shape, fill, and size.")
#-----------------------------------


#Author: Jared Bigelow
#Date: April 10 2015
#Purpose: To decide which shape to print
#Parameters: None
#Return Value: None
#-----------------------------------
def draw():
    intShape = shape.get()
    intFill = fill.get()
    intSize = size.get()
    
    if intShape == 0:
        printSquare (intFill,intSize)
    else:
        printTriangle (intFill,intSize)
#-----------------------------------

#MAIN
        
root = Tk()
root.title("Star Pattern")
root.config(width = 677, height = 518)


shapeGroup = LabelFrame(root, text="Shape",padx=22, pady=5)
shapeGroup.place(x=12.5, y=72.5)
fillGroup = LabelFrame(root, text="Fill",padx=25, pady=5)
fillGroup.place(x=12.5,y=170)

Label (root, text="Size:",font=("Arial","10")).place(x=15,y=290)
Label (root, text="Star Pattern",font=("Arial","15")).place(x=18,y=15)

size = Scale (root, from_ = 1, to = 30,resolution = 1,orient = HORIZONTAL)
size.place(x=20,y=312.5)

shape = IntVar(0)
fill = IntVar(0)

Radiobutton (shapeGroup,text = "Square",variable = shape, value = 0).grid(row = 0, sticky = W)
Radiobutton (shapeGroup,text = "Triangle",variable = shape, value = 1).grid(row = 1, sticky = W)

Radiobutton (fillGroup,text = "Solid",variable = fill, value = 0).grid(row = 0, sticky = W)
Radiobutton (fillGroup,text = "Hollow",variable = fill, value = 1).grid(row = 1, sticky = W)

textframe = LabelFrame(root)
textframe.place (x=150,y=0)
textbox = Text (textframe, height = 32, width = 63)
textbox.pack(side=LEFT,fill=Y)

scrollbar = Scrollbar(textframe)
scrollbar.pack(side=RIGHT,fill=Y)
textbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=textbox.yview)

drawButton = Button (root, text = "Draw",width = 16, height = 2,command = lambda:draw())
drawButton.place(x=12.5,y=375)

clearButton = Button (root, text = "Clear",width = 16, height = 1,command = lambda:clear())
clearButton.place(x=12.5,y=417.5)

helpButton = Button (root, text = "Help",width = 7, height = 1,command = showhelp)
helpButton.place(x=12.5,y=445)

exitButton = Button (root, text = "Exit",width = 7, height = 1,command = lambda: root.destroy())
exitButton.place(x=75,y=445)



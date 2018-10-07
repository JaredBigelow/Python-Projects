#Author:Jared Bigelow
#Date: March 31 2015
#Purpose: To put a GUI front end on an existing program

#GUI Permutations and Combinations
##################################################################################################
from tkinter import*

#SUBS

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
#Date: March 31 2015
#Purpose: To get both numbers and decide which calculation to use
#Parameters: None
#Return Value: None
#-----------------------------------
def calculate():
    strNumber1 = number1.get()
    strNumber2 = number2.get()
    if strNumber1.isdigit() and strNumber2.isdigit():
        if num.get() == 0:
            a = calcPermutations (int(strNumber1),int(strNumber2))
            a = int (a)
            answer.set ("Permutations = " + str(a))
        else:
            a = calcCombinations(int(strNumber1),int(strNumber2))
            a = int (a)
            answer.set ("Combinations = " + str(a))
    else:
        answer.set ("Incorrect Input")
#-----------------------------------
        
#MAIN

root = Tk()
root.title("Permutations and Combinations")
root.config(width = 225, height = 225)

number1 = StringVar()
number1.set (value = "0")
number2 = StringVar()
number2.set(value = "0")
num = IntVar(0)
answer = StringVar()
answer.set(value = " ")

Label (root, text="First Number:").place(x=12.5,y=12.5)
Label (root, text="Second Number:").place(x=12.5,y=50)

Entry (root, width = 8, textvariable = number1).place(x=112.5,y=12.5)
Entry (root, width = 8, textvariable = number2).place(x=112.5,y=50)

Radiobutton (root,text = "Permutations",variable = num, value = 0).place(x=12.5,y=87.5)
Radiobutton (root,text = "Combinations",variable = num, value = 1).place(x=112.5,y=87.5)

Button (root, text = "Calculate", width = 18,height = 2,command = lambda:calculate()).place(x=37.5,y=125)

Label (root, textvariable = answer,width = 20, height = 2,font=("Arial","11","bold")).place(x=12.5,y=175)

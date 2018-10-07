#Author: Jared Bigelow
#Date: April 20 2015
#Purpose: To demonstrate classes/objects/methods/data elements

##################################################################################################

import random

class Card:
    def __init__(self,rank=2,suit="H"):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return str(self.rank) + self.suit

    def shuffle(self):
        self.rank = random.randint (1,13)
        self.suit = random.choice (["H","C","D", "S"])
        if self.rank ==1:
            self.name = "Ace"
        elif self.rank ==10:
            self.name = "Ten"
        elif self.rank ==11:
            self.name = "Jack"
        elif self.rank ==12:
            self.name = "Queen"
        elif self.rank ==13:
            self.name = "King"
        else:
            self.name = str(self.rank) + " "

    def value (self):
        if self.rank > 1 and self.rank <=10:
            val = self.rank
        elif self.rank == 1:
            val = 1
        else:
            val = 10
        return val
    
#MAIN
testCard = Card ()
testCard.shuffle ()
testOutput = "My card is a " + testCard.__str__()
print (testOutput)
print (testCard.value())

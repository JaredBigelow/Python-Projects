#Author: Jared Bigelow
#Date: March 23 2015
#Purpose: To play a game of Red Dog

#Red Dog
##################################################################################################

import math
import random

#CLASS DEFINITIONS

class TwoCard:
    def __init__(self,card1=0,card2=0):
        self.card1 = card1
        self.card2 = card2

#SUBS

#Author: Jared Bigelow
#Date: March 11 2015
#Purpose: To get a positive integer
#Parameters: Prompt, low, high
#Return Value: Positive Integer
#-----------------------------------
def  getPositiveInteger (prompt="Please enter a positive integer", low=0,high=100):
    intNumber = low -1
    while (intNumber < low or intNumber > high):
        strNumber = input (prompt+" between "+str(low)+" and "+str(high)+": ")
        #while not str.isdigit (strNumber):
            #strNumber = input ("Invalid. Please enter a positive integer between "+str(low)+" and "+str(high)+": ")
        intNumber = int (strNumber)
    return intNumber
#-----------------------------------

#Author: Jared Bigelow
#Date: March 23 2015
#Purpose: To get a random number between 2 and 14
#Parameters: None
#Return Value: Random number between 2 and 14
#-----------------------------------
def  getCard (): 
    card = random.randint (2,14)
    return card
#-----------------------------------

#Author: Jared Bigelow
#Date: March 24 2015
#Purpose: To get a two card object
#Parameters: Card 1 and card 2
#Return Value: Two card object
#-----------------------------------
def  getHand(): 
    card1 = getCard ()
    card2 = getCard ()
    hand = TwoCard (card1,card2)
    return hand
#-----------------------------------


#Author: Jared Bigelow
#Date: March 24 2015
#Purpose: To print the two integers of a two card object
#Parameters: Two card object
#Return Value: None
#-----------------------------------
def  printHand(hand): 
    print ("Hand:",hand.card1,hand.card2)
#-----------------------------------


#Author: Jared Bigelow
#Date: March 24 2015
#Purpose: To get the type of hand
#Parameters: Two card object
#Return Value: Type of hand
#-----------------------------------
def  handType(hand): 
    if hand.card1 == hand.card2:
        handType = "Pair"
    elif (hand.card1+1) == hand.card2 or (hand.card1-1) == hand.card2:
        handType = "Consecutive"
    else:
        handType = "Non-Consecutive"
    return handType
#-----------------------------------


#Author: Jared Bigelow
#Date: March 25 2015
#Purpose: To get the spread of a two card object
#Parameters: Two card object
#Return Value: Spread of the hand
#-----------------------------------
def  spread(hand): 
    if hand.card1 < hand.card2:
        hand.card1,hand.card2 = hand.card2,hand.card1
    if hand.card1 > hand.card2:
        spread = hand.card1 - hand.card2 - 1
    else:
        spread = 0
    return spread
#-----------------------------------


#Author: Jared Bigelow
#Date: March 25 2015
#Purpose: To get the payout of a two card object
#Parameters: Two card object
#Return Value: Payout of the hand
#-----------------------------------
def  payout(hand): 
    handSpread = spread (hand)
    if handSpread == 1:
        payout = 5
    elif handSpread == 2:
        payout = 4
    elif handSpread == 3:
        payout = 2
    elif handSpread > 3:
        payout = 1
    return payout
#-----------------------------------


#Author: Jared Bigelow
#Date: March 25 2015
#Purpose: To see if a third card is between a two card object
#Parameters: Two card object and a third card
#Return Value: True or false
#-----------------------------------
def  between(hand,card3): 
    if card3 > hand.card1 and card3 < hand.card2 or card3 < hand.card1 and card3 > hand.card2:
        between = True
    else:
        between = False
    return between
#-----------------------------------

#MAIN

purse = 100
print ("Purse:",purse)
while purse > 0:
    bet = getPositiveInteger ("Bet",1,purse)
    hand1 = getHand ()
    printHand (hand1)
    hand1Type = handType (hand1)
    if hand1Type == "Pair":
        thirdCard = getCard ()
        print ("Third Card:",thirdCard)
        handBetween = between (hand1,thirdCard)
        if handBetween == True:
            purse = purse + bet * 11
            print ("You win")
        else:
            print ("It's a tie")
    if hand1Type == "Consecutive":
        print ("It's a tie")
    if hand1Type == "Non-Consecutive":
        if bet > (purse - bet):
            smallest = purse - bet
        else:
            smallest = bet
        additionalBet = getPositiveInteger ("Additional bet",0,smallest)
        bet = bet + additionalBet 
        thirdCard = getCard ()
        print ("Third Card:",thirdCard)
        handBetween = between (hand1,thirdCard)
        handPayout = payout (hand1)
        if handBetween == True:
            purse = purse + bet *  handPayout
            print ("You win")
        else:
            purse = purse - bet
            print ("You lose")
    print ("Purse:",purse)
print ("GAME OVER")

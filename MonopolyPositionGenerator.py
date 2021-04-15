# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 03:12:59 2020

@author: jackb
"""

import random 
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

def roll():
    dice = []
    for i in range(2):
        dice.append(random.randint(1,6))
    return dice

#Initialize empty board
board = [0 for i in range(40)]
start = 0

def turn(index):
    counter = 0
    rollAgain = True
    
    while (rollAgain == True):
        ds = roll()
        
        if ds[0] == ds[1]:
            counter += 1
            if counter >= 3:
                index = 10
                board[index] += 1
                break
            else:
                index += sum(ds)
                rollAgain = True
                index = index % len(board)
                board[index] += 1

        else:
            index += sum(ds)
            rollAgain = False
            index = index % len(board)
            board[index] += 1
    
    return index

spaces = []
n = 50
index = start
for i in range(n):
    index = turn(index)
    spaces.append(index)

print(board)

df=pd.DataFrame({'x': [i for i in range(n)], 'Positions': spaces})
 
# multiple line plot
plt.plot( 'x', 'Positions', data=df, marker='', color='blue', linewidth=2)

def drawCard(index):
    p = 1/16
    s = np.random.binomial(1, p, 1)
    if s == 1:
        index, inJail = Jail, True
    return index, inJail
    

'''
totalRolls = 50

#Positions to draw a card
cardSpaces = [2,7,17,22,33,36]

#Determine if player is in jail
inJail = False

#Go to jail space
goJail = 29

#Jail space
Jail = 10

#Start at beginning
index = 0
for i in range(totalRolls):
    #Move index
    roll,doubles = rollDice(2)
    index += roll
    if doubles == True:
        
    
    elif index == goJail:
        index, inJail = Jail, True
    
    elif index in cardSpaces:
        index, inJail = drawCard(index)
        
'''
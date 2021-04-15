# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 16:32:02 2020

@author: jackb
"""
import matplotlib.pyplot as plt
import pandas as pd
#import numpy as np
import random as rn

board = [0 for i in range(40)]

print(board)
position = 0
probBoard = []
benchmarkedBoard = []

numRolls = 1000         #Enter number of rolls to simulate
benchmarkRate = .1      #Enter value between 0 and 1, smaller means more intervals
benchMod = int(numRolls*benchmarkRate)
change = []
avgChanges = []
counts = []
boards =[]
boards.append(board)
for i in range(numRolls):
    roll1 = rn.randint(1,6)
    roll2 = rn.randint(1,6)
    tRoll = roll1 + roll2
    moded = (tRoll+position) % len(board)
    board[moded] += 1
    position = moded
    
    if i>0:
        if i % benchMod == 0:
            count = i
            counts.append(count)
            benchmarkedBoard = [board[j]/count for j in board]
            #Subtract benchmark board from last benchmark
            change = [a_i - b_i for a_i, b_i in zip(benchmarkedBoard, boards[len(boards) - 1])]
            boards.append(benchmarkedBoard)
            avgChange = sum(change)/len(change)
            avgChanges.append(avgChange)

        

for i in board:
    probBoard.append(board[i]/numRolls)
print(probBoard)


# Put data into Pandas Df
df=pd.DataFrame({'x': counts, 'Average Changes': avgChanges})
 
# multiple line plot
plt.plot( 'x', 'Average Changes', data=df, marker='', color='blue', linewidth=2)

plt.legend()
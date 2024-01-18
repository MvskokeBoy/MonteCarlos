# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 16:46:29 2020

@author: DeAngelo
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy import random
from random import randint


plays = 1000000 # 1 play cost $5


win_array = []
lose_array = []
retry_array = []
win_from_retry = []
lose_re = []





def throwdice(): # I am creating a function that throws a random dice
   # Throw dice
  random_number = randint(MIN, MAX)
  return random_number   



MIN = 1
MAX = 6


  

 
        

    
# PASS LINE
for i in range(0,plays,1): #does this for loop (n - plays) times, in increments of 1 
    rand_dice_1 = throwdice()
    rand_dice_2 = throwdice()
    rand_sum = rand_dice_2 + rand_dice_1
    first =  rand_sum
    if rand_sum == 7 or rand_sum == 11: #you have to physically type the word 'and' or 'or' for a comparsion statement
       win_array.append([1])
       #print(rand_sum,'win')
       #print("this is a win",'\n')
    elif rand_sum==2 or rand_sum==3 or rand_sum==12:
        #print(rand_sum,"lost")
        lose_array.append([1])
        #print("this is a lost 2 or 3 or 12",'\n')
    #step up for point
    else:
    # add that portion from your other code.
        #print(rand_sum,'You retry')
        first_rand_sum = rand_sum
        continued_rolls = 0
        retry_array.append([1])
        # Establish point
        while first_rand_sum != continued_rolls and continued_rolls != 7: #This needs to be nested within the else statement for the win retrys and lose retries to work properly
          continued_roll_1 = throwdice()
          continued_roll_2 = throwdice()
          continued_rolls = continued_roll_1 + continued_roll_2
    # Seven out: PASS LINE looses (point established)
        if continued_rolls == 7 :   
            #print(continued_rolls,'lose from retry') #Double checking to make sure that it works
            lose_re.append([1])
            #print('You lost from retry')
    # PASS LINE wins (point established)
        elif continued_rolls == first_rand_sum:
            #print(continued_rolls,'Win from retry')
            win_from_retry.append([1])
            #print('You win from retry')
           




how_many_wins = len(win_array)
how_many_loses = len(lose_array)
how_many_retries = len(retry_array)
how_many_wins_from_retry = len(win_from_retry)
how_many_loses_from_retry = len(lose_re)

print('\n',how_many_wins,how_many_loses,how_many_retries,how_many_wins_from_retry,how_many_loses_from_retry,"Comparision",'\n')


performace =[how_many_wins,how_many_loses] 

        
        
outcome = ('wins','loses','retry' ,'wins retry','lose retry')    



rects1 = plt.bar(outcome[0],how_many_wins)
rects2 = plt.bar(outcome[1],how_many_loses)
rects3 = plt.bar(outcome[2],how_many_retries)
rects2 = plt.bar(outcome[3],how_many_wins_from_retry,color='gold')
rects2 = plt.bar(outcome[4], len(lose_re), color='red')
plt.title("Simulation of Casino Game Craps",color='red',fontweight='bold')
plt.show()



print("Win prob -->", (how_many_wins/plays)*100,"%")
print("Lose prob -->", (how_many_loses/plays)*100,"%")
print("Retry prob -->", (how_many_retries/plays)*100,"%")
print("Win from retry prob -->", (how_many_wins_from_retry/how_many_retries)*100,"%")
print("Lose from retry prob -->", (how_many_loses_from_retry/how_many_retries)*100,"%")



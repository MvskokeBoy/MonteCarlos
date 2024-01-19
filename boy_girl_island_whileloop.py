# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 16:16:23 2024

@author: 13232
"""


import random
from random import randint
import math 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt 
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt; plt.rcdefaults()
import seaborn as sns


endpoint =5000

girl =np.array([])
boy =np.array([])


for i in range(0,endpoint):
    probability = random.uniform(0,100) # This creates a random number from 0 to 100
    while probability <= 52:
        girl = np.append(girl,1) #if girl append 1
        probability = random.uniform(0,100)
    else:
        boy = np.append(boy, 1 ) #if boy append 1
        
total_girls = len(girl)
total_boys = len(boy)
        
print("girl",len(girl))
print("boy",len(boy))


print("ratio of girls to boys", total_girls/total_boys)

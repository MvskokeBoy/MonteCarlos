# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 20:32:32 2019

@author: DeAngelo
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


PI = 3.1415926
e = 2.71828


#this will be the code for 3 possible types of decay

#For everygamma you will have a seperate for loop


#IT Stands for internal transition ignore this. You only want beta decay chain and look for gammas you should mutilpy the percentage by whats under the decay mode





x=100 #End point for range

Gamma = [] #Create list for all gammas

U238gamma = []

for i in range(0,x):
     roll  = random.uniform(0,100) #Counting 0-100,Endpoints are included. Has to be a flot random generator
     if roll <=7.3: #percentage of happening
         Gamma.append(13) #I put the number 13 into this array,because that is what Kev level corresponds to it I do this with each subsequential gamma ray emmsion. "Or just the next for loop" :)
         
         
for i in range(0,x):
     roll  = random.uniform(0,100) #Counting 0-100,Endpoints are included. Has to be a flot random generator
     if roll <=0.064: #percentage of happening
         Gamma.append(49.55)#Corresponding Kev value

     
for i in range(0,x):
          roll  = random.uniform(0,100) #Counting 0-100,Endpoints are included. Has to be a flot random generator
          if roll <=.00068:
              Gamma.append(89.957)#Corresponding Kev value


for i in range(0,x):
          roll  = random.uniform(0,100) #Counting 0-100,Endpoints are included. Has to be a flot random generator
          if roll <=0.0011: #percentage of happening
              Gamma.append(93.35)#Corresponding Kev value

for i in range(0,x):
          roll  = random.uniform(0,100) #Counting 0-100,Endpoints are included. Has to be a flot random generator
          if roll <=0.000136: #percentage of happening
              Gamma.append(104.819)#Corresponding Kev value

for i in range(0,x):
          roll  = random.uniform(0,100) #Counting 0-100,Endpoints are included. Has to be a flot random generator
          if roll <=0.00026:
              Gamma.append(105.604)

for i in range(0,x):
          roll  = random.uniform(0,100) #Counting 0-100,Endpoints are included. Has to be a flot random generator
          if roll <=0.000055:
              Gamma.append(108.582)
              
for i in range(0,x):
          roll  = random.uniform(0,100) #Counting 0-100,Endpoints are included. Has to be a flot random generator
          if roll <=0.0102:
              Gamma.append(113.5)


Th234gamma = []



for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=7.1:#percentage of happening
        Gamma.append(13.3)#Coressponding energy in Kev
        
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=3.7:
        Gamma.append(63.29)
        
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=2.13:
        Gamma.append(92.38)
        
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=2.10:
        Gamma.append(92.80)
        
#For 234Pa there was no chance of a gamma emission over 1%
        
U234gamma_13 = []

for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=10:#percentage
        Gamma.append(13)#Coressponding energy in Kev
        
        
TH230gamma_12_3 = []

for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=7.7:#percentage
        Gamma.append(12.3)#Coressponding energy in Kev
        
        
Ra230gamma_186_211 = []

for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=3.64:#percentage
        Gamma.append(186.211)#Coressponding energy in Kev
        
        
        
        
pb214gamma=[]

for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=12:#percentage
        Gamma.append(10.8)#Coressponding energy in Kev
        
        
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=1.075:
        Gamma.append(53.2284)
        
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=5.8:
        Gamma.append(74.815)
        
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=9.7:
        Gamma.append(77.107)
    
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=1.17:
        Gamma.append(86.83)
        
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=2.24:
        Gamma.append(87.349)
        
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=7.251:
        Gamma.append(241.9950)
        
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=18.42:
        Gamma.append(295.2228)
        
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=35.60:
        Gamma.append(351.9321)
        
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=1.06:
        Gamma.append(1.06)
        
       
        
        

Bi214gamma=[]


for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=15.3:#percentage
        Gamma.append(1764.491) #Energy in Kev
        
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=1.160:
        Gamma.append(2118.514)
        
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=4.924:
        Gamma.append(2204.059)
        
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=1.548:
        Gamma.append(2447)
        
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=2.878:
        Gamma.append(1729.595)
        
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=1.047:
        Gamma.append(1661.274)
        
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=2.130:
        Gamma.append(1509.210)
        
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=2.394:
        Gamma.append(1407.988)
        
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=1.330:
        Gamma.append(1401.515)
        
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=3.988:
        Gamma.append(1377.669)
        
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=1.434:
        Gamma.append(1280.976)
        
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=5.834:
        Gamma.append(1238.122)
        
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=1.633:
        Gamma.append(1155.210)
        
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=14.92:
        Gamma.append(1120.294)
        
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=3.107:
        Gamma.append(934.056)
        
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=1.264:
        Gamma.append(806.180)
        
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=4.894:
        Gamma.append(786.360)
        
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=1.531:
        Gamma.append(665.447)
        
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=45.49:
        Gamma.append(609.320)
        
#None for Po214

Pb210gamma = []

for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=22.7:#percentage
        Gamma.append(10.8)#Coressponding energy in Kev
        
        

for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=4.25:
        Gamma.append(46.539)
        

Bi210gamma = []

for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=5.69:#percentage
        Gamma.append(10.3)#Coressponding energy in Kev
        

for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=3.76:
        Gamma.append(70.832)
             

for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=6.3:
        Gamma.append(72.873)
             
       
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=1.46:
        Gamma.append(82.574)
             
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=51:
        Gamma.append(265.6)
             
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=28:
        Gamma.append(304.6)
             
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=3.4:
        Gamma.append(649.6)
        
#Po210 no gammas have above a 1% chance of being emitted.
        """
pb206Gamma = []

# The problem was I added the decays for pb206 and Profssor svoboda didnt

for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=6.4:#percentage
        Gamma.append(10.6)#Coressponding energy in Kev
        
             
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=4.09:
        Gamma.append(72.805)
             
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=6.8:
        Gamma.append(74.969)
             
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=1.58:
        Gamma.append(84.938)
             
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=28:
        Gamma.append(343.51)
             
        
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=91:
        Gamma.append(516.18)
             
        
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=29:
        Gamma.append(537.47)
             
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=98:
        Gamma.append(803.06)
        
for i in range(0,x):
    roll = random.uniform(0,100)
    if roll <=67:
        Gamma.append(880.98)
             

"""



Gamma_60kev_threshold = [i for i in Gamma if i >=60] #This creats the Gamma list and removes all values below 60kev
Gamma_80kev_threshold = [i for i in Gamma if i >=80]
Gamma_100kev_threshold = [i for i in Gamma if i >=100]
Gamma_200kev_threshold = [i for i in Gamma if i >=200]
Gamma_300kev_threshold = [i for i in Gamma if i >=300]
Gamma_400kev_threshold = [i for i in Gamma if i >=400]
Gamma_500kev_threshold = [i for i in Gamma if i >=500]
Gamma_600kev_threshold = [i for i in Gamma if i >=600]
Gamma_700kev_threshold = [i for i in Gamma if i >=700]
Gamma_800kev_threshold = [i for i in Gamma if i >=800]
Gamma_900kev_threshold = [i for i in Gamma if i >=900]
Gamma_1000kev_threshold = [i for i in Gamma if i >=1000]
Gamma_1100kev_threshold = [i for i in Gamma if i >=1100]
Gamma_1200kev_threshold = [i for i in Gamma if i >=1200]
Gamma_1300kev_threshold = [i for i in Gamma if i >=1300]
Gamma_1400kev_threshold = [i for i in Gamma if i >=1400]
Gamma_1500kev_threshold = [i for i in Gamma if i >=1500]
Gamma_1600kev_threshold = [i for i in Gamma if i >=1600]
Gamma_1700kev_threshold = [i for i in Gamma if i >=1700]
Gamma_1800kev_threshold = [i for i in Gamma if i >=1800]
Gamma_1900kev_threshold = [i for i in Gamma if i >=1900]
Gamma_2000kev_threshold = [i for i in Gamma if i >=2000]

#print(Gamma, "<--This is all gammas", "\n") #This will show all gamma rays emitted from list

#print (Gamma_60kev_threshold,"<-- This is how many gammas you have above 60kev", "\n") #This will create list from gamma list,but everything 60 and below will be removed




Total_gammas_above60kev = len(Gamma_60kev_threshold) #Creates new varible that stores all counted elements in list, this will not have 60 or anything below that
print(len(Gamma_60kev_threshold),"<--This is how many elements are in your list with 60kev threshold","\n")

Total_gammas_above80kev = len(Gamma_80kev_threshold) 
print(len(Gamma_80kev_threshold),"<--This is how many elements are in your list with 80kev threshold","\n")

Total_gammas_above100kev = len(Gamma_100kev_threshold) 
print(len(Gamma_100kev_threshold),"<--This is how many elements are in your list with 100kev threshold","\n")

Total_gammas_above200kev = len(Gamma_200kev_threshold) 
print(len(Gamma_200kev_threshold),"<--This is how many elements are in your list with 200kev threshold","\n")

Total_gammas_above300kev = len(Gamma_300kev_threshold) 
print(len(Gamma_300kev_threshold),"<--This is how many elements are in your list with 300kev threshold","\n")

Total_gammas_above400kev = len(Gamma_400kev_threshold) 
print(len(Gamma_400kev_threshold),"<--This is how many elements are in your list with 400kev threshold","\n")

Total_gammas_above500kev = len(Gamma_500kev_threshold) 
print(len(Gamma_500kev_threshold),"<--This is how many elements are in your list with 500kev threshold","\n")


Total_gammas_above600kev = len(Gamma_600kev_threshold) 
print(len(Gamma_600kev_threshold),"<--This is how many elements are in your list with 600kev threshold","\n")

Total_gammas_above700kev = len(Gamma_700kev_threshold) 
print(len(Gamma_700kev_threshold),"<--This is how many elements are in your list with 700kev threshold","\n")

Total_gammas_above800kev = len(Gamma_800kev_threshold) 
print(len(Gamma_800kev_threshold),"<--This is how many elements are in your list with 800kev threshold","\n")

Total_gammas_above900kev = len(Gamma_900kev_threshold) 
print(len(Gamma_900kev_threshold),"<--This is how many elements are in your list with 900kev threshold","\n")

Total_gammas_above1000kev = len(Gamma_1000kev_threshold) 
print(len(Gamma_1000kev_threshold),"<--This is how many elements are in your list with 1000kev threshold","\n")

Total_gammas_above1100kev = len(Gamma_1100kev_threshold) 
print(len(Gamma_1100kev_threshold),"<--This is how many elements are in your list with 1100kev threshold","\n")

Total_gammas_above1200kev = len(Gamma_1200kev_threshold) 
print(len(Gamma_1200kev_threshold),"<--This is how many elements are in your list with 1200kev threshold","\n")

Total_gammas_above1300kev = len(Gamma_1300kev_threshold) 
print(len(Gamma_1300kev_threshold),"<--This is how many elements are in your list with 1300kev threshold","\n")

Total_gammas_above1400kev = len(Gamma_1400kev_threshold) 
print(len(Gamma_1400kev_threshold),"<--This is how many elements are in your list with 1400kev threshold","\n")

Total_gammas_above1500kev = len(Gamma_1500kev_threshold) 
print(len(Gamma_1500kev_threshold),"<--This is how many elements are in your list with 1500kev threshold","\n")

Total_gammas_above1600kev = len(Gamma_1600kev_threshold) 
print(len(Gamma_1600kev_threshold),"<--This is how many elements are in your list with 1600kev threshold","\n")

Total_gammas_above1700kev = len(Gamma_1700kev_threshold) 
print(len(Gamma_1700kev_threshold),"<--This is how many elements are in your list with 1700kev threshold","\n")

Total_gammas_above1800kev = len(Gamma_1800kev_threshold) 
print(len(Gamma_1800kev_threshold),"<--This is how many elements are in your list with 1800kev threshold","\n")

Total_gammas_above1900kev = len(Gamma_1900kev_threshold) 
print(len(Gamma_1900kev_threshold),"<--This is how many elements are in your list with 1900kev threshold","\n")





Total_gammas = len(Gamma) #Creates new varible that stores all counted elements in list, this will have all gammas
print (len(Gamma),"<-- This is how many gammas you have with no threshold")


print("Now I will calculate the mass of the uranium 238",'\n')


half_life = 1.41*(10**17)

natural_log = np.log(2)

Activity = x

atomic_mass = 238

Avo_num = 6.02*(10**23)


Mass = (atomic_mass*half_life*Activity)/(Avo_num*natural_log)

print(Mass, "<-- This is the mass in grams with" , x ," number of decays per second","\n")





print ("Your speific activity is ", Total_gammas/Mass , "with no threshold")

print ("Your speific activity is ", Total_gammas_above60kev/Mass , "with 60kev  threshold")

print ("Your speific activity is ", Total_gammas_above80kev/Mass , "with 80kev  threshold")

print ("Your speific activity is ", Total_gammas_above100kev/Mass , "with 100kev  threshold")

print ("Your speific activity is ", Total_gammas_above200kev/Mass , "with 200kev  threshold")

print ("Your speific activity is ", Total_gammas_above300kev/Mass , "with 300kev  threshold")

print ("Your speific activity is ", Total_gammas_above400kev/Mass , "with 400kev  threshold")

print ("Your speific activity is ", Total_gammas_above500kev/Mass , "with 500kev  threshold")

print ("Your speific activity is ", Total_gammas_above600kev/Mass , "with 600kev  threshold")

print ("Your speific activity is ", Total_gammas_above700kev/Mass , "with 700kev  threshold")

print ("Your speific activity is ", Total_gammas_above800kev/Mass , "with 800kev  threshold")

print ("Your speific activity is ", Total_gammas_above900kev/Mass , "with 900kev  threshold")

print ("Your speific activity is ", Total_gammas_above1000kev/Mass , "with 1000kev  threshold")

print ("Your speific activity is ", Total_gammas_above1100kev/Mass , "with 1100kev  threshold")

print ("Your speific activity is ", Total_gammas_above1200kev/Mass , "with 1200kev  threshold")

print ("Your speific activity is ", Total_gammas_above1300kev/Mass , "with 1300kev  threshold")

print ("Your speific activity is ", Total_gammas_above1400kev/Mass , "with 1400kev  threshold")

print ("Your speific activity is ", Total_gammas_above1500kev/Mass , "with 1500kev  threshold")

print ("Your speific activity is ", Total_gammas_above1600kev/Mass , "with 1600kev  threshold")

print ("Your speific activity is ", Total_gammas_above1700kev/Mass , "with 1700kev  threshold")

print ("Your speific activity is ", Total_gammas_above1800kev/Mass , "with 1800kev  threshold")

print ("Your speific activity is ", Total_gammas_above1900kev/Mass , "with 1900kev  threshold")






n_bins = 100
fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)
axs[0].hist(Gamma, bins=n_bins)
axs[1].hist(Gamma_60kev_threshold, bins=n_bins)
axs[0].set_title('Number of decays vs Energy level ')
axs[0].set_xlabel("Energy in Kev (No Threshold)")
axs[0].set_ylabel("Number of decays U-238")
axs[1].set_title('Number of decays vs Energy level')
axs[1].set_xlabel("Energy in Kev(60kev Threshold)")
axs[1].set_ylabel("Number of decays U-238")


plt.yscale('log')
plt.show()


#n_bins = 100
#fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)
#axs[0].hist(Gamma, bins=n_bins)
#axs[1].hist(Gamma_1000kev_threshold, bins=n_bins)

#plt.yscale('log')
#plt.show()

plt.rcParams['figure.figsize'] = (20,30)   #Height and width of figure 900 works,
Thresholds = ('0 kev','60 kev','80 kev','100kev','200kev','300kev','400kev','500kev','600kev','700kev','800kev','900kev','1000kev','1100kev','1200kev','1300kev','1400kev','1500kev','1600kev','1700kev','1800kev','1900kev')
Speific_Activity = [Total_gammas/Mass, Total_gammas_above60kev/Mass, Total_gammas_above80kev/Mass,Total_gammas_above100kev/Mass, Total_gammas_above200kev/Mass,Total_gammas_above300kev/Mass,Total_gammas_above400kev/Mass,Total_gammas_above500kev/Mass,Total_gammas_above600kev/Mass,Total_gammas_above700kev/Mass,Total_gammas_above800kev/Mass,Total_gammas_above900kev/Mass,Total_gammas_above1000kev/Mass,Total_gammas_above1100kev/Mass,Total_gammas_above1200kev/Mass,Total_gammas_above1300kev/Mass,Total_gammas_above1400kev/Mass,Total_gammas_above1500kev/Mass,Total_gammas_above1600kev/Mass,Total_gammas_above1700kev/Mass,Total_gammas_above1800kev/Mass,Total_gammas_above1900kev/Mass]
plt.bar(Thresholds,Speific_Activity, align='center', width=1, edgecolor='black')
plt.xticks(Thresholds,)
plt.yticks(Speific_Activity,fontsize=10)
plt.ylabel('Specific  Avtivity')
plt.title('Specific  Activity vs Kev Thresholds')
#plt.grid(color='black', axis='y')

plt.show()







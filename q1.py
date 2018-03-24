# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 10:36:36 2018 by Apoorva Karn """
#random numbers
import random
from random import randint
a = randrange(0,101)
a = random.sample(range(1,101),100)
a
len(a)
#mean
mean= [sum(a)/len(a)]
mean
a
#minimum
m=min(a)
#maximum
n=max(a)
#median
median= [[a[49]+a[50]/2]]
median
#second minimum
min2=a[0]
for i in a:
    if i < min2 and i > m:
        min2=i
        
min2
#second maximum
max2=a[-1]
for i in a:
    if i > max2 and i < n:
        max2=i
        
max2
#%%

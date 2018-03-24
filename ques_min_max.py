# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 11:10:39 2018 by Apoorva Karn """
from random import randint

random_list = []
for i in range(1,10):
   random_list.append(randint(1,10))

# if I use sort there will be error in case of duplicates
print(sorted(random_list))
print(str(sorted(random_list)[1]) + " " + str(sorted(random_list)[-2]))

#Without sort function ??
print(random_list)
max=0
sec_max = 0
min = 99999999
sec_min = 0
for number in random_list:
   if(number>max):
       sec_max = max
       max = number
   if(number<min):
       sec_min = min
       min = number
   if(number<sec_min and number>min):
       sec_min = number
   if(number> sec_max and number <max):
       sec_max = number
print(str(sec_min) + " " + str(sec_max))



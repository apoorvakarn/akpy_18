# -*- coding: utf-8 -*-
#question 1-----
import random
from random import randint
random.seed(123)
random_list = []
for i in range(1,10):
    random_list.append(randint(1,10))
    
random_list
range(len(random_list))
newlist=random_list[:]
newlist

number =input("enter a number:")
for i in range(len(random_list)):
    newlist[i]=random_list[i-int(number)]
    
    
print(newlist)

#question2------
list=[]
for i in range(0,9):
    number= input("enter a number?")
    list.append(int(number))
list1=sorted(list)
for i in list1:
    print("*" * i)
    


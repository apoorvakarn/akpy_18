# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 10:27:19 2018 by Apoorva Karn """
number = int(input("enter length of pyramid"))
hidden_triangle = number-1
i=1
while(i<=number):
    if(hidden_triangle >0):
        print(hidden_triangle * " ",end=' ')
        hidden_triangle-=1
    print(i* "* ")
    i+=1




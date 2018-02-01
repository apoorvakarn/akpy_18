# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 11:21:04 2018 by Apoorva Karn """
import numpy as np
from numpy import *
import array
l = list(range(10))
a = array.array('i',l)
a
a.shape
type(a)
a.type
np.shape(a)
np.dtype(a)
np.size(a)
a[1]
# array slicing #
a = np.array([[1,2,3],[4,5,6]],float)
print (a)
print (a.shape, "\n", a.itemsize)
print (a.dtype, a.dtype.type)
type(a[0,0]) is type (a[1,2])
# array slicing# views#
b = a[:,::2]
b
c = a[:,::2].copy()
c
c[1,0]= 500
a
c
a = np.arange(0,80,10)
a
y = a[[1,2,-3]]
y
y = np.take(a,[1,2,-3])
y
mask = np.array([0,1,1,0,0,1,0,0],dtype=bool)
mask
y = a[mask]
y
y = np.compress(mask, a)
y
a= arange(0,36)
a.reshape(6,6)
a = (np.arange(36).reshape(6,6))
a
a[(0,1,2,3,4),(1,2,3,4,5)]
a[3:,[0,2,5]]
mask = np.array([1,0,1,0,0,1],dtype=bool)
mask
a[mask,2]
#sum function
a = np.array([[1,2,3],[4,5,6]],float)
a
sum(a)
a.sum()
sum(a, axis=0)#sum columnwise
sum(a, axis=-1)#sum rowwise
a.sum()
a.min()
a.max()
a.max(axis=0)
np.amin(a)
np.amax(a)
a.argmin(axis=0)#functional form
argmin(a,axis=1)#find index of minimum value
argmax(a,axis=0)#find index of maximum value
argmax(a,axis=0)#functional form
a.mean(axis =0)
mean(a,axis = 0)#mean value of each column
average(a,weights=[1,2],axis=0)#avg can also calculate a weighted average
a.std(axis=0)#standard deviation
#clip
#limit values to a range
a.clip(3,5)
#round
#round values in array
#numpy rounds to even ,so 1.5 & 2.5 both round to 2
a = np.array([1.35,2.5,1.5])
a.round()
a.round(decimals=1)
#point to point
#calculate max-min for array along columns
round(a.ptp(axis=0))
a.ptp(axis = None)
#math functions
x = arange(11.)
x
a= (2*pi)/10
a
a*x
x *= a

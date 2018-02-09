# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 11:37:58 2018 by Apoorva Karn """


import numpy
from numpy import *
a = arange(0,80,10)
#fancy indexing
y = a[[1, 2, -3]]
print (y)
mask = array([0,1,0,1,1,1,0,0], dtype=bool)
y = a[mask]
print(y)
#%% spliting of arrays
x =[ 1,2,3,99,3,2,1]
x1,x2,x3 = split(x,[3,5])
print(x1,x2,x3)
#%%np.sum function
a = array([[1,2,3],[4,5,6]],float)
sum(a)
%timeit sum(a)
a.sum()
%timeit a.sum()
#%%creating 2x3 matrix;
m= array([[1,2,3],[4,5,6]],float)
m
#%%find index of maximum value.
m.argmax(axis=None)
m.argmin(axis=0)
m.max(axis=None)
average(m, weights=[1,2],axis=0)
m.mean()
mean(m, axis=0)
average(m,axis=0)
m.std()
m.std(axis=0)
m.var(axis=0)
var(m,axis=0)
#%%clip
#set values <3 equal to 3.
#set values >5 equal to 5.
m.clip(3,5)
m
#%%
m.ptp(axis=0)
m.ptp(axis=None)
m.itemsize
m.flatten()#returns a 1D copy of a multi dimensional array
m.ravel()# same as flatten, but returns a view if possible
id(m)
m.resize((3,2))#resizing
m
m.swapaxes(0,1)#transpose
m.transpose()
m.T
m.squeeze()
m.copy()
m.tolist()
m.tostring()
m
m[0,1]=0
m
m.nonzero()
m.sort(axis=-1)
m

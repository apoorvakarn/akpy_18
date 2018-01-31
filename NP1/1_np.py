# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:26:53 2018 by Apoorva Karn """
import numpy as np
np.__version__
import array
l = list(range(10))
a = array.array('i',l)
a
#integer array
import numpy as np
np.array([1,4,2,5,3])
np.array([3.14,4,2,3])
np.array([1,2,3,4],dtype='float32')
np.array([range(i, i+3) for i in[2,4,6]])
#list comprehension
l = [i for i in range(5)]
l
#creating arrays from scratch
np.zeros(10,dtype = int)
np.ones((3,5),dtype = float)
np.full((3,5),25)
np1=np.arange(0,20,2)
np1
len(np1)
np.random.normal(0,1,(3,3))
np.random.random((3,3))
np.random.randint(0,10,(3,3))
np.random.randint(10,20,(3,2))
np.eye(3)
np.eye(2)
np.empty(3)
np.random.seed(0)
x1=np.random.randint(10,size=6)
x1
x2=np.random.randint(10, size=(3,4))
x2
x3=np.random.randint(10, size=(3,4,5))
x3
x1,x2,x3
x3.ndim
x3.shape
x3.size
x1.shape
x1.ndim
x2.ndim
x2.shape
x3.itemsize
x3.nbytes
x2[0,0]
x2
x2[1,2]
x = np.arange(10)
x
x[:5]
x[2:]
x[4:7]
x[::2]
x[1::2]
x[::-1]
x[5::-2]
x2
x2[:2,:3]
x2[:3,::2]
x2[:3,::2]
x2[:,0]
x2[0:,]
x2[0,0] = 99
x2
z=x2[:2,:2].copy()
z
x2

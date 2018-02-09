# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 15:02:02 2018 by Apoorva Karn """
#%%
%matplotlib inline
import matplotlib.pyplot as plt 
import numpy as np
x= np.linspace(0,10,100)
fig=plt.figure()
plt.plot(x,np.sin(x), '-')
plt.plot(x,np.cos(x), '--')
fig.savefig("my figure.png")
!dir *.png
plt.show()

#%%
%matplotlib inline
plt.subplot(2,1,1)
plt.plot(x, np.sin(x))
plt.subplot(2,1,2)
plt.plot(x, np.cos(x))
#object oriented interface
fig, ax=plt.subplots(3)
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))
ax[2].plot(x, np.tan(x))
fig, ax=plt.subplots(4)
ax[0].plot(x, np.sin(x))
ax[1].plot(x, np.cos(x))
ax[2].plot(x, np.tan(x))
ax[3].plot(x, np.cosec(x))
#%%
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
fig = plt.figure()
ax = plt.axes()
x=np.linspace(0,10,1000)
ax.plot(x,np.sin(x))
#%%
fig, ax=plt.subplots(3)
ax[0].plot((x, np.sin(x - 0)),color ="pink")
ax[1].plot((x, np.cos(x - 1)),color = "g")
ax[2].plot((x, np.tan(x - 2)), color="0.75")
plt.plot(x, np.sin(x), '-g', label='sin(x)')
plt.plot(x, np.cos(x), ':b', label='cos(x)')
plt.axis('equal')
plt.legend();




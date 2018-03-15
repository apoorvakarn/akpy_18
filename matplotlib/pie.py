# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 14:59:02 2018 by Apoorva Karn """
import matplotlib.pyplot as plt
x=[1,2,3]
y=[2,4,1]
plt.plot(x,y)
x1=[1,2,3]
y1=[2,4,1]
x2=[1,2,3]
y2=[4,1,3]
plt.plot(x1,y1 , label='line1')
plt.plot(x2,y2 , label='line2')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('two lines on the same plot')
plt.show()
plt.bar(x1,y1)
plt.bar(x2,y2)
plt.show()
tick_label=['one','two','three']
plt.bar(x1,y1,tick_label= tick_label, width=0.8, color=['red','green'])
#%%
import numpy as np
marks=np.random.uniform(30,100,1000)
marks
np.all(marks >=30)
np.all(marks <100)
range =(20,100)
bins=10
plt.hist(marks,bins,range, color='green', histtype='bar',rwidth=0.8)
plt.xlabel('marks')
plt.ylabel('no of students')
plt.title('histogram 0f marks of student')
plt.show()
#%%
y
activity=['sleep','eat','study']
colors=['red','green','pink']
plt.pie(y)
plt.pie(y,labels=activity ,colors= colors, startangle=70,shadow=True, radius=1,explode=(0.5,0.0,0.0))

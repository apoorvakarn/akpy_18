# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 11:34:24 2018 by Apoorva Karn """
#%%
#marks
import numpy as np
import pandas as pd
rng=np.random.RandomState(42)
rng
marks= pd.Series(rng.randint(50,100,11))
marks
marks.sum()
round(marks.std())
#%%
#dictionary
{'x':1,'y':[1,2]}
dict(x=1,y=[1,2])
#%%
#groupwise
df = pd.DataFrame({'a':rng.randint(1,10,6),'b':rng.randint(1,10,6)})
df
df.mean()
df.mean(axis=0)
df.mean('rows')
df.mean(axis=1)
df.mean('columns')
df.describe()
#%%
#group by
#split - apply - combine
#repeat
['a','b','c']*2
np.repeat(['a','b','c'],2)
np.repeat(['a','b','c'],[1,2,3])
df1=pd.DataFrame({'key':['a','b','c']*2,'data1':range(6),'data2':rng.randint(0,10,6)},columns=['key','data1','data2'])
df1
df1.groupby('key')#nothing will happen
df1.groupby('key').sum()
df1.groupby('key').aggregate(['min','max','median'])
df1.groupby('key').aggregate([np.median,'median'])#error
df1.groupby('key').aggregate({'data1':'min','data2':'max'})
df1.groupby('key').aggregate({'data1':'max','data2':'median'})
df1.groupby('key').aggregate({'data1':'max','data2':['median','min']})
#%%
#filter
df1.filter(items=['key','data1'])
df1.filter(like='2',axis=0)
df1.filter(like='d',axis=1)
round(df1.groupby('key').std())
#%%
#lambda
df1['data2'].mean()
grouped=df1.groupby('key')
df1.groupby('key').filter(lambda x :x['data2'].mean()>4)
grouped.filter(lambda x :x['data2'].mean()>4)
grouped.filter(lambda x :x['data2'].std()>3)
#%%
#examples of lambda
x=2
y=3
product= lambda x,y:x*y
product(x,y)
grouped.transform(lambda x:x - x.mean())
df1
grouped.apply(lambda x: x['data2']*2)
# change the index to key values
df2=df.set_index('key')
df2
newmap= {'a':'pg','b':'msc','c':'bsc'}
newmap
df2.groupby(newmap).sum()
df2.groupby('key').sum()
df2.groupby(str.upper).mean()#str is key value
df2.groupby([str,str.upper,newmap]).mean()
#%%
#stack
df1.groupby('key').sum().unstack()





















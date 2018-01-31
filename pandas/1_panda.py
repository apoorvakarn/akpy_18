# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 14:11:50 2018 by Apoorva Karn """
#pandas
import pandas as pd
pd.__version__
data= pd.Series([0.25,0.5,0.75,1.0])
data
data.index
data[1]
data[3]
data[1:4]
data1=pd.Series([0.25,0.5,0.75,1.0],index=["a","b","c","d"])
data1
data1[2]
pd.Series(2, index =[101,102,103])
pd.Series({2:"a",3:"b"})
pd.Series({2:"a",3:"b"},index=[3,2])
population= [100,200,300]
area= [10,20,30]
states = pd.DataFrame({"population":population,"area":area})
states
pd.DataFrame(population,columns=["population"])
pd.DataFrame(area,columns=["area"])
rollno=[1,2,3]
names=["a","b","c"]
df1=pd.DataFrame(rollno,names,columns=["rollno"])
df1
df1["names"]=names
df1
gender= ["m","m","f"]
df1["gender"]=gender
df1
df2=pd.DataFrame(list(zip(rollno,names,gender)))
df2
df2.columns=["rollno","names","gender"]
df2
pd.DataFrame([{"a":1,"b":2},{"b":2,"c":3}])
import numpy as np
pd.DataFrame(np.random.rand(3,2),columns=["foo","bar"],index=["a","b","c"])
df2
df2.loc[1]
df2.loc[1:3]
df2.iloc[2]
states["area"]
states["population"]
states.area
states.population
states.area is states["area"]
states.pop is states["pop"]
states.T
states.values[0]
states
states.iloc[:2,:2]
states.ix[:2,:2]

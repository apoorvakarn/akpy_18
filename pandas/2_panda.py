# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 13:39:14 2018 by Apoorva Karn """

import pandas as pd
import numpy as np
s = pd.Series([3,7,4,4,0.3],index=["a","b","c","d","e"])
s
df= pd.DataFrame(np.arange(9).reshape(3,3),index=["b","a","c"],columns=["paris","berlin","madrid"])
df
s["b"]
df[1:2]
df["paris"]
df[df["paris"]>4]
df[df["paris"]>1]
df.berlin[df["berlin"]>1]=0
df
df.ix["a","berlin"]
df.ix[["b","c"],"berlin"]
df.drop("c")
df.drop("berlin",axis=1)
s2=pd.Series([0,1,2],index=["a","c","f"])
s2
s+s2
s.add(s2, fill_value=0)
df2= pd.DataFrame(np.arange(12).reshape(4,3),index=["b","e","c","a"],columns=["paris","lisbon","madrid"])
df2
df+df2
#merge, join , concatenate
import numpy
from numpy import *
dic={"data1":arange(7),"keyleft":["b","b","a","c","a","a","b"]}
dic
df1= pd.DataFrame(dic,columns=["data1","keyleft"])
df1
dic1={"data2":arange(4),"key":["a","b","d","a"]}
df2= pd.DataFrame(dic1,columns=["data2","key"])
df2
pd.merge(df1,df2,left_on="keyleft",right_on="key",how="inner")
pd.merge(df1,df2,left_on="keyleft",right_on="key",how="outer")
dic2={"data1":arange(7),"key":["b","b","a","c","a","a","b"]}
dic2
df3= pd.DataFrame(dic2,columns=["data1","key"])
df3
dic3={"data2":arange(4),"key":["a","b","d","a"]}
df4= pd.DataFrame(dic3,columns=["data1","key"])
df4
pd.merge(df3,df4,on="key",how="left")
pd.merge(df3,df4,on="key",how="right")
s.rank()
s.rank(method="first")
s.rank(method= "max", ascending=False)
df.rank()
df.rank(axis=1)
#sorting/ordering
s.sort_index(ascending=False)
df.sort_index(by="berlin")
df
df.max()
df+df.max()
f= lambda x:math.sqrt(x)
df.applymap(f)
df.berlin= df["berlin"].map(f)
df.berlin
#descriptive statsistics
df.describe()
df.cov()
df.corr()
#reindexing
df
df.reindex(["c","b","a","m"])
df.reindex(["c","b","a","m"], fill_value=14)
df.reindex(columns=["noida","berlin","madrid"])#works with only unique index values






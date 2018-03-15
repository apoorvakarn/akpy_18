# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 12:41:00 2018 by Apoorva Karn """

import numpy as np
import pandas as pd
data= pd.read_csv("C:/pyWork/pyProjects/akpy_18/student.csv")
data
data.head()
data.columns
data.dtypes
data.select_dtypes(['object'])
data['rollno'].dtype
del data['Unnamed: 0']
data.columns
data.describe()
data.groupby('course')['sclass'].describe()
data.groupby('sclass').aggregate(['min',np.median, max])
data[['sclass','python','sas']].groupby('sclass').aggregate(['min',np.median,max, np.sum, np.std])
data[['python']]
#%%
data.groupby('course')['hadoop','sas'].aggregate([np.mean,np.median,'min',max])
pd.pivot_table(data,index='course',values=['sas','hadoop'],aggfunc = [np.mean,np.median,min,max])
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
pd.pivot_table(data,index='gender',columns='sclass', values='sas').plot(kind='bar')
#%%
# multiple statistics per group
aggregation={'sas':{'totalsas':'sum','avgsas':'mean'}, 'hadoop':{'meanhadoop':'mean','stdhadoop':'std'}}
data[data['sclass']=='c1'].groupby('gender').agg(aggregation)
data.groupby(['gender','sclass']).agg({'python':[min,max,np.mean]})




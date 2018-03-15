# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 15:38:13 2018 by Apoorva Karn """
#pivot table in python
import numpy as np
import pandas as pd
rollnoL=[101,102,103,104,105,106,107,108,109,110,111]
nameL=["achal","apoorva","goldie","hitesh","kaustav","lalit","meena","shruti","shubham","varun","vijay"]
genderL=["m","f","m","m","m","m","f","f","m","m","m"]
courseL=['pg','pg','pg','pg','msc','pg','pg','pg','msc','bsc','pg']
hadoopL=np.random.randint(71,90,11)
pythonL= np.random.randint(60,90,11)
sasL=np.random.randint(65,85,11)
feesL=np.random.randint(200000,300000,11)
hostelL=[True, False,False,False,True,True,True,False,False,False,True]
df1=pd.DataFrame({'rollno':rollnoL,'name':nameL,'gender':genderL,'course':courseL,'hadoop':hadoopL,'python':pythonL,'sas':sasL,'fees':feesL,'hostel':hostelL},columns=['rollno','name','gender','course','hadoop','python','sas','fees','hostel'])
df1
df1['total'] = df1['hadoop']+df1['python'] +df1['sas']
df1
df1.to_csv("student.csv")
df1.columns
df1.groupby('gender').mean()
df1.groupby('gender').sum()
df1.groupby('gender').median()
df1.groupby('gender').size()
from numpy import random
classes= ['c1','c2','c3']
sclass=random.choice(classes,11)
sclass
df1['sclass']= pd.Series(sclass)
df1
df1.to_csv("student.csv")
pd.pivot_table(df1, index=['name'])
pd.pivot_table(df1, index=['name','sclass','hostel'])
pd.pivot_table(df1, index=['sclass','gender'])
pd.pivot_table(df1, index=['course','sclass'],values=['total','python'])#default is mean
pd.pivot_table(df1, index=['course','gender'],values=['total','python'], aggfunc=np.sum)
pd.pivot_table(df1, index=['course','sclass'],values=['total','python'], aggfunc=[np.sum, np.mean, len])
ss























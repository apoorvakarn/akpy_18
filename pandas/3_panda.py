# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 15:04:13 2018 by Apoorva Karn """
#%%
#creating a list of roll numbers----
rollnoL=[101,102,103,104,105,106,107,108,109,110,111]
nameL=["achal","apoorva","goldie","hitesh","kaustav","lalit","meena","shruti","shubham","varun","vijay"]
genderL=["m","f","m","m","m","m","f","f","m","m","m"]
import numpy as np
pythonL= np.random.randint(60,90,11)
sasL=np.random.randint(65,85,11)
import pandas as pd
student= pd.Series(nameL,index=rollnoL)
student
type(student)
(111) in student
(112) in student
print (student.index)
student.keys()
print( student.iteritems)
student.values
#%%
list(student.items())
student[108]
student[110]= "vjain"
list(student)
student[0:5]
student.iloc[0:5]#
student[107]
student.iloc[0]#implicit
student.loc[107]#explicit
student[0:1]
student.iloc[4:6]
student.loc[102:110]
student.ix[108]
student
#%%
rollno=pd.Series(rollnoL)
name=pd.Series(nameL)
gender=pd.Series(genderL)
sas=pd.Series(sasL)
python=pd.Series(pythonL)
student1=pd.concat([rollno,name,gender,sas,python],axis=1)
student1
#%%
student2=pd.DataFrame({'rollno':rollno,'name':nameL,'gender':genderL,'sas':sasL,'python':pythonL})
student2
df=pd.DataFrame({'rollno':rollnoL,'name':nameL,'gender':genderL,'sas':sasL,'python':pythonL},columns=['rollno','name','gender','sas','python'])
df
df.index=rollno
df
df.T
df.loc[102]
df.iloc[0:1]
df[name]
df.name
df.name[0:2][0:3]
df.iloc[:3,:2]
#%%
df.loc[101:105,:"sas"]
df.iloc[0:5,0:2]
df['total'] = df['python'] +df['sas']
df
df[0:5]
df[df['total']>150]
df.head
df.tail





























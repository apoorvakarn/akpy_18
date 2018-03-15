import numpy as np
import pandas as pd
import csv
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import math
train = pd.read_csv('train.csv')
train.isnull().sum()
train1 = train.fillna(0)
test = pd.read_csv('test.csv')
test.isnull().sum()
test1 = test.fillna(0)
prod2 = list(set(list(train1.Product_ID.unique()) + list(test1.Product_ID.unique())))
dict0 = dict(zip(prod2,range(len(prod2))))
dict1 = dict(zip(list(train1.Gender.unique()),range(len(train1.Gender.unique()))))
dict2 = dict(zip(list(train1.Age.unique()),range(len(train1.Age.unique()))))
dict3 = dict(zip(list(train1.City_Category.unique()),range(len(train1.City_Category.unique()))))
dict4 = dict(zip(list(train1.Stay_In_Current_City_Years.unique()),range(len(train1.Stay_In_Current_City_Years.unique()))))
dict5 = dict(zip(list(train1.User_ID.unique()),range(len(train1.User_ID.unique()))))
train1.loc[:,'Product_ID'] = [dict0[train1.Product_ID.values[i]] for i in range(len(train1))]
train1.loc[:,'Gender'] = [dict1[train1.Gender.values[i]] for i in range(len(train1))]
train1.loc[:,'Age'] = [dict2[train1.Age.values[i]] for i in range(len(train1))]
train1.loc[:,'City_Category'] = [dict3[train1.City_Category.values[i]] for i in range(len(train1))]
train1.loc[:,'Stay_In_Current_City_Years'] = [dict4[train1.Stay_In_Current_City_Years.values[i]] for i in range(len(train1))]
train1.loc[:,'User_ID'] = [dict5[train1.User_ID.values[i]] for i in range(len(train1))]
purchase = train1.Purchase
train1 = train1.drop(['Purchase'],axis=1)
trainer = np.array(train1)
trainer1 = trainer[0:540000]
trainer2 = trainer[540000:]
target = np.array(purchase)
target1 = target[0:540000]
target2 = target[540000:]
userid = test1.User_ID
pid = test1.Product_ID
test1.loc[:,'Product_ID'] = [dict0[test1.Product_ID.values[i]] for i in range(len(test1))]
test1.loc[:,'Gender'] = [dict1[test1.Gender.values[i]] for i in range(len(test1))]
test1.loc[:,'Age'] = [dict2[test1.Age.values[i]] for i in range(len(test1))]
test1.loc[:,'City_Category'] = [dict3[test1.City_Category.values[i]] for i in range(len(test1))]
test1.loc[:,'Stay_In_Current_City_Years'] = [dict4[test1.Stay_In_Current_City_Years.values[i]] for i in range(len(test1))]
test1.loc[:,'User_ID'] = [dict5[test1.User_ID.values[i]] for i in range(len(test1))]
tester = np.array(test1)
model = GradientBoostingRegressor(loss='ls',learning_rate=0.75,n_estimators=390,subsample=1.0,criterion='friedman_mse',min_samples_split=2,min_samples_leaf=1,\
max_depth=3,min_impurity_split=1e-07,init=None,random_state=37,max_features=None,alpha=0.9,verbose=1,max_leaf_nodes=None,warm_start=False,presort='auto')
model = model.fit(trainer1,target1)
scorer = mean_squared_error(target2,model.predict(trainer2))
print(math.sqrt(scorer))
pred = model.predict(tester)
submission = pd.DataFrame(userid,columns=['User_ID'])
submission['Product_ID'] = pid
submission['Purchase'] = pred
submission.to_csv('BlackFriday6.csv',index=False)


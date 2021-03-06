# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 18:18:58 2019

@author: Administrator
"""

# -*- coding: utf-8 -*-
""

import numpy as np
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
import sklearn
from sklearn.metrics import accuracy_score,mean_squared_error,r2_score


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False

df=pd.read_csv("F:/shuju/niu熊.csv",sep=",",engine="python")
df=df[["行使价","期货","买1价"]]
print(df)
X=df.iloc[:,:-1]
y=df['买1价']
print()
sns.pairplot(df, x_vars=["行使价","期货"], y_vars='买1价', size=5, aspect=0.5)
plt.show()

X_train,X_test, y_train, y_test = train_test_split(X,y,test_size=0.7,random_state=50)
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)

linreg = LinearRegression()

model=linreg.fit(X_train, y_train)
print (model)
print("2组线性图中，买1价和行使价对买溢价相关性显著,期货和现货对买溢价的相关性不显著")
#样本返回预测值
print("随机训练7成样本所给的预测值：")
y_pred = linreg.predict(X_test)
print (y_pred)

#输入截距和对应X的斜率
print("所得到的截距为：",linreg.intercept_)
print(linreg.coef_)


r2=linreg.score(X_test,y_test)
print("r2越接近1越拟合,所得到的r2值为",r2)
#绘制真实的数据值和预测值区别
fig,ax=plt.subplots(figsize=(12,4))
ax.plot(range(len(y_test)),sorted(y_test),color="r",label="true")
ax.plot(range(len(y_pred)),sorted(y_pred),color="black",label="predict")
ax.legend(loc="best")
plt.show()

#配对斜率
A=[*zip(X_train.columns,linreg.coef_)]
A=pd.DataFrame(A)
print(A)

#Q求均方差
MSE=mean_squared_error(y_test, y_pred)
print("均方差为:","%.7f" % MSE)


print("最终方程组为:买1价=0.01585520034706494-0.000082*行使价+0.000082*期货")


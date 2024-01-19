import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
from sklearn import datasets
from sklearn.model_selection import train_test_split



df = pd.read_csv(r"C:\Users\shubh\Downloads\1553768847-housing.csv.zip")
print(df)

print(df.isnull().sum())
X = df[["housing_median_age","households"]]
print(X)
y = df["median_house_value"]
print(y)
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0,test_size=0.3)
lr = linear_model.LinearRegression()
lr.fit(X_train,y_train)
c = lr.intercept_
print("The intercept is :: ",c)
m = lr.coef_
print("The coefficient is :: ",m)
y_pred_train = lr.predict(X_train)
print("The prediction of X_train is :: ",y_pred_train)

plt.plot(y_train,y_pred_train)
plt.show()

from sklearn.metrics import r2_score
score = r2_score(y_train,y_pred_train)
print("How accurate is your model :: ",score)

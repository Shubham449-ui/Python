import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
from sklearn import datasets
from sklearn.model_selection import train_test_split

iris = sns.load_dataset('iris')

iris = iris[["petal_length","petal_width"]]

X = iris["petal_length"]
y = iris["petal_width"]

plt.scatter(X,y,color = "red",marker = "*")
plt.xlabel("Petal Length")
plt.ylabel("Petal width")
plt.show()


X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.4,random_state=10)

X_train = np.array(X_train).reshape(-1,1)
y_train = np.array(y_train).reshape(-1,1)

X_test = np.array(X_test).reshape(-1,1)
y_test = np.array(y_test).reshape(-1,1)

lr = linear_model.LinearRegression()
lr.fit(X_train,y_train)

c = lr.intercept_
print("The Intercept is :: ",c)

m = lr.coef_
print("The coefficient is :: ",m)

y_pred_train1 = lr.predict(X_train)

plt.scatter(X_train,y_train)
plt.plot(X_train,y_pred_train1,color = "red")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.show()

y_pred_test1 = lr.predict(X_test)

plt.scatter(X_test,y_test)
plt.plot(X_test,y_pred_test1,color = "red")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.show()

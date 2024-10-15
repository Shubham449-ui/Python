import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix

#import CSV file
df = pd.read_csv(r"D:\train_loan_data.csv")
print(df.head())

print("The Shape of the data :: ",df.shape)
print("\n The Null values in Data :: ",df.isnull().sum())
print(("\n The Columns in Datasets :: ",df.columns))
print("\n Description of Data :: ",df.describe())
print("\n Data Types :: ",df.dtypes)

#Loan ID is unique for each row so we can drop the column 
df.drop(['Loan_ID'],axis = 1,inplace = True)
print(df.head())

#Change object type column into integer type column
labelencoder  = LabelEncoder()
categorical_columns = df.select_dtypes(include=['object']).columns
for col in categorical_columns:
    df[col] = labelencoder.fit_transform(df[col])
print("\n Data Types :: ", df.dtypes)

#Null Values in Data
print("\n The Null values in Data :: ",df.isnull().sum())

for col in df.columns:
    df[col] = df[col].fillna(df[col].mean())
#After Replacing the Null value
print("\n The Null values in Data :: ",df.isnull().sum())

X = df.drop(["Loan_Status"],axis = 1)
y = df["Loan_Status"]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=4)


knn = KNeighborsClassifier(n_neighbors=3)
rfc = RandomForestClassifier(n_estimators=7,criterion="entropy",random_state=7)
svc = SVC()
lc = LogisticRegression()

for clf in (knn,rfc,svc,lc):
    clf.fit(X_train,y_train)
    y_pred = clf.predict(X_train)
    print("Accuracy score of ",clf.__class__," = ",accuracy_score(y_pred,y_train))


for clf in (rfc, knn, svc,lc):
    clf.fit(X_train, y_train)
    Y_pred = clf.predict(X_test)
    print("Accuracy score of ",
          clf.__class__.__name__,"=",
          accuracy_score(y_test,Y_pred))


#As you can see the accuracy score is high for randomforest Classifier and logistic regression so we apply random forest Classifier
rfc = RandomForestClassifier(n_estimators=200,max_depth=15,min_samples_split=5,min_samples_leaf=2,criterion="entropy",random_state=7)
rfc.fit(X_train,y_train)
y_pred = rfc.predict(X_test)
print(accuracy_score(y_pred,y_test))

conf_matrix = confusion_matrix(y_pred,y_test)
print(conf_matrix) #Print the confusion matrix



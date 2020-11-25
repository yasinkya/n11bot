# data process 

#importing dataset
import numpy as np
import pandas as pd

dataset = pd.read_excel("n11_bot.xlsx")
x = dataset.iloc[:,1:10].values
y = dataset.iloc[:,-1].values

#edit missing values
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan ,strategy='most_frequent')
imputer.fit(x[:])
x[:] = imputer.transform(x[:])

#encoding all independent cetegorical values in x
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(sparse =False)
x_ohe = ohe.fit_transform(x)

#splitting into the training and test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test =train_test_split(x_ohe,y,test_size=0.25,random_state=1)

#feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train[:,:]=sc.fit_transform(x_train[:,:])
x_test[:,:] = sc.fit_transform(x_test[:,:])


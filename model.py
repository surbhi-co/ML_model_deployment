
import pandas as pd
import numpy as np


data = pd.read_csv("...\"online_shoppers_intention.csv")
print(data)

# dropping the unwanted columns/columns having vague information

data=data.drop(["PageValues","TrafficType",'OperatingSystems', 'Browser', 'Region'],axis=1)

# The boolean columns to be converted to numerical ones
data["Weekend"]=data["Weekend"].astype(int)
data["Revenue"]=data["Revenue"].astype(int)

# The Categorial columns
#  we will be changing the Visitortype and the Month coulmns to nominal columns by using `get_dummies`
datacopy=pd.get_dummies(data,columns=["VisitorType","Month"])

print(datacopy.columns)
print(datacopy.info)

print(datacopy.shape)

#  Importing the models and evaluation metric tools
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix,classification_report

# mentioning the feature and label
X=datacopy.drop("Revenue",axis=1)
Y=datacopy["Revenue"]

# setting the random state
np.random.seed(42)

# splitting the data into testing and training data sets
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2)

print(X_train.shape,X_test.shape,Y_train.shape,Y_test.shape)

# instantiating the best fit model obtained through hyperparametertuning
rfc_best= RandomForestClassifier(max_depth= None,min_samples_split= 6,n_estimators= 160)
# fitting the model
rfc_best.fit(X_train,Y_train)

# prediction:
Y_preds=rfc_best.predict(X_test)
print(Y_preds.shape)

# Evaluating the model using evaluation metrics
# confusion metrics: this shows where our model got confused
print(confusion_matrix(Y_test,Y_preds))

# evaluating using the classification Report
print(classification_report(Y_test,Y_preds))

#  saving the model
import pickle
pickle.dump(rfc_best,open("online_shopping_model.pkl","wb"))

# loading the model
best_model = pickle.load(open("online_shopping_model.pkl","rb"))


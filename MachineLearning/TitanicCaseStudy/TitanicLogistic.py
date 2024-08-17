from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd

#step1 : load data
titanic_data = pd.read_csv("MarvellousTitanicDataset.csv")
# print(titanic_data)

print("No of passengers are : ",str(len(titanic_data)))

#step2 : clean the  data

titanic_data.drop('zero',axis=1,inplace=True)
# print(titanic_data.head(5))

print(pd.get_dummies(titanic_data["Sex"]))

Sex = pd.get_dummies(titanic_data["Sex"],drop_first=True)

print(Sex.head(5))

Pclass = pd.get_dummies(titanic_data["Pclass"],drop_first=True)

print(Pclass.head(5))


titanic_data = pd.concat([titanic_data,Sex,Pclass],axis=1)
print(titanic_data.head(5))



#drop irrevent columns

titanic_data.drop(['Sex','sibsp','Parch','Embarked'],axis=1,inplace=True)

print(titanic_data.head(5))

titanic_data.columns = titanic_data.columns.astype(str)


x = titanic_data.drop("Survived",axis=1)
y = titanic_data["Survived"]

X_train,X_test, Y_train, Y_test = train_test_split(x,y,test_size=0.5) #50% training amd 50% for testing

logmodel = LogisticRegression()

print("Y_train ::")

print()
print()
print()
print()
print()
print()
print()
print(Y_train)

# print("Y_train",Y_train)


logmodel.fit(X_train,Y_train)
# y_pred = logmodel.predict(X_test)

# print("Classification report of LogisticRegression is :  ")
# print(classification_report(Y_test,y_pred))


# print("Confusion matrix  of LogisticRegression is :  ")
# print(confusion_matrix(Y_test,y_pred))

# print("Accuracy  of LogisticRegression is :  ")
# print(accuracy_score(Y_test,y_pred))








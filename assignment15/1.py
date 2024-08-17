import os.path
from sys import *
import numpy as np 
import pandas as pd 
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def Predictor():
    filename = 'WinePredictor.csv'
    exists = os.path.exists(filename)
    # print("exists",exists)

    if(exists):
        dataFrame  = pd.read_csv(filename)
        # print("dataFrame",dataFrame)

        data = dataFrame.drop(['Class'],axis=1)

        target = dataFrame.Class

        X_train,X_test, Y_train, Y_test = train_test_split(data,target,test_size=0.3) #70% training amd 30% for testing
        print(X_test[0:5],"\n\n\n\n")
        print(X_train[0:5])

        knn = KNeighborsClassifier(n_neighbors=3)

        knn.fit(data,target)

        y_pred = knn.predict(X_test)

        # print('predictions : ',y_pred)
        # print('Y_test : ',Y_test)
        for predict in y_pred:
            if(predict == 1):
                print("Class 1")
            elif predict == 2:
                print("Class 2")
            else:
                print("Class 3")
        
        print("Accuracy : ",CheckAccuracy(data,target)*100,"%")	



def CheckAccuracy(data,target):
    X_train,X_test, Y_train, Y_test = train_test_split(data,target,test_size=0.3) #70% training amd 30% for testing
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train,Y_train)
    y_pred = knn.predict(X_test)
    
    return accuracy_score(Y_test,y_pred)


def main():
    if(len(argv) == 2):
        if(argv[1].lower() == '-h'):
            print("\n\n\t\t........................This is Wine Predictor ........................\n\n")
            print("\n " + argv[0]+ " -h For Help")
            print("\n " + argv[0]+ " -u For Usage")		
            exit()
        
        if(argv[1].lower() == "-u"):
            print("\n <Usage> " + argv[0] )
            exit()
    
    Predictor()

if __name__ == '__main__':
    main()
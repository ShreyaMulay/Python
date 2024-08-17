# run as python3 1.py 'MarvellousInfosystems_PlayPredictor.csv'

import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
import os
from sys import *

def PredictorWithoutInput():
    data_path = 'MarvellousInfosystems_PlayPredictor.csv'
    exists = os.path.exists(data_path)

    if(exists):
        #Step 1: load the data
        data = pd.read_csv(data_path,index_col=0)
        print("size of actual dataset : ",len(data))

        #step 2: clean ,prepare and manupulate the data
        feature_name = ['Wether','Temperature']

        print("Names of features : ",feature_name)

        Wether = data.Wether
        Temperature = data.Temperature
        Play = data.Play

        #creating labelEncoder here

        le = preprocessing.LabelEncoder()

        #converting string labels into number

        wether_encoded = le.fit_transform(Wether)
        print("wether_encoded :",wether_encoded)

        #converting string labels into number

        temperature_encoded = le.fit_transform(Temperature)
    
        print("temperature_encoded :",temperature_encoded)

        label = le.fit_transform(Play)

        print("label :",label)

        #combining weather and temperature into single list of tuple 
        features = list(zip(wether_encoded,temperature_encoded))

        print("features :",features)

        #step 3: train data 

        model = KNeighborsClassifier(n_neighbors=3)

        #train the model using the training sets
        model.fit(features,label)

        #step 4 test the data

        predicted = model.predict([[0,2]]) # 0:Overcast 2: Mild
        print("predicted : ",predicted) 

        if(predicted):
            print("You can play")
        else:
            print("No play")
    else:
        print("No CSV exists")


def ManualInput():
    Wether = []
    Tempearture = []

    Wether = input("Enter the wether ( Sunny Rainy Overcast ',' sepetated ) : ").split(',')
    #print(Wether)
    Tempearture = input("Enter the temperature ( Hot Mild Cool ',' sepetated ) : ").split(',')

    dictionary = {}

    dictionary['Wether'] = pd.Series(Wether)
    dictionary['Tempearture'] = pd.Series(Tempearture)

    return dictionary

def Predictor(data_test):
    data_path = 'MarvellousInfosystems_PlayPredictor.csv'
    exists = os.path.exists(data_path)

    if(exists):
        #Step 1: load the data
        data = pd.read_csv(data_path,index_col=0)
        print("size of actual dataset : ",len(data))

        #step 2: clean ,prepare and manupulate the data
        feature_name = ['Wether','Temperature']

        print("Names of features : ",feature_name)

        Wether = data.Wether
        Temperature = data.Temperature
        Play = data.Play

        #creating labelEncoder here

        le = preprocessing.LabelEncoder()

        #converting string labels into number

        wether_encoded = le.fit_transform(Wether)
        print("wether_encoded :",wether_encoded)

        #converting string labels into number

        temperature_encoded = le.fit_transform(Temperature)
    
        print("temperature_encoded :",temperature_encoded)

        label = le.fit_transform(Play)

        print("label :",label)

        #combining weather and temperature into single list of tuple 
        features = list(zip(wether_encoded,temperature_encoded))

        print("features :",features)

        #step 3: train data 

        model = KNeighborsClassifier(n_neighbors=3)

        #train the model using the training sets
        model.fit(features,label)

        #step 4 test the data

        predicted = model.predict([[0,2]]) # 0:Overcast 2: Mild
        print("predicted : ",predicted) 

        if(predicted):
            print("You can play")
        else:
            print("No play")



    else:
        print("No data found")

def main():
    print("________________________________________________________________")
    if(len(argv) == 2):
        if(argv[1].lower() == '-h'):
            print("\n\n\t\t........................This is Play Predictor........................\n\n")
            print("\n " + argv[0]+ " -h For Help")
            print("\n " + argv[0]+ " -u For Usage")		
            exit()

        if(argv[1].lower() == "-u") :
            print("\n <Usage> " + argv[0] )
            exit()
    
        confirm = input("Do you want automatic input values (Y/N) : ").lower()
        if(confirm == 'y'):
            PredictorWithoutInput()
        else:
            dictionary = ManualInput()
            print(dictionary)
            Predictor(pd.DataFrame(dictionary))

    

if __name__ == '__main__':
    main()

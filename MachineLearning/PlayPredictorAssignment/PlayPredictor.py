import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

def MarvellousPlayPredictor(data_path):

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

def main():
    print()
    print("________________________________________________________________")
    print("________   Play Predictor Application using K Nearest Knighbor Algorithm    _______")
    print()
    MarvellousPlayPredictor('MarvellousInfosystems_PlayPredictor.csv')

if __name__ == '__main__':
    main()

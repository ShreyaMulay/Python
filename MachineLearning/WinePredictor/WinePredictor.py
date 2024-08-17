from sklearn import metrics
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def MarvellousWinePredictor():

    #load the dataser
    wine = datasets.load_wine()

    #print the names of the features
    print(wine.feature_names)

    #print the wine record upto 5 (top 5 records)
    print(wine.data[0:5])

    #print the wine labels (0:Class_0 ,1:Class_1,2:Class_2)
    print(wine.target)

    #split the dataser into training set and test set

    X_train,X_test, Y_train, Y_test = train_test_split(wine.data,wine.target,test_size=0.3) #70% training amd 30% for testing


    #create knn classifier
    knn = KNeighborsClassifier(n_neighbors=3)

    #train the model using training set
    knn.fit(X_train,Y_train)


    #predict the response for test dataset 
    y_pred = knn.predict(X_test)

    #model accuracy ,how often is the classification correct?
    print("Accuracy : ",metrics.accuracy_score(Y_test,y_pred))


def main():
    print()
    print("________________________________________________________________")
    print("________   Wine Predictor Application using K Nearest Knighbor Algorithm    _______")
    print()
    MarvellousWinePredictor()

if __name__ == '__main__':
    main()
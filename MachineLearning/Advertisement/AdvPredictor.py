import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np 
from sklearn import metrics
from sklearn.metrics import mean_squared_error




def MarvellousAdvertisementPredictor(data_path):
    data = pd.read_csv(data_path,index_col=0)
    print("Actual siz eof dataset :  ",len(data))
   
    feature_names = ['TV','Radio','Newspaper']
    print("Feature names : ",feature_names)

    X= data[feature_names]
    Y = data.Sales

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5)

    print("Size of training dataset : ",len(X_train))
    print("Size of testing dataset : ",len(X_test))

    linreg = LinearRegression()

    linreg.fit(X_train,Y_train)

    y_pred = linreg.predict(X_test)

    print("Result of testing : ",y_pred)

    print(np.sqrt(metrics.mean_squared_error(Y_test,y_pred)))


def main():
    MarvellousAdvertisementPredictor('Advertising.csv')


if __name__ == '__main__':
    main()
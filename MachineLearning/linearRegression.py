import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt


def MarvellousPredictor():

    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]


    print("Value of  Independent  variable x :",X)
    print("Value of  dependent  variable x :",Y)

    #Latest square method
    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    print("Mean of Independent  variable x :",mean_x)
    print("Mean of dependent  variable x :",mean_y)
    n = len(X)

    numerator = 0
    denominator = 0

    # equation of line is y = mx+c

    for i in range(n):
        numerator += (X[i] -mean_x)*(Y[i] - mean_y)
        
        denominator += (X[i] - mean_x)**2

    m = numerator / denominator

    # c = y' - mx'


    c = mean_y - (m * mean_x)

    print("Slope of Regression line :",m)
    print("Y intercept is :",c)

    #display plotting of above points
    x = np.linspace(1,6,n)

    y =c + m * x

    plt.plot(x,y,color="blue",label="Regression Line")

    plt.scatter(X,Y,color="red",label="Scatter Plot")

    plt.xlabel('X - Independent Variable')
    plt.ylabel('Y - Dependent Variable')


    plt.legend()
    plt.show()

    #Findness of goodness of fit i.e R2 value

    ss_t = 0
    ss_r = 0

    for i in range(n):
        y_pred = c + m *X[i]
        ss_t +=(Y[i] -mean_y) ** 2
        ss_r +=(Y[i] -y_pred) ** 2
    
    r2 = 1 - (ss_r/ss_t)

    print("Goodness of fit using R2 meathos is :",r2)



    

def main():
    print("--------Marvellous Infosystem---------")
    print("--------Supervised Machine Learning---------")
    print("--------Linear Regression---------")

    MarvellousPredictor()




if __name__ == "__main__":
    main()
from sklearn import tree

def main():
    print("Ball classification case study")

    #feature encoding
    Features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1]]


    #label encoding
    Labels = [1,1,2,1,2,1,2,1,2,1]

    #Decide the algorithm here
    obj = tree.DecisionTreeClassifier()


    #train the model
    obj = obj.fit(Features,Labels)

    #test the model
    print(obj.predict([[96,0]]))
    print(obj.predict([[43,1]]))

if __name__ == "__main__":
    main()

from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.model_selection  import train_test_split
from sklearn.metrics import accuracy_score



def main():
    print("-----------Iris flower classification case study-----------")

    iris = load_iris()

    # print(iris)
    # print(type(iris))
    # print(shape(iris))



    Features = iris.data
    Labels = iris.target


    print("Features are : ", Features)
    print("LAbeks are : ", Labels)

    data_train,data_test,target_train,target_test = train_test_split(Features, Labels,test_size=0.5)

    obj = tree.DecisionTreeClassifier()

    obj = obj.fit(data_train, target_train)

    output = obj.predict(data_test)

    print(output)

    print(accuracy_score(target_test, target_train)*100)







if __name__ == '__main__':
    main()
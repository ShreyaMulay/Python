# 4. Write a program which contains filter), map() and reduce) in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which are even. Map function will calculate its square.Reduce will return addition of all that numbers



from functools import reduce

def main():
    myList = []
    print("How many numbers do u want :")
    n = int(input())

    print("Enter numbers :")
    for i in range(0,n):
        nos = int(input())
        myList.append(nos)

    print("Input List is ** ",myList)

    myFilter = list(filter(lambda x: (x % 2 ==0 ), myList))
    print("Even Numbers are  :" ,myFilter)

    myMap = list(map(lambda x: x**2, myFilter))
    print("square of  Number is   :" ,myMap)

    myReduce = reduce(lambda x,y: x+y, myMap)
    print("Addition  of all  numbers   :" ,myReduce)



if __name__ == "__main__":
    main()



Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
List after filter = [2, 4, 4, 2, 8, 10]
List after map = [4, 16, 16,

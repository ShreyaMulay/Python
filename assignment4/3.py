# 3. Write a program which contains filter), map() and reduce) in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. Map function will increase each number by 10. Reduce will return product of all that numbers.

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

    myFilter = list(filter(lambda x: x >= 70 and x <= 90, myList))
    print("Numbers between 70 and 90 are  :" ,myFilter)

    myMap = list(map(lambda x: x+10, myFilter))
    print("increase Numbers by 10   :" ,myMap)

    myReduce = reduce(lambda x,y: x*y, myMap)
    print("product of all  numbers   :" ,myReduce)



if __name__ == "__main__":
    main()


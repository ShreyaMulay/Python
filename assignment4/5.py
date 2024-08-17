# 4. Write a program which contains filter), map() and reduce) in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all prime numbers. Map function should multiply each no  by 2. Reduce will return maximum no from all nus



from functools import reduce

def ChkPrime(No):
    isPrime = True

    if(No <= 1):  
        isPrime = False
    else:
        for i in range(2,int(No / 2) + 1):
            if(No % i == 0):
                isPrime =  False
                break
    
    if(isPrime == True):
        return True
    else:
        return False

def main():
    myList = []
    print("How many numbers do u want :")
    n = int(input())

    print("Enter numbers :")
    for i in range(0,n):
        nos = int(input())
        myList.append(nos)

    print("Input List is ** ",myList)

    # myFilter = list(filter(lambda x: ChkPrime(x), myList)) Or 
    myFilter = list(filter(ChkPrime, myList))

    print("Prime nos  are  :" ,myFilter)

    myMap = list(map(lambda x: x*2, myFilter))
    print("multiplication  of  Number is   :" ,myMap)

    myReduce = reduce(lambda x,y: max(x,y), myMap)
    print("Maximum no is  :" ,myReduce)



if __name__ == "__main__":
    main()

#  5. Write a program which accept one number for user and check whether number is prime or not.

def primeOrNot(No):
    isPrime = True

    if(No <= 1):  
        isPrime = False
    else:
        for i in range(2,int(No / 2)):
            if(No % i == 0):
                isPrime =  False
                break
    
    if(isPrime == True):
        return True
    else:
        return False

def main():
    print("Enter a number")

    key = int(input())

    Result = primeOrNot(key)

    print("Number  is prime : " ,Result)

   
if __name__ == '__main__':
    main()  
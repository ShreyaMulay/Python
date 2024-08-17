# Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.



def Add(Number1,Numebr2):
    Ans = 0
    Ans = Number1 + Numebr2
    return Ans


def main():
    print("Enter first number : ")
    No1 = int(input())

    print("Enter 2nd number : ")
    No2 = int(input())
    
    Result = Add(No1,No2)
    print("Addtion is  : ",Result)


if __name__ == '__main__':
    main()
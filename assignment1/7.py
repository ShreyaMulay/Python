# Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.

def divisibleBy5(Number):
    if(Number % 5 == 0):
        return True
    else:
        return False


def main():
    print("Enter a number : ")
    No = int(input())

    Result = divisibleBy5(No)
    print("No divisible by 5 is  : ",Resultc)
    

if __name__ == '__main__':
    main()
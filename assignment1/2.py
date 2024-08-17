# Write a program which contains one function named as ChkNum which accept one parameter as number. If number is even then it should display "Even number" otherwise display "Odd number" on console.


def ChkNum(Number):
    if(Number % 2 == 0):
        print("Even number")
    else:
        print("Odd number")


def main():
    print("Enter number : ")
    No = int(input())
    ChkNum(No)

if __name__ == '__main__':
    main()
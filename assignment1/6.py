# Write a program which accept number from user and check whether that number is positive or negative or zero.

def check(No):
    if(No > 0):
        print("Number is positive.  ")
    elif(No < 0):
        print("Number is negative.")
    else:
        print("Number is zero. ")


def main():
    print("Enter Number : ")
    Number = int(input())
    check(Number)

if __name__ == '__main__':
    main()
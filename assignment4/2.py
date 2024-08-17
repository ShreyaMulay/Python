# Write a program which contains one lambda function which accepts two parameters and return its multiplication.


def main():
    multiplication = lambda a,b : (a*b)

    print("Enter 1st Number : ")
    n1 = int(input())

    print("Enter 2st Number : ")
    n2 = int(input())

    mult = multiplication(n1,n2)

    print("Multiplication of {} and {} is {} ".format(n1,n2,mult))


if __name__ == "__main__":
    main()

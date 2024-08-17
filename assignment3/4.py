# Write a program which accept N numbers from user and store it into List. Return addition of all prime numbers from that List. Main python file accepts N numbers from user and pass each number to ChkPrimel) function which Is part of our user defined module named as MarvellousNum. Name of the function from main python file should be ListPrime().

from MarvellousNum import *

def ListPrime(numbers):
    sum = 0
    for num in numbers:
        if ChkPrime(num):
            print("number",num)
            sum = sum + num
    return sum

def main():
    list = []
    print("Enter how many numbers do u want")
    n = int(input())
    print("Enter the number")
    for i in range(0, n):
        nos = int(input())
        list.append(nos)

    result = ListPrime(list)
    
    print("Sum of prime numbers:", result)



if __name__ == "__main__":
    main()
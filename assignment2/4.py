# Write a program which accept one number form user and return addition of its factors.

def sumOfFactors(No):
    sum = 0
    for i in range(1,No):
        if(No % i == 0):
            sum = sum + i
    return sum


def main():
    print("Enter a number")

    key = int(input())

    Result = sumOfFactors(key)

    print("Sum of factors" ,Result)

   
if __name__ == '__main__':
    main()  
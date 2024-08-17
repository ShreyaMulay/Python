# Write a program which accept number from user and return addition of digits in that number.

def additionOfDigit(no):
    sum = 0
    while no > 0:
        ld = no % 10
        sum = sum + ld
        no //= 10
    
    return sum

    
def main():
    print("Enter a number")

    Key = int(input())

    result = additionOfDigit(Key)
    print("addition   of digit  : ",result)


   
if __name__ == '__main__':
    main()  
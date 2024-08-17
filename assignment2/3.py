#  Write a program which accept one number from user and return its factorial.

def main():
    print("Enter a number")

    no = int(input())

    result = 1
    if(no == 0 or no == 1):
        print(result)
    else:
        for i in range(2, no + 1):
            result *= i
        print(result)

   
if __name__ == '__main__':
    main()  
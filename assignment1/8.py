# Write a program which accept number from user and print that number of "*" on screen.

def main():
    print("Enter a Number : ")
    No = int(input())
    for i in range(No):
        print("*" , end=" ")


if __name__ == '__main__':
    main()  
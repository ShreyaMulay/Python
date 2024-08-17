# Write a program which accept N numbers from user and store it into List. Return Maximum and Minimum number from that List.

def main():
    list = []
    print("Enter how many numbers do u want")
    n = int(input())
    print("Enter the number")
    for i in range(0, n):
        nos = int(input())
        list.append(nos)

    print("List",list)
    maximum = max(list)
    print("Maximum number is  : ",maximum)

    minimum = min(list)
    print("Minimum number is  : ",minimum)

if __name__ == "__main__":
    main()
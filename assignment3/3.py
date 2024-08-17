# Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.



def main():
    list = []
    print("Enter how many numbers do u want")
    n = int(input())
    print("Enter the number")
    for i in range(0, n):
        nos = int(input())
        list.append(nos)

    print("Enter no to find frequency :  ")
    search = int(input())

    # if search in list:
    #     print("present")
    result = list.count(search)
    print("Frequency of ", search , " is : ", result)
   

if __name__ == "__main__":
    main()
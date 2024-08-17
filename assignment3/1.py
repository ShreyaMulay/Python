# 1. Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.

def Addition(nos):
    sum = 0
    for i in nos:
        sum = sum + i
    return sum

def main():
    list = []
    print("Enter how many numbers do u want")
    n = int(input())
    print("Enter the number")
    for i in range(0, n):
        nos = int(input())
        list.append(nos)
        
    
    print("List",list)
    result = Addition(list)
    print("Addtion : ",result)

if __name__ == "__main__":
    main()
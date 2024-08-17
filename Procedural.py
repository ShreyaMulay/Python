print("Demonstration of Procedural : ")


def Addtion(No1,No2):
    Add = No1 + No2
    return Add

def Subtraction(No1,No2):
    Sub = No1 - No2
    return Sub

def main():
    print("Enter 1st no ")
    no1 = int(input())

    print("Enter21st no ")
    no2 = int(input())

    add = Addtion(no1, no2)
    print("Addtion is : ",add)

    sub = Subtraction(no1, no2)
    print("Subtraction is : ",sub)


if __name__ == "__main__":
    main()





def Addition(no):
    Ans = 0
    for i in no:
        Ans = Ans + i
    return Ans

def main():
    Arr = []

    cnt = int(input("How many numbers do u want : "))

    print("Enter list item : ")
    for i in range(cnt):
        Arr.append(int(input()))

    print("Elements are ",Arr)


    Result = Addition(Arr)
    print("Addition is  ",Result)


main()

print("--------------------------------")
#  Write a program which accept one number and display below pattern.

def main():
    print("Enter a number")

    key = int(input())

    for i in range(1,key+1):
        for j in range(1,i+1):
            print("j",j)
            print(j, end=" ")
        print()

   
if __name__ == '__main__':
    main()  
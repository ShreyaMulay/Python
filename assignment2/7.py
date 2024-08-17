# Write a program which accept one number and display below pattern. 
#   1 2 3
#   1 2 3
#   1 2 3



def main():
    print("Enter a number")

    key = int(input())

    for i in range(key):
        for j in range(1,key+1):
            print(j , end=" ")
        print()

   
if __name__ == '__main__':
    main()  
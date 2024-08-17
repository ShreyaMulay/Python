#  Write a program which accept one number and display below pattern.

#       * * *
#       * * 
#       *


def main():
    print("Enter a number")

    key = int(input())

    for i in range(key, 0, -1):
        print("* " * i)

   
if __name__ == '__main__':
    main()  
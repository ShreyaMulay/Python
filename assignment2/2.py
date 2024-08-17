# Write a program which accept one number and display below pattern.
#                           * * *
#                           * * *
#                           * * *



def main():
    print("Enter a number")

    key = int(input())

    for i in range(key):
        print("* " * key)

   
if __name__ == '__main__':
    main()  
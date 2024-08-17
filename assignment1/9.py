# 9. Write a program which display first 10 even numbers on screen.


def main():
    counter = 0
    No = 0
    while counter < 10:
        if(No % 2 == 0):
            print(No , end = " ")
            counter = counter + 1
        No = No + 1



if __name__ == '__main__':
    main()  
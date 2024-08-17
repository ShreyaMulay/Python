# Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction, Mult for multiplication and Div) for division. All functions accepts two parameters as number and perform the operation. Write on python program which call all the functions from Arithmetic module by accepting the parameters from user.

from Arithmetic import *

def main():
    print("Enter which operation do u want to perform : 1.Add, 2.Sub, 3.Mult, 4.Div")

    key = int(input())

    if(key == 1 or key == 2 or  key == 3 or key == 4):
        print("Enter 1st number :")
        No1 = int(input())

        print("Enter 2st number :")
        No2 = int(input())
     
#    switch(x):
#         case 'one':
#             print '1'
#         case 'two':
#             print '2'
#         case 'three':
#             print '3'
#         else:
#             print "D'oh!"

    if(key == 1):
        Result = Add(No1, No2)
        print("Addition is : ",Result)

    elif(key == 2):
        Result = Sub(No1, No2)
        print("Subtraction  is : ",Result)

    elif(key == 3):
        Result = Mult(No1, No2)
        print("Multiplication is : ",Result)

    elif(key == 4):
        Result = Div(No1, No2)
        print("Division is : ",Result)

    else:
        print("Invalid input ")

if __name__ == '__main__':
    main()  
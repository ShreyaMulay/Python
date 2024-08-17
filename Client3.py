# all import

import Marvellous as m

def main():

    print("Enter 1st no")
    no1= int(input())

    print("Enter 2st no")
    no2= int(input())

    ans = m.Addition(no1,no2)

    print("Addition is : ",ans)

    ans = m.Multiplication(no1,no2)

    print("Multiplication is : ",ans)

main()  
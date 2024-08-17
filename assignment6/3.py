# 3.Design python application which creates two threads as evenlist and oddlist. Both the threads accept list of integers as parameter. Evenlist thread add all even elements from input list and display the addition. Oddlist thread add all odd elements from input list and display the addition.


import threading

def EvenThread(No):
    print("::No",No)
    sum = 0
    print("Sum of Even Number are : ")

    for i in No:
        if(i%2==0):
            sum = sum + i
    
    print(sum)
    print()


def OddThread(No):
    sum = 0
    print("Sum of  Odd Number are : ")

    for i in No:
        if(i%2 != 0):
            sum = sum + i
    
    print(sum)

    
def main():
    mylist = []
    print("How many number")
    n = int(input())
    print("Enter the numbers")
    for i in range(n):
        nos = int(input())
        mylist.append(nos)

    # p1 = EvenThread(nos)
    # p2 = OddThread(nos)

    p1=threading.Thread(target= EvenThread, args=(mylist,))
    p2=threading.Thread(target= OddThread, args=(mylist,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()

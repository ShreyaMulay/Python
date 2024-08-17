# 1.Design python application which creates two thread named as even and odd. Even thread will display first 10 even numbers and odd thread will display first 10 odd numbers.

import threading

def EvenThread(No):
    x=2
    print("First 10 Even Number are : ")

    for i in range(No):
        print(x , end=" ")
        x=x+2
    print()
    print()


def OddThread(No):
    x=1
    print("First 10 Odd Number are : ")

    for i in range(No):
        print(x , end=" ")
        x=x+2
    
def main():
    print("Enter the number")
    n = int(input())
    # EvenThread(n)
    # OddThread(n)
    p1=threading.Thread(target= EvenThread, args=(n,))
    p2=threading.Thread(target= OddThread, args=(n,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == "__main__":
    main()

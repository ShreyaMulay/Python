# 2.Design python application which creates two threads as evenfactor and oddfactor.
# Both the thread accept one parameter as integer. Evenfactor thread will display addition of even factors of given number and oddfactor will display addition of odd factors of given number. After execution of both the thread gets completed main thread should display message as "exit from main".

import threading

def EvenThread(No):
    x=2
    sum = 0
    print("Sum of Even Number are : ")

    for i in range(No):
        if(i%2==0):
            sum = sum + i
    
    print(sum)
    print()


def OddThread(No):
    x=1
    sum = 0
    print("Sum of  Odd Number are : ")

    for i in range(No):
        if(i%2 != 0):
            sum = sum + i
    
    print(sum)
    
def main():
    print("Enter the number")
    n = int(input())

    p1=threading.Thread(target= EvenThread, args=(n,))
    p2=threading.Thread(target= OddThread, args=(n,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Exit from main")

if __name__ == "__main__":
    main()

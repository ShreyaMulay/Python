# 5.Design python application which contains two threads named as thread and thread2.Thread1 display 1 to 50 on screen and thread display 50 to 1 in reverse order on screen. After execution of thread gets completed then schedule thread2.

import threading

def Display(No):
    for i in range(1,No+1):
        print(i, end=' ')
    print()
       
def reverseDisplay(No):
    for i in range(No,0,-1):
        print(i, end=' ')
    print()
    

def main():
    print("Enter nos")
    n = int(input())

    p1= threading.Thread(target=Display, args=(n,))
    p2= threading.Thread(target=reverseDisplay, args=(n,))

    p1.start()
    p1.join()

    print("End of 1st process")

    p2.start()
    p2.join()

    print("End of 2nd process")

if __name__ == "__main__":
    main()




    
# Example of multi threading
# callback function:  p1=threading.Thread(target= EventDisplay, args=(Value,))
# 

# display first 5 even or odd nos
import os
import threading

def EventDisplay(No):
    print("List of even nos : ",os.getpid())
    print("Thread id of even nos : ",threading.get_ident())

    X = 2
    for i in range(No):
        print("Even",X)
        X= X+2

def OddDisplay(No):
    print("Thread id of odd nos : ",threading.get_ident())

    print("List of odd nos : ",os.getpid())

    X = 1

    for i in range(No):
        print("Odd",X)
        X= X+2


def main():
    print("PID of main process", os.getpid())
    print("Thread id of main process nos : ",threading.get_ident())

    print("Enter no")
    Value = int(input())

    p1=threading.Thread(target= EventDisplay, args=(Value,))
    p2=threading.Thread(target= OddDisplay, args=(Value,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("End of main process")
    # EventDisplay(no)
    # OddDisplay(no)


if __name__ == '__main__':
    main()
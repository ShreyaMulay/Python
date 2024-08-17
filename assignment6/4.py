# 4.Design python application which creates three threads as small, capital, digits. All the threads accepts string as parameter. Small thread display number of small characters, capital thread display number of capital characters and digits thread display number of digits. Display id and name of each thread.

import threading

def smallThread(str):
    count = 0 
    for c in str:
        # print(c)
        if(c.islower()):
            count = count + 1
    print("::count of small charachers : ",count)

def capitalThread(str):
    count = 0 
    for c in str:
        # print(c)
        if(c.isupper()):
            count = count + 1
    print("::count of capital letters",count)

def digitsThread(str):
    count = 0 
    for c in str:
        # print(c)
        if(c.isdigit()):
            count = count + 1
    print("::count of digits ",count)


def main():
    print("Enter String : ")
    str = input()

    p1= threading.Thread(target=smallThread, args=(str,))
    p2= threading.Thread(target=capitalThread, args=(str,))
    p3= threading.Thread(target=digitsThread, args=(str,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("Exit from main")

if __name__ == "__main__":
    main()

import multiprocessing
import os

def Cube(No):
    print("PID is : ",os.getpid())
    return No*No*No

def main():
    Arr = [10,20,30,40]
    result = []
    
    p = multiprocessing.Pool()
    result= p.map(Cube,Arr)
    p.close()
    p.join()

    print(result)

if __name__ == '__main__':
    main()
import multiprocessing
import os
import time

def Fun(No):
    sum = 0
    print("PID is : ",os.getpid())
    for i in range(No):
        sum = sum + (No*No*No)
    return sum

def main():
    starttime = time.time()
    Arr = [1000000,2000000,3000000,4000000]
    result = []
    
    for i in Arr:
        result.append(Fun(i))

    print(result)
    endtime = time.time()
    print("time required : ",endtime-starttime)

if __name__ == '__main__':
    main()
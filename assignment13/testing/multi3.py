# Example of multi processing

# display first 5 even or odd nos
import multiprocessing 

def EventDisplay(No):
    print("List of even nos : ")
    X = 2
    for i in range(No):
        print(X)
        X= X+2

def OddDisplay(No):
    print("List of odd nos : ")
    X = 1

    for i in range(No):
        print(X)
        X= X+2


def main():
    print("Enter no")
    Value = int(input())


    p1=multiprocessing.Process(target= EventDisplay, args=(Value,))
    p2=multiprocessing.Process(target= OddDisplay, args=(Value,))

    p1.start()
    p1.join()
    p2.start()
    p2.join()

    print("End of main process")
    # EventDisplay(no)
    # OddDisplay(no)


if __name__ == '__main__':
    main()
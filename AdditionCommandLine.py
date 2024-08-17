import sys

def Addition(No1,No2):
    Ans = No1 + No2
    return Ans


def VariableLengthAddition(*No):
    Ans = 0

    for i in No:
         Ans = Ans + i
    return Ans

def main():
    print("Welcome to the application",sys.argv[0])
    if(len(sys.argv) < 3):
        print("Please prvideo 2 nos ")
        return
    
    Result = Addition(int(sys.argv[1]), int(sys.argv[2]))

    print("Addtion is ",Result)

    Result1 = VariableLengthAddition(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

    print("Addtion is :",Result1)

if __name__ == '__main__':
    main()
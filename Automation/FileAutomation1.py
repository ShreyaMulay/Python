import sys

def Addition(A,B):
    sum =0
    sum = A + B
    return sum

def main():

    if(len(sys.argv) == 2):
        print("________________________________________________________________")
        print("__________ Automation to perform Addtion ________________")
        print("________________________________________________________________")

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This is used  to perform the addition of 2 integer values")
            exit()

        if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage of the script : ")
            print("Name_of_file first_argument second_argument ")
            print("Note : Both arguments should be integers")
            exit()
        else:
            print("Invalid ")
            exit()

    if(len(sys.argv) ==3):
        try:
            ret = Addition(int(sys.argv[1]),int(sys.argv[2]))
            print("Addtion is :",ret)
        except Exception as obj:
            print("Exception occured :",obj)

    else:
        print("Invalid ")
        exit()

if __name__ == '__main__':
    main()
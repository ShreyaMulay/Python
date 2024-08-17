import sys

def main():
    print("Demonstration of command line arguments :")
    print("Name of Application : ", sys.argv[0])

    print("Data type  of argv : ", type(sys.argv))

    print("Number commandline of argument are : ", len(sys.argv))

    print("Arguments : ", sys.argv)



if __name__ == "__main__":
    main()
import os

def main():
    print("Enter the name of file that you want to write  : ")
    Fname = input()

    if(os.path.exists(Fname)):
        fobj = open(Fname,"r")
        print("File opened successfully in reading mode : ")
    
        
        # data1 = fobj.readline()
        # data2 = fobj.readline()
        # data3 = fobj.readline()
        # data4 = fobj.readline()

        # print(data1)
        # print(data2)
        # print(data3)
        # print(data4)

           
        for line in fobj:
            print(line)


        fobj.close()


    else:
        print("Unable to file since file is not present at current directory : ")

if __name__ == '__main__':
    main()


# Absolute path : C:/shreya/Desktop/Python/Automation/Marvellous.py
# Relative path : Automation/Marvellous.py
import os

def main():
    print("Enter the name of file that you want to write  : ")
    Fname = input()

    if(os.path.exists(Fname)):
        fobj = open(Fname,"a")
        print("File opened successfully in writin mode : ")

        print("Enter data that u want to write in file :")
       
        data = input()
        fobj.write(data)

        fobj.close()


    else:
        print("Unable to file since file is not present at current directory : ")

if __name__ == '__main__':
    main()


# Absolute path : C:/shreya/Desktop/Python/Automation/Marvellous.py
# Relative path : Automation/Marvellous.py
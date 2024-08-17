import os

def main():
    print("Enter the name of file that you want to delete  : ")
    Fname = input()

    if(os.path.exists(Fname)):
        os.remove(Fname)
        print("File deleted successfully  : ")
    else:
        print("File does not exists  : ")


if __name__ == '__main__':
    main()


# Absolute path : C:/shreya/Desktop/Python/Automation/Marvellous.py
# Relative path : Automation/Marvellous.py
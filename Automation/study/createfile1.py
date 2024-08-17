import os
# open(Fname,"x")
# here x means exclusive

def main():
    print("Enter the name of file that you want to create  : ")
    Fname = input()

    # print("::os.path",os.path)
    if(os.path.exists(Fname)):
        print("File already exists")
    else:
        open(Fname,"x")
        print("File created successfully")


if __name__ == '__main__':
    main()


# Absolute path : C:/shreya/Desktop/Python/Automation/Marvellous.py
# Relative path : Automation/Marvellous.py
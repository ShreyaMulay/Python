import sys
import os
import time

def DeleteFile(size,filename):
    # Count = 0 
    if(size == 0):
        os.remove(filename)
        print("Deleted successfully")
        # Count = Count + 1



def DirectoryWatcher(dirName):
    Count =0
    flag = os.path.isabs(dirName)

    if(flag == False):
        dirName = os.path.abspath(dirName)
        print("Converted absolute path is : ",dirName)
    
    exists = os.path.exists(dirName)
    
    if(exists == True):
        for foldername,subfoldername,filenames in os.walk(dirName):
            print("Current folder is : ", foldername)
            for folder in subfoldername:
                print("Subfoldername : ", folder)
            for fname in filenames:
                # print("Filename : ",fname)
                print("Filename : ",os.path.join(foldername,fname))
                print("Size : ",os.path.getsize(os.path.join(foldername,fname)) , " bytes")
                print()
                # Delete file
                if(os.path.getsize(os.path.join(foldername,fname)) == 0):
                    DeleteFile(os.path.getsize(os.path.join(foldername,fname)),os.path.join(foldername,fname))
                    Count = Count + 1
        print("Delete files count :",Count)
    else:
        print("Directory  does not exist")

def main():

    if(len(sys.argv) == 2):
        print("________________________________________________________________")
        print("__________ Directory Watcher  ________________")
        print("________________________________________________________________")

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This is used  to perform the directory traversor")
            exit()

        if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage of the script : ")
            print("Name_of_file name_of_directory ")
            exit()
        
        try:
            # Fun call
            starttime = time.time()
            DirectoryWatcher(sys.argv[1])
            endtime = time.time()

            print("Time require to execute : " ,endtime - starttime)
        
           
        except Exception as obj:
            print("Exception occured :",obj)

    else:
        print("Invalid ")
        exit()

    print("________________________________________________________________")
    print("____________  Thank you for using our script  ____________________")
    print("________________________________________________________________")


if __name__ == '__main__':
    main()




# python3 DirectoryAutomation1.py Study

# sys.argv[0] = DirectoryAutomation1.py
# sys.argv[1] = Study


# run as python3 DirectoryAutomation1.py study >> Output.txt or
# run as python3 DirectoryAutomation1.py study > Output.txt


# 4. Design automation script which accept directory name and delete all duplicate files from that directory. Write names of duplicate files from that directory into log file named as Log.txt. Log.txt file should be created into current directory. Display execution time required for the script.
# Usage : DirectoryDusplicateRemoval.py “Demo” 
# Demo is name of directory.




from sys import *
import os
import datetime
import ChecksumFunctionalityModule as module

#for creating output log file 
def CreateOutput(FileName,list):
    data = "Files Deleted :\n\n"
    for string in list:
        data += string
        data += "\n"
    defaultFileName = module.ChkFileExists(FileName +"_Duplicate_File_Deleted_Output.txt")
    fd = open(defaultFileName,"x")
    fd.write(data)
    fd.close()
    

def main():
    print("----  Marvellous Infosystems by Shreya Mulay ----")

    print("Design automation script which accept directory name and display checksum of all files.")

    if(len(argv) != 2):
        print("Error: Invalid number of arguments")
        exit()

    if (argv[1] == "h") or (argv[1] == "-H"):
        print("\n\n\t\t........................This is FileSystem Automation........................\n\n")
        print("This Script is used to traverse specific directory and display checksum of files")
        print("\n " + argv[0]+ " -h For Help")
        print("\n " + argv[0]+ " -u For Usage")
        exit()
    
    if (argv[1]=="u") or (argv[1]=="-U"):
        print("\n <Usage> " + argv[0]+ " Directory_Name")
        exit()


    try:
        arr = {}
        arr =  module.GetChecksum(argv[1])
        List = module.removeDuplicate(arr)
        print("::List",List)
        CreateOutput(argv[0],List)

    except Exception as E:
        print(E)
        fd = open("Error_Log.txt",'a')
        logmsg = "\n\n Error : "+ str(E) +"\n Log Time " + str(datetime.datetime.now()) +"\n\n"
        fd.write(logmsg)
        fd.close()


if __name__ == "__main__":
    main()
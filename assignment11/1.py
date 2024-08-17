#1.Design automation script which accept directory name and display checksum of all files.
#Usage : DirectoryChecksum.py “Demo”
#Demo is name of directory.

#run as  python3 1.py ../MachineLearning (it will create new txt file)
#Or  run as python3 1.py ../MachineLearning >> output.txt (it will create new output.txt file)

from sys import *
import os
import datetime
import ChecksumFunctionalityModule as module

#for creating output log file 
def CreateOutput(FileName,dictionary):
	
	data = "File Checksum :\n\n"
	for Key, Value in dictionary.items(): 
		data += Key +" : "+ str(Value) +"\n\n"

	defaultFileName = module.ChkFileExists(FileName +"_Output.txt")

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
        # print("DirName : " , arr)
        CreateOutput(argv[0],arr)

    except Exception as E:
        print(E)
        fd = open("Error_Log.txt",'a')
        logmsg = "\n\n Error : "+ str(E) +"\n Log Time " + str(datetime.datetime.now()) +"\n\n"
        fd.write(logmsg)
        fd.close()


if __name__ == "__main__":
    main()
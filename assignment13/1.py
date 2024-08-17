# run as 
# python3 1.py testing 'shreyamule17@gmail.com' 'tcfy rwdc zkbo wsca' zzz.txt
# testing folder contain duplicate files
# 'tcfy rwdc zkbo wsca' is password for shreyamule17@gmail.com email
# zzz.txt contains emails of receipiants 

import os
import time
import schedule
from sys import *
import EmailModule
import datetime
import time
import ChecksumFunctionalityModule as module

def CreateOutput(DirName,Output_File):
    # print("Creating output file" ,DirName,Output_File)
    List =  module.removeDuplicate(DirName)
    # print("Creating output file" ,List)
    if(List):
        data = "\n\n Files Deleted  At  :  " + str(datetime.datetime.now()) + "\n\n"
        for string in List:
            data += string
            data += "\n"
        fd = open(Output_File,"a")
        fd.write(data)
        fd.close()

def sendmail(UserName,Password,To_FileName,Attachment):
    print("UserName",UserName)
    print(os.path.exists(To_FileName))

    print(os.path.exists(Attachment))

    if(os.path.exists(To_FileName) and os.path.exists(Attachment)):
        print("Path exists")
        if(EmailModule.is_connected()):
            print("Connected")
            EmailModule.sendmail(UserName,Password,To_FileName,Attachment)




def main():
    print("----  Marvellous Infosystems by Shreya Mulay ----")

    # print("Design automation script which accept directory name and display checksum of all files.")

    if (argv[1] == "h") or (argv[1] == "-H"):
        print("\n\n\t\t........................This is FileSystem Automation........................\n\n")
        print("This Script is used to traverse specific directory and display checksum of files")
        print("\n " + argv[0]+ " -h For Help")
        print("\n " + argv[0]+ " -u For Usage")
        exit()
    
    if (argv[1]=="u") or (argv[1]=="-U"):
        print("\n <Usage> " + argv[0]+ " Directory_Name")
        exit()

    if(len(argv) != 5):
        print("Invalid number of arguments")
        exit()


    try:

        DirName = argv[1]
        UserName = argv[2]
        Password = argv[3]
        To_FileName = argv[4]
        Output_File = "Files_Deleted.txt"
        schedule.every(1).second.do(lambda: CreateOutput(DirName,Output_File))
        # schedule.every(1).hours.do(CreateOutput(DirName,Output_File))

        # schedule.every().day.at("01:00").do(sendmail(UserName,Password,To_FileName,Output_File))
        schedule.every(1).second.do(lambda: sendmail(UserName,Password,To_FileName,Output_File))

        
        while True:
            schedule.run_pending()
            time.sleep(1)

    except Exception as E:
        print(E)
        fd = open("Error_Log.txt",'a')
        logmsg = "\n\n Error : "+ str(E) +"\n Log Time " + str(datetime.datetime.now()) +"\n\n"
        fd.write(logmsg)
        fd.close()


if __name__ == '__main__':
    main()


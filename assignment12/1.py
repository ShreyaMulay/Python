#1.Design automation script which display information of running processes as its name, PID,
#Username.
#Usage : ProcInfo.py

# run as  python3 1.py process.txt

import psutil
import time
import schedule
import os
import datetime
import time
from sys import *
import ProcessModule as ProcessModule


def CreateLog(filename):
    defaultFileName = ProcessModule.ChkFileExists(filename)

    data =""
    processData = ProcessModule.DisplayProcesses()
    for ele in processData:
       data +=str(ele) + "\n"
    
    fp = open(defaultFileName, "a")
    fp.write("LOG file created as "+ time.ctime() + "\n")
    fp.write("\n")

    fp.write(data)
    fp.close()

    # fp = open(filename, "a")
    # separator = "_"* 70
    # fp.write(separator + "\n")
    # fp.write("Marvellous Process log" + "\n")
    # fp.write("LOG file created as "+ time.ctime() + "\n")
    # fp.write(separator + "\n")
    
    # fp.write("CONTENT OF FILE ARE :" +"\n")
    # fp.write(separator + "\n")

    # processData = ProcessModule.DisplayProcesses()
    # for data in processData:
    #     fp.write("%s \n" %data)

    # fp.write(separator + "\n")

    # fp.close()



def main():
   
    print("----  Marvellous Infosystems by Shreya Mulay ----")

    print("List of running processes are : ")

    print("________________________________________________________________")
    

    if(len(argv) != 2):
        print("Error: Invalid number of arguments")
        exit()

    if(argv[1] == "h") or (argv[1] == "-H"):
        print("\n\n\t\t........................This is Process Automation........................\n\n")
        print("\n " + argv[0]+ " -h For Help")
        print("\n " + argv[0]+ " -u For Usage")
        exit()
    
    if (argv[1]=="u") or (argv[1]=="-U"):
        print("\n <Usage> " + argv[0]+ " Directory_Name")
        exit()


    try:
        FileName = argv[1]
        schedule.every(1).second.do(CreateLog(FileName))
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
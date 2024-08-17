# run as python3 Reminder.py 'shreyamule17@gmail.com' 'tcfy rwdc zkbo wsca' emails.txt

import os
import time
import schedule
from sys import *
import EmailModule
import datetime
import time

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
    print("---- Shreya Mulay ----")
    if(argv[1] == "h") or (argv[1] == "-H"):
        print("\n\n\t\t........................This is EmailSystem Automation........................\n\n")
        print("This Script is used to give reminder")
        print("\n " + argv[0]+ " -h For Help")
        print("\n " + argv[0]+ " -u For Usage")
        exit()
    
    if (argv[1]=="u") or (argv[1]=="-U"):
        print("\n <Usage> " + argv[0]+ " Directory_Name")
        exit()

    if(len(argv) != 4):
        print("Invalid number of arguments")
        exit()

    try:
        UserName = argv[1]
        Password = argv[2]
        To_FileName = argv[3]
        Output_File = "Reminder.txt"


        # schedule.every(1).second.do(lambda: sendmail(UserName,Password,To_FileName,Output_File))
        schedule.every().friday.at("17:00").do(lambda: sendmail(UserName,Password,To_FileName,Output_File))

        # schedule.every().monday.at("20:39").do(lambda: sendmail(UserName,Password,To_FileName,Output_File))



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
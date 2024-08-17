# run as python3 MeetingReminder.py

import os
import time
import schedule
from sys import *
import EmailModule
import datetime
import time
import pandas as pd


def sendmail(UserName,Password,To_FileName,Attachment):
    print("Path exists")
    if(EmailModule.is_connected()):
        print("Connected")
        EmailModule.sendmailToPariticipant(UserName,Password,To_FileName,Attachment)

def main():
    print("---- Shreya Mulay ----")

    try:
        UserName = 'shreyamule17@gmail.com'
        Password = 'tcfy rwdc zkbo wsca'
        # To_FileName = argv[1]
        Output_File = "Reminder.txt"

        receipintList = []
        participants = pd.read_csv('participants.csv')
        emails = participants['email']

        for email in emails:
            print(email)
            receipintList.append(email)

        print("receipintList",receipintList)
        schedule.every(1).second.do(lambda: sendmail(UserName,Password,receipintList,Output_File))

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
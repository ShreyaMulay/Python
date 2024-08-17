# send email in python 
# run code processex4.py
# csv file mhe mail id asel tr tyala bday cha mail

import psutil
import time
import schedule
import os
import sys
import urllib2

def CheckConnection():
    try:
        urllib2.urlopen('www.google.com',timeout=1)
        return True
    except urllib2.HTTPError as e:
        return False

def MainSender(filename,time):
    try:
        fromAdd = "shreyamule17@gmail.com"
        toAdd = "shreyamule17@gmail.com"

        msg = MIMEMultipart() # 1)multi purpose internet message  2) security purpose 3)send ascii data

        msg['From'] = fromAdd

        msg['To'] = toAdd

        body = """ 
        HEllo %s,
        Welcome to Marvelous InfoSystem.
        Running processes are attached to this email .
        Log file created at : %s
        
        This is auto gerented email.

        Thanks and regards,
        Shreya Mulay

        """ %(toAdd,time)

        Subject = """
        Process gerenerated email %s
        """ %(time)

        msg['Subject'] = Subject
        msg.attached(MIMEMultipart)


    except Exception as e:
        print("Error",,e)

def CreateLog(FolderName = "Marvellous"):
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)
    
    timeStamp = time.ctime()
    timeStamp = timeStamp.replace(" ","")
    timeStamp = timeStamp.replace(":","_")
    timeStamp = timeStamp.replace("/","_")


    filename = os.path.join(FolderName, "Marvellous%s.log" %(timeStamp))

    fp = open(filename, "w")
    separator = "_"* 70
    fp.write(separator + "\n")
    fp.write("Marvellous Process log" + "\n")
    fp.write("LOG file created as "+ time.ctime() + "\n")
    fp.write(separator + "\n")
    
    fp.write("CONTENT OF FILE ARE :" +"\n")
    fp.write(separator + "\n")

    processData = DisplayProcesses()
    for data in processData:
        fp.write("%s \n" %data)

    fp.write(separator + "\n")

    isConnected = CheckConnection()

    if isConnected:
        MainSender(processData,time.ctime())
    else:
        print("No Internet connection")

    fp.close()



def DisplayProcesses():
    listOfProcesses = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        listOfProcesses.append(proc.info)

    return listOfProcesses

def main():
    print("List of running processes are : ")
    print("________________________________________________________________")
    
    # schedule.every(1).minute.do(CreateLog)
    schedule.every(int(sys.argv[1])).minutes.do(CreateLog)

    while True:
        schedule.run_pending()
        time.sleep(1)

    # CreateLog()


if __name__ == '__main__':
    main()
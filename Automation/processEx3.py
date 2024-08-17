import psutil
import time
import schedule
# import datetime


# print(psutil.pids())

def CreateLog(filename = "Marvellous.log"):
    fp = open(filename, "a")
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



    fp.close()



def DisplayProcesses():
    listOfProcesses = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        listOfProcesses.append(proc.info)

    return listOfProcesses

def main():
    print("List of running processes are : ")
    print("________________________________________________________________")
    
    schedule.every(1).minute.do(CreateLog)
    while True:
        schedule.run_pending()
        time.sleep(1)

    # CreateLog()


if __name__ == '__main__':
    main()
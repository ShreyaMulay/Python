import psutil
import time
# print(psutil.pids())

def CreateLog(filename = "Marvellous.log"):
    fp = open(filename, "w")
    separator = "_"* 70
    fp.write(separator + "\n")
    fp.write("Marvellous Process log" + "\n")
    fp.write("LOG file created as "+ time.ctime() + "\n")
    fp.write(separator + "\n")
    
    fp.write("CONTENT OF FILE ARE :" +"\n")
    fp.write(separator + "\n")

    fp.close()



def DisplayProcesses():
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        print(proc.info)


def main():
    print("List of running processes are : ")
    print("________________________________________________________________")
    # DisplayProcesses()
    CreateLog()


if __name__ == '__main__':
    main()
import datetime
import time
import schedule

def Schedule_Minute():
    print("schedular executes after each minute :",datetime.datetime.now())


def main():
    print("Current time is :",datetime.datetime.now())

    schedule.every(1).minute.do(Schedule_Minute)
    # canonical function call => call 1st fun =>2nd =>3rd....

if __name__ == '__main__':
    main()
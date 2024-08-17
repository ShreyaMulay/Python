import datetime
import time
import schedule

def Schedule_Minute():
    print("schedular executes after each minute :",datetime.datetime.now())


def Schedule_Hour():
    print("schedular executes after each hour :",datetime.datetime.now())

def Schedule_Sunday():
    print("schedular executes after each sunday :",datetime.datetime.now())


def main():
    print("Current time is :",datetime.datetime.now())

    schedule.every(1).minute.do(Schedule_Minute)
    # canonical function call => call 1st fun =>2nd =>3rd....

    schedule.every(1).hour.do(Schedule_Hour)
    schedule.every(1).sunday.do(Schedule_Sunday)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()
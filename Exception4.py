
def main():
    Ans = 0
    
    try:
        print("Enter 1st number : ")
        no1 = int(input())

        print("Enter 2st number : ")
        no2 = int(input())

        Ans = no1 / no2
    
    except ZeroDivisionError as zobj:
        print("Exception occur by",zobj)

    except ValueError as e:   #specific exception
        print("Exception occur ",e)

    except Exception as e:          #gerenric exception handler
        print("Exception occur ",e)


    print("Division is ", Ans)


if __name__ == '__main__':
    main()
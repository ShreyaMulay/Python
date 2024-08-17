# 5. Write a recursive program which accept number from user and return its factorial.


def Display(no):
    if(no == 0 or no == 1):
        return 1
    else:
       return no * Display(no - 1)

def main():
    print("Enter number  :")
    no = int(input())
    ret = Display(no) 
    print("factorial of {}  is {} ". format(no,ret))

if __name__ == "__main__":
    main()
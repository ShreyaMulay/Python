# 3.Write code of  Perfect number
# a no  which  is equal to the sum of its divisors i.e 1+ 2+ 3 = 6  

def Perfect(No):
    sum = 0
    for i in range(1, No):
        if(No % i == 0):
            sum = sum + i 
    if(No == sum):
        return True
    else:
        return False


def main():
    print("enter number")
    no = int(input())
    result = Perfect(no)
    print("Perfect number is : " , result)

if __name__ == '__main__':
    main()
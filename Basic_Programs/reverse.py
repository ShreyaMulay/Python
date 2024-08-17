# 1. Write a code to reverse a number
def Reverse(No):
    rev = 0
    while No > 0:
        ld = No % 10
        rev = rev * 10 + ld
        No = No // 10
    return rev

def main():
    print("enter number")
    no = int(input())
    result = Reverse(no)
    print("Reverse number is : " , result)

if __name__ == '__main__':
    main()
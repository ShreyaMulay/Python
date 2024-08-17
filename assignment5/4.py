# 4.Write a recursive program which accept number from user and return summation of its digits.
#  879  - 24


def Display(no):
    sum =0
    if(no < 10):
        return no
    else:
        # while no > 0:
        #     ld = no % 10
        #     sum = sum+ld
        #     no = no // 10
        # return sum 
        return no % 10 + Display(no // 10)

def main():
    print("Enter number  :")
    no = int(input())
    ret = Display(no) 
    print("summation of its digits : ",ret)

if __name__ == "__main__":
    main()
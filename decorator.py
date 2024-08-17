def sub(A,B):      # 0x100  //hashcode 
    print(A-B)

#SmartSub decorator
def SmartSub(fptr):   # 0x200
    def Inner(A,B):      #0x300
        if(A < B):
            A,B = B,A    #swap
        return fptr(A,B)    #0x100(1992,1990)
    return Inner         # return 0x300


sub = SmartSub(sub)    #  SmartSub(0x100)

def main():     #0x400
    No1 = int(input("Enter 1st number : "))
    No2 = int(input("Enter 2st number : "))
    
    sub(No1, No2)    # 0x300(1990,1992)

if __name__ == '__main__':
    main()
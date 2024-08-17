def ChkPrime(No):
    isPrime = True

    if(No <= 1):  
        isPrime = False
    else:
        for i in range(2,int(No / 2) + 1):
            if(No % i == 0):
                isPrime =  False
                break
    
    if(isPrime == True):
        return True
    else:
        return False


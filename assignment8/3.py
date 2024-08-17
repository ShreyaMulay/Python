# # Write a program which contains one class named as Numbers.
# Arithmetic class contains one instance variables as Value.
# Inside init method initialise that instance variables to the value which is accepted from user.
# There are four instance methods inside
# class as ChkPrime, ChkPerfect), SumFactors),
# Factors).
# ChkPrime) method will returns true if number is prime otherwise return false.
# ChkPerfect method will returns true if number is perfect otherwise return false.
# Factors) method will display all factors of instance variable.
# SumFactors) method will return addition of all factors. Use this method in any another method as a helper method if required.
# After designing the above class call all instance methods by creating multiple objects.


class Numbers:
    def __init__(self):
        self.Value = 0 
    
    def Accept(self):
        print("Enter a number : ")
        self.Value = int(input())

    def ChkPrime(self):
        isPrime = True

        # 2,int(No / 2)
        for i in range(2 , self.Value):
            if(self.Value % i == 0):
                isPrime = False
                break
            
        if(isPrime == True):
            return True
        else:
            return False

    def ChkPerfect(self):
        sum = 0
        for i in range(1, self.Value):
            if(self.Value % i == 0):
                sum = sum + i
                print(i , "+",end= " ")

        print()
        if(self.Value == sum):
            return True
        else: 
            return False


        
obj = Numbers()
obj.Accept()
# isPrime = obj.ChkPrime()
# if(isPrime == True):
#     print("PRime no")
# else:
#     print("Not prime")

isPerfect = obj.ChkPerfect()
if(isPerfect == True):
    print("Perfect no")
else:
    print("Not Perfect")
def Calculation(no1,no2):
    def Addtion(no1,no2):
        add= no1+no2
        return add
    def Subtraction(no1,no2):
         sub= no1-no2
         return sub
    Result1 = Addtion(no1,no2)
    Result2 = Subtraction(no1,no2)
    return Result1, Result2



print("Enter 1st number :")
a = int(input())

print("Enter 2nd number :")
b = int(input())

Result1,Result2 = Calculation(a,b)

print("Result : " )
print("Addtion is : ",Result1)
print("Result : ",Result2)

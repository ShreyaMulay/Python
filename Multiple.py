def Calculation(no1,no2):
    add= no1+no2
    sub= no1-no2
    return add,sub

print("Enter 1st number :")
a = int(input())

print("Enter 2nd number :")
b = int(input())

Result1,Result2 = Calculation(a,b)

print("Result : " )
print("Addtion is : ",Result1)
print("Result : ",Result2)

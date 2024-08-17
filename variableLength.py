def Addtion(*No):
    print("type : ", type(No))
    print("Length : ", len(No))


    Ans = 0
    for i in No:
        Ans = Ans + i
    
    return Ans



Result = Addtion(10,20,30,40)

print("addition is ", Result)


Result = Addtion(10,20,30)

print("addition is ", Result)


from functools import reduce

print("Demonstration of Filter Map Reduce : Using normal Functions ")


def EventChk(no):
    return (no % 2 == 0)

def Increase(no):
    return (no + 2)

def Add(a,b):
    return (a + b)


Arr = [8,9,5,16,2,4,21,30,11]

eventArr = list(filter(EventChk, Arr))

print("Data after filter: ", eventArr)


MapArr = list(map(Increase,eventArr))

print("Data after map: ", MapArr)

sum = reduce(Add, MapArr)

print("Data after reduce: ", sum)


from functools import reduce

print("Demonstration of Filter Map Reduce : Using Lambda Functions ")

# FMR is preimplimentated in python

Arr = [8,9,5,16,2,4,21,30,11]

eventArr = list(filter(lambda no : (no % 2 == 0), Arr))

print("Data after filter: ", eventArr)


MapArr = list(map(lambda no : no + 2,eventArr))

print("Data after map: ", MapArr)

sum = reduce(lambda a,b: (a+b), MapArr)

print("Data after reduce: ", sum)

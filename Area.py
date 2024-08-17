#  PI = 3.14) is deault argument 
def Area(Radius , PI = 3.14):
    Result = PI * Radius * Radius
    return Result

Ans = Area(10.7)

print("Ans",Ans)

# used in print fun (\n)
# used in range fun (start or in displacement)

# positional arg
Ans = Area(10.7,7.90)

print("Ans",Ans)

# keyword arg

Ans = Area(PI=3,Radius = 5)

print("Ans",Ans)
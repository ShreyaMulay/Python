#Dictionary datatype

# 1.Heterogeneous
# 2.Ordered
# 3.Indexed
# 4.Mutable
# 5.Allows Duplicates but aft addiing remove old value



price = {"Python" : 2000, "Java": 12000, "C": 1000, "C++":290 ,"C":2500}

print(type(price))
print(price)

print(price["Python"])

print(price.keys())
print(price.values())


price["Python"] = 340

print(price)


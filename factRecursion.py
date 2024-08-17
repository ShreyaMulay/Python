print("Demonstration of Factorial Recursion: ")


def fact(no):
    if(no == 0 or no == 1):
        return 1
    else:
        return no * fact(no- 1)


result = fact(5)

print("factorial of 5 is : ",result)



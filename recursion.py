print("Demonstration of Scope of Recursion: ")

# recursion is replacement for loops
#  but as a programmer loops are better to use

import sys

print ("Maximum number of recursive call are {} in python".format(sys.getrecursionlimit()))


# Changing recursion limit
sys.setrecursionlimit(1500)
print (" Maximum number of recursive call are {} python".format(sys.getrecursionlimit())) 



# Recursive function which goes into infinite recursive calls

# def fun():
#     print("inside Function")
#     fun()



# Recursive function which performs recursive calls 10 times

i = 1

def gun():
    global i
    if(i <= 10):
        print("i : ",i)
        i = i+1
        gun()
    
gun()

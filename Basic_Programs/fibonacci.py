# 2.Write the code to find the Fibonacci series upto the nth term.
#  addtion of previous two numbers 0,1, 2,3,5,8,13,21,34...
def Fibonacci(No):
    n1 = 0
    n2 = 1
    n3 = 0
    i = 0
    while i < 20 and n3 < 20:
        n3 = n1 + n2
        n1 = n2 
        n2 = n3
        print(n3, end=" ")
        i = i + 1
    print()

def Fibonacci1(No):
    n1 = 0
    n2 = 1
    n3 = 0
    for i in range(2, No):
        print(n3, end=" ")
        n3 = n1 + n2
        n1 = n2 
        n2 = n3
        # print(n3, end=" ")
    print()
    

def main():
    print("enter a number upto where u want series")
    no = int(input())
    # using while loop
    Fibonacci(no) 
   
    # using for loop
    Fibonacci1(no)

if __name__ == '__main__':
    main()
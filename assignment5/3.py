# 3.Write a recursive program which display below pattern.
# 5 - 5 4 3 2 1



def Display(no):
    if(no >= 1):
        print(no, end=" ")
        Display(no - 1)

def main():
    print("Enter number  :")
    no = int(input())
    Display(no)

if __name__ == "__main__":
    main()


def checkEven(no):
    if no%2 == 0:
        print("No is Even")
    else:
        print("No is ODd")


def main():
    print("Enter no : ")
    a = int(input())

    checkEven(a)

print(__name__)

# Starter
if __name__ == "__main__":
    main()
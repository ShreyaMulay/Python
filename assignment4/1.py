# 1. Write aprogram which contains one lambda function which accepts one parameter and return power of two

def main():
    print("Enter no: ")
    no = int(input())

    power = lambda X: X ** 2

    print("Power IS ", power(no))

if __name__ == "__main__":
    main()


#  Write code to Calculate frequency of characters in a string

def main():
    print("enter string : ")
    str = input()
    
    print("enter character that u want to count : ")
    letter = input()
    
    result = str.count(letter)
    print("frequency of characters ", letter , " is ", result)
    
if __name__ == '__main__':
    main()
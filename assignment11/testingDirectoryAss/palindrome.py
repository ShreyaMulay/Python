# 5. Write code Check if the given string is Palindrome or not
# read from start or end is same  i.e 121 = 121 , level,madam, civic

def Palindrome(str):
    s1 = str
    s2 = str[::-1]
    print(s1)
    print(s2)

    if s1 == s2:
        return True
    else:
        return False

def main():
    print("enter string")
    str1 = input()
    result = Palindrome(str1)
    print("Palindrome  is : " , result)

if __name__ == '__main__':
    main()
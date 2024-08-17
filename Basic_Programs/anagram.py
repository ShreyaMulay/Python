# 4.Write code to Check if two strings are Anagram or not
# rearranging the letters that form  another word  i.e secure = rescue , end = den , net = ten

def Anagram(str1, str2):
    if(len(str1) != len(str2)):
        return False
    else:
        s1 = sorted(str1)
        s2 = sorted(str2)

        print("s1",s1)
        print("s2",s2)

        if(s1 == s2):
            return True
        else:
            return False
   

def main():
    print("enter 1st string ")
    str1 = input()
    print("enter 2st string ")
    str2 = input()
    result = Anagram(str1,str2)
    print("Anagram number is : " , result)

if __name__ == '__main__':
    main()
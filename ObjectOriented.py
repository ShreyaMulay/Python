print("Demonstration of Object Orientation : ")

class Arithmetic:
    def __init__(self,Value1,Value2): #Constructor
        self.No1 = Value1             #Characteristics =>data
        self.No2 = Value2               #Characteristics

    def Addtion(self):              #BEHAVIOUR =>function
        ans = self.No1 + self.No2
        return ans
    
    def Subtraction(self):      #BEHAVIOUR
        ans = self.No1 - self.No2
        return ans


print("Enter 1st no ")
no1 = int(input())

print("Enter 2nd no ")
no2 = int(input())

obj = Arithmetic(no1, no2)
add = obj.Addtion()
print("Addtion is : ",add)

sub = obj.Subtraction()
print("Subtraction is : ",sub)


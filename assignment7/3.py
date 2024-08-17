# Write a program which contains one class named as Arithmetic.
# Arithmetic class contains three instance variables as Value1 ,Value2.
# Inside init method initialise all instance variables to 0.
# There are three instance methods inside
# Multiplication, Division).
# class as Accept, Addition), Subtraction(),
# Accept method will accept value of Valuel and Value from user.
# Addition) method will perform addition of Valuel ,Value and return result.
# Subtraction() method will perform subtraction of Value1 Value and return result.
# Multiplication method will perform multiplication of Value, Value and return result.
# Division) method will perform division of Value Value and return result.
# After designing the above class call all instance methods by creating multiple objects.


class Arithmetic:
    def __init__(self):
        self.Value1 =0
        self.Value2 =0

    def Accept(self):
        print("Enter 1st no. : ")
        self.Value1 = float(input())
        print("Enter 2st no. : ")
        self.Value2 = float(input())

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        return self.Value1 / self.Value2


obj1 = Arithmetic()
obj1.Accept()
print("Addition is : ",obj1.Addition())
print("Subtraction is : ",obj1.Subtraction())
print("Multiplication is : ",obj1.Multiplication())
print("Division is : ",obj1.Division())







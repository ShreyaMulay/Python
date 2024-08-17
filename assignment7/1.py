
#  Write a program which contains one class named as Demo.
# Demo class contains two instance variables as no1 ,no2.
# That class contains one class variable as Value.
# There are two instance methods of class as Fun and Gun which displays values of instance variables.
# Initialise instance variable in init method by accepting the values from user.
# After creating the class create the two objects of Demo class as
# Obj1 = Demo(11,21)
# Obj2 = Demo(51,101)
# Now call the instance methods as
# Obj1.Fun()
# Obj2.Fun()
# Obj1.Gun()
# Obj2.Gun()



class Demo():
    Value = 10

    def __init__(self,no1,no2):
        self.No1 = no1
        self.No2 = no2

    def Fun(self):
        print("Value of no1 Fun: " ,self.No1)
        print("Value of no2 Fun: " ,self.No2)

    def Gun(self):
        print("Value of no1 Gun: " ,self.No1)
        print("Value of no2 Gun: " ,self.No2)


print("Demo.Value",Demo.Value)
Obj1 = Demo(11,21)
Obj2 = Demo(51,101)

Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()
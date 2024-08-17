class Demo:
    Data1 = 11 #class variabl
    Data2 = 21 #class variabl

    def __init__(self,A,B):
        print("Inside Constructor : " )
        self.No1 =A   #instancee variable
        self.No2 =B   #instancee variable

    def Display(self):    #instancee method
        print("Value of no1 : " ,self.No1)
        print("Value of no2 : " ,self.No2)
        print("Value of Demo1 no2 : " ,Demo.Data1)
        print("Value of Demo1 no2 : " ,Demo.Data2)

    @classmethod
    def Fun(cls):     #class method
        print("Value of Data1 from Fun : " ,Demo.Data1)
        print("Value of Data2 from Fun : " ,Demo.Data2)

    @staticmethod
    def Gun():         #static method
        print("Inside Static Method")

Demo.Fun()
Demo.Gun()


obj1 = Demo(5,8)

obj1.Display()
# obj2 = Demo(90,89)

# obj2.Display()

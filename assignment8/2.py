# Write a program which contains one class named as BankAccount.
# BankAccount class contains two instance variables as Name & Amount.
# That class contains one class variable as ROT which is initialise to 10.5.
# Inside init method initialise all name and amount variables by accepting the values from user.
# There
# are Four instance methods inside class as Display, Deposito),
# Withdraw(),
# Calculateintrest).
# Deposit() method will accept the amount from user and add that value in class instance variable
# Amount.
# Withdraw() method will accept amount to be withdrawn from user and subtract that amount from class instance variable Amount.
# CalculateIntrest) method calculate the interest based on Amount by considering rate of interest which is Class variable as ROL.
# And Display( method will display value of all the instance variables as Name and Amount.
# After designing the above class call all instance methods by creating multiple objects.


class BankAccount:
    ROT = 10.5

    def __init__(self,name,amount):
        self.name =name
        self.amount = amount

    def Deposite(self):
        print("Enter amount to deposit : ")
        amt = float(input())
        self.amount = self.amount + amt
        self.Display()
    
    def Withdraw(self):
        print("Enter amount to withdraw : ")
        amt = float(input())
        if(amt < self.amount):
            self.amount = self.amount - amt
        else:
            print("Insufficient amount to withdraw")
            return 
        self.Display()
    
    def CalculateInterest(self):
        interest =  (self.amount * BankAccount.ROT) / 100
        print("Interest is : ",interest)
        self.amount = self.amount + interest
        self.Display()

    def Display(self):
        print("Hello ",self.name )
        print("Total Amount is  ",self.amount)

obj1 = BankAccount("Shreya",1000)
while True:
    print()
    print("Press 1 key to deposite amount or press 2 to withdraw or press 3 to calculate interest Or press 0 to return : ")
    key = int(input())
    if(key == 1):
        obj1.Deposite()
    elif(key == 2):
        obj1.Withdraw()
    elif(key == 3):
        obj1.CalculateInterest()
    elif(key == 0):
        print("Exiting the program.")
        break
    else:
        print("Wrong key pressed.")
        break


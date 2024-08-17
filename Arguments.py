# Type of arguments :
#  1 . Positional arguments
#  2. Keyword arguments
#  3. Default arguments
#  4.variable no of arguments


def Information(Name , Age , Salary=10000):
    print("Name: ", Name)
    print("Age: ", Age)
    print("Salary: ", Salary)



#  Positional argument --------------------------------
Information("Shreya",25,50000)  

print("")


#  Keyword argument --------------------------------

Information(Age = 30000,Salary = 100000,Name = "Rita")

print("")


#  Default argument --------------------------------

# give only required arguments

Information("Nik",26)


# print("")

#  Variable number of arguments --------------------------------




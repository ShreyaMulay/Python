# Write a program which contains one class named as BookStore.
# BookStore class contains two instance variables as Name ,Author.
# That class contains one class variable as NoOfBooks which is initialise to 0.
# There is one instance methods of class as Display which displays name, Author and number of books.
# Initialise instance variable in init method by accepting the values from user as name and author.
# Inside init method increment value of NoOfBooks by one.
# After creating the class create the two objects of BookStore class as
# Obj1 = BookStore("Linux System Programming", "Robert Love")
# Obj1. Display (
# # Linux System Programming by Robert Love. No of books : 1
# Obj2 = BookStore("C Programming", "Dennis Ritchie")
# Obj2.Display()|
# # C Programming by Dennis Ritchie. No of books: 2


class BookStore:
    NoOfBooks = 0

    def __init__(self,bname,aname):
        self.book_name = bname
        self.author_name = aname
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Accept(self):
        print("Enter Book name : ")
        self.book_name = input()

        print("Enter Author name : ")
        self.author_name = input()

        # print("Enter No of Books : ")
        # self.no_of_books = int(input())

    def Display(self):
        print(self.book_name , "by", self.author_name, ".","No of books: ",BookStore.NoOfBooks)

obj1 = BookStore("Linux System Programming","Robert Love")
# obj1.Accept()
obj1.Display()


obj1 = BookStore("C Programming"," Dennis Ritchie")
# obj1.Accept()
obj1.Display()


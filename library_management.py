class library():
    def __init__(self):
        self.no_books = [] # list to store book numbers
        self.Book_name = [] # list to store book names
        self.name=input("Enter the Library Name")
        self.booklimit = int(input("Enter the book limit"))  # limit for number of books
        

    def getinfo(self):
        for i in range(self.booklimit):
            self.no_books.append(int(input("Entere the book number\n")))
            self.Book_name.append(input("Enter the Book name\n"))


    def display(self):
        print(f"The name of the library is {self.name}")
        for i in range(self.booklimit):
            print(f"The no of book is {self.no_books[i]} and the name of the book is {self.Book_name[i]}")



p1=library()
p1.getinfo()
p1.display()



# for i in range(p1.booklimit):
#     p1.getinfo()


# for i in range(p1.booklimit):
#     p1.display()







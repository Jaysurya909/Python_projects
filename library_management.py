class library():
    booklimit=0
    no_books=[]
    Book_name=[]



l1=library()

l1.booklimit=int(input("How many books you wanna enter"))


for i in range(0,l1.booklimit):
    l1.no_books.append(int(input("Enter the book number\n")))   #cannot use l1.no_books[i] as it is not defined yet and it is a nonexistent index
    l1.Book_name.append(input("Enter the book name\n"))


for i in range(0,l1.booklimit):
    print(f"The book number is {l1.no_books[i]} and name of the book is {l1.Book_name[i]}")




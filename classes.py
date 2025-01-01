#Library Management System
#Book Class
class Book:
    def __init__(self, title: str, author: str, isbn: int):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        self.borrowed_by = None

    def _str_(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Borrowed: {'Yes' if self.is_borrowed else 'No'}"
#Users Class
class Users:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, ID: {self.user_id}, email: {self.email}"
    
        
#Library Class
class Library(Book, Users):
    #Keys are the ID and values are user objects.
    def __init__(self):
        self.books = []
        self.users = {}

    def add_book(self, b):
        self.books.append(b)
        print(f"Book {b.title} added to the library.")
    
    def list_books(self):
        if len(self.books) != 0:
            for i in (self.books):
                print(i.title)
        else:
            print("No books present.")

    def borrow_book(self, isbn: int, user_id):
        if user_id not in self.users:
            print(f"User {user_id} does not exist.")
            return
        for i in self.books:
            if i.is_borrowed == False and i.isbn == isbn:
                i.is_borrowed = True
                i.borrowed_by = user_id
                print(f"User: {user_id} has borrowed {i.title}.")
                return
        print("Book is not available. or has been borrowed")

    def return_book(self, isbn):
        for i in self.books:
            if i.is_borrowed == True and i.isbn == isbn:
                i.is_borrowed = False
                print(f"You have returned {i.title}")
                return
        print("Book is not available or has not been borrowed.")

    def add_user(self, user):
        if user in self.users:
            print(f"User with ID {user.user_id} already exists.")
            return
        self.users[user.user_id] = user
        print(f"User: {user.name}, added with ID: {user.user_id}")

    def list_users(self):
        if not self.users:
            print("No users registered.")
            return
        for key,value in self.users.items():
            print(value)

    def update_user(self,user_id, name: None, email: None):
        if user_id not in self.users:
            print("User not found.")
            return

        if name:
            self.users[user_id].name = name

        if email:
            self.users[user_id].email = email

        print(f"User '{user_id}' updated.") 
    def delete_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]
            print(f"User {user_id} deleted.")

        else:
            print("User not found.")



library = Library()
# b1 = Book("Atomic Habits","James Clear",9783442178582)
# b2 = Book("Harry Potter","J.K. Rowling",9780590353427)
# library.add_book(b2)
# library.add_book(Book("Narein Boddapati","Narein",5134882192))
# library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", 9780743273565))
# # library.list_books()
# library.borrow_book(5134882192)
# library.return_book(5134882192)

library.add_user(Users(123,"Narein","nareinbod@gmail.com"))
library.list_users()
library.update_user(123)
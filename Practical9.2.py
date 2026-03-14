class Library:
    books = [] # List to store book names

    def add_book(self):
        title = input("Enter book name to add: ")
        self.books.append(title)
        print("Book added!")

    def display_books(self):
        print("\nBooks in Library:", self.books)

    def lend_book(self):
        title = input("Enter book to borrow: ")
        if title in self.books:
            self.books.remove(title)
            print("You have borrowed the book.")
        else:
            print("Book not available.")

    def return_book(self):
        title = input("Enter book name to return: ")
        self.books.append(title)
        print("Book returned!")

# Start the system
lib = Library()

while True:
    print("\n1. Add  2. Display  3. Borrow  4. Return  5. Exit")
    choice = input("Select an option: ")

    if choice == '1':
        lib.add_book()
    elif choice == '2':
        lib.display_books()
    elif choice == '3':
        lib.lend_book()
    elif choice == '4':
        lib.return_book()
    elif choice == '5':
        break
    else:
        print("Wrong choice!")

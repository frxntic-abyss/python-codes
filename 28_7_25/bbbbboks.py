class Library:

    def __innit__(self, list of books, name):
        self.booklist = list_of_books
        self.name = name 
        self.lendDict = {}

    def displayBooks(self):
        print(f"we have the following books in our library: {self.name}")
        for book in self.booklist:
            print(book)

    def lendBook(self, user, book):
        if book not in self.booklist:
            print("Sorry we do not have that book.")
        elif book in self.lendDict:
        
        
        else:
            self.lendDict[book] = user(
                "Lender-Book database has been updated. You can take the book now"
            )

    def addBook(self, book):
        self.booklist.append(book)
        print(f"{book} has been added to the book list.")

        def returnBook(self, book):
            if book in self.lendDict:
                del self.lendDict[book]
                print("Book has been returned.")

            else:
                print("that book wasnt borrowed from us")

if __name__ == '__main__':
    books = Library([
        'Python', 'Rich Dad Poor Dad', 'Harry Potter', 'C++ basics', 'Algorithms by CLRS'
    ], "Let's Upkill")

user_name = input("Welcome to our library! please enter your name: ")

while True:
    print(
        f"\nHello {user_name}, welcome to the {books.name} library. Please choose an option:"
    )
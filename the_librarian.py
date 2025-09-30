# [
#     {"title": "Richest man in Babylon", "author": "Author 1", "year_of_publication": 2002, "isbn": "987-3789-773-23", "available": True},
#     {"title": "Richest man in Babylon", "author": "Author 1", "year_of_publication": 2002, "isbn": "987-3789-773-23", "available": True},
#     {"title": "Richest man in Babylon", "author": "Author 1", "year_of_publication": 2002, "isbn": "987-3789-773-23", "available": True},
#     {"title": "Richest man in Babylon", "author": "Author 1", "year_of_publication": 2002, "isbn": "987-3789-773-23", "available": True},
# ]



library = [] 


def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = int(input("Enter year of publication: "))
    isbn = input("Enter ISBN: ")
    book = {
        "Title": title,
        "Author": author,
        "Year": year,
        "ISBN": isbn,
        "Available": True
    }
    library.append(book)
    print("Book added successfully!\n")


def view_books():
    if not library:
        print("No books in the library.\n")
        return
    for book in library:
        print(
            f"Title: {book['Title']}, Author: {book['Author']}, "
            f"Year: {book['Year']}, ISBN: {book['ISBN']}, "
            f"Available: {'Yes' if book['Available'] else 'No'}"
        )
    print()


def update_book(isbn):
    for book in library:
        if book["ISBN"] == isbn:
            print("Leave input blank if you don’t want to update a field.")
            title = input(f"New title (current: {book['Title']}): ")
            author = input(f"New author (current: {book['Author']}): ")
            year = input(f"New year (current: {book['Year']}): ")

            if title:
                book["Title"] = title
            if author:
                book["Author"] = author
            if year:
                book["Year"] = int(year)

            print("Book updated successfully!\n")
            return
    print("Book not found.\n")


def delete_book(isbn):
    global library
    for book in library:
        if book["ISBN"] == isbn:
            library.remove(book)
            print("Book deleted successfully!\n")
            return
    print("Book not found.\n")


def search_book(title):
    for book in library:
        if book["Title"].lower() == title.lower():
            print(
                f"Found -> Title: {book['Title']}, Author: {book['Author']}, "
                f"Year: {book['Year']}, ISBN: {book['ISBN']}, "
                f"Available: {'Yes' if book['Available'] else 'No'}\n"
            )
            return
    print("Book not found.\n")


def borrow_book(isbn):
    for book in library:
        if book["ISBN"] == isbn:
            if book["Available"]:
                book["Available"] = False
                print("Book borrowed successfully!\n")
            else:
                print("Book is already borrowed.\n")
            return
    print("Book not found.\n")


def return_book(isbn):
    for book in library:
        if book["ISBN"] == isbn:
            if not book["Available"]:
                book["Available"] = True
                print("Book returned successfully!\n")
            else:
                print("Book was not borrowed.\n")
            return
    print("Book not found.\n")


def menu():
    while True:
        print("Library Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Search Book by Title")
        print("6. Borrow Book")
        print("7. Return Book")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            isbn = input("Enter ISBN of the book to update: ")
            update_book(isbn)
        elif choice == "4":
            isbn = input("Enter ISBN of the book to delete: ")
            delete_book(isbn)
        elif choice == "5":
            title = input("Enter title of the book to search: ")
            search_book(title)
        elif choice == "6":
            isbn = input("Enter ISBN of the book to borrow: ")
            borrow_book(isbn)
        elif choice == "7":
            isbn = input("Enter ISBN of the book to return: ")
            return_book(isbn)
        elif choice == "8":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    menu()

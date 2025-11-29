list  = []
def book():
    Title = str(input("Enter the book title: "))
    Author = str(input("Enter the author name: "))
    Pulication_year = int(input("Enter the publication year: "))
    Genre = str(input("Enter the genre: "))
    read_status = bool(input("Have you read the book? (True/False): "))
    book_info  = {
        "Title" :Title , 
        "Author": Author,
        "Pulication_year": Pulication_year, 
        "Genre" : Genre,
        "read_status" : read_status
    }
    list.append(book_info)
    return list
def remove_book():
    title_to_remove = str(input("Enter the title of the book to remove: "))
    author_to_remove = str(input("Enter the author of the book to remove: "))
    for book in list:
        if book["Title"] == title_to_remove and book["Author"] == author_to_remove:
            list.remove(book)
            print(f'Book "{title_to_remove} author {author_to_remove}" removed successfully.')
            return
    print(f'Book "{title_to_remove}" not found in the library.')
def search_book():
    title_to_search = str(input("Enter the title of the book to search: "))
    for book in list:
        if book["Title"] == title_to_search:
            print("Book found:")
            print(book)
            return
    print(f'Book "{title_to_search}" not found in the library.')
def display_books():
    if not list:
        print("No books in the library.")
        return
    print("Books in the library:")
    for book in list:
        print(book)
def display_statistics():
    total_books = len(list)
    if total_books == 0:
        print("No books in the library to display statistics.")
        return
    read_books = sum(1 for book in list if book["read_status"])
    percentage_read = (read_books / total_books) * 100
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.2f}%")
def exit_system():
    print("Exiting the library system. Goodbye!")
def menu_system():
        y :str = 'y'
        while (y =='y'): 
            print("Welcome to Library! ")
            print("1.Add a book")
            print("2.Remove a book")
            print("3.Search for a book")
            print("4.Display all books")
            print("5.Display statistics (total books, percentage read)")
            print("6.Exit")
            choice = int(input("Please provide your choice : "))
            match choice :
                case 1:
                    book()
                case 2:
                    remove_book()
                case 3:
                    search_book()
                case 4:
                    display_books()
                case 5:
                    display_statistics()
                case 6:
                    exit_system()
            y = input("Do you want to perform new action? (y/n): ")
menu_system()
Book = {}

# function to add book
def add_book(): 
    name = input("Enter the book name:")
    progress = input("Enter number of pages read:")
    Book[name] = progress

# function to search for a book
def search_book(): 
    search_name = input("Enter the book name")
    if search_name in Book: 
            print(search_name, "'s progress is", Book[search_name])


# function to display all books in the list
def display_book():
    print("Name\t\tBook Progress")
    for key in Book: 
        print("{}\t\t{}".format(key,Book.get(key)))


# function to update a boook in the list 
def update_book(): 
    edit_book = input("Enter the book name to updated")
    if edit_book in Book: 
            progress = input("Enter the updated progress")
            Book[edit_book]=progress
            print("Progress updated")
            display_book()

# function to delete a book in the list 
def delete_book(): 
    del_book = input("Enter the book to be deleted")
    if del_book in Book: 
            confirm = input("Do you want to delete this book y/n?")
            if confirm == 'y' or confirm == 'Y':
                Book.pop(del_book)
            display_book()

Book = {}

def print_menu():
    print ("""Choose a number:
    1. Add a book
    2. Update a book
    3. View all books
    4. Delete a book
    """)




print("Welcome to ProgRead, your personal reading tracker")
while(True): 
    print_menu()
    response = int(input())
    if response == 1:
        print("Add a book")
        name = input("Enter the book name:")
        progress = input("Enter number of pages read:")
        Book[name] = progress
    elif response == 2:
        print("Updating a book")
    elif response == 3: 
        print("All your current books")
    elif response == 4:
        print("Deleting a book")
    else: 
        print("Enjoy your reading")
        break
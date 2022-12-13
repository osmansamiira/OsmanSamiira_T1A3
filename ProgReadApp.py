def print_menu():
    print ("""Choose a number:
    1. Add a book
    2. Update a book
    3. View all books
    4. View wishlist
    5. Delete a book
    """)




print("Welcome to ProgRead, your personal reading tracker")
while(True): 
    print_menu()
    response = int(input())
    if response == 1:
        print("Add a book")
    elif response == 2:
        print("Updating a book")
    elif response == 3: 
        print("All your current books")
    elif response == 4:
        print("My Wishlist")
    elif response == 5:
        ("Deleting a book")
    else: 
        print("Enjoy your reading")
        break
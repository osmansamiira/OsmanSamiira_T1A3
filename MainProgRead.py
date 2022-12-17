import os
from functions import add_book, search_book, display_book, update_book, delete_book
import datetime
Book = {}
now = datetime.datetime()

# function to display the menu
def print_menu():
    print ("""Choose a number:
    1. Add a book
    2. Search for a book
    3. View all books
    4. Update a book
    5. Delete a book
    6. Exit from app
    """)

print("Welcome to ProgRead, your personal reading tracker")
while(True): 
    print_menu()
    try:
        response = int(input())
    except ValueError: 
        print("Invalid input. Please enter a number.")
        response = int(input())
    if response == 1:
        print("Add a book")
        add_book
    elif response == 2:
        search_name = input("Enter the book name")
        if search_name in Book: 
            print(search_name, "'s progress is", Book[search_name])
        else: 
            print("Book is not found in the list")
    elif response == 3: 
       if not Book: 
        print("Empty book list") 
       else: 
        display_book()
    elif response == 4: 
        edit_book = input("Enter the book name to updated")
        if edit_book in Book: 
            progress = input("Enter the updated progress")
            Book[edit_book]=progress
            print("Progress updated")
            display_book()
        else: 
            print("Book is not found in the list")
    elif response == 5:
        del_book = input("Enter the book to be deleted")
        if del_book in Book: 
            confirm = input("Do you want to delete this book y/n?")
            if confirm == 'y' or confirm == 'Y':
                Book.pop(del_book)
            display_book()
        else: 
            print("Book is not found in the list")
    elif response == 6: 
        print("Have fun reading, we hope to see you again soon!")
       
        
from os import system 
import webbrowser
import csv
import pandas as pd
from functions import add_book, search_book, display_book, update_book, delete_book
Book = {}
wishlist = {}

# function to display the menu
def print_menu():
    print ("""Choose an option:
    1. Add a book
    2. Search for a book
    3. View all books
    4. Update a book
    5. Delete a book
    6. View Amazon wishlist
    """)

print("Welcome to ProgRead, your personal reading tracker")
while (True): 
    option = print_menu()
    #error handling if a number isn't chosen
    try:
        option = int(input())
    except ValueError: 
        print("Invalid option. Please enter a number between 1-6.")
        option = int(input())
    if option == 1:
        print("Add a book")
        add_book()
    elif option == 2:
        search_book()
    elif option == 3:  
        display_book()
    elif option == 4: 
        update_book()
    elif option == 5:
        delete_book() 
    elif option == 6: 
         df= pd.read_csv('./wishlist.csv')
         print(df.to_string()) 

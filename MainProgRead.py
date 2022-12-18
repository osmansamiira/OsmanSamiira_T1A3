from os import system 
import csv
from csv import writer
import pandas as pd
from functions import add_book, search_book, display_book, update_book, delete_book, view_wishlist, add_wishlist
Book = {}
wishlist = {}

# function to display the menu options
def print_menu():
    print("1. Add a book")
    print("2. Search for a book ")
    print("3. Display all my books")
    print("4. Update a book")
    print("5. Delete a book")
    print("6. Add to my wishlist")
    print("7. View my wishlist")
    print("8. Return to menu")
    print("9. Exit app")
    opt = input("Choose your option (1-9): ")
    return opt


option = ""
    
print("- Welcome to ProgRead, your personal reading tracker -")
while option != "9":
    option = print_menu() 
    if option == "1":
        print("Add a book")
        add_book()
    elif option == "2":
        search_book()
    elif option == "3":  
        display_book()
    elif option == "4": 
        update_book()
    elif option == "5":
        delete_book() 
    elif option == "6": 
        add_wishlist()
    elif option == "7":
        view_wishlist()
    elif option == "8": 
        continue
    elif option == "9": 
        break

    # error handling if a number between 1-9 isn't selected

    try:
        option = int(input())
        if (option == 1): 
            add_book()
        elif (option == 2): 
            search_book()
        elif (option == 3): 
            display_book()
        elif (option == 4): 
            update_book()
        elif (option == 5): 
            delete_book()
        elif (option == 6): 
            add_wishlist()
        elif (option == 7): 
            view_wishlist()
        elif (option == 8): 
            continue 
        elif (option == 9): 
            break
    except ValueError:
        print("Invalid input. Please enter a number between 1-9.")
   


    
        








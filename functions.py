Book = {}
import csv
from os import system
from csv import writer 
import pandas as pd

# function to add book
def add_book(): 
    name = input("Enter the book name: ")
    progress = input("Enter number of pages read: ")
    print("Book has been successfully added")
    print("Select 8 to return to menu")
    Book[name] = progress
    
# function to search for a book
def search_book(): 
    search_name = input("Enter the book name: ")
    if search_name in Book: 
            print(search_name,"'s progress is", Book[search_name])
            print("Select 8 to return to menu")
    else: 
            print("Book is not found in the list")
            print("Select 8 to return to menu")


# function to display all books in the list
def display_book():
    if not Book: 
        print("Empty book list") 
        print("Select 8 to return to menu")
    else:
       print("Name\t\tBook Progress")
    for key in Book: 
        print("{}\t\t{}".format(key,Book.get(key)))
        print("Select 8 to return to menu")


# function to update a boook in the list 
def update_book(): 
    edit_book = input("Enter the book name to updated: ")
    if edit_book in Book: 
            progress = input("Enter the updated progress: ")
            Book[edit_book]=progress
            print("Progress updated")
            display_book()
    else: 
            print("Book is not found in the list")
            print("Select 8 to return to menu")

# function to delete a book in the list 
def delete_book(): 
    del_book = input("Enter the book to be deleted: ")
    if del_book in Book: 
            confirm = input("Do you want to delete this book y/n?")
            if confirm == 'y' or confirm == 'Y':
                Book.pop(del_book)
            display_book()
    else: 
            print("Book is not found in the list")
            print("Select 8 to return to menu")

# function to view wishlist 
def view_wishlist(): 
     df= pd.read_csv('./amazonbookswishlist.csv')
     print('')
     print('*********************')
     print('Books Amazon Wishlist')
     print('*********************')
     print(df.to_string (index=False))
     print('')
     print("Select 8 to return to menu")
     

# function to add to Amazon wishlist 
def add_wishlist(): 
     with open('amazonbookswishlist.csv', 'w+') as file: 
        myfile = csv.writer(file)
        myfile.writerow(["Book Name", "Amazon Link"])
        noOfBooks = int(input("Please enter how many books you would like to add: "))
        # create a loop for number of books input
        for i in range (noOfBooks): 
            BookName = input("Book" + str(i +  1) + " : Please enter the name of the book: ")
            AmazonLink = input("Book" + str(i +  1) + " : Please enter the Amazon link: ") 
            myfile.writerow([BookName, AmazonLink])
        print("Books have been added")
        print("Select 8 to return to menu")
        


       

        
  


    
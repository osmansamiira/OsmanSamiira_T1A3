# Progread
## App for all your reading tracker needs
Progread is designed for avid readers who often find themselves losing track of which books they are currently reading and how far they've progressed. This is a simple and easy to use app which will allow them to note down their progress and even save which books they're wishing to read in the future. 

**Name:** Samiira Osman

**Repository Link:** https://github.com/osmansamiira/OsmanSamiira_T1A3

**Presentation link:** https://drive.google.com/file/d/12SCxy0KXoP2przehYNwRdaJJAyqAsj1l/view

## Features

The features which are present in this app include: 

_**- Add a book**_

This feature users readers to add books that they have begun reading as well as how far they've progressed into the book. 

_**- Search for a book**_

This feature allows for users to search for a book that they've added to their list so that they can see how far they've progressed into this book. 

_**- Display all books**_

This feature allows for users to see a list of all the books that they have added

_**- Update a book**_

This feature allows users to update their progress on a book which is currently in their list

_**- Delete a book**_

This feature allows users to delete a book from their list (i.e. if they've finished reading the book)

_**- Add to my wishlist/view my wishlist**_ 

These are additional features which allow users to add in any books that they are hoping to read in the future, by adding the name of the book along with the amazon link to purchase the book. They can also view all the books currently in their wishlist. 

## Implementation plan

## Instructions 

**How to open the app:**

- Install python3
- Check that the terminal is in the appropriate directory to run the app
- Use command: 
``` .\run_mainpy.bat ```
- App will automatically open and can commence use of features. 

**How to use the features:**

![menufeature](https://user-images.githubusercontent.com/115801257/208289334-f6012107-4a97-4173-8cc6-c0a469cce57a.JPG)

Once the main menu has been opened, select an option to proceed. 

_Option 1:_

Once you've selected 1, the following should appear: 

![addbookfeature](https://user-images.githubusercontent.com/115801257/208289223-37cb8b63-ed8b-4f89-a780-8b21f22e68b9.JPG)

- Enter both the book name and number of pages
- Once the message reads "book has been successfully added" then hit **8** to return back to the menu 

_Option 2:_

**2** allows you to search for a book. If you haven't added any books to the list, the following will appear: 

![searchwnobook](https://user-images.githubusercontent.com/115801257/208289253-aa11aa23-f409-4bba-98d4-36ab3096a1de.JPG)

However, once you've added a book to the list, the following will appear: 

![searchwbook](https://user-images.githubusercontent.com/115801257/208289240-a5ac8a85-9c5b-4f98-82fc-c09a255403a8.JPG)

_Option 3:_

**3** allows you to view all the books you've added so far: 

![displaybooksfeature](https://user-images.githubusercontent.com/115801257/208289264-43234962-044c-4d5a-9db9-48f8342554d3.JPG)

_Option 4:_

This features allows you to update a book that is currently on your reading list to reflect the progress you have made. 

Once you enter which book to update, hit enter and the change will be reflected in the list. 

![updatedbook](https://user-images.githubusercontent.com/115801257/208289270-3a1329fe-9af0-4de3-9b44-facfae04548f.JPG)

_Option 5:_

This features allows you to delete a book from the list. 
Once you've selected **5**, you enter the name of the book you wish to delete. 

Then a confirmation should appear: select **y** if you wish to delete this book followed by enter. 

If this was the only book on your list the list will now show up as empty. 

![deleteconfirmfeature](https://user-images.githubusercontent.com/115801257/208289278-9db9db5b-f6d2-4bdd-b9f9-abbd24983490.JPG)

_Option 6&7:_

These are the wishlist features of the app. In order to add an item to the wishlist, first enter option **6**. 

The app will then ask how many books you wish to add to the wishlist, followed by asking for the name and link to the amazon page to purchase this book.

After this, hit enter and the books have been added to the list.

![addtowishlist](https://user-images.githubusercontent.com/115801257/208289292-61ea9717-42ad-48a1-8d08-3589012fc2e6.JPG)

Once you've added a book, select option **7** to view these books in your wishlist: 

![viewwishlist](https://user-images.githubusercontent.com/115801257/208289306-79bd7fc4-e761-45e9-b2f2-ce4fa373e44b.JPG)



## Manual Testing 

![image](./docs/Manual%20Error%20Testing.JPG)




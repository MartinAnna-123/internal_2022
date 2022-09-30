# function for adding a new book (title, author, pages, genre) - press A
def book_add():
  
  keys = ["author", "year", "genre", "pages"]

  title = input("Enter books title: ")

  # the ___edited variables are just the users input that has had the first letters capitalized so the dictionary is consistent no matter what the user enters. 
  titleEdited = title.title()

  author = input ("Enter books author: ")

  authorEdited = author.title()

  year = input ("Enter the books year of publishing: ")

  genre = input ("what genre is {}: ".format(title))

  genreEdited = genre.capitalize()

  pages = input ("how many pages does {} have?: ".format(titleEdited))

  values = [str(authorEdited), str(year), str(genreEdited), str(pages)]

  data = dict(zip(keys,values))

  finaldata  = {titleEdited : data}

  # adds the information the user has entered into the dictionary that can be accessed from all functions so it ensures cohesion across the program
  books.update(finaldata)

  # prints out the data the user has added 
  print(titleEdited)
  print("Author:", books[titleEdited]['author'], "\nYear:", books[titleEdited]['year'], "\nGenre:", books[titleEdited]['genre'], "\nPages:", books[titleEdited]['pages'],)
  





  


# function for printing out the pages and author of all the books in the dictionary(books)  - press B
def book_info():
  for key, value in books.items():
    print(key)
    print("Pages:", books[key]['pages'], "      Author:", books[key]['author'])
    
 
  


    
    
# function for modifying number of pages of a book  - press C
def modify_pages():

  # a while loop that will continue until the user enters a title of a book that is in the dictionary: books
  valid = False

  while valid == False:

    bookChoice = input("what book do you want to adjust the pages of?")

    bookChoiceEdited = bookChoice.title()

    try:

      bookChoicePages = books.get(str(bookChoiceEdited)).get('pages')

      valid = True

    except AttributeError:

        print("The book title you have entered is not in the system \nHint: You may have spelt the title wrong. Check your spelling \nTry Again")

  # if statement adjusting the output depending on the number of pages the book title the user entered has (plural/singular)
  if int(bookChoicePages) > 1:

    print(bookChoiceEdited, "currently has", bookChoicePages, "Pages")

  elif int(bookChoicePages) == 1:

    print(bookChoiceEdited, "currently has", bookChoicePages, "Page")

  else:

    print(bookChoiceEdited, "currently has", bookChoicePages, "Pages")

  # once the user has entered a title that is in the dictionary(books) and automatically exited the previous loop they will enter this second loop which requires them to enter a new number of pages. This loop will continue looping if an integer is not added.
  valid = False
  while valid == False:

    newPages = input("what do you want to change the pages to? \nplease enter a number:")
    try:

      int(newPages)

      valid = True

    except ValueError:

      print("Oops, that was not an integer - try again")

  # the new page number is replaces the old page number in the dictionary
  books[bookChoiceEdited]['pages'] = newPages

  # if statement adjusting the output depending on the number the user enters(plural/singular)
  if int(newPages) > 1:

    print(bookChoiceEdited, "now has", newPages, "Pages")

  elif int(newPages) == 1:

    print(bookChoiceEdited, "now has", newPages, "Page")

  else:

    print(bookChoiceEdited, "now has", newPages, "Pages")
  








    
# function for printing out the updated number of pages of a book - press D
def book_page_print ():
  
  book = input("please type a book title that you want to know the number of pages\n")
  
  bookEdited = book.title()

  number = False 
  while number == False:
    try:

      pageTest = books[str(bookEdited)]['pages']

      # if statement adjusting the output depending on the number the user enters
      if int(pageTest) > 1:

        print('There are ' + pageTest + ' pages in {}'.format(bookEdited))

        number = True

      elif int(pageTest) == 1:

        print('There is ' + pageTest + ' page in {}'.format(bookEdited))

        number = True
      else:

        print('INVALID. Please follow the instructions')

        book_page_print ()

    except AttrubuteError:

      print("Oops, the book you have entered is not in the system - try again")







      
# dictionary containing all the information entered in the program about the books. The hunger games is in 'books' to format the dictionary.
books = {
  'The Hunger Games':{
    'author': 'Suzanne Collins',
    'year': '2008',
    'genre': 'Dystopian',
    'pages': '600',
  }
  
}




# This code is the 'start of the program'. The functions and dictionary are all accessed and sourced and used depending on what is selected in the menu loop.

# the introduction. The initial text the user sees when they press run
print('what do you want to do?')
quit = True

# The main menu is in a while loop so it will repeat until the user selects 'e' which is quit. The main menu navigates to all the functions and 'controls' the program
while quit == True:

  menu = input('\n a) Add a book to the library database \n b) Print all the book information (pages and author) \n c) Modify the pages in your chosen book \n d) print the amount of pages in your chosen book \n e) Quit \n')

  # depending on what the users input is, the if statement will direct them to the corresponding function
  if menu == 'a':

    book_add()

    print('\nwhat do you want to do next?')

  elif menu == 'b':

    book_info()

    print('\nwhat do you want to do next?')

  elif menu =='c':

    modify_pages()

    print('\nwhat do you want to do next?')

  elif menu == 'd':

    book_page_print()

    print('\nwhat do you want to do next?')

  elif menu == 'e':

    print('\nYou have quit the program.')

    # this will break the loop and the program will end
    quit = False

  else:
    # if the user hasn't entered a,b,c,d or e the loop will repeat and the user will be required to enter a letter again
    print('please enter either: a, b, c, d or e')

    








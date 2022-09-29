# function for adding a new book (title, author, pages, genere) - press A
def book_add():
  keys = ["author", "year", "genre", "pages"]
  title = input("Enter books title: ")
  titleEdited = title.title()
  author = input ("Enter books author: ")
  authorEdited = author.title()
  year = input ("Enter books year of publishing: ")
  genre = input ("what genre is {}: ".format(title))
  genreEdited = genre.capitalize()
  pages = input ("how many pages does {} have?: ".format(titleEdited))
  values = [str(authorEdited), str(year), str(genreEdited), str(pages)]
  data = dict(zip(keys,values))
  finaldata  = {titleEdited : data}
  print(finaldata)
  books.update(finaldata)
  


# function for printing out all books information  - press B
def book_info():
 print(books)


# function for modifying number of pages of a book  - press C
def book_pages():
  valid = False
  while valid == False:
    bookChoice = input("what book do you want to adjust the pages of?")
    bookChoiceEdited = bookChoice.title()
    try:
      bookChoicePages = books.get(str(bookChoiceEdited)).get('pages')
      valid = True
    except AttributeError:
        print("Oops, the book you have entered is not in the system - try again")
  
  print('The '+ bookChoiceEdited + ' currently has ' + bookChoicePages + ' pages')
  
  valid = False
  while valid == False:
    newPages = input("what do you want to change the pages to? please enter a number")
    try:
      int(newPages)
      valid = True
    except ValueError:
        print("Oops, that was not an integer - try again")
        
  books[bookChoiceEdited]['pages'] = newPages

# if statement adjusting the output depending on the number the user enters
  if int(newPages) > 1:
    print(bookChoiceEdited, "now has", newPages, "Pages")
  elif int(newPages) == 1:
    print(bookChoiceEdited, "now has", newPages, "Page")
  else:
    print(bookChoiceEdited, "now has", newPages, "Pages")
  # else:
  #   print(bookChoice, " does not exist.")

  
  


# function for printing out the updated number of pages of a book - press D

def book_page_print ():
  book = input("please type a book title that you want to know the number of pages\n")
  page_print = True 
  while page_print == True:
    if str(book) in books:
      a = books[str(book)]['pages']
      # if statement adjusting the output depending on the number the user enters
      if int(a) > 1:
        print('There are ' + a + ' pages in {}'.format(book))
      elif int(a) == 1:
        print('There is ' + a + ' page in {}'.format(book))
      page_print = False
    else:
      print('INVALID. Please follow the instructions')
      book_page_print ()

# the dictionary contains all the information entered in the program about the books 
books = {
  'Hunger Games':{
    'author': 'Suzanne Collins',
    'year': '2008',
    'genre': 'Dystopian',
    'pages': '600',
  }
  
}

# main function - contains the menu 

print('what do you want to do?')
quit = True
while quit == True:
  menu = input('\n a) Add a book to the library database \n b) Print all book information \n c) Modify the pages in your chosen book \n d) print the amount of pages in your chosen book \n e) Quit \n')
  if menu == 'a':
    book_add()
  elif menu == 'b':
    book_info()
  elif menu =='c':
    book_pages()
  elif menu == 'd':
    book_page_print()
  elif menu == 'e':
    print('You have quit the program.')
    quit = False
  else:
    print('please enter either: a, b, c, d or e')
  
    








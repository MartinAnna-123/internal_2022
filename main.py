# function for adding a new book (title, author, pages, genere) - press A
def book_add():
  keys = ["author", "year", "genre", "pages"]
  title = input("Enter books title: ")
  author = input ("Enter books author: ")
  year = input ("Enter books year of publishing: ")
  genre = input ("what genre is {}: ".format(title))
  pages = input ("how many pages does {} have?: ".format(title))
  values = [str(author), str(year), str(genre), str(pages)]
  data = dict(zip(keys,values))
  finaldata  = {title : data}
  print(finaldata)
  books.update(finaldata)
  


# function for printing out all books information  - press B
def book_info():
 print(books)


# function for modifying number of pages of a book  - press C
def book_pages():
  bookChoice = input("what book do you want to adjust the pages of?")
  print('The '+ bookChoice + ' currently has ' + books.get(str(bookChoice)).get('pages') + ' pages')

  if bookChoice in books:
    newPages = input("what do you want to change the pages to? please enter a number")
    books[bookChoice]['pages'] = newPages
    if int(newPages) > 1:
      print(bookChoice, "now has", newPages, "Pages")
    elif int(newPages) == 1:
      print(bookChoice, "now has", newPages, "Page")
    else:
      print(bookChoice, "now has", newPages, "Pages")
  else:
    print(bookChoice, " does not exist.")

  
  


# function for printing out the updated number of pages of a book - press D

def book_page_print ():
  book = input("please type a book title that you want to know the number of pages\n")
  page_print = True 
  while page_print == True:
    if str(book) in books:
      a = books[str(book)]['pages']
      if int(a) > 1:
        print('There are ' + a + ' pages in {}'.format(book))
      elif int(a) == 1:
        print('There is ' + a + ' page in {}'.format(book))
      page_print = False
    else:
      print('INVALID. Please follow the instructions')
      book_page_print ()


# main function - contains the menu 
def main ():
  quit = True 
  print('what do you want to do?')
  while quit == True:
    menu = input('a) Add a book to the library database \n b) Print all book information \n c) Modify the pages in your chosen book \n d) print the amount of pages in your chosen book \n e) Quit \n')
    if menu == 'a':
      book_add()
    elif menu == 'b':
      book_info()
    elif menu =='c':
      book_pages()
    elif menu == 'd':
      book_page_print ()
    elif menu == 'e':
      quit == False

# the dictionary contains all the information entered in the program about the books 
books = {
  'hunger games':{
    'author': 'Suzanne Collins',
    'year': '2008',
    'genre': 'Dystopian',
    'pages': '600',
  }
}

# run main function, which is running the menu 
main()

# this prints the author of the hunger games which is stored in the dictionary (books). 
print(dictionary['Hunger Games']['author'])



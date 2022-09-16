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
  


# function for printing out all books information  - press b 

def book_info():
 print(books)


# function for modifying number of pages of a book  
def book_pages():
  bookChoice = input("what book do you want to add info too?")
  choice1 = input("what section for {} do you want to add information too?".format(bookChoice))
  if (choice1 == "Author") or (choice1 == "author"):
    entered = input("enter the author of {}".format(bookChoice))
    books.update(entered)
  elif (choice1 == "Year") or (choice1 == "year"):
    entered = input("enter the year {} was published".format(bookChoice))
    books.update(entered)
  elif (choice1 == "Genre") or (choice1 == "genre"):
    entered = input("enter the genre of {}".format(bookChoice))
    books.update(entered)
  elif (choice1 == "Pages") or (choice1 == "pages"):
    entered = input("enter the number of pages in {}".format(bookChoice))
    books.update(entered)
  else:
    print("you didn't type anything correctly")
    book_info()
    
  print('this is the updated version of the pages in your book')
  book_page_print()


# function for printing out the updated number of pages of a book - Press c

def book_page_print ():
  a = dictionary['title'].get(str(book))
  print(a)
  a = int(a)
  choice = input("what do you want to know about {}. Please type: Author, Year,  Genre  or Pages: ".format(str(book)))
  if choice == "Author" or choice == "author":
    print("the author of" + str(book) + "is {}".format(dictionary.get(a)))
  elif choice == "Year" or choice == "year":
    print("the year " + str(book) + " was published was {}".format(dictionary['year'].get(a)))
  elif choice == "Genre" or choice == "genre":
    print("the genre of " + str(book) + " is {}".format(dictionary['genre'].get(a)))
  elif choice == "Pages" or choice == "pages":
    print(str(book) + "has {} pages".format(dictionary['pages'].get(a)))
  else:
    print("you didn't type anything correctly")
    book_info()


# main function - contains the menu 
def main ():
  quit = True 
  print('what do you want to do?')
  while quit == True:
    menu = input('a) Add a book to the library database \n b) Print all book information \n c) adjust the pages in you chosen book \n d) Quit \n')
    if menu == 'a':
      book_add()
    elif menu == 'b':
      book_info()
    elif menu =='c':
      book_pages()
    elif menu == 'd':
      quit == False

# the dictionary contains all the information entered in the program about the books 
books = {
  'Hunger Games':{
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



# def book_list ():
 
#  title = input("Enter books title: ")
#  dictionary.update({"title" : str(title)})
#  author = input("Enter books author: ")
#  dictionary.update({"author" : str(author)})
#  year = input("Enter books year of publishing: ")
#  dictionary.update({"year" : str(year)})
#  genre = input("what genre is {}: ".format(title))
#  dictionary.update({"genre" : str(genre)})
#  pages = input("how many pages does {} have?: ".format(title))
#  dictionary.update({"pages" : str(pages)})
#  print(dictionary)







# keys = ["title", "author", "year", "genre", "pages"]


# bookTitles = ["Hunger Games", "Little Women"] 
# bookAuthors = ["Suzanne Collins", "Lousia May Alcott"]
# bookYear = ["2008","1868"]
# bookGenre = ["dystopian", "coming-of-age"]
# bookPages = ["600", "670"]

# book = input('enter a title')
# a = dictionary['title'].get(str(book))
#   print(a)

# print ("Title: {}, Author: {}, Published: {}, Genre: {}, Pages: {}," .format(bookTitles, bookAuthors, bookYear, bookGenre, bookPages ))

# repeat = True
# while repeat == True:
#   question = input("do you want to add a book to the list?")
#   if question == "yes":
#     book_list()
#   else:
#     question2 = input("do you want to find out information about a book?")
#     if question2  == "yes":
#       book = input("what book do  you want to know information about?")
#       book_info()
#     else:
#       "ok"
#       repeat = False
    

# print ("Title: {}, Author: {}, Published: {}, Genre: {}, Pages: {}," .format(bookTitles, bookAuthors, bookYear, bookGenre, bookPages ))



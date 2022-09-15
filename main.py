def main ():
  quit = True 
  while quit == True:
    menu = input('a) Add a book to the library database \n b) Find information about a chosen book \n c) change or add information about a book \n d) Quit \n')
    if menu == 'a':
      book_list()
    elif menu == 'b':
      book_info()
    elif menu == 'c':
      book_update()
    elif menu == 'd':
      quit == False
    else:
      main()

    
def book_list ():
 
 title = input("Enter books title: ")
 dictionary.update({"title" : str(title)})
 author = input("Enter books author: ")
 dictionary.update({"author" : str(author)})
 year = input("Enter books year of publishing: ")
 dictionary.update({"year" : str(year)})
 genre = input("what genre is {}: ".format(title))
 dictionary.update({"genre" : str(genre)})
 pages = input("how many pages does {} have?: ".format(title))
 dictionary.update({"pages" : str(pages)})
 print(dictionary)


def book_info ():
  a = dictionary['title'].get(str(book))
  print(a)
  # a = int(a)
  # choice = input("what do you want to know about {}. Please type: Author, Year,  Genre  or Pages: ".format(str(book)))
  # if choice == "Author" or choice == "author":
  #   print("the author of" + str(book) + "is {}".format(dictionary.get(a)))
  # elif choice == "Year" or choice == "year":
  #   print("the year " + str(book) + " was published was {}".format(dictionary['year'].get(a)))
  # elif choice == "Genre" or choice == "genre":
  #   print("the genre of " + str(book) + " is {}".format(dictionary['genre'].get(a)))
  # elif choice == "Pages" or choice == "pages":
  #   print(str(book) + "has {} pages".format(dictionary['pages'].get(a)))
  # else:
  #   print("you didn't type anything correctly")
  #   book_info()

def dict_zip ():
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
  dictionary.update(finaldata)
  print(dictionary[str(title)]['author''year''genre''pages'])

def book_update():
  bookChoice = input("what book do you want to add info too?")
  choice1 = input("what section for {} do you want to add information too?".format(bookChoice))
  if (choice1 == "Author") or (choice1 == "author"):
    entered = input("enter the author of {}".format(bookChoice))
    dictionary.update(entered)
  elif (choice1 == "Year") or (choice1 == "year"):
    entered = input("enter the year {} was published".format(bookChoice))
    dictionary.update(entered)
  elif (choice1 == "Genre") or (choice1 == "genre"):
    entered = input("enter the genre of {}".format(bookChoice))
    dictionary.update(entered)
  elif (choice1 == "Pages") or (choice1 == "pages"):
    entered = input("enter the number of pages in {}".format(bookChoice))
    dictionary.update(entered)
  else:
    print("you didn't type anything correctly")
    book_info()


dict_zip ()
dictionary = {
  'Hunger Games':{
    'author': 'Suzanne Collins',
    'year': '2008',
    'genre': 'Dystopian',
    'pages': '600',
  }
}
print(dictionary['Hunger Games']['author'])

keys = ["title", "author", "year", "genre", "pages"]
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



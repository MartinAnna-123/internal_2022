def book_list ():
 
 title = input("Enter books title: ")
 bookTitles.append(title)
 author = input ("Enter books author: ")
 bookAuthors.append(author)
 year_of_publishing = input ("Enter books year of publishing: ")
 bookYear.append(year_of_publishing)
 genre = input ("what genre is {}: ".format(title))
 bookGenre.append(genre)
 pages = input ("how many pages does {} have?: ".format(title))
 bookPages.append(pages)

def book_info ():
  a = bookTitles.index(book)
  choice = input("what do you want to know about {}. Please type: Author, Year,  Genre  or Pages".format(book))
  if (choice == "Author") or (choice == "author"):
    print("the author of" + book + "is {}".format(bookAuthors(int(a))))
  elif (choice == "Year") or (choice == "year"):
    print("the year " + book + " was published was {} ".format(bookYear(int(a))))
  elif (choice == "Genre") or (choice == "genre"):
    print("the genre of " + book +  " is {}".format(bookGenre(int(a))))
  elif (choice == "Pages") or (choice == "pages"):
    print(book  + "has {} pages".format(bookPages(int(a))))
  else:
    print("you didn't type anything correctly")
    book_info()

bookTitles = ["Hunger Games", "Little Women"] 
bookAuthors = ["Suzanne Collins", "Lousia May Alcott"]
bookYear = ["2008","1868"]
bookGenre = ["dystopian", "coming-of-age"]
bookPages = ["600", "670"]

print("lets add some more books to the list")
book_list()



print ("Title: {}, Author: {}, Published: {}, Genre: {}, Pages: {}," .format(bookTitles, bookAuthors, bookYear, bookGenre, bookPages ))

repeat = True
while repeat == True:
  question = input("do you want to add a book to the list?")
  if question == "yes":
    book_list()
  else:
    question2 = input("do you want to find out information about a book?")
    if question2  == "yes":
      book = input("what book do  you want to know information about?")
      book_info()
    else:
      "ok"
      repeat = False
    

print ("Title: {}, Author: {}, Published: {}, Genre: {}, Pages: {}," .format(bookTitles, bookAuthors, bookYear, bookGenre, bookPages ))



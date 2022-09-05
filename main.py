def book_store ():
 
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
    

bookTitles = [] 
bookAuthors = []
bookYear = []
bookGenre = []
bookPages = []


book_store()
book_store()


print ("Title: {}, Author: {}, Published: {}, Genre: {}, Pages: {}," .format(bookTitles, bookAuthors, bookYear, bookGenre, bookPages ))
print(bookTitles, bookAuthors, bookYear, bookGenre, bookPages)
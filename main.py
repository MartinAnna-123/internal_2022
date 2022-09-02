def book_store (title, author, year_of_publishing, genre, pages):
    
    # title = input("Enter books title: ")
    # author = input ("Enter books author: ")
    # year_of_publishing = input ("Enter books year of publishing: ")
    # genre = input ("what genre is {}: ".format(title))
    # pages = input ("how many pages does {} have?: ".format(title))

    print ("Title: " + title + ", Author: " + author + ", Published: " + 
  year_of_publishing + ", Genre: " + genre + ", Pages: " + pages)

bookTitles = [] 
bookAuthors = []
bookYear = []
bookGenre = []
bookPages = []

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

book_store(title, author, year_of_publishing, genre, pages)
print(bookTitles, bookAuthors, bookYear, bookGenre, bookPages)
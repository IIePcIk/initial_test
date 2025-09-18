class Book:
    def __init__(self, Name, Author, Date, ISBN, Pages, Genre, Topic):
        self.Name = Name
        self.Author = Author
        self.Date = Date
        self.ISBN = ISBN
        self.Pages = Pages
        self.Genre = Genre
        self.Topic = Topic

book1 = Book("Pyton", "Djorsh Bush", "1999", "2837563836", "320", "ПТехнічна література", "Програмування")
book2 = Book("Pyton", "Djorsh Bush", "1999", "2837563836", "320", "ПТехнічна література", "Програмування")
book3 = Book("Pyton", "Djorsh Bush", "1999", "2837563836", "320", "ПТехнічна література", "Програмування")
print(book1.ISBN)
print(book1.Topic)
print(book1.Date)

class Book:
    def __init__(self, Name, Author, Date, ISBN, Pages, Genre, Topic):
        self.Name = Name
        self.Author = Author
        self.Date = Date
        self.ISBN = ISBN
        self.Pages = Pages
        self.Genre = Genre
        self.Topic = Topic

book1 = Book("Pyton", "Djorsh Bush", "1999", "2837563835", "320", "ПТехнічна література", "Програмування")

book2 = Book("Pyton", "Djorsh Bush", "1999", "2837563834", "320", "ПТехнічна література", "Програмування")

book3 = Book("Pyton", "Djorsh Bush", "1999", "2837563833", "320", "ПТехнічна література", "Програмування")

print(book1.ISBN)
print(book1.Topic)
print(book1.Date)

class Library:
    def __init__(self, name, address , contacts, readers = []):
        self.readers = readers
        self.name = name
        self.address = address
        self.contacts = contacts
    
    def info(self):
        return f"Бібліотека {self.name} знаходиться за адресою {self.address}. Контакти: {self.contacts}"
    
    def add_reader(self, reader_name):
        self.readers.append(reader_name)
        print(f"Читача '{reader_name}' додано до бібліотеки.")
    
    def display_readers(self):
        if self.readers:
            print("\nСписок читачів:")
            for i, reader in enumerate(self.readers):
                print(f"{i + 1}. {reader}")
        else:
            print("\nСписок читачів порожній.")

Library1 = Library("Central Library", "123 Main St", +123456789)
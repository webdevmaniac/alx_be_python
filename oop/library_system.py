class Book:
    def __init__(self, title, author):
        """
        Initialize a Book instance.
        :param title: Title of the book.
        :param author: Author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        """
        Initialize an EBook instance.
        :param title: Title of the book.
        :param author: Author of the book.
        :param file_size: File size of the ebook in KB.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """
        Initialize a PrintBook instance.
        :param title: Title of the book.
        :param author: Author of the book.
        :param page_count: Number of pages in the book.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        """
        Initialize a Library instance with an empty collection of books.
        """
        self.books = []

    def add_book(self, book):
        """
        Add a book to the library.
        :param book: An instance of Book, EBook, or PrintBook.
        """
        self.books.append(book)

    def list_books(self):
        """
        Print details of all books in the library.
        """
        for book in self.books:
            print(book)

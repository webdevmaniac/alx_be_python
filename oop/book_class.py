class Book:
    def __init__(self, title, author, year):
        """
        Constructor to initialize the Book instance.
        :param title: Title of the book.
        :param author: Author of the book.
        :param year: Publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor that prints a message when a Book instance is deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String representation of the Book instance.
        :return: A formatted string with book details.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official representation of the Book instance.
        :return: A string that recreates the Book instance.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"

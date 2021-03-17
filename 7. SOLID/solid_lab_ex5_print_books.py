from abc import ABC, abstractmethod


class Book:
    def __init__(self, title, author, content: str):
        self.title = title
        self.author = author
        self.content = content


class Formatter(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        pass


class ContentFormatter(Formatter):
    def format(self, book: Book) -> str:
        return book.content


class AuthorFormatter(Formatter):
    def format(self, book: Book) -> str:
        return book.author


class Printer:
    def print(self, book: Book, formatter: Formatter):
        return formatter.format(book)


book = Book("Harry Potter", "J.K.Rowling", "The boy who lived....")
printer = Printer()
print(printer.print(book, AuthorFormatter()))


from abc import ABC, abstractmethod


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

class NotificationServiceBase(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass

class SMS(NotificationServiceBase):
    def send_notification(self, message):
        print(f'Sending SMS: {message}')

class EMail(NotificationServiceBase):
    def send_notification(self, message):
        print(f'Sending email: {message}')

class BookGiver:
    @staticmethod
    def give_book(user: User, book: Book):
        user.borrowed_books.append(book)

class BorrowingProcessor:
    @staticmethod
    def borrow_book(user: User, book: Book, notif_service: NotificationServiceBase):
        if not book.is_borrowed:
            book.is_borrowed = True
            BookGiver.give_book(user, book)
            notif_service.send_notification(f'Book {book.title} has been borrowed by {user.name}')
        else: notif_service.send_notification('Book is already borrowed')


sms = SMS()
user1 = User('Natasha')
book1 = Book('1984', 'George Orwell')

BorrowingProcessor.borrow_book(user1, book1, sms)

print(book1.is_borrowed)
print(user1.borrowed_books[0].title)
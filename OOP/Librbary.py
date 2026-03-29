from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class Book:
    title: str
    author: str
    isbn: str


class BookCopy:
    def __init__(self, copy_id: int, book: Book):
        self.copy_id = copy_id
        self.book = book
        self.available = True


class Member:
    def __init__(self, member_id: str):
        self.member_id = member_id
        self.borrowed_books: List[BookCopy] = []


class Loan:
    def __init__(self, member: Member, book_copy: BookCopy):
        self.member = member
        self.book_copy = book_copy


class Library:

    def __init__(self):
        self.books: Dict[str, Book] = {}
        self.book_copies: List[BookCopy] = []
        self.members: Dict[str, Member] = {}
        self.loans: List[Loan] = []

    def add_book(self, book: Book, copies: int):

        self.books[book.isbn] = book

        for i in range(copies):
            copy = BookCopy(len(self.book_copies) + 1, book)
            self.book_copies.append(copy)

    def register_member(self, member_id: str):
        self.members[member_id] = Member(member_id)

    def search_book(self, title: str):

        for book in self.books.values():
            if book.title == title:
                return book

        return None

    def borrow_book(self, member_id: str, isbn: str):

        member = self.members.get(member_id)

        for copy in self.book_copies:

            if copy.book.isbn == isbn and copy.available:

                copy.available = False

                loan = Loan(member, copy)
                self.loans.append(loan)

                member.borrowed_books.append(copy)

                return copy

        raise ValueError("No available copies")

    def return_book(self, member_id: str, copy_id: int):

        member = self.members.get(member_id)

        for book_copy in member.borrowed_books:

            if book_copy.copy_id == copy_id:

                book_copy.available = True
                member.borrowed_books.remove(book_copy)

                return book_copy

        raise ValueError("Book not borrowed by this member")
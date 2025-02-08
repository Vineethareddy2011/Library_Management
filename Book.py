from typing import List
from MinHeap import MinHeap
from Patron import Patron


class Book():
    # Remove the List[Patron] annotation as it's now a MinHeap
    def __init__(self, bookId, bookName, authorName, availabilityStatus) -> None:
        self.bookId = bookId
        self.bookName = bookName
        self.authorName = authorName
        self.availabilityStatus = availabilityStatus
        self.borrowedBy = None
        self.reservationHeap = MinHeap()
        self.parent = None
        self.left = None
        self.right = None
        self._color = 1
        self.transformations = -1
        self.flipCount=0
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, value):
        self.transformations += 1
        self._color = value
    def __str__(self) -> str:
        reservations_str = ", ".join([str(patron.patronId) for patron in self.reservationHeap.get_all_elements()])
        book_info = (
            f"BookId = {self.bookId}\n"
            f"Title = {self.bookName}\n"
            f"Author = {self.authorName}\n"
            f"Availability = {self.availabilityStatus}\n"
            f"BorrowedBy = {self.borrowedBy}\n"
            f"Reservations = {reservations_str}"
        )
        return book_info
    def __insert_into_reservation(self, patronId, patronPriority):
        patron = Patron(patronId, patronPriority)
        existing_patrons = [p for p in self.reservationHeap.get_all_elements() if p.patronId == patronId]
        if existing_patrons:
            already_reserved_patron = existing_patrons[0]
            already_reserved_patron.patronPriority = patronPriority
            print(f"Book {self.bookId} Reservation Updated for Patron {patronId} \n")
        else:
            print(f"Book {self.bookId} Reserved By Patron {patronId} \n")
            self.reservationHeap.insert(patron)

    def borrowBook(self, patronId, patronPriority):
        if self.borrowedBy is None:
            self.borrowedBy = patronId
            self.availabilityStatus = "No"
            print(f"Book {self.bookId} Borrowed By Patron {self.borrowedBy}\n")
        else:
            # Add patron to reservations
            self.__insert_into_reservation(patronId, patronPriority)
    def returnBook(self, patronId):
        if self.borrowedBy == patronId:
            print(f"Book {self.bookId} Returned By Patron {self.borrowedBy}\n")
            # Check if there are reservations
            if not self.reservationHeap.is_empty():
                next_patron = self.reservationHeap.remove_min()
                self.borrowedBy = next_patron.patronId
                print(f"Book {self.bookId} Allotted to Patron {self.borrowedBy}\n")
            else:
                # No reservations, mark the book as available
                self.borrowedBy = None
                self.availabilityStatus = 'Yes'
        else:
            return(f"Book {self.bookId} not borrowed by Patron {patronId}\n")

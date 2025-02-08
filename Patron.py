from typing import List

class Patron:
    def __init__(self, patronId, patronPriority) -> None:
        self.patronId = patronId
        self.patronPriority = patronPriority
    def compare(self, other):
        return self.patronPriority < other.patronPriority
    def __str__(self):
        return f"PatronID: {self.patronId}, Priority: {self.patronPriority}"
    def __gt__(self, other):
        return self.patronPriority > other.patronPriority

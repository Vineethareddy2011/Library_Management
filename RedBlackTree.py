from typing import List
from Book import Book
from MinHeap import MinHeap

class RedBlackTree():
    def __init__(self):
        self.TNULL = Book(0, '', '', '')
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL
        self.colorFlip = 0
        self.reservationHeap = MinHeap()
    # Search the tree
    def __search_tree_helper(self, node, key) -> Book:
        if node == self.TNULL or key == node.bookId:
            return node
        if key < node.bookId:
            return self.__search_tree_helper(node.left, key)
        return self.__search_tree_helper(node.right, key)
    # Balancing the tree after deletion
    def __delete_fix(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    self.colorFlip+=2
                    s.color = 0
                    x.parent.color = 1
                    self.__left_rotate(x.parent)
                    s = x.parent.right
                if s.left.color == 0 and s.right.color == 0:
                    self.colorFlip+=1
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        self.colorFlip+=2
                        s.left.color = 0
                        s.color = 1
                        self.__right_rotate(s)
                        s = x.parent.right
                    self.colorFlip+=2
                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.__left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    self.colorFlip+=2
                    s.color = 0
                    x.parent.color = 1
                    self.__right_rotate(x.parent)
                    s = x.parent.left
                if s.right.color == 0 and s.right.color == 0:
                    self.colorFlip+=1
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        self.colorFlip+=2
                        s.right.color = 0
                        s.color = 1
                        self.__left_rotate(s)
                        s = x.parent.left
                    self.colorFlip+=2
                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.__right_rotate(x.parent)
                    x = self.root
        x.color = 0
    def __rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
    # Node deletion
    def __delete_node_helper(self, node, key):
        z = self.TNULL
        while node != self.TNULL:
            if node.bookId == key:
                z = node
            if node.bookId <= key:
                node = node.right
            else:
                node = node.left
        if z == self.TNULL:
            print("Cannot find key in the tree")
            return
        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.__rb_transplant(z, z.right)
        elif (z.right == self.TNULL):
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.__minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:
            self.__delete_fix(x)
    # Balance the tree after insertion
    def __fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    self.colorFlip+=3
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.__right_rotate(k)
                    self.colorFlip+=2
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.__left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == 1:
                    self.colorFlip+=3
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.__left_rotate(k)
                    self.colorFlip+=2
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.__right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0
    def __minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node
    def __left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
    def __right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
    def __closest_node(self, node, bookId, min_diff, min_diff_book):
        if node == self.TNULL:
            return
        if node.bookId == bookId:
            min_diff_book[0] = node
            return
        # update min_diff and min_diff_key by
        # checking current node value
        if min_diff > abs(node.bookId - bookId):
            min_diff = abs(node.bookId - bookId)
            min_diff_book[0] = node
        # if k is less than ptr->key then move
        # in left subtree else in right subtree
        if bookId < node.bookId:
            self.__closest_node(node.left, bookId, min_diff, min_diff_book)
        else:
            self.__closest_node(node.right, bookId, min_diff, min_diff_book)
        return min_diff_book[0]
    def findClosestBook(self, targetId):
    # Find the closest book
        closest_book = self.__find_closest_node(self.root, targetId, None)
        if closest_book is None:
            print("No books found in the tree.")
            return []

        # Check for ties
        closest_books = [closest_book]
        distance = abs(closest_book.bookId - targetId)
        self.__find_ties(self.root, targetId, distance, closest_books)

        # Sort by book IDs if there are ties
        closest_books.sort(key=lambda book: book.bookId)

        # Create a list of strings representing the closest book(s)
        closest_books_str = [str(book) for book in closest_books]

        return closest_books_str

    def __find_closest_node(self, node, targetId, currentClosest):
        if node == self.TNULL:
            return currentClosest
        if currentClosest is None or abs(node.bookId - targetId) < abs(currentClosest.bookId - targetId):
            currentClosest = node
        if node.bookId > targetId:
            return self.__find_closest_node(node.left, targetId, currentClosest)
        else:
            return self.__find_closest_node(node.right, targetId, currentClosest)
    def __find_ties(self, node, targetId, distance, closestBooks):
        if node == self.TNULL:
            return
        currentDistance = abs(node.bookId - targetId)
        if currentDistance == distance and node not in closestBooks:
            closestBooks.append(node)
        self.__find_ties(node.left, targetId, distance, closestBooks)
        self.__find_ties(node.right, targetId, distance, closestBooks)
    def insertBook(self, bookId, bookName, authorName, availabilityStatus):
        book = Book(bookId, bookName, authorName, availabilityStatus)
        book.parent = None
        book.left = self.TNULL
        book.right = self.TNULL
        book.color = 1
        y = None
        x = self.root
        while x != self.TNULL:
            y = x
            if book.bookId < x.bookId:
                x = x.left
            else:
                x = x.right
        book.parent = y
        if y == None:
            self.root = book
        elif book.bookId < y.bookId:
            y.left = book
        else:
            y.right = book
        if book.parent == None:
            book.color = 0
            return
        if book.parent.parent == None:
            return
        self.__fix_insert(book)
        
    def deleteBook(self, bookId):
        book = self.searchBook(bookId)
        res=""
        if book:
            reservations_str = ", ".join([str(patron.patronId) for patron in book.reservationHeap.get_all_elements()])
            res=(f"Book {book.bookId} is no longer available. Reservations made by Patrons {reservations_str} have been cancelled!\n")
            self.__delete_node_helper(self.root, bookId)
        return res
    def searchBook(self, bookId):
        return self.__search_tree_helper(self.root, bookId)
    def printBook(self, bookId):
        book = self.__search_tree_helper(self.root, bookId)
        if book != self.TNULL:  # Check if the book is not the sentinel node
            return str(book)
    def printBooks(self, bookId1, bookId2):
        arr=[]
        for bookId in range(bookId1, bookId2+1):
            if self.printBook(bookId) is not None:
                arr.append(self.printBook(bookId))
        return arr
    def borrowBook(self, patronId, bookId, patronPriority):
        book = self.searchBook(bookId)
        if (book):
            book.borrowBook(patronId, patronPriority)
        return str(book)
    def returnBook(self, patronId, bookId):
        book = self.searchBook(bookId=bookId)
        if (book):
            book.returnBook(patronId)
        return str(book)
    def colorFlipCount(self):
        print(self.colorFlip)
        return(f"Colour Flip Count: {self.colorFlip}\n")
    def in_order_helper(self, node: Book):
        transformations = 0
        if node != self.TNULL:
            transformations += self.in_order_helper(node.left)
            if node.color == 0:  # Only count transformations for black nodes
                transformations += node.transformations
            transformations += self.in_order_helper(node.right)
        return transformations
    def quit(self):
        print("Program Terminated!!")

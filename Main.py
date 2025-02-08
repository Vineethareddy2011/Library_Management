from typing import List
from RedBlackTree import RedBlackTree

if __name__== "__main__":
    gator_library = RedBlackTree()

    try:
        with open("input.txt", 'r') as input_file, open("output_file.txt", 'w') as output_file:
            for line in input_file:
                input_line = line.strip()
                
                in_params = input_line[input_line.find("(") + 1:input_line.find(")")].split(",")

                if input_line.startswith("InsertBook"):
                    book_id = int(in_params[0].strip())
                    book_name = in_params[1].strip()  # assuming the book name is within quotes
                    author_name = in_params[2].strip()  # assuming the author name is within quotes
                    availability_status = in_params[3].strip()  # assuming the status is within quotes

                    node=gator_library.insertBook(book_id, book_name, author_name, availability_status)
                    # Assuming the insertBook method does not return any value
                    
                    #output_file.write(f"Book {book_id} inserted\n\n")
                    output_file.write("\n")
                elif input_line.startswith("PrintBook"):
                    if len(in_params) == 1:
                        book_id = int(in_params[0].strip())
                        book = gator_library.searchBook(book_id)
                        if book != gator_library.TNULL:  # Check if the book is not the sentinel node
                            output_file.write(str(book))
                        else:
                            output_file.write(f"Book {book_id} not found in the Library\n")
                        output_file.write("\n")
                    
                    else:
                        print("hello")
                        book_id1 = int(in_params[0].strip())
                        print(book_id1)
                        book_id2 = int(in_params[1].strip())
                        arr=gator_library.printBooks(book_id1, book_id2)
                        # Assuming printBooks directly prints to the console.
                        for i in arr:
                            output_file.write(str(i))
                        ##output_file.write("Printed books in range\n\n")
                            output_file.write("\n")
                elif input_line.startswith("BorrowBook"):
                    patron_id = int(in_params[0].strip())
                    book_id = int(in_params[1].strip())
                    patron_priority = int(in_params[2].strip())
                    
                    gator_library.borrowBook(patron_id, book_id, patron_priority)
                    # Assuming borrowBook method does not return any value
                    output_file.write(f"Book {book_id} borrowed by Patron {patron_id}\n\n")
                    output_file.write("\n")

                elif input_line.startswith("ReturnBook"):
                    patron_id = int(in_params[0].strip())
                    book_id = int(in_params[1].strip())
                    gator_library.returnBook(patron_id, book_id)
                    # Assuming returnBook method does not return any value
                    output_file.write(f"Book {book_id} returned by Patron {patron_id}\n\n")
                    output_file.write("\n")

                elif input_line.startswith("FindClosestBook"):
                    target_id = int(in_params[0].strip())
                    p=gator_library.findClosestBook(target_id)
                    for i in p:
                        output_file.write(str(i))
                    # Assuming findClosestBook directly prints to the console.
                    #output_file.write("Closest book found\n\n")
                    output_file.write("\n")

                elif input_line.startswith("DeleteBook"):
                    book_id = int(in_params[0].strip())
                    output_file.write(gator_library.deleteBook(book_id))
                    # Assuming deleteBook method does not return any value
                    output_file.write(f"Book {book_id} deleted\n\n")
                    output_file.write("\n")

                elif input_line.startswith("ColorFlipCount"):
                    output_file.write(gator_library.colorFlipCount())
                    # Assuming colorFlipCount directly prints to the console.
                    #output_file.write("Color flip count displayed\n\n")
                    output_file.write("\n")

                elif input_line.startswith("Quit"):
                    output_file.write("Program Terminated!!\n")
                    break

    except Exception as e:
        print(f"An error occurred: {e}")
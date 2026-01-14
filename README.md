# library-management-system

This project was developed as part of practice core Python programming concepts, including:

1) File handling (reading from/writing to text files)
2) Data structure manipulation (working with lists and tuples)
3) User interaction through a console menu
4) Error handling and input validation

**Functional requirements **

**Storage Format:**

Each book's information must be stored in a text file using the format:
Title|Author|Year

Example:
War and Peace|Leo Tolstoy|1869

Functional Requirements:

**Add Books:**

Users can input book information including Title, Author, and Publication Year

The program stores each book as a tuple in a list: [('War and Peace','Leo Tolstoy',1869), ...]

**Read Books from File:**

On startup, the program attempts to load books from a file (e.g., books.txt)

If the file doesn't exist, the program notifies the user and continues with an empty list

**Search Books:**

Users can search books by title or author

The program displays all found books in a readable format

**Remove Books:**

Users can delete books by title or author

Removed books disappear from the file on the next program run

**Display Book List:**

After adding books and before program termination, the full current book list should be displayed

**Save Data to File:**

Before exiting, the program saves the updated book list back to the text file in the specified format

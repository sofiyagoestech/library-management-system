class Library:
    def __init__(self):
        self.items = []
        self.filename = "new_library.txt"

    def start_library(self):
        """By starting the programme it displays the current books from txt file"""
        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()
                library = []
                for i, line in enumerate(lines, start=1):
                    library.append(f"{i}. {line.strip()}")

            return "\n".join(library)

        except FileNotFoundError:
            return "Library file not found"


    def add_item(self, item):
        """Add an item to the library list"""
        info = []
        for i in item.values():
            info.append(i)
        self.items.append(tuple(info))
        return self.items

    def save_items(self):
        """Save a book from list to txt file.
        If list is empty, error message: No books found
        Otherwise, add title, author, year into txt file and display success message: Book added successfully"""

        if self.items:
            with open(self.filename, "a") as file:
                for item in self.items:
                    title, name, year = item
                    file.write(f"{title}|{name}|{year}\n")

            return True, "Book added successfully"
        else:
            return False, "No books found"


    def remove_item(self, item):

        """Remove book from txt file.
        User input book title or author's name. Function searches for matches and removes them from txt file.
        If found, success message: Book removed successfully.
        Otherwise, error message: No book found"""

        with open(self.filename, "r") as file:
            lines = file.readlines()
        with open(self.filename, "w") as file:
            match = False
            for line in lines:
                if item not in line:
                    file.write(line)
                else:
                    match = True
                    continue
        if match:
            return True, "Book removed successfully"
        else:
            return False, "No book found"

    def search_item(self,item):
        """Search book in txt file and display it if found. 
        Otherwise, error message: No book found"""
        search = []
        with open(self.filename, "r") as file:
            lines = file.readlines()
            match = False
            for line in lines:
                if item in line:
                    search.append(line)
                    match = True
                else:

                    continue
        if not match:
            return False, "No book found"
        else:
            return "\n".join(search)

class Book:
    def __init__(self):
        self.book = {}

    def create_book(self):
        """Creating book from user input and returning it in dict format"""
        self.book["title"] = input("Enter title: ")
        self.book["author"] = input("Enter author: ")
        self.book["year"] = input("Enter year: ")
        return self.book

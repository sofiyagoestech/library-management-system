"""Library programme"""

class Library:

    def __init__(self):
        self.filename = "library1.txt"
        self.items = self.start_library()

    def __enter__(self):
        print("Loading your library".center(50, "="))
        print(self.items)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Saving new items".center(50, "="))
        print(self.save_items())

    def start_library(self):
        """By starting the programme it should display the current books from txt file"""
        try:
            with open(self.filename, "r") as file:
                library = []
                for line in file:
                    line = line.strip().split("|")
                    library.append(tuple(line))

            return library

        except FileNotFoundError:
            return []


    def add_item(self, item):
        """Add an item to the library list"""
        self.items.append(item)
        return self.items

    def save_items(self):
        """Save a book to the library list."""
        if self.items:
            with open(self.filename, "w") as file:
                for item in self.items:
                    title, name, year = item
                    file.write(f"{title}|{name}|{year}\n")
            return "Book(s) added successfully"
        else:
            return "No books found"


    def remove_item(self,**kwargs):
        removed = []
        for remove_item in self.search_item(**kwargs):
            if remove_item in self.items:
                self.items.remove(remove_item)
                removed.append(remove_item)
            else:
                return "Item not found"
        return f"{removed} removed"


    def search_item(self, **kwargs):
        """Search book in list and display it if found.
        Otherwise, error message: No book found"""
        search = []
        if kwargs.get("title"):
            for item in self.items:
                title, name, year = item
                if title.lower() == kwargs["title"].lower():
                    search.append(item)

        elif kwargs.get("author"):
            for item in self.items:
                title, name, year = item
                if name.lower() == kwargs["author"].lower():
                    search.append(item)
        else:
            return "No book matching your criteria"

        if not search:
            return "No book found"
        return search

class Book:
    def __init__(self, title, author, year):
        self.book = title, author, year

    def __str__(self):
        return f"{self.book[0]}|{self.book[1]}|{self.book[2]}"

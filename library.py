"""Library programme"""

class Library:
    def __init__(self):
        self.items = []
        self.filename = "new_library.txt"

    def start_library(self):
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
        """Adding new book into the LIST"""
        new_item = item.split(", ")
        self.items.append(tuple(new_item))
        return self.items

    def save_items(self):
        with open(self.filename, "a") as file:
            for item in self.items:
                title, name, year = item
                file.write(f"{title}|{name}|{year}\n")

        return True, "Book added successfully"

    def remove_item(self, item):
        with open(self.filename, "r") as file:
            lines = file.readlines()
        with open(self.filename, "w") as file:
            for line in lines:
                if item not in line:
                    file.write(line)
                else:
                    continue
        return True, "Book removed successfully"

    def search_item(self,item):
        search = []
        with open(self.filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                if item in line:
                    search.append(line)
                else:
                    continue
        return "\n".join(search)

**Library Management System**

A small Python project built to demonstrate my approach to application logic and automated testing.

The application manages a text-based library of books and supports loading data from a file, adding new books, searching by title or author, removing books, and saving updates back to storage. Alongside the core functionality, the project includes automated tests written with pytest to validate the main user flows and file-based behaviors.

**Why I Built This Project
**
I created this project to strengthen my practical Python and test automation skills in a simple but realistic scenario.

**It gave me a chance to work with:**

Python classes and methods
file handling
context managers
automated tests with pytest
fixtures and parametrized tests
isolated test data using temporary files

This repository is part of my QA / test automation portfolio and reflects how I approach structuring tests around application behavior rather than testing for its own sake.

**Project Overview**

The application stores books in a text file using the format:

Title|Author|Year
Crime and Punishment|Fyodor Dostoevsky|1866
Anna Karenina|Leo Tolstoy|1877

When loaded into the program, books are represented as tuples such as:

("Crime and Punishment", "Fyodor Dostoevsky", "1866")

**The Library class is responsible for:**

loading books from a file
storing them in memory
adding new items
searching for books
removing books
saving updates back to the file

The class uses a context manager so that data is loaded on entry and saved on exit.

**Features**
Load books from a text file
Add books to the in-memory collection
Search for books by title or author
Remove matching books
Save the updated library back to file
Use a context manager for loading and saving data
Automated Testing

The project includes automated tests written with pytest to validate the main library workflows.

**Current test coverage
**
The current test suite covers:

loading books from a sample file
adding new books
removing books by title or author
searching for existing and non-existing books
Testing approach

**The test suite uses:
**
pytest
fixtures for reusable setup
@pytest.mark.parametrize for broader input coverage
tmp_path to create temporary test files and keep tests isolated

Using temporary files helps ensure tests are repeatable and do not affect real project data.

**Project Structure
**

library-management-system/
├── library.py
├── test_library.py
├── README.md
└── library.txt

**How to Run the Tests**

Install pytest:

pip install pytest

**Run the test suite:**

pytest -v

**Example Scenarios Covered**

The automated tests currently validate scenarios such as:

loading a library containing multiple books
adding a new book and checking the collection updates correctly
removing a book by title or author
searching for a book that exists
searching for a book that does not exist
What This Project Demonstrates

This project reflects my current learning and practice in Python-based test automation. In particular, it demonstrates:

writing readable automated tests
using parametrization to extend test coverage
isolating file-based tests with temporary data
validating core application behavior through repeatable checks
Current Limitations

**This project is still a work in progress. At its current stage:
**
books are stored as tuples rather than a separate Book class
input validation is still limited
some methods could be refactored for clearer and more consistent return values
edge cases and negative scenarios need broader coverage
Next Steps

**Planned improvements include:
**
introducing a separate Book class
improving validation and error handling
expanding negative and edge-case coverage
improving consistency of method behavior and return types
adding stronger persistence checks
potentially adding CI with GitHub Actions to run tests automatically
Portfolio Note

This is a learning project, but it is also intended to show how I think about testing: focusing on core behavior, maintainable test structure, and realistic validation of user flows.

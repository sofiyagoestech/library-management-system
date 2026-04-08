import pytest
from pathlib import Path
from LibraryClass import Library

@pytest.fixture
def sample_library_file(tmp_path):
    library_file = tmp_path/ "test_library.txt"
    library_file.write_text("Crime and Punishment|Fyodor Dostoevsky|1866\n"
    "Anna Karenina|Leo Tolstoy|1877\n"
    "The Master and Margarita|Mikhail Bulgakov|1967\n"
    "Doctor Zhivago|Boris Pasternak|1957\n"
    "One Day in the Life of Ivan Denisovich|Alexander Solzhenitsyn|1962\n")
    return library_file


def test_load_library(sample_library_file):
    with Library(sample_library_file) as library:
        assert len(library.items) == 5

@pytest.mark.parametrize("book", [("Crime and Punishment", "Fyodor Dostoevsky", "1866"), ("Anna Karenina", "Leo Tolstoy", "1877")])
def test_add_item(sample_library_file, book):
    with Library(sample_library_file) as library:
        start_len = len(library.items)
        library.add_item(book)
        assert len(library.items) == start_len + 1

@pytest.mark.parametrize("kwargs", [
    {"title": "Crime and Punishment"},
    {"author": "Fyodor Dostoevsky"},
    {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky"},
    {"title": "Anna Karenina"},
    {"author": "Leo Tolstoy"},
    {"title": "Anna Karenina", "author": "Leo Tolstoy"},
])
def test_remove_item(sample_library_file, kwargs):
    with Library(sample_library_file) as library:
        start_len = len(library.items)
        library.remove_item(**kwargs)
        assert len(library.items) == start_len - 1

@pytest.mark.parametrize("kwargs, expected", [
    ({"title": "Crime and Punishment"}, True),
    ({"author": "Fyodor Dostoevsky"}, True),
    ({"title": "Harry Potter"}, False)])
def test_search_item(sample_library_file, kwargs, expected):
    with Library(sample_library_file) as library:
        search = library.search_item(**kwargs)
        if search == "No book found":
            found = False
        else:
            found = True
        assert found == expected


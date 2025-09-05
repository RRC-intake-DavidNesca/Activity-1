# This import brings in the Genre enumeration we will use for valid genres.
from genre.genre import Genre

# This variable records the author of this file as requested by the course template.
__author__ = "David Nesca"
# This variable records the version string for this file.
__version__ = "1.0.0"
# This variable records optional credits information for this file.
__credits__ = "6"

# This class definition starts the LibraryItem class which will hold all related data and behavior.
class LibraryItem:
    # This docstring explains the purpose of the class and its attributes.
    """
    Represents a library item with a title, author, genre, item id, and a borrowed flag.
    """

    # This method constructs a new LibraryItem and validates each input using simple checks.
    def __init__(self, title, author, genre, item_id, is_borrowed):
        # This line removes leading and trailing spaces from the title so that only meaningful characters remain.
        cleaned_title = str(title).strip()
        # This line checks that the title is not blank and raises a ValueError if it is.
        if cleaned_title == "":
            raise ValueError("Title cannot be blank.")
        # This line removes leading and trailing spaces from the author so that only meaningful characters remain.
        cleaned_author = str(author).strip()
        # This line checks that the author is not blank and raises a ValueError if it is.
        if cleaned_author == "":
            raise ValueError("Author cannot be blank.")
        # This line checks that the genre matches one of the known Genre members using direct equality checks.
        if not (genre == Genre.FICTION or genre == Genre.NON_FICTION or genre == Genre.FANTASY or genre == Genre.TRUE_CRIME):
            # This line raises a ValueError because the provided genre value is not one of the allowed Genre values.
            raise ValueError("Genre must be a valid Genre.")
        # This try-block converts the item_id to an integer to ensure it is numeric.
        try:
            # This line attempts to convert item_id into an integer and stores it in numeric_id.
            numeric_id = int(item_id)
        # This except-block catches any error from the conversion when item_id is not numeric.
        except Exception:
            # This line raises a ValueError to clearly report that the item id must be numeric.
            raise ValueError("Item ID must be numeric.")
        # This line checks that the is_borrowed value is a real boolean by accepting only True or False exactly.
        if not (is_borrowed is True or is_borrowed is False):
            # This line raises a ValueError when the is_borrowed value is not a proper boolean.
            raise ValueError("Is Borrowed must be a boolean value.")

        # This line stores the cleaned title in a private attribute so it cannot be edited directly.
        self.__title = cleaned_title
        # This line stores the cleaned author in a private attribute so it cannot be edited directly.
        self.__author = cleaned_author
        # This line stores the validated genre in a private attribute so it cannot be edited directly.
        self.__genre = genre
        # This line stores the numeric id in a private attribute so it cannot be edited directly.
        self.__item_id = numeric_id
        # This line stores the exact boolean flag in a private attribute so it cannot be edited directly.
        self.__is_borrowed = is_borrowed

    # This decorator marks the following method as a read-only getter for the title.
    @property
    def title(self):
        # This line returns the private title attribute to the caller.
        return self.__title

    # This decorator marks the following method as a read-only getter for the author.
    @property
    def author(self):
        # This line returns the private author attribute to the caller.
        return self.__author

    # This decorator marks the following method as a read-only getter for the genre.
    @property
    def genre(self):
        # This line returns the private genre attribute to the caller.
        return self.__genre

    # This decorator marks the following method as a read-only getter for the item id.
    @property
    def item_id(self):
        # This line returns the private item id attribute to the caller.
        return self.__item_id

    # This decorator marks the following method as a read-only getter for the borrowed flag.
    @property
    def is_borrowed(self):
        # This line returns the private borrowed flag attribute to the caller.
        return self.__is_borrowed

    # This method returns a nicely formatted string so the object prints in a readable way.
    def __str__(self):
        # This line builds and returns the formatted multi-line string.
        return ("Title: " + self.__title + "\n"
                + "Author: " + self.__author + "\n"
                + "Genre: " + self.__genre.name.replace("_", " ").title() + "\n"
                + "Item ID: " + str(self.__item_id) + "\n"
                + "Borrowed: " + str(self.__is_borrowed))

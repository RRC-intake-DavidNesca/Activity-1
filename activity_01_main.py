# This import brings in LibraryItem so we can create and test objects in this small client.
from library_item.library_item import LibraryItem
# This import brings in the Genre enum so we can pass valid values for the genre field.
from genre.genre import Genre

# This variable records the author name for this script in the same style used by course files.
__author__ = "Student"
# This variable records the version string for this script.
__version__ = "1.0.0"
# This variable records optional credits for this script.
__credits__ = ""

# This function is the program entry point for this simple client.
def main():
    # This try-block constructs a valid LibraryItem and prints the object and each attribute.
    try:
        # This line creates a valid LibraryItem instance with realistic values.
        good = LibraryItem("Clean Code", "Robert C. Martin", Genre.NON_FICTION, 2025, False)
        # This line prints the formatted object so we can see all values at once.
        print(good)
        # This line prints the title using the accessor.
        print(good.title)
        # This line prints the author using the accessor.
        print(good.author)
        # This line prints the genre using the accessor.
        print(good.genre)
        # This line prints the item id using the accessor.
        print(good.item_id)
        # This line prints the borrowed flag using the accessor.
        print(good.is_borrowed)
    # This except-block shows any unexpected ValueError from the valid construction.
    except ValueError as e:
        # This line prints the error message if one happens.
        print(e)

    # This try-block shows an invalid example to demonstrate exception handling.
    try:
        # This line passes a blank title which should raise a ValueError from the constructor.
        bad = LibraryItem("   ", "Anon", Genre.FICTION, 1, False)
        # This line prints the object only if no exception occurs (which would be unexpected).
        print(bad)
    # This except-block catches the expected error and prints the message.
    except ValueError as e:
        # This line prints the error message from the invalid construction.
        print(e)

# This runs main() only when this script is the program entry point.
if __name__ == "__main__":
    # This line calls main() to execute the client code.
    main()

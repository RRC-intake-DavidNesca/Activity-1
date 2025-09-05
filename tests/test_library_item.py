# This import brings in the unittest framework used for writing simple unit tests.
import unittest
# This import brings in the LibraryItem class we want to test.
from library_item.library_item import LibraryItem
# This import brings in the Genre enum used for valid genre values.
from genre.genre import Genre

# This class defines a group of unit tests for the LibraryItem class.
class TestLibraryItem(unittest.TestCase):
    # This method prepares a fresh valid instance before each test so each test starts in a known state.
    def setUp(self):
        # This line creates a valid LibraryItem with typical values that can be reused in tests.
        self.item = LibraryItem("The Hobbit", "J. R. R. Tolkien", Genre.FANTASY, 101, False)

    # This test checks that a valid construction stores each attribute exactly.
    def test_init_sets_attributes(self):
        # This assertion checks the title property returns the expected string.
        self.assertEqual("The Hobbit", self.item.title)
        # This assertion checks the author property returns the expected string.
        self.assertEqual("J. R. R. Tolkien", self.item.author)
        # This assertion checks the genre property returns the expected enum value.
        self.assertEqual(Genre.FANTASY, self.item.genre)
        # This assertion checks the item_id property returns the expected integer.
        self.assertEqual(101, self.item.item_id)
        # This assertion checks the is_borrowed property returns the expected boolean.
        self.assertFalse(self.item.is_borrowed)

    # This test verifies that a blank title triggers a ValueError with the exact required message.
    def test_init_raises_when_title_blank(self):
        # This context expects a ValueError with the specific error message.
        with self.assertRaisesRegex(ValueError, "Title cannot be blank."):
            # This construction uses a blank title which should raise the error.
            LibraryItem("   ", "Some Author", Genre.FICTION, 1, False)

    # This test verifies that a blank author triggers a ValueError with the exact required message.
    def test_init_raises_when_author_blank(self):
        # This context expects a ValueError with the specific error message.
        with self.assertRaisesRegex(ValueError, "Author cannot be blank."):
            # This construction uses a blank author which should raise the error.
            LibraryItem("Some Title", "   ", Genre.FICTION, 1, False)

    # This test verifies that an invalid genre triggers a ValueError with the exact required message.
    def test_init_raises_when_genre_invalid(self):
        # This context expects a ValueError with the specific error message.
        with self.assertRaisesRegex(ValueError, "Genre must be a valid Genre."):
            # This construction passes a string for genre which should raise the error.
            LibraryItem("Some Title", "Some Author", "FICTION", 1, False)

    # This test verifies that a non-numeric item_id triggers a ValueError with the exact required message.
    def test_init_raises_when_item_id_not_numeric(self):
        # This context expects a ValueError with the specific error message.
        with self.assertRaisesRegex(ValueError, "Item ID must be numeric."):
            # This construction passes a non-numeric string for item_id which should raise the error.
            LibraryItem("Some Title", "Some Author", Genre.NON_FICTION, "ABC", False)

    # This test verifies that a non-boolean is_borrowed triggers a ValueError with the exact required message.
    def test_init_raises_when_is_borrowed_not_boolean(self):
        # This context expects a ValueError with the specific error message.
        with self.assertRaisesRegex(ValueError, "Is Borrowed must be a boolean value."):
            # This construction passes a string instead of a proper boolean which should raise the error.
            LibraryItem("Some Title", "Some Author", Genre.NON_FICTION, 5, "no")

    # This test checks the title accessor returns the correct value.
    def test_title_accessor(self):
        # This assertion confirms the title matches exactly.
        self.assertEqual("The Hobbit", self.item.title)

    # This test checks the author accessor returns the correct value.
    def test_author_accessor(self):
        # This assertion confirms the author matches exactly.
        self.assertEqual("J. R. R. Tolkien", self.item.author)

    # This test checks the genre accessor returns the correct value.
    def test_genre_accessor(self):
        # This assertion confirms the genre matches exactly.
        self.assertEqual(Genre.FANTASY, self.item.genre)

    # This test checks the item_id accessor returns the correct value.
    def test_item_id_accessor(self):
        # This assertion confirms the item id matches exactly.
        self.assertEqual(101, self.item.item_id)

    # This test checks the is_borrowed accessor returns the correct value.
    def test_is_borrowed_accessor(self):
        # This assertion confirms the borrowed flag matches exactly.
        self.assertFalse(self.item.is_borrowed)

# This boilerplate runs the tests when the file is executed directly.
if __name__ == "__main__":
    # This line invokes the unittest runner.
    unittest.main()

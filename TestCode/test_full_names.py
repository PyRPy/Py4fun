import unittest
from full_names import get_full_name

class NamesTestCase(unittest.TestCase):
    """Test for names.py."""

    def test_first_last(self):
        """Test nmae like Janis Jophlin."""
        full_name = get_full_name('janis', 'joplin')
        self.assertEqual(full_name, 'Janis Joplin')

unittest.main()

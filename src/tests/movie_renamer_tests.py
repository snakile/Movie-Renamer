import unittest
from movie_renamer import rename
from movie_renamer_test_data import filenames

class Test(unittest.TestCase):

    def test_rename(self):
        for old_filename, new_filename in filenames.items():
            self.assertEqual(rename(old_filename), new_filename)


if __name__ == "__main__":
    unittest.main()
import unittest
from filename_to_movie import create_imdb_query_from_filename

class Test(unittest.TestCase):

    def test_xvid_arrow(self):
        filename = r'Inception.DVDRiP.XviD-ARROW'
        self.assertEqual(create_imdb_query_from_filename(filename), 'inception')

if __name__ == "__main__":
    unittest.main()
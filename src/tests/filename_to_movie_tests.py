import unittest
from movie import Movie

def create_movie_from_filename(raw_name):
    return Movie("Inception", 2010)

class Test(unittest.TestCase):


    def test_xvid_arrow(self):
        raw_name = r'Inception.DVDRiP.XviD-ARROW'
        self.assertEqual(create_movie_from_filename(raw_name), 
                        Movie("Inception", 2010))

if __name__ == "__main__":
    unittest.main()
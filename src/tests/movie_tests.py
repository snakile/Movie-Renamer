import unittest
from movie import Movie


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_str(self):
        self.assertEqual(str(Movie('Pulp Fiction', 1995)), 'Pulp Fiction (1995)')
        self.assertEqual(str(Movie('Pulp Fiction', '1995')), 'Pulp Fiction (1995)')
    
    def test_create_movie_from_query_exact_title(self):
        the_prestige = Movie.create_movie_from_query('the prestige')
        self.assertEqual(the_prestige.title, "The Prestige")
        self.assertEqual(the_prestige.year, 2006)
    
    def test_create_movie_from_query_partial_title(self):
        the_matrix = Movie.create_movie_from_query('matrix')
        self.assertEqual(the_matrix.title, "The Matrix")
        self.assertEqual(the_matrix.year, 1999)

    def test_create_movie_from_query_no_spaces(self):
        the_dark_knight = Movie.create_movie_from_query('TheDarkKnight')
        self.assertEqual(the_dark_knight.title, "The Dark Knight")
        self.assertEqual(the_dark_knight.year, 2008)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
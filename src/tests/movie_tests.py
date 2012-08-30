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
    
    def test_equal(self):
        the_godfather = Movie('The Godfather', 1972)
        movie = Movie('Inception', 2010)
        self.assertNotEqual(the_godfather, movie)
        movie.title, movie.year = 'The Godfather', 1972
        self.assertEqual(the_godfather, movie)
    
    def test_create_movie_from_query_exact_title(self):
        the_prestige = Movie.create_movie_from_query('the prestige')
        self.assertEqual(the_prestige, Movie("The Prestige", 2006))
    
    def test_create_movie_from_query_partial_title(self):
        the_matrix = Movie.create_movie_from_query('matrix')
        self.assertEqual(the_matrix, Movie("The Matrix", 1999))

    def test_create_movie_from_query_no_spaces(self):
        the_dark_knight = Movie.create_movie_from_query('TheDarkKnight')
        self.assertEqual(the_dark_knight, Movie("The Dark Knight", 2008))
    
    def test_create_movie_from_query_dots_and_hyphens(self):
        LOTR_2 = Movie.create_movie_from_query('lord.of.rings-two.towers')
        self.assertEqual(LOTR_2, 
                    Movie("The Lord of the Rings: The Two Towers", 2002))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
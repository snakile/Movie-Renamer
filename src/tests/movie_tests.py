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
    
    def test_create_movie_from_query_simple(self):
        the_prestige = Movie.create_movie_from_query('the prestige')
        self.assertEqual(the_prestige.title, "The Prestige")
        self.assertEqual(the_prestige.year, 2006)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
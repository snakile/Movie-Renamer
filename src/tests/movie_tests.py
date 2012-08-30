import unittest
from movie import Movie


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_str(self):
        self.assertEqual(str(Movie('Pulp Fiction', 1995)), 'Pulp Fiction (1995)')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
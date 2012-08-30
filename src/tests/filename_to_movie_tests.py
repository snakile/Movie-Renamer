import unittest
from filename_to_movie import create_imdb_query_from_filename

class Test(unittest.TestCase):

    def test_filename_to_query(self):
        from filename_to_movie_test_data import expected_query
        for filename, imdb_query in expected_query.items():
            self.assertEqual(create_imdb_query_from_filename(filename), imdb_query)

if __name__ == "__main__":
    unittest.main()
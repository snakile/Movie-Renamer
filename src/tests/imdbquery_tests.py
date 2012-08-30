import unittest
from imdbquery import ImdbQuery

class TestImdbQuery(unittest.TestCase):

    def test_exclude_terms(self):
        query = ImdbQuery('Inception.DVDRiP.XviD-ARROW')
        terms_to_exclude = ('dvdrip', 'xvid', 'arrow')
        self.assertEqual(query.lower().exclude_terms(terms_to_exclude), 'inception. . -')


if __name__ == "__main__":
    unittest.main()
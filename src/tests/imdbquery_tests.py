import unittest
from imdbquery import ImdbQuery

class TestImdbQuery(unittest.TestCase):

    def test_exclude_terms(self):
        filename = ImdbQuery('Inception.DVDRiP.XviD-ARROW')
        terms_to_exclude = ('dvdrip', 'xvid', 'arrow')
        query = filename.lower().exclude_terms(terms_to_exclude)
        self.assertEqual(query, 'inception. . -')

    def test_remove_non_alphanumeric_chars(self):
        filename = ImdbQuery('Inception.2010.DVDRip.x264.dxva-TiMPE')
        query = filename.remove_non_alaphnumeric_chars()
        self.assertEqual(query, 'Inception 2010 DVDRip x264 dxva TiMPE')
    
    def test_add_parentheses_around_years(self):
        filename = ImdbQuery('Inception.2010.DVDRip.x264.dxva-TiMPE')
        query = filename.remove_non_alaphnumeric_chars().add_parentheses_around_years()
        self.assertEqual(query, 'Inception (2010) DVDRip x264 dxva TiMPE')
        
    def test_create_query_from_filename(self):
        from imdbquery_test_data import expected_query
        for filename in expected_query.keys():
            query = ImdbQuery.create_query_from_filename(filename)
            self.assertEqual(query, expected_query[filename])

if __name__ == "__main__":
    unittest.main()
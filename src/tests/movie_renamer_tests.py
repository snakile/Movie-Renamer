import unittest


class Test(unittest.TestCase):


    def test_rename(self):
        old_filename = 'Inception.DVDRiP.XviD-ARROW.avi'
        new_filename = 'Inception (2010).avi'
        self.assertEqual(rename(old_filename), new_filename)


if __name__ == "__main__":
    unittest.main()
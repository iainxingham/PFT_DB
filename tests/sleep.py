# Test sleep parsers

import unittest
from scripts.parsers.rad8 import Rad8Parse
from scripts.parsers.oldoxi import OldOxiParse
from scripts.parsers.newoxi import NewOxiParse


class TestSleep(unittest.TestCase):

    # Test Rad 8 parser
    def test_rad8(self):
        rad8 = Rad8Parse('./test_files/rad8test.pdf')
        self.assertTrue(rad8.is_ok())
        data = rad8.get_data()
        self.assertEqual(data['odi'], '14')
        self.assertEqual(data['hri'], '8.4')
        self.assertIn('dob', data)
        self.assertIn('date', data)

    # Test old oxi
    def test_oldoxi(self):
        oldoxi = OldOxiParse('./test_files/oxi_old.pdf')
        self.assertTrue(oldoxi.is_ok())
        data = oldoxi.get_data()
        self.assertEqual(data['odi'], '63.20')
        self.assertEqual(data['hri'], '66.75')
        self.assertTrue('dob' in data)
        self.assertTrue('date' in data)

    # Test new oxi
    def test_newoxi(self):
        newoxi = NewOxiParse('./test_files/oxi_new.pdf')
        self.assertTrue(newoxi.is_ok())
        data = newoxi.get_data()
        self.assertEqual(data['odi'], '2.06')
        self.assertEqual(data['hri'], '65.99')
        self.assertTrue('dob' in data)
        self.assertTrue('date' in data)


if __name__ == '__main__':
    unittest.main()
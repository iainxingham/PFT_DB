# Test PFT parser

import unittest
from scripts.parsers.pft import PFTParse

class TestPFT(unittest.TestCase):

    def test_rad8(self):
        pft = PFTParse('./test_files/pft1.pdf')
        self.assertTrue(pft.is_ok())
        data = pft.get_data()
        self.assertEqual(data['height'], '163.0')
        self.assertEqual(data['weight'], '83.6')
        
        self.assertIn('dob', data)
        self.assertIn('date', data)
        self.assertNotIn('odi', data)
        
        self.assertIn('FEV1', data)
        self.assertIn('FVC', data)
        self.assertIn('KCO', data)
        self.assertIn('VC', data)

        self.assertEqual(len(data['VAsb']), 3)
        self.assertEqual(len(data['TLco']), 4)

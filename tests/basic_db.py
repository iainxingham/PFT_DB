# Test of database

import unittest

from scripts.database.db import Patient, Record_sources
from scripts.config import PFT_configs

class TestDB(unittest.TestCase):
    def setUp(self):
        self.cfg = PFT_configs('./test_files/test.log', \
                               'sqlite:///.///test_files///test.db')
        self.cfg.set_up_logging()
        self.cfg.set_up_db()
        self.cfg.build_new_db()

    def testConfig(self):
        self.assertEqual(self.cfg.settings['logfile'], './test_files/test.log')

    def testAddSources(self):
        # Check added to db
        self.cfg.add_sources()
        self.assertIsNotNone(self.cfg.session.query(Record_sources).filter(Record_sources.\
            short == 'Old oxi').first())
        # Check only added once
        self.cfg.add_sources()
        self.assertIs(len(self.cfg.session.query(Record_sources).filter(Record_sources.\
            short == 'Rad-8').all()), 1)


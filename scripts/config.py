# Config routines

import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import scripts.database.db as db

class PFT_configs():
    def __init__(self, logfile: str='pft_db.log'):
        self.settings = {}
        self.settings['logfile'] = logfile

    def set_up_logging(self):
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO, \
                            filename=self.settings['logfile'])

    def set_up_db(self, dbfile: str='sqlite:///test.db'):
        self.engine = create_engine(dbfile)
        DBSession = sessionmaker(bind=self.engine)
        self.session = DBSession()

    def add_sources(self):
        SOURCES = {
            'Rad-8': 'Download from Rad-8 oximeter, processed in R',
            'Old oxi': 'Old style oximetry report, from \"PulseOx\" software',
            'New oxi': 'New style oximetry report, from \"Visidownload\" software',
            'Full pft': 'Spirometry +/- gas transfer from PFT machine pdf'
        }

        for s, l in SOURCES.items():
            if self.session.query(db.Record_sources).filter(db.Record_sources.short == s).first() is None:
                    rec = db.Record_sources(short = s, description = l)
                    self.session.add(rec)
            
        self.session.commit()

    def build_new_db(self):
        # OK for tests - should Alembic do this for main code?
        # Seems safe even if db already exists
        from scripts.database.db import Base

        Base.metadata.create_all(self.engine)



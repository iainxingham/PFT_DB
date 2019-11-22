# Config routines

import logging

def set_up_logging():
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO, \
                        filename='pft_db.log')

# Pulmonary function database

import argparse
import logging
import os
import sys

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

from config import PFT_configs
import database.db as db

cli_parse = argparse.ArgumentParser(description='Gather lung function results into a database')
cli_parse.add_argument('-b', '--build', help='Build database from scratch', action='store_true')
cli_parse.add_argument('-u', '--update', help='Search for new reports', action='store_true')
cli_parse.add_argument('-v', '--version', action='version', version='%(prog)s 0.1a')
cli_parse.add_argument('-a', '--addpath', nargs=2, help='Add new folder to search\n'\
                       '-a [PATH] [PARSER]')
cli_parse.add_argument('-l', '--listpaths', help='List folders to search', action='store_true')
cli_parse.add_argument('-s', '--showparsers', help='Show available parsers', action='store_true')


def main():
    cfg = PFT_configs()
    cfg.set_up_logging()
    cfg.set_up_db()

    args = cli_parse.parse_args()

    if args.showparsers:
        print('List of available parsers: \n')
        for p in cfg.session.query(db.Record_sources).all():
            if len(p.short) < 8:
                print('Parser: {0}\t\t{1}'.format(p.short, p.description))
            else:
                print('Parser: {0}\t{1}'.format(p.short, p.description))
    print('\n')

    if args.listpaths:
        for p in cfg.session.query(db.Folders).all():
                print('Path: {0}, parser: {1}'.format(p.folder, p.parser_rel))

    if args.build:
        print('Building database from scratch\n')
        
        if os.path.exists(cfg.settings['dbfile']):

            # Replace with simply dropping tables to keep paths?
            # ?? Doesn't work?
            print('Warning - database already exists\n')
            print('This will be saved as {0}.old'.format(cfg.settings['dbfile']))
            os.rename(cfg.settings['dbfile'], '{0}.old'.format(cfg.settings['dbfile']))
            logging.info('Old database saved as {0}.old'.format(cfg.settings['dbfile']))
            os.remove(cfg.settings['dbfile'])

        cfg.build_new_db()
        cfg.add_sources()

        # Read files into database

        logging.info('New database completed')
        print('New database completed')

    elif args.update:

        # Read time of last update from db
        # Search for lung function since
        # Add to database
        pass

    elif args.addpath:
        # Want this before build
        pass


if __name__ == '__main__':
    main()
import argparse
from . import __version__
import sys
from marksman.app import crud_handler, email_handler, visualization_handler
import logging

def main():
    ''' Command line entry point
    '''

    parser = argparse.ArgumentParser()

    parser.add_argument('func',
                        help='what do you want to do',
                        choices=['crud', 'email', 'visualize'])

    parser.add_argument('-v', '--verbose',
                        help='increase output verbosity',
                        action='store_true')

    if len(sys.argv) == 1:
        print(f'marksman {__version__}')
        print('Created by Aahnik Daw.\n\n')
        parser.print_help(sys.stderr)
        sys.exit(0)

    args = parser.parse_args()

    if args.verbose:
        print('Verbosity turned on')
        logging.basicConfig(level=logging.INFO)

    if args.func == 'crud':
        crud_handler()
    elif args.func == 'email':
        email_handler()
    elif args.func == 'visualize':
        visualization_handler()

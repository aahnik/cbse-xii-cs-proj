import argparse
from argparse import RawTextHelpFormatter
from marksman.settings import DB_PATH
from marksman import __version__
import sys
from marksman.app import crud_handler, email_handler, visualization_handler
import logging
import sqlite3


def main():
    ''' Command line entry point
    '''

    main_parser = argparse.ArgumentParser(
        description='CLI Tool to manage marks of students',
        epilog='''To learn how to use an action (crud|email|visualize) use \n\tmarksman <action> -h
        \n\nFor tutorials and documentation visit https://git.io/JL1iI ''', formatter_class=RawTextHelpFormatter)

    main_parser.add_argument('-l', '--loud',
                             help='increase output verbosity',
                             action='store_true')
    main_parser.add_argument(
        '-v', '--version', action='version', version=__version__)

    subparsers = main_parser.add_subparsers(
        title='actions', help='actions you can take')

    crud_parser = subparsers.add_parser('crud',
                                        help='Do crud operations', )

    email_parser = subparsers.add_parser('email',
                                         help='Email results to students',)

    vis_parser = subparsers.add_parser('visualize',
                                       help='Visualize the results',)

    crud_parser.add_argument('what',
                             help='Choose what data you want to crud',
                             choices=['students', 'exams', 'marks'])
    crud_parser.set_defaults(func=crud_handler, which='crud_parser')

    email_parser.add_argument('exam',
                              help='exam id',
                              type=int)
    email_parser.set_defaults(func=email_handler, which='email_parser')

    vis_parser.add_argument('exam',
                            help='exam id',
                            type=int)

    vis_parser.add_argument('student',
                            help='roll number of student',
                            type=int,
                            default=0)

    vis_parser.set_defaults(func=visualization_handler, which='vis_parser')

    if len(sys.argv) == 1:
        print(f'marksman {__version__}')
        print('Created by Aahnik Daw.\n')
        main_parser.print_help(sys.stderr)
        sys.exit(0)

    args = main_parser.parse_args()

    if args.loud:
        logging.basicConfig(level=logging.INFO)
        logging.info('Verbosity turned on')

    if hasattr(args, 'func'):
        my_conn = sqlite3.connect(DB_PATH)
        cursor = my_conn.cursor()
        args.func(args, cursor)
        my_conn.commit()
        my_conn.close()

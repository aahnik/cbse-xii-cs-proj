import argparse
from argparse import RawTextHelpFormatter
from marksman.db import create_tables
from marksman.utils import ensure_parent
from marksman.settings import DB_PATH, LOUD, SHOW_PATH, SENDER_EMAIL, SENDER_AUTH
from marksman import __version__
import sys
from marksman.app import crud_handler, email_handler, visualization_handler
import logging
import sqlite3
from rich.logging import RichHandler
import os
logger = logging.getLogger(__name__)


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

    if args.loud or LOUD:
        level = logging.INFO
    else:
        level = logging.WARNING

    logging.basicConfig(level=level,
                        format='[dim]%(name)s[/dim]\t%(message)s', handlers=[RichHandler(markup=True, show_path=SHOW_PATH,)])

    logger.info('Verbosity turned on')

    if hasattr(args, 'func'):

        logger.info('Starting database connection')
        ensure_parent(DB_PATH)

        pre_exists = os.path.isfile(DB_PATH)

        my_conn = sqlite3.connect(DB_PATH)
        cursor = my_conn.cursor()

        if not pre_exists:
            create_tables(cursor)
        try:
            args.func(args, cursor)
        except Exception as err:
            logger.exception(err)
        my_conn.commit()
        my_conn.close()
        logger.info('Closed database connection')

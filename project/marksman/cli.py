import argparse
from argparse import RawTextHelpFormatter
from marksman.db import create_tables, foreign_key_constraint
from marksman.utils import ensure_parent
from marksman.settings import DB_PATH, LOUD, SHOW_PATH, SENDER_EMAIL, SENDER_AUTH
from marksman import __version__
import sys
from marksman.app import crud_handler, email_handler, visualization_handler, utils_handler
import logging
import sqlite3
from rich.logging import RichHandler
import os
logger = logging.getLogger(__name__)


def parse_commands():

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

    utils_parser = subparsers.add_parser(
        'utils', help='Additional utility tools for marksman')

    crud_parser.add_argument('what',
                             help='Choose what data you want to crud',
                             choices=['students', 'exams', 'marks'])
    crud_parser.set_defaults(func=crud_handler)

    email_parser.add_argument('exam',
                              help='exam uid',
                              type=int)
    email_parser.set_defaults(func=email_handler, which='email_parser')

    vis_parser.add_argument('exam',
                            help='exam uid',
                            type=int)

    vis_parser.add_argument('--r',
                            metavar='ROLL',
                            help='roll number of student (default=0 for all)',
                            type=int,
                            default=0)

    vis_parser.set_defaults(func=visualization_handler, which='vis_parser')

    utils_parser.add_argument('task', help='Choose the task you want to perform', choices=[
                              'dummy', 'import', 'export'])

    utils_parser.set_defaults(func=utils_handler)

    if len(sys.argv) == 1:
        print(f'marksman {__version__}')
        print('Created by Aahnik Daw.\n')
        main_parser.print_help(sys.stderr)
        sys.exit(0)

    return main_parser.parse_args()


def call_func(args):
    if hasattr(args, 'func'):

        logger.info('Starting database connection')
        ensure_parent(DB_PATH)

        pre_exists = os.path.isfile(DB_PATH)

        my_conn = sqlite3.connect(DB_PATH)
        cursor = my_conn.cursor()

        foreign_key_constraint(cursor)

        if not pre_exists:
            create_tables(cursor)
        try:
            args.func(args, cursor)
        except Exception as err:
            logger.exception(err)
        my_conn.commit()
        my_conn.close()
        logger.info('Closed database connection')


def main():
    ''' Command line entry point
    '''

    args = parse_commands()

    if args.loud or LOUD:
        level = logging.INFO
    else:
        level = logging.WARNING

    logging.basicConfig(level=level,
                        format='[dim]%(name)s[/dim]\t%(message)s', handlers=[RichHandler(markup=True, show_path=SHOW_PATH,)])

    logger.info('Verbosity turned on')

    call_func(args)

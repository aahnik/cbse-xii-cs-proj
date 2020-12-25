import logging
from sqlite3 import Cursor


def crud_handler(args, cursor: Cursor):
    logging.info(f'called crud handler with {args.what}')


def email_handler(args, cursor: Cursor):
    logging.info(f'called email handler with {args.exam}')


def visualization_handler(args, cursor: Cursor):
    logging.info(f'called vis handler with {args.exam} and {args.student}')

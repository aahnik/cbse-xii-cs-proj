import logging
import re
logger = logging.getLogger(__name__)


def get_pos_int(msg: str) -> int:
    ''' takes input and returns after assuring that it is a positive integer

    Returns:
        int: the correct integer
    '''
    while True:
        try:
            integer = int(input(msg))
            assert integer > 0
        except ValueError:
            logger.warn('The value you entered is not an integer')
        except AssertionError:
            logger.warn('You must enter an integer greater than zero')
        else:
            return integer


def get_str(msg='Enter name: ', default: str = '') -> str:
    max_len = 64
    while True:
        try:
            string = input(msg)
            assert len(string) <= max_len
        except AssertionError:
            logger.warn(
                f'The string must not be longer than {max_len} characters')
        else:
            if string:
                return string

            if default:
                return default

            logger.warn('You cant keep this empty')


def get_email(default: str = '') -> str:
    while True:
        try:
            email = get_str('Enter email: ', default=default)
            if email == default:
                logger.info('Email unchanged, not checking')
                return email
            logging.info('Checking email for validity')
            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
            assert re.search(regex, email)
        except AssertionError:
            logger.warn('The email you enterd is invalid')
        else:
            return email

from rich import print
import logging
import re
logger = logging.getLogger(__name__)


def get_pos_int(msg: str = 'Enter marks: ') -> int:
    ''' takes input and returns after assuring that it is a positive integer

    Returns:
        int: the correct integer
    '''
    while True:
        try:
            print(f'\n{msg}')
            integer = int(input())
            assert integer > 0
        except ValueError:
            logger.warn('The value you entered is not an integer')
        except AssertionError:
            logger.warn('You must enter an integer greater than zero')
        else:
            return integer


def get_str(msg='Enter [bold]name[/bold]: ') -> str:
    max_len = 64
    while True:
        try:
            print(f'\n{msg}')
            string = input()
            assert len(string) <= max_len
        except AssertionError:
            logger.warn(
                f'The string must not be longer than {max_len} characters')
        else:
            return string


def get_email(msg='Enter [bold]email[/bold]: ') -> str:
    while True:
        try:
            email = get_str(msg)
            if email:
                logging.info('Checking email for validity')
                regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
                assert re.search(regex, email)
        except AssertionError:
            logger.warn('The email you enterd is invalid')
        else:
            return email


def roll():
    return get_pos_int('Enter [bold]roll number[/bold] of student:')


def uid():
    return get_pos_int('Enter the [bold]unique id[/bold] of exam:')

''' This Module has functions validate various user inputs
'''

import sys
import logging
import re

from rich.console import Console

logger = logging.getLogger(__name__)

console = Console()


def get_pos_int(msg: str = 'Enter marks: ') -> int or None:
    ''' Takes input and returns after assuring that it is a positive integer.
        Allows empty input.

    Returns:
        int: the correct integer
    '''
    console.print(f'\n{msg}')
    inp = input()
    if inp:
        try:
            integer = int(inp)
            assert integer > 0
        except ValueError:
            logger.warning('The value you entered is not an integer')
        except AssertionError:
            logger.warning('You must enter an integer greater than zero')
        else:
            return integer
        sys.exit(1)


def get_str(msg: str = 'Enter [bold]name[/bold]: ') -> str or None:
    ''' Takes a string input and assures that it is valid.
        Allows empty input.

    Args:
        msg (str, optional): [description]. Defaults to 'Enter [bold]name[/bold]: '.

    Returns:
        str or None: User input
    '''
    max_len = 64
    while True:
        try:
            console.print(f'\n{msg}')
            string = input()
            assert len(string) <= max_len
        except AssertionError:
            logger.warning(
                f'The string must not be longer than {max_len} characters')
        else:
            return string


def get_email(msg: str = 'Enter [bold]email[/bold]: ') -> str or None:
    ''' Takes a string from user and assures that it matches the regex of email.
        Allows empty input.

    Args:
        msg (str, optional): [description]. Defaults to 'Enter [bold]email[/bold]: '.

    Returns:
        str or None: User input
    '''
    while True:
        try:
            email = get_str(msg)
            if email:
                logging.info('Checking email for validity')
                regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
                assert re.search(regex, email)
        except AssertionError:
            logger.warning('The email you enterd is invalid')
        else:
            return email


def roll() -> int or None:
    ''' Asks the user to enter roll number of student
        .. Note:: This wrapper is essential for certain internal implementation reasons.
    Returns:
        int or None: User input
    '''
    return get_pos_int('Enter [bold]roll number[/bold] of student:')


def uid() -> int or None:
    ''' Asks the user the uid of exam
        .. Note:: This wrapper is essential for certain internal implementation reasons.

    Returns:
        int or None: User input
    '''
    return get_pos_int('Enter the [bold]unique id[/bold] of exam:')

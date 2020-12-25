import re


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
            print('The value you entered is not an integer')
        except AssertionError:
            print('You must enter an integer greater than zero')
        else:
            return integer


def get_str(msg: str, max_len: int = 64) -> str:
    while True:
        try:
            string = input(msg)
            assert len(string) <= max_len
        except AssertionError:
            print(f'The string must not be longer than {max_len} characters')
        else:
            return string


def get_email(msg: str) -> str:
    while True:
        try:
            email = get_str(msg)
            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
            assert re.search(regex, email)
        except AssertionError:
            print('The email you enterd is invalid')
        else:
            return email

''' A module that defines various helper functions to avoid repeatition of code
'''

import os
import logging
import sys
from typing import Iterable

from rich.console import Console
from rich.table import Table

from marksman.settings import (DB_PATH, GLOBAL_CONFIG_PATH,
                               SENDER_EMAIL, SENDER_AUTH, SMTP_HOST, SMTP_PORT, INST_NAME)
from marksman.validators import get_email, get_str


logger = logging.getLogger(__name__)

console = Console()


def ___(text: str) -> str:
    ''' Logs a SQL query and returns the query
    To be wrapped around a query string before executing it.

    Args:
        text (str): query string

    Returns:
        str: query string
    '''
    sql_query_logger = logging.getLogger('SQL Executor')
    sql_query_logger.info(f'{text}')
    return text


def not_empty(inp: str) -> str:
    ''' Disallows empty inputs

    Args:
        inp (str): input string

    Returns:
        str: the same input string is returned. If input string is empty, quits the program.
    '''
    if not inp:
        logger.warning('Empty value not allowed. > Quitting ...')
        sys.exit(1)
    return inp


def handle_choice(choices: dict) -> None:
    ''' Provides the user with a menu and executes apt function based on user choice

    Args:
        choices (dict): Dictionary containing the option strings as keys
        and the functions to execute when that option is selected as values.

    - this function is specific to my use case and not generic
    - the number of choices in the dict is expected to be one or two and not large
    - all choice str are meant to have unique prefix chars
    - this handler does not resolve prefix collisions, the first come first server
    '''

    ch_list = []
    prefix = '[dim]Choose your action[/dim] '
    msg = prefix
    for char in choices.keys():
        ch_list.append(char[0])
        msg += f'[reverse]{char[0]}[/reverse]{char[1:]} '
    console.print('\n'+msg)
    user_choice = input().lower().strip()
    if not user_choice:
        logger.warning('You did not choose anything')
        return
    for char in choices.keys():
        if char.startswith(user_choice):
            func = choices.get(char)
            func()
            return
    logger.warning('Invalid Choice ...quitting')
    sys.exit(1)


def display_table(title: str, headers: Iterable, table_list: Iterable) -> None:
    ''' Display data in tabular format

    Args:
        title (str): the title of the data
        headers (Iterable): headings or the first row
        table_list (Iterable): the 2D Matrix or list of rows
    '''

    table = Table(title=title, show_lines=True)

    for heading in headers:
        table.add_column(heading, justify='center')

    for row in table_list:
        renderable = [str(c) for c in row]
        table.add_row(*renderable)

    console.print(table)


def ensure_parent(filename: str) -> None:
    ''' Ensures that the parent folder of a file exists

    Args:
        filename (str): the file name
    '''
    parent_folder = os.path.split(filename)[0]
    os.makedirs(parent_folder, exist_ok=True)
    logger.info(f'Ensured that parent folder of {DB_PATH} exists')


def save_email_config(thing: str, env_var: str, value: str) -> None:
    ''' Prompts the use to save a particular configuration related to email

    Args:
        thing (str): the thing concerned
        env_var (str): the name of the environment variable dedicated for that thing
        value (str): the value of the thing
    '''

    text = f'''[red]If you do not want to enter [bold]{thing}[/bold] every time,
    then save it in [blue]{env_var}[/blue] environment variable.[/red]
        \nYou can write the following line in your {GLOBAL_CONFIG_PATH} file:\n
        [center][dim]{env_var}={value}[/dim][/center]
        \nRead more about configuring your marksman environment http://bit.ly/configure-marksman \n'''
    logger.warning(text)
    console.print(
        f'''Do you want [bold]marksman[/bold] to save your [blue]{thing}[/blue] ?
        [reverse]Y[/reverse]es or [reverse]n[/reverse]o''')
    choice = input().lower()
    if choice in 'yes':
        with open(GLOBAL_CONFIG_PATH, 'a') as _file:
            _file.write(f'{env_var}={value}\n')
        console.print(f'Saved [bold]{thing}[/bold] to {GLOBAL_CONFIG_PATH}')
    elif choice in 'no':
        console.print('Ok. Not saving')
    else:
        console.print('Invalid Choice ...not saving')


def configure_email() -> tuple:
    ''' Help the use configure the settings for emailing

    Returns:
        tuple: (SENDER_EMAIL, SENDER_AUTH, SMTP_HOST, SMTP_PORT, INST_NAME)
    '''

    (sender_email, sender_auth,
     smtp_host, smtp_port,
     inst_name) = (SENDER_EMAIL, SENDER_AUTH,
                   SMTP_HOST, intify(SMTP_PORT),
                   INST_NAME)

    if not sender_email:
        sender_email = not_empty(
            get_email('Enter [bold]sender email[/bold] address: '))
        save_email_config('email', 'marksman_sender', sender_email)
    if not sender_auth:
        sender_auth = not_empty(get_str(
            f'Enter password or auth-code to login into email account {sender_email}'))
        save_email_config('auth-code', 'marksman_auth', sender_auth)

    if not sender_email.endswith('@gmail.com'):
        if not smtp_host:
            logger.warning(
                '''SMTP sever url could not be derrived from email address.
                Learn more https://git.io/JLMFl ''')
            smtp_host = not_empty(get_str(
                '''Enter address of your email provider\'s SMTP host server
                (keep empty to continue with smtp.gmail.com) : '''))
            save_email_config('smtp host address',
                              'marksman_smptp_host', smtp_host)
        else:
            logger.info(
                f'Sender Email does not end with gmail.com > SMTP_HOST is {SMTP_HOST}')
    else:
        smtp_host = 'smtp.gmail.com'
        logger.info(f'SMTP_HOST is set to {smtp_host}')

    if not isinstance(smtp_port, int):
        logger.warning(
            'The SMTP Port you have set is not an integer > using default 587')
        smtp_port = 587
    if not smtp_port in (587, 2525):
        logger.warning(
            'The SMTP Port you have set is probably incorrect or insecure')

    return sender_email, sender_auth, smtp_host, smtp_port, inst_name


def intify(string: str) -> int or str:
    ''' Converts a string to int if possible

    Args:
        string (str): input string

    Returns:
        int or str: output int or string
    '''
    try:
        return int(string)
    except ValueError:
        return string


def load_template() -> str:
    ''' Loads the template file, or provides the default template

    Returns:
        str: the template string
    '''

    templ_file = 'marksman_email_template.md'
    if os.path.isfile(templ_file):
        with open(templ_file, 'r') as file:
            template = file.read()
    else:
        logger.warning(
            'Template file not found. Proceeding with default template')
        template = '''Result and Performance Analysis of ::exam::
        \n### Hi ::name:: you have scored ::marks:: and your rank is ::rank:: in ::exam::.
        \nFind the performance report attached.
        Best regards,
        ::inst::

        _Sent via marksman.mailer_'''
    return template

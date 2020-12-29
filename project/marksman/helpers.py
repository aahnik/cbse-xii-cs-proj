
from typing import Iterable
from rich import print
from rich.console import Console
from marksman.settings import DB_PATH
import os
import logging
from rich.table import Table
import sys
logger = logging.getLogger(__name__)


def ___(text):
    logger = logging.getLogger('SQL Executor')
    logger.info(f'{text}')
    return text


def not_empty(inp):
    if not inp:
        logger.warn('Empty value not allowed. > Quitting ...')
        sys.exit(1)
    return inp


def handle_choice(choices: dict) -> None:

    # this function is specific to my use case and not generic
    # the number of choices in the dict is expected to be one or two and not large
    # the choices dict should be like this -> key : choice str, value : choice func
    # all choice str are meant to have unique prefix chars
    # this handler does not resolve prefix collisions, the first come first server

    ch_list = []
    prefix = '[dim]Choose your action[/dim] '
    msg = prefix
    for ch in choices.keys():
        ch_list.append(ch[0])
        msg += f'[reverse]{ch[0]}[/reverse]{ch[1:]} '
    print('\n'+msg)
    user_choice = input().lower().strip()
    if not user_choice:
        logger.warn('You did not choose anything')
        return
    for ch in choices.keys():
        if ch.startswith(user_choice):
            func = choices.get(ch)
            return func()
    logger.warn('Invalid Choice ...quitting')


def display_table(title: str, headers: Iterable, table_list: Iterable):

    table = Table(title=title, show_lines=True)

    for heading in headers:
        table.add_column(heading, justify='center')

    for row in table_list:
        renderable = [str(c) for c in row]
        table.add_row(*renderable)

    console = Console()
    console.print(table)





def ensure_parent(filename: str) -> None:
    parent_folder = os.path.split(filename)[0]
    os.makedirs(parent_folder, exist_ok=True)
    logger.info(f'Ensured that parent folder of {DB_PATH} exists')


def save_email_config(thing, env_var, value):
    from marksman.settings import GLOBAL_CONFIG_PATH

    text = f'''[red]If you do not want to enter [bold]{thing}[/bold] every time, then save it in [blue]{env_var}[/blue] environment variable.[/red]
        \nYou can write the following line in your {GLOBAL_CONFIG_PATH} file:\n
        [center][dim]{env_var}={value}[/dim][/center]
        \nRead more about configuring your marksman environment https://git.io/JLMFl\n'''
    logger.warn(text)
    print(
        f'Do you want [bold]marksman[/bold] to save your [blue]{thing}[/blue] ? [reverse]Y[/reverse]es or [reverse]n[/reverse]o')
    choice = input().lower()
    if choice in 'yes':
        with open(GLOBAL_CONFIG_PATH, 'a') as f:
            f.write(f'{env_var}={value}\n')
        print(f'Saved [bold]{thing}[/bold] to {GLOBAL_CONFIG_PATH}')
    elif choice in 'no':
        print('Ok. Not saving')
    else:
        print('Invalid Choice ...not saving')


def configure_email():
    from marksman.settings import SENDER_EMAIL, SENDER_AUTH, SMTP_HOST, SMTP_PORT, INST_NAME
    from marksman.validators import get_email, get_str

    if not SENDER_EMAIL:
        SENDER_EMAIL = not_empty(
            get_email('Enter [bold]sender email[/bold] address: '))
        save_email_config('email', 'marksman_sender', SENDER_EMAIL)
    if not SENDER_AUTH:
        SENDER_AUTH = not_empty(get_str(
            f'Enter password or auth-code to login into email account {SENDER_EMAIL}'))
        save_email_config('auth-code', 'marksman_auth', SENDER_AUTH)

    if not SENDER_EMAIL.endswith('@gmail.com'):
        if not SMTP_HOST:
            logger.warn(
                'SMTP sever url could not be derrived from email address. Continuing with default. \n Learn more https://git.io/JLMFl ')
            SMTP_HOST = not_empty(get_str(
                'Enter address of your email provider\'s SMTP host server : '))
            save_email_config('smtp host address',
                              'marksman_smptp_host', SMTP_HOST)
        else:
            logger.info(
                f'Sender Email does not end with gmail.com > SMTP_HOST is {SMTP_HOST}')
    else:
        SMTP_HOST = 'smtp.gmail.com'
        logger.info(f'SMTP_HOST is set to {SMTP_HOST}')

    if not isinstance(SMTP_PORT, int):
        logger.warning(
            'The SMTP Port you have set is not an integer > using default 587')
        SMTP_PORT = 587
    if not SMTP_PORT in (587, 2525):
        logger.warning(
            'The SMTP Port you have set is probably incorrect or insecure')
    if not INST_NAME:
        logger.warn(
            'Institute Name not set thus your email will be visible on top, Learn More https://git.io/JLMFl')

    return SENDER_EMAIL, SENDER_AUTH, SMTP_HOST, SMTP_PORT, INST_NAME


def intify(string: str):
    try:
        return int(string)
    except ValueError:
        return string

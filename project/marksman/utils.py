
from rich import print
from marksman.settings import DB_PATH
import os
import logging


logger = logging.getLogger(__name__)


def ___(text):
    logger = logging.getLogger('SQL Executor')
    logger.info(f'{text}')
    return text


def handle_choice(choices: dict) -> None:

    # this function is specific to my use case and not generic
    # the number of choices in the dict is expected to be one or two and not large
    # the choices dict should be like this -> key : choice str, value : choice func
    # all choice str are meant to have unique prefix chars
    # this handler does not resolve prefix collisions, the first come first server

    ch_list = []
    msg = 'Choose your action  '
    for ch in choices.keys():
        ch_list.append(ch[0])
        msg += f'[red]{ch[0]}[/red]{ch[1:]} '
    print('\n'+msg)
    user_choice = input('>>> ').lower().strip()
    if not user_choice:
        logger.warn('You did not choose anything.')
        return
    for ch in choices.keys():
        if ch.startswith(user_choice):
            func = choices.get(ch)
            return func()
    logger.warn('Invalid Choice')


def clear_screen():
    pass


def display_table():
    pass


def ensure_parent(filename: str) -> None:
    parent_folder = os.path.split(filename)[0]
    os.makedirs(parent_folder, exist_ok=True)
    logger.info(f'Ensured that parent folder of {DB_PATH} exists')


def fill_dummy(students, exams, marks):
    import random

    for i in range(1, 50):
        students.insert((i, f'stud_{i}', f'{i}@email.com'))
    logger.info('Created 50 dummy students')

    for j in range(1, 10):
        exams.insert((j, f'exam_{j}'))
    logger.info('Created 10 dummy exams')

    for j in range(1, 10):
        for i in range(1, 50):
            m = random.randint(1, 100)
            marks.insert((i, j, m))
    logger.info('Filled with random dummy marks entries')

def load_csv(students,exams,marks):
    pass


def export_csv(students,exams,marks):
    pass


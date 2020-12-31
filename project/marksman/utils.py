''' This module implements various extra utilities for marksman.
Such as filling database with dummy data, or importing or exporting CSV.
'''

import os
import logging
import random
import csv
from datetime import datetime

from rich import console
from rich.progress import track
from rich.console import Console

from marksman.validators import get_str
from marksman.db import DbModelz
from marksman.helpers import intify

console = Console()

logger = logging.getLogger(__name__)


def fill_dummy(students: DbModelz, exams: DbModelz, marks: DbModelz) -> None:
    ''' Fill the database with dummy data

    Args:
        students (DbModelz): DbModelz object with table as students
        exams (DbModelz): DbModelz object with table as exams
        marks (DbModelz): DbModelz object with table as marks
    '''

    for i in track(range(1, 51), description='Creating dummy students'):
        students.insert((i, f'stud_{i}', f'{i}dontsend@example.com'))
    logger.info('Created 50 dummy students')

    for j in track(range(1, 11), description='Creating dummy exams'):
        exams.insert((j, f'exam_{j}'))
    logger.info('Created 10 dummy exams')

    for j in track(range(1, 11), description='Creating dummy marks entries'):
        for i in range(1, 51):
            _marks = random.randint(1, 100)
            marks.insert((i, j, _marks))
    logger.info('Filled with random dummy marks entries')

    console.print('Filling dummy data complete!')


class ImportExport:
    ''' A class that implements methods related to import and export of data for marksman.
    '''

    def __init__(self, students: DbModelz, exams: DbModelz, marks: DbModelz) -> None:
        ''' Constructor to initialize ImportExport object

        Args:
            students (DbModelz): DbModelz object with table as students
            exams (DbModelz): DbModelz object with table as exams
            marks (DbModelz): DbModelz object with table as marks
        '''
        self.structure = [('students', ('roll', 'name', 'email'), students),
                          ('exams', ('uid', 'name'), exams),
                          ('marks', ('student', 'exam', 'marks'), marks)]

    def load_csv(self) -> None:
        ''' Read CSV files and insert data into database
        '''
        import_dir = get_str(
            '''Enter the path of the directory which has the csv files:
            ( leave empty if files in current directory )''')
        if not import_dir:
            import_dir = os.getcwd()
        if not os.path.isdir(import_dir):
            logger.warning('Given path is not a directory... quitting')
            return

        for item in self.structure:
            path = f'{import_dir}/{item[0]}.csv'
            try:
                with open(path) as _file:
                    reader = csv.DictReader(_file)
                    for row in reader:
                        values = []
                        for _, value in row.items():
                            values.append(intify(value))
                        item[2].insert(tuple(values))
            except FileNotFoundError:
                logger.warning(
                    f'Could not find {path} > Skipped importing {item[0]}')
            except Exception as err:
                logger.warning(
                    f'''Problem occured while trying to import data from {path}
                    \nPlease follow specified format.  Read more http://bit.ly/marksman-utils''')
                logger.exception(err)
            else:
                console.print(f'Finished loading {item[0]} from CSV.')

    def export_csv(self) -> None:
        ''' Read data from database and write them onto CSV files
        '''

        timestamp = str(datetime.now().strftime("%d %b %I:%M %p"))

        export_dir = f'Marksman Export {timestamp}'  # export directory
        os.makedirs(export_dir, exist_ok=True)

        for item in self.structure:
            with open(f'{export_dir}/{item[0]}.csv', 'w') as _file:
                writer = csv.writer(_file)
                writer.writerow(item[1])
                writer.writerows(item[2].fetch())

        console.print(
            f'Finished exporting to CSV. See the {export_dir} folder.')

    def do_apt(self, task: str) -> None:
        ''' Call the apt method based on provided task argument

        Args:
            task (str): the task
        '''
        if task == 'import':
            self.load_csv()
        else:
            self.export_csv()

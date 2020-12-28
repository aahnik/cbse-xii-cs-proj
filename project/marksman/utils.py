
import csv
from marksman.validators import get_str
from marksman.settings import DB_PATH
import os
import logging
from datetime import datetime
from marksman.db import Modelz
from marksman.helpers import intify
logger = logging.getLogger(__name__)


def fill_dummy(students, exams, marks):
    import random

    for i in range(1, 51):
        students.insert((i, f'stud_{i}', f'{i}@email.com'))
    logger.info('Created 50 dummy students')

    for j in range(1, 11):
        exams.insert((j, f'exam_{j}'))
    logger.info('Created 10 dummy exams')

    for j in range(1, 11):
        for i in range(1, 51):
            m = random.randint(1, 100)
            marks.insert((i, j, m))
    logger.info('Filled with random dummy marks entries')


class ImportExport:
    def __init__(self, students, exams, marks):
        self.structure = [('students', ('roll', 'name', 'email'), students),
                          ('exams', ('uid', 'name'), exams),
                          ('marks', ('student', 'exam', 'marks'), marks)]

    def load_csv(self):
        import_dir = get_str(
            'Enter the path of the directory which has the csv files: ( leave empty if files in current directory )', default=os.getcwd())
        if not os.path.isdir(import_dir):
            logger.warn('Given path is not a directory... quitting')
            return

        for item in self.structure:
            path = f'{import_dir}/{item[0]}.csv'
            try:
                with open(path) as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        values = []
                        for _, value in row.items():
                            values.append(intify(value))
                        item[2].insert(tuple(values))
            except FileNotFoundError:
                logger.warn(
                    f'Could not find {path} > Skipped importing {item[0]}')
            except Exception as err:
                logger.warn(
                    f'''Problem occured while trying to import data from {path}
                    \nPlease follow specified format.  Read more''')  # TODO
                logger.exception(err)
            else:
                logger.info(f'Finished loading {item[0]}')

    def export_csv(self):

        timestamp = str(datetime.now().strftime("%d %b %I:%M %p"))

        export_dir = f'Marksman Export {timestamp}'  # export directory
        os.makedirs(export_dir, exist_ok=True)

        for item in self.structure:
            with open(f'{export_dir}/{item[0]}.csv', 'w') as f:
                writer = csv.writer(f)
                writer.writerow(item[1])
                writer.writerows(item[2].fetch())

    def do(self, task):
        return self.load_csv() if task == 'import' else self.export_csv()

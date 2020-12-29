import logging
from typing import Iterable
from marksman.db import DbModelz
from sqlite3 import Cursor
from marksman.helpers import display_table, not_empty
import sys
logger = logging.getLogger(__name__)


class Models:

    def __init__(self, db_modelz: DbModelz, pks_fn: dict, values_fn: dict):
        self.db_modelz = db_modelz
        pks = {}
        for k, v in pks_fn.items():
            pks[k] = v()
        self.pks = pks  # dict of pk and value

        if not all(self.pks.values()):
            matches = self.db_modelz.fetch(**self.pks)
            self.display(data=matches)
            sys.exit(0)

        self.values_fn = values_fn  # dict of value_field_name : func
        self.object = self.read()

    def read(self):
        return self.db_modelz.exists(**self.pks)

    def display(self, data=None):
        what = self.db_modelz.table
        if not data:
            data = [self.object]
        if what == 'students':
            display_table('Student Data', ['Roll', 'Name', 'Email'], data)
        elif what == 'exams':
            display_table('Exam Data', ['Uid', 'Name'], data)
        else:  # marks
            display_table('Marks Data', ['Student', 'Uid', 'Marks'], data)

    def create(self):
        calculated = []
        for _, v in self.pks.items():
            calculated.append(v)
        for _, fn in self.values_fn.items():
            val = not_empty(fn())
            calculated.append(val)
        self.db_modelz.insert(tuple(calculated))

    def show_related(self):
        what = self.db_modelz.table
        obj = self.object
        if what == 'exams':
            related = self.db_modelz.query(
                f'''SELECT students.roll,students.name,marks.marks
            FROM students
            INNER JOIN marks
            ON students.roll=marks.student
            WHERE marks.exam={obj[0]}
            ORDER BY marks.marks DESC''')
            display_table(f'Students who appeared in {obj[1]}', [
                          'Roll', 'Name', 'Marks'], related)
        elif what == 'students':
            related = self.db_modelz.query(
                f'''SELECT exams.uid,exams.name,marks.marks 
                FROM exams 
                INNER JOIN marks
                ON exams.uid=marks.exam
                WHERE marks.student={obj[0]}
                ORDER BY exams.uid''')
            display_table(f'Exams given by {obj[1]}', [
                          'Uid', 'Exam Name', 'Marks'], related)
        else:  # marks
            student = self.db_modelz.query(
                f'SELECT name FROM students WHERE roll={obj[0]}')[0]
            exam = self.db_modelz.query(
                f'SELECT name FROM exams WHERE uid={obj[1]} ')[0]
            display_table('Marks Entry', ['Student', 'Exam', 'Marks'], [
                          (student, exam, obj[2])])

    def update(self):
        calculated = {}
        for k, v in self.values_fn.items():
            calculated[k] = v()
        if any(calculated.values()):
            self.db_modelz.update(calculated, **self.pks)
        else:
            logger.warning('You left all values empty > Not updating anything')

    def delete(self):
        self.db_modelz.delete(**self.pks)

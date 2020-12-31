''' This module implements a generic class to handle the CRUD operations
for 3 different type of data: Students/Exams/Marks
'''

import sys
import logging
from marksman.db import DbModelz
from marksman.helpers import display_table, not_empty

logger = logging.getLogger(__name__)


class Models:
    ''' Generic class for the three types Student or Exam or MarksEntry '''

    def __init__(self, db_modelz: DbModelz, pks_fn: dict, values_fn: dict) -> None:
        self.db_modelz = db_modelz
        pks = {}
        for k, pk_fn in pks_fn.items():
            pks[k] = pk_fn()
        self.pks = pks  # dict of pk and value

        if not all(self.pks.values()):
            matches = self.db_modelz.fetch(**self.pks)
            self.display(_data=matches)
            sys.exit(0)

        self.values_fn = values_fn  # dict of value_field_name : func
        self.object = self.read()

    def read(self) -> tuple or None:
        ''' Read the data using primary key

        Returns:
            tuple or None: Returns a tuple of the data record, if exists else None
        '''
        return self.db_modelz.exists(**self.pks)

    def display(self, _data: list = None) -> None:
        ''' Displays the data of the model in a beautified fashion

        Args:
            _data ([list], optional): If _data not provided then [self.object] will be used.
            Defaults to None.
            This is done to enhance the functionality of this method.
            This method can be used to display a single row or multiple rows.
        '''
        what = self.db_modelz.table
        if _data is None:
            _data = [self.object]
        if what == 'students':
            display_table('Student Data', ['Roll', 'Name', 'Email'], _data)
        elif what == 'exams':
            display_table('Exam Data', ['Uid', 'Name'], _data)
        else:  # marks
            display_table('Marks Data', ['Student', 'Uid', 'Marks'], _data)

    def create(self) -> None:
        ''' Create a new entry for model
        '''
        calculated = []
        for _, pk_val in self.pks.items():
            calculated.append(pk_val)
        for _, val_fn in self.values_fn.items():
            val = not_empty(val_fn())
            calculated.append(val)
        self.db_modelz.insert(tuple(calculated))

    def show_related(self) -> None:
        ''' Show data from other tables, that is related to current model
        '''

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
                f'SELECT name FROM students WHERE roll={obj[0]}')[0][0]
            exam = self.db_modelz.query(
                f'SELECT name FROM exams WHERE uid={obj[1]} ')[0][0]
            display_table('Marks Entry', ['Student', 'Exam', 'Marks'], [
                          (student, exam, obj[2])])

    def update(self) -> None:
        ''' Update data entry of current model
        '''
        calculated = {}
        for k, val_fn in self.values_fn.items():
            calculated[k] = val_fn()
        if any(calculated.values()):
            self.db_modelz.update(calculated, **self.pks)
        else:
            logger.warning('You left all values empty > Not updating anything')

    def delete(self) -> None:
        ''' Delete a data entry of current model
        '''
        self.db_modelz.delete(**self.pks)

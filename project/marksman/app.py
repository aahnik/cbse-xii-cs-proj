import logging
from sqlite3 import Cursor
from marksman.models import Modelz
from marksman.validators import get_pos_int, get_str, get_email


def _roll():
    return get_pos_int('Enter roll number of student: ')


def _uid():
    return get_pos_int('Enter the unique id of exam: ')


def crud_students(cursor: Cursor):
    students = Modelz('students', cursor)
    roll = _roll()
    st = students.exists(roll=roll)
    if st:
        print(st)
        print('Update/delete')
    else:
        print('Create')


def crud_exams(cursor: Cursor):
    exams = Modelz('exams', cursor)
    uid = _uid()
    exam = exams.exists(uid=uid)
    if exam:
        print(exam)
        print('u/d')
    else:
        print('create')


def crud_marks(cursor: Cursor):
    marks = Modelz('marks', cursor)
    marks_entry = marks.exists(roll=_roll(), uid=_uid())
    if marks_entry:
        print(marks_entry)
    else:
        print('create')


def crud_handler(args, cursor: Cursor):
    _handlers = {'students': crud_students,
                 'exams': crud_exams,
                 'marks': crud_marks}

    logging.info(f'called crud handler with {args.what}')
    apt_handler = _handlers.get(args.what)
    apt_handler(cursor)


def email_handler(args, cursor: Cursor):
    logging.info(f'called email handler with {args.exam}')


def visualization_handler(args, cursor: Cursor):
    logging.info(f'called vis handler with {args.exam} and {args.student}')

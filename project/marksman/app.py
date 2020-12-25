import logging
from sqlite3 import Cursor
from marksman.models import Student, Exam, MarksEntry
from marksman.db import Modelz


# def crud_students(cursor: Cursor):
#     students = Modelz('students', cursor)
#     student = students.exists(roll=_roll())
#     if student:
#         print(student)
#         print('Update/delete')
#     else:
#         print('Create')


# def crud_exams(cursor: Cursor):
#     exams = Modelz('exams', cursor)
#     exam = exams.exists(uid=_uid())
#     if exam:
#         print(exam)
#         print('u/d')
#     else:
#         print('create')


# def crud_marks(cursor: Cursor):
#     marks = Modelz('marks', cursor)
#     marks_entry = marks.exists(student=_roll(), exam=_uid())
#     if marks_entry:
#         print(marks_entry)
#     else:
#         print('create')


def crud_handler(args, cursor: Cursor):
    _handler_classes = {'students': Student,
                        'exams': Exam,
                        'marks': MarksEntry}

    logging.info(f'called crud handler with {args.what}')

    AptClass = _handler_classes.get(args.what)
    modelz = Modelz(args.what, cursor)

    

    apt = AptClass(modelz)

    if not apt.object:
        # if does not exist -> create
        handle_choice({'create': apt.create})
    else:
        # if exists -> update/delete
        handle_choice({'update': apt.update, 'delete': apt.delete})


def email_handler(args, cursor: Cursor):
    logging.info(f'called email handler with {args.exam}')


def visualization_handler(args, cursor: Cursor):
    logging.info(f'called vis handler with {args.exam} and {args.student}')

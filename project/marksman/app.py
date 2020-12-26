
import logging
from sqlite3 import Cursor
from marksman.models import Student, Exam, MarksEntry
from marksman.db import Modelz
from marksman.utils import handle_choice, fill_dummy, load_csv, export_csv

logger = logging.getLogger(__name__)


def crud_handler(args, cursor: Cursor):

    _handler_classes = {'students': Student,
                        'exams': Exam,
                        'marks': MarksEntry}

    logger.info(f'Called crud handler with {args.what}')

    AptClass = _handler_classes.get(args.what)
    modelz = Modelz(args.what, cursor)

    # display_table(modelz.fetch())

    apt = AptClass(modelz)

    if not apt.object:
        # if does not exist -> create
        logging.warn('Object does not Exist')
        handle_choice({'create': apt.create})
    else:
        # if exists -> update/delete
        print(apt.object)
        handle_choice({'update': apt.update, 'delete': apt.delete})


def email_handler(args, cursor: Cursor):
    logger.info(f'Called email handler with {args.exam}')


def visualization_handler(args, cursor: Cursor):
    from marksman.plot import plot_student_performance, plot_batch_performance
    logger.info(f'Called vis handler with {args.exam} and {args.r}')
    if args.r == 0:
        # plot performance of batch
        plot_batch_performance(cursor, args.exam)
    elif args.r > 0:
        # plot performance of specific student
        plot_student_performance(cursor, args.r, args.exam)
    else:
        logger.warn('Roll number must be greater than 0')


def utils_handler(args, cursor: Cursor):
    logger.info(f'Called utils with {args.task}')
    students = Modelz('students', cursor)
    exams = Modelz('exams', cursor)
    marks = Modelz('marks', cursor)

    if args.task == 'dummy':
        fill_dummy(students, exams, marks)
    if args.task == 'import':
        load_csv(students, exams, marks)
    if args.task == 'export':
        export_csv(students, exams, marks)

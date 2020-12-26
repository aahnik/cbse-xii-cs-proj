import logging
from sqlite3 import Cursor
from marksman.models import Student, Exam, MarksEntry
from marksman.db import Modelz
from marksman.utils import handle_choice

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
    logging.info(f'Called email handler with {args.exam}')


def visualization_handler(args, cursor: Cursor):
    logging.info(f'Called vis handler with {args.exam} and {args.student}')

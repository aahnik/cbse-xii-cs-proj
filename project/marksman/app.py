''' All the handlers for actions the app supports are registered in this module
'''

from argparse import Namespace
import logging
from smtplib import SMTP, SMTPAuthenticationError
from sqlite3 import Cursor

from rich.console import Console

from marksman.db import DbModelz, create_tables
from marksman.validators import get_email, get_pos_int, get_str, roll, uid
from marksman.models import Models
from marksman.helpers import handle_choice, configure_email
from marksman.mailer import Mailer
from marksman.plot import analyse_exam, plot_student_performance, plot_batch_performance
from marksman.utils import ImportExport, fill_dummy

logger = logging.getLogger(__name__)

console = Console()


def crud_handler(args: Namespace, cursor: Cursor) -> None:
    ''' Handle the crud action

    Args:
        args (Namespace): the arguments provided at command line
        cursor (Cursor): sqlite3 cursor object
    '''
    logger.info(f'Called crud handler with {args.what}')

    pks_fns = {
        'students': {'roll': roll},
        'exams': {'uid': uid},
        'marks': {'student': roll, 'exam': uid}
    }

    values_fns = {
        'students': {'name': get_str, 'email': get_email},
        'exams': {'name': get_str},
        'marks': {'marks': get_pos_int}
    }

    db_modelz = DbModelz(args.what, cursor)
    pks_fn = pks_fns.get(args.what)
    values_fn = values_fns.get(args.what)

    model = Models(db_modelz=db_modelz, pks_fn=pks_fn, values_fn=values_fn)
    obj = model.object

    if not obj:
        logger.warning('Object does not exist')
        handle_choice({'create': model.create})
    else:
        model.display()

        handle_choice({'more': model.show_related,
                       'update': model.update, 'delete': model.delete})


def email_handler(args: Namespace, cursor: Cursor) -> None:
    ''' Handles the email action

    Args:
        args (Namespace): the arguments provided at command line
        cursor (Cursor): sqlite3 cursor object
    '''

    logger.info(f'Called email handler with {args.exam}')
    sender_email, sender_auth, smtp_host, smtp_port, inst_name = configure_email()

    try:
        server = SMTP(host=smtp_host, port=smtp_port)
        server.connect(host=smtp_host, port=smtp_port)
    except Exception as err:
        logger.warning('Could not connect to SMTP server.')
        logger.exception(err)
        return
    else:
        logger.info('Connected to SMTP server')

    server.ehlo()
    server.starttls()
    server.ehlo()

    try:
        server.login(user=sender_email, password=sender_auth)
    except SMTPAuthenticationError as err:
        logger.warning(
            'Could not login to SMTP server using credentials you provided')
        console.print(
            f'''\nMost probably you gave incorrect email and password!
            Error Code {err.smtp_code}\n{err.smtp_error}\n''')
        return

    mailer = Mailer(server=server, cursor=cursor,
                    sender=sender_email, inst=inst_name, exam_uid=args.exam)

    mailer.mail_all_students()

    server.quit()
    logger.info('Disconnected from SMTP server')


def visualization_handler(args: Namespace, cursor: Cursor) -> None:
    ''' Handles the visualize action

    Args:
        args (Namespace): the arguments provided at command line
        cursor (Cursor): sqlite3 cursor object
    '''

    logger.info(f'Called vis handler with {args.exam} and {args.r}')
    if args.r == 0:
        # plot performance of batch
        plot_batch_performance(cursor, args.exam)
    elif args.r > 0:
        # plot performance of specific student
        plot_student_performance(
            cursor, args.r, args.exam, analyse_exam(cursor, args.exam))
    else:
        logger.warning('Roll number must be greater than 0')


def utils_handler(args: Namespace, cursor: Cursor) -> None:
    ''' Handles the utils action

    Args:
        args (Namespace): the arguments provided at command line
        cursor (Cursor): sqlite3 cursor object
    '''

    logger.info(f'Called utils with {args.task}')
    students = DbModelz('students', cursor)
    exams = DbModelz('exams', cursor)
    marks = DbModelz('marks', cursor)

    if args.task == 'dummy':
        logging.warning(
            'Any existing data will be deleted. Proceed ? [ENTER] to continue')
        input()
        create_tables(cursor)
        fill_dummy(students, exams, marks)
    if args.task in ['import', 'export']:
        imp_exp = ImportExport(students, exams, marks)
        imp_exp.do_apt(args.task)

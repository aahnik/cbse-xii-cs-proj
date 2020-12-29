from argparse import Namespace
import logging
from marksman.validators import get_email, get_pos_int, get_str, roll, uid
from smtplib import SMTP, SMTPAuthenticationError
from sqlite3 import Cursor
from rich import print

from marksman.db import DbModelz
from marksman.models import Models
from marksman.helpers import  handle_choice, configure_email
from marksman.mailer import Mailer

from marksman.plot import plot_student_performance, plot_batch_performance
from marksman.analyser import analyse_exam
from marksman.utils import ImportExport, fill_dummy

logger = logging.getLogger(__name__)


def crud_handler(args, cursor: Cursor):
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


def email_handler(args: Namespace, cursor: Cursor):
    ''' Handles the email action '''

    logger.info(f'Called email handler with {args.exam}')
    SENDER_EMAIL, SENDER_AUTH, SMTP_HOST, SMTP_PORT, INST_NAME = configure_email()

    try:
        server = SMTP(host=SMTP_HOST, port=SMTP_PORT)
        server.connect(host=SMTP_HOST, port=SMTP_PORT)
    except Exception as err:
        logger.warn('Could not connect to SMTP server.')
        logger.exception(err)
        return
    else:
        logger.info('Connected to SMTP server')

    server.ehlo()
    server.starttls()
    server.ehlo()

    try:
        server.login(user=SENDER_EMAIL, password=SENDER_AUTH)
    except SMTPAuthenticationError as err:
        logger.warn(
            'Could not login to SMTP server using credentials you provided')
        print(
            f'''\nMost probably you gave incorrect email and password! 
            Error Code {err.smtp_code}\n{err.smtp_error}\n''')
        return

    mailer = Mailer(server=server, cursor=cursor,
                    sender=SENDER_EMAIL, inst=INST_NAME, exam_uid=args.exam)

    mailer.mail_all_students()

    server.quit()
    logger.info('Disconnected from SMTP server')


def visualization_handler(args: Namespace, cursor: Cursor):

    logger.info(f'Called vis handler with {args.exam} and {args.r}')
    if args.r == 0:
        # plot performance of batch
        plot_batch_performance(cursor, args.exam)
    elif args.r > 0:
        # plot performance of specific student

        plot_student_performance(
            cursor, args.r, args.exam, analyse_exam(cursor, args.exam))
    else:
        logger.warn('Roll number must be greater than 0')


def utils_handler(args: Namespace, cursor: Cursor):

    logger.info(f'Called utils with {args.task}')
    students = DbModelz('students', cursor)
    exams = DbModelz('exams', cursor)
    marks = DbModelz('marks', cursor)

    if args.task == 'dummy':
        fill_dummy(students, exams, marks)
    if args.task in ['import', 'export']:
        ie = ImportExport(students, exams, marks)
        ie.do(args.task)

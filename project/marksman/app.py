import logging
from smtplib import SMTPAuthenticationError
from sqlite3 import Cursor
from rich import print

logger = logging.getLogger(__name__)


def crud_handler(args, cursor: Cursor):
    from marksman.db import Modelz
    from marksman.models import Student, Exam, MarksEntry
    from marksman.utils import handle_choice
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
    from marksman.utils import configure_email
    from marksman.mailer import Mailer
    from smtplib import SMTP
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
            f'\nMost probably you gave incorrect password! Error Code {err.smtp_code}\n{err.smtp_error}\n')
        return

    mailer = Mailer(server=server, cursor=cursor,
                    sender=SENDER_EMAIL, inst=INST_NAME, exam_uid=args.exam)

    mailer.mail_all_students()

    server.quit()
    logger.info('Disconnected from SMTP server')


def visualization_handler(args, cursor: Cursor):
    from marksman.plot import plot_student_performance, plot_batch_performance
    from marksman.analyser import analyse_exam
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


def utils_handler(args, cursor: Cursor):
    from marksman.db import Modelz
    from marksman.utils import fill_dummy, load_csv, export_csv
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

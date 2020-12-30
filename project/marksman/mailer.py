''' Module to implement the email functionality '''

import os
import time
import logging
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

from email import encoders
from sqlite3 import Cursor

import markdown
from rich.progress import track

from marksman.plot import analyse_exam, plot_student_performance
from marksman.helpers import ___, load_template


logger = logging.getLogger(__name__)


class Mailer:
    ''' Class to implement related methods for sending emails to students
    '''

    def __init__(self, server: SMTP, cursor: Cursor, sender: str, inst: str, exam_uid: int) -> None:
        ''' Constructor to initialize the mailer object

        Args:
            server (SMTP): SMTP sever object, which is logged in and ready to send mails
            cursor (Cursor): sqlite3 cursor object
            sender (str): email address of sender
            inst (str): institute name of sender
            exam_uid (int): uid of the exam, whose results are to be mailed
        '''
        self.server = server
        self.cursor = cursor
        self.sender = sender
        self.inst = inst if inst else ''
        self.exam_uid = exam_uid
        self.exam_name = self.get_exam_name()
        self.analysis = analyse_exam(self.cursor, self.exam_uid)
        self.template = load_template()
        self.recipient = {}

    def get_exam_name(self) -> str:
        ''' Fetches the name of the exam of the current Mailer object
        Returns:
            [str]: name of exam
        '''

        self.cursor.execute(
            ___(f'SELECT name FROM exams WHERE uid={self.exam_uid}'))
        exam_name = self.cursor.fetchone()[0]
        return exam_name

    def parse_template(self) -> str:
        '''
        Access any variable in your template by ::name:: style

        List of variables passed to template
            1. name
            2. roll
            3. email
            4. exam
            5. marks
            6. rank
            7. highest
            8. average
            9. inst

        Returns:
            str: the template string

        '''
        message = self.template

        def merge(dict1, dict2):
            res = {**dict1, **dict2}
            return res
        _vars = merge(self.recipient, self.analysis)

        _vars.update({'exam': self.exam_name, 'inst': self.inst})
        logger.info(f'varibles supplied to template\n{_vars}')

        for var in _vars.keys():
            message = message.replace(
                f'::{var}::', str(_vars.get(var)))

        return message

    def get_files(self) -> list:
        ''' Plot the necessary graphs and return a list of file paths

        Returns:
            list: file paths
        '''

        path = f'temp/{self.recipient["roll"]}_Performance.png'
        plot_student_performance(
            self.cursor, self.recipient['roll'], self.exam_uid, self.analysis, path=path)
        return [path]

    def send_mail(self) -> bool:
        ''' Send an email to the current recipient

        Returns:
            bool: status of sending
        '''

        message = self.parse_template()
        recipient = self.recipient['email']
        files = self.get_files()

        multipart_msg = MIMEMultipart("alternative")

        multipart_msg["Subject"] = message.splitlines()[0]
        multipart_msg["From"] = self.inst + f' {self.sender}'
        multipart_msg["To"] = recipient

        text = message
        html = markdown.markdown(text)

        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        multipart_msg.attach(part1)
        multipart_msg.attach(part2)

        for path in files:

            display_file_name = os.path.split(path)[1].split('_')[1]

            time.sleep(2)

            with open(path, 'rb') as _file:
                file_content = _file.read()

            logger.info(f'Attaching {display_file_name}')
            attach_part = MIMEBase('application', 'octet-stream')
            attach_part.set_payload(file_content)
            encoders.encode_base64(attach_part)
            attach_part.add_header('Content-Disposition',
                                   f"attachment; filename= {display_file_name}")
            multipart_msg.attach(attach_part)

        try:
            logger.info(f'Sending email to {recipient} ...')
            if not recipient.endswith('dontsend@example.com'):
                self.server.sendmail(self.sender,
                                     recipient,
                                     multipart_msg.as_string())
            else:
                logger.warning('Not sending email. Faking Process.')
        except Exception as err:
            logger.warning(f'Failed to send email to {recipient}')
            logger.exception(err)
            return False
        else:
            logger.info(f'Successfully sent email to {recipient}')
            return True

    def mail_all_students(self):
        ''' Method to loop over all students marks entries for the exam and send them emails.
        Updates the self.recipients and calls self.send_mail in every iteration.
        '''
        self.cursor.execute(
            ___(f'SELECT student,marks FROM marks WHERE exam={self.exam_uid} ORDER BY marks DESC'))
        students_roll_list = self.cursor.fetchall()
        os.makedirs('temp', exist_ok=True)
        rank = 1
        for roll_marks in track(students_roll_list, description='Sending emails'):
            self.cursor.execute(
                ___(f'SELECT * FROM students WHERE roll={roll_marks[0]}'))
            student = self.cursor.fetchone()
            self.recipient['roll'] = student[0]
            self.recipient['name'] = student[1]
            self.recipient['email'] = student[2]
            self.recipient['rank'] = rank
            self.recipient['marks'] = roll_marks[1]

            self.send_mail()

            rank += 1

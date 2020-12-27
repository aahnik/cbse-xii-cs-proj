import logging
from marksman.analyser import analyse_exam
from sqlite3 import Cursor
from marksman.plot import plot_student_performance
from smtplib import SMTP
import os
import markdown
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from marksman.db import ___
from email import encoders


logger = logging.getLogger(__name__)


class Mailer:
    def __init__(self, server: SMTP, cursor: Cursor, sender: str, inst: str, exam_uid: int):
        self.server = server
        self.cursor = cursor
        self.sender = sender
        self.inst = inst if inst else ''
        self.exam_uid = exam_uid
        self.exam_name = self.get_exam_name()
        self.analysis = analyse_exam(self.cursor, self.exam_uid)
        self.template = self.load_template()
        self.recipient = {}

    def get_exam_name(self):
        self.cursor.execute(
            ___(f'SELECT name FROM exams WHERE uid={self.exam_uid}'))
        exam_name = self.cursor.fetchone()[0]
        return exam_name

    def load_template(self):
        templ_file = 'marksman_email_template.md'
        if os.path.isfile(templ_file):
            with open(templ_file, 'r') as file:
                template = file.read()
        else:
            logger.warn(
                'Template file not found. Proceeding with default template')
            template = '''Result and Performance Analysis of ::exam::
            \n### Hi ::name:: you have scored ::marks:: and your rank is ::rank:: in ::exam::. 
            \nFind the performance report attached. 
            Best regards,
            ::inst:: 
            
            _Sent via marksman.mailer_'''
        return template

    def parse_template(self):
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

    def get_files(self):
        path = plot_student_performance(
            self.cursor, self.recipient['roll'], self.exam_uid, self.analysis, save=True)
        return [path]

    def send_mail(self) -> bool:

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

        for file in files:

            file_name = os.path.split(file)[1]

            with open(file, 'rb') as f:
                file_content = f.read()

            logger.info(f'Attaching {file_name}')
            attach_part = MIMEBase('application', 'octet-stream')
            attach_part.set_payload(file_content)
            encoders.encode_base64(attach_part)
            attach_part.add_header('Content-Disposition',
                                   f"attachment; filename= {file_name}")
            multipart_msg.attach(attach_part)

        try:
            logger.info(f'Sending email to {recipient} ...')
            self.server.sendmail(self.sender,
                                 recipient,
                                 multipart_msg.as_string())
        except Exception as err:
            logger.warning(f'Failed to send email to {recipient}')
            logger.exception(err)
            return False
        else:
            logger.info(f'Successfully sent email to {recipient}')
            return True

    def mail_all_students(self):
        self.cursor.execute(
            ___(f'SELECT student,marks FROM marks WHERE exam={self.exam_uid} ORDER BY marks'))
        students_roll_list = self.cursor.fetchall()

        for rank, roll_marks in enumerate(students_roll_list, start=1):
            self.cursor.execute(
                ___(f'SELECT * FROM students WHERE roll={roll_marks[0]}'))
            student = self.cursor.fetchone()
            self.recipient['roll'] = student[0]
            self.recipient['name'] = student[1]
            self.recipient['email'] = student[2]
            self.recipient['rank'] = rank
            self.recipient['marks'] = roll_marks[1]

            self.send_mail()

            os.remove('Performance.png')

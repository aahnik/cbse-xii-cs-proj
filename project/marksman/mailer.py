import logging
import os
import markdown
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

from email import encoders


logger = logging.getLogger(__name__)


class MarksEmail:
    def __init__(self,server, sender, inst,exam):
        pass

    def parse_template(self):
        pass

    def get_files(self):
        pass

    def send_mails(self) -> bool:

        message = self.parse_template()
        recipient = self.recipient
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

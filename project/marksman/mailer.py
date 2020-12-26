import logging

import markdown
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

from email import encoders

from .settings import sender_address, sender_name

logger = logging.getLogger(__name__)

def send_email(server, recipient: str, message: str, files: list) -> bool:

    multipart_msg = MIMEMultipart("alternative")

    multipart_msg["Subject"] = message.splitlines()[0]
    multipart_msg["From"] = sender_name
    multipart_msg["To"] = recipient

    text = message
    html = markdown.markdown(text)

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    multipart_msg.attach(part1)
    multipart_msg.attach(part2)

    for attachment, filename in files:
        logger.info(f'Attaching {filename}')
        attach_part = MIMEBase('application', 'octet-stream')
        attach_part.set_payload((attachment).read())
        encoders.encode_base64(attach_part)
        attach_part.add_header('Content-Disposition',
                               f"attachment; filename= {filename}")
        multipart_msg.attach(attach_part)

    try:
        server.sendmail(sender_address,
                        recipient,
                        multipart_msg.as_string())
    except Exception as err:
        logger.warning(f'Failed to send email to {recipient}')
        logger.exception(err)
        return False
    else:
        logger.info(f'Successfully sent email to {recipient}')
        return True

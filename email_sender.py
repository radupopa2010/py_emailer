#!/usr/bin/env python3
"""
Python3 version.
"""

import smtplib
import os
import random
import sys
import time

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

# Settings.
from settings import (
    USER,
    PASSWORD,
    SUBJECT,
    MESSAGE_BODY,
    ATTACH_DIR,
    RECIPIENTS_FILE,
    # Pause between emails.
    MIN_SLEEP,
    MAX_SLEEP,
    SMTP_SERVER,
    PORT
)


def create_custom_msg():
    """Create custom message, based on the settings."""
    # Create the messaje object.
    msg = MIMEMultipart()
    # Customize the message.
    msg['From'] = USER
    msg['Subject'] = SUBJECT
    # Attach the message body.
    with open(MESSAGE_BODY, 'r') as fh:
        msg.attach(MIMEText(fh.read()))

    return msg


def get_attachments_list():
    """Gennerate a list of files to attach.
    Returns a list of relative pathname for each file in ATTACH_DIR.
    """
    return [ATTACH_DIR + os.path.sep + fname for fname in os.listdir(ATTACH_DIR)]


# Attach all the fils in the attachment dir.
def attach_files(msg):
    """Func to attach files to custom message."""
    attach_list = get_attachments_list()
    for attach in attach_list:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(attach, 'rb').read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        'attachment; filename="%s"' % os.path.basename(attach))
        msg.attach(part)

    return msg


def send_email(to, mail_server):
    msg = create_custom_msg()
    attach_files(msg)
    msg['To'] = to
    mail_server.sendmail(USER, to, msg.as_string())


def get_all_recipients():
    """Helper function.
    Return a list of al recipients"""
    with open(RECIPIENTS_FILE, 'r') as fh:
        return [email.rstrip() for email in fh.readlines()]


def send_emails(recipients, slowly=True):
    """Send all the email message to all recipients.
    Avoid being flagged as SPAM by:
    - sending to one message / recipient;
    - control the speed of sending the messages.
    """
    # Create a new instance of a custom message
    try:
        # Try to connect to the email server.
        mail_server = smtplib.SMTP(SMTP_SERVER, PORT)
        mail_server.ehlo()
        mail_server.starttls()
        mail_server.ehlo()
        mail_server.login(USER, PASSWORD)

        # If loggin is ok, try to send the messeage for each recipient.
        for email_addr in recipients:
            try:
                send_email(email_addr, mail_server)
            except:
                print("Unable to send the email to: ", email_addr)
                print("Error: ", sys.exc_info()[0])
            else:
                print('Email sent successfully to: ', email_addr)
            # Control the sending speed
            if slowly:
                rand_no = random.randint(MIN_SLEEP, MAX_SLEEP)
                print('Controlling the sending speed, sleeping for: ', rand_no)
                time.sleep(rand_no)
            else:
                print('Sending fast ...')
    except:
        print("Unable to connect to the server. Error: ", sys.exc_info()[0])
        raise
    finally:
        mail_server.close()
    print('All emails we sent successfully !!!')


def main():
    """Entry point  for the script."""

    recipients = get_all_recipients()
    send_emails(recipients)

    return


if __name__ == '__main__':
    main()

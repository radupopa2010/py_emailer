"""Settings module for emailer."""

# Settings Loredana.
# USER = 'i_loredana20@yahoo.com'
# PASSWORD = 'ILbalanta8701'
# SUBJECT = 'Job Application: Dressmaker'
# MESSAGE_BODY = 'cover_letter_Loredana_dressmaker.txt'


# Settings Radu.
USER = 'radupopa2010@yahoo.com'
PASSWORD = 'Rm.Valcea'
SUBJECT = 'Job Application: Back-End Developer'
MESSAGE_BODY = 'cover_letter_radu.txt'


# Folder containing all the files you want to attach.
# Can not contain other directories / folders.
ATTACH_DIR = 'attachments'
# Text file, containing a list of recipients, separated by a new line
RECIPIENTS_FILE = 'recipients.txt'
# The program is designed to make a small break between sending each email,
# to prevent your email account from being flagged as spam.
# Pause between emails.
# Random time to sleep, in seconds, between sending a new message.
MIN_SLEEP = 15
MAX_SLEEP = 23
# SMTP server
SMTP_SERVER = 'smtp.mail.yahoo.com'
PORT = 587

# py_emailer
Send emails with attachments in Python

# How to use this program

To configure the e-mail account open `settings.py`

USER = 'exemple@yahoo.com'

PASSWORD = 'secret'

SUBJECT = 'Subject of the message'

ATTACH_DIR = 'attachments'

    This is the name of the folder where to put the files you want to 
    attach. **NOTE: FILES ONLY**

MESSAGE_BODY = 'message.txt'
    
    File containing the message you want to send.

MIN_SLEEP = 15

MAX_SLEEP = 23

    To make sure that the message is sent successfully the robot sleeps for a 
    random number of seconds before sending a new message.

"recipients.txt" = put here all the e-mails where you want to send your message.

## SMTP server.

SMTP_SERVER = 'smtp.mail.yahoo.com'

PORT = 587

    The SMTP server from your e-mail provider. You can always find this domain
    by doing a Google search.   

### Run the program

Make sure you have installed [Python](https://www.python.org/).

Open a terminal (Linux / Mac) or a command promt (Windows: cmd.exe)

`python email_sender.py`

### ROMANA Cum se foloseste acest program 

Pentru a configura mesajul, trebuie sa editezi fisierul "settings.py",
in felul urmator:

Nota: daca textul este intre ghilimele, trebuie sa modici ce este intre ghilimele,
ghilimelele raman.

USER = 'exemplu@yahoo.com'
    adresa ta de email
PASSWORD = 'parola super secreata aici'

SUBJECT = 'Subiectul mesajului'

ATTACH_DIR = 'attachments'
    Numele foldereului unde trebuie sa pui fisierele pe care doresti sa le 
    atasezi. NU ATASAEAZA ALTE FOLDERE!

MESSAGE_BODY = 'coverLetter.txt'
    Numele fierului unde scrii textul care reprezinta continutul,
    daca vrei sa il redenumesti, trebuie sa il schimbi si in settings.py

MIN_SLEEP = 15
MAX_SLEEP = 23
    Pentru a se asigura ca mesajul ajunge cu success la destinatar, robotul 
    face o pauza intre 15 si 23 de secunde. Parametrii pot fi modificati in 
    functie de interes.


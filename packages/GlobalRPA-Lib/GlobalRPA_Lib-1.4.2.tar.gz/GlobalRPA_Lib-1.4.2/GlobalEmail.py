import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(subject, body, email_to, email_from, appPassword, attachmentPath=None):  
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = email_from
    msg['To'] = email_to
    password = appPassword

    msg.attach(MIMEText(body, 'html'))

    if attachmentPath:
        attach_file(msg, attachmentPath)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    
    s.login(msg['From'], password)

    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    
    print('Email was successfully sent to: ' + email_to)

def attach_file(msg, attachmentPath):
    attachment = open(attachmentPath, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= " + attachmentPath)
    msg.attach(part)
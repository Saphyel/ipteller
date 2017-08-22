import smtplib
import os

class Mailer:

    def __init__(self):
        self.host = "smtp.gmail.com"
        self.port = 465
        self.user = os.environ["GMAIL_USER"]
        self.pwd = os.environ["GMAIL_PASS"]

    def send(self, email_from, email_to, subject, message):
        try:
            server = smtplib.SMTP_SSL(self.host, self.port)
            server.login(self.user, self.pwd)
            msg = """\
From: %s
To: %s
Subject: %s

%s
""" % (email_from, email_to, subject, message)
            server.sendmail(email_from, email_to, msg)
            server.close()
        except:
            print 'Something went wrong...'

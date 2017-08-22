import smtplib
import os

class Mailer:

    def __init__(self):
        self.host = "smtp.gmail.com"
        self.port = 465
        self.user = os.environ["GMAIL_USER"]
        self.pwd = os.environ["GMAIL_PASS"]

    def send(subject, message):
        try:
            server = smtplib.SMTP_SSL(self.host, self.port)
            server.login(self.user, self.pwd)
            msg = """\
From: %s
To: %s
Subject: %s

%s
""" % (self.user, self.user, subject, message)
            server.sendmail(self.user, self.user, msg)
            server.close()
        except:
            print 'Something went wrong...'

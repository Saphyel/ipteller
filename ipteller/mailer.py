#!/usr/bin/env python

import logging
import os
import smtplib


class Mailer(object):
    def __init__(self, subject, body):
        self.host = "smtp.gmail.com"
        self.port = 465
        self.user = os.environ["GMAIL_USER"]
        self.pwd = os.environ["GMAIL_PASS"]
        self.subject = subject
        self.body = body

    def send(self):
        try:
            server = smtplib.SMTP_SSL(self.host, self.port)
            server.login(self.user, self.pwd)
            server.sendmail(self.user, self.user, self.message())
            server.close()
            logging.info('Notification of the new IP sent')
        except smtplib.SMTPAuthenticationError as error:
            logging.exception('Authentication error:' + error.smtp_error)
            quit(0)
        except ValueError as error:
            logging.exception(error.message)
            quit(0)

    def message(self):
        return """\
From: %s
To: %s
Subject: %s

%s
""" % (self.user, self.user, self.subject, self.body)

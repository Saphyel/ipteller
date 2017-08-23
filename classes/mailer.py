#!/usr/bin/env python
"""Mailer Entity"""

import os
import smtplib


class Mailer(object):
    """Base class for mailer."""

    def __init__(self):
        self.host = "smtp.gmail.com"
        self.port = 465
        self.user = os.environ["GMAIL_USER"]
        self.pwd = os.environ["GMAIL_PASS"]
        self.subject = ""
        self.message = ""

    def set_subject(self, subject):
        """Sets the subject of the email."""
        self.subject = subject

    def set_message(self, message):
        """Sets the message of the email."""
        self.message = message

    def send(self):
        """Sends the email."""
        try:
            server = smtplib.SMTP_SSL(self.host, self.port)
            server.login(self.user, self.pwd)
            msg = """\
From: %s
To: %s
Subject: %s

%s
""" % (self.user, self.user, self.subject, self.message)
            server.sendmail(self.user, self.user, msg)
            server.close()
        except:
            print 'Something went wrong...'

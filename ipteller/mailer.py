#!/usr/bin/env python

import logging
import smtplib


class Mailer(object):
    @staticmethod
    def send(data):
        host = "smtp.gmail.com"
        port = 465
        try:
            server = smtplib.SMTP_SSL(host, port)
            server.login(data['user'], data['pwd'])
            server.sendmail(data['user'], data['user'], Mailer.message(data))
            server.close()
            logging.info('Notification of the new IP sent')
        except smtplib.SMTPAuthenticationError as error:
            logging.exception('Authentication error:' + error.smtp_error)
            quit(0)
        except ValueError as error:
            logging.exception(error.message)
            quit(0)

    @staticmethod
    def message(data):
        return """\
From: %s
To: %s
Subject: %s

%s
""" % (data['user'], data['user'], data['subject'], data['body'])

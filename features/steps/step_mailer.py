"""
Get a notification ``email`` flavour
"""

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import when, then
from ipteller.mailer import Mailer


@when('I want to send an email with the subject "{subject}" and body "{body}"')
def step_impl(context, subject, body):
    context.subject = subject
    context.body = body
    context.message = Mailer.message({'user': 'test', 'pwd': 'pwd', 'subject': subject, 'body': body})


@then('I expect to get it with a proper format')
def step_impl(context):
    assert context.subject in context.message
    assert context.body in context.message

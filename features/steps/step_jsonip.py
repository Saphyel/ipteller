"""
Get the right IP address ``jsonip`` flavour
"""

from types import StringType

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import when, then
from ipteller.jsonip import JsonIp


@when('I want to check my IP address')
def step_impl(context):
    context.provider = JsonIp()


@then('I expect to get a string')
def step_impl(context):
    assert type(context.provider.get_ip({'ip': '27.18.50.2'})) is StringType

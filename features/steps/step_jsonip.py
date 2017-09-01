"""
Get the right IP address ``jsonip`` flavour
"""

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import when, then
from types import StringType
from ipteller.jsonip import JsonIp


@when('I want to check my IP address')
def step_impl(context):
    provider = JsonIp()
    context.public_ip = provider.public_ip


@then('I expect to get a string')
def step_impl(context):
    assert type(context.public_ip) is StringType

"""
Save the IP address ``filesystem`` flavour
"""

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then
from ipteller.address import Address


@given('I have the entity in {loc}')
def step_impl(context, loc):
    context.address = Address(loc)


@when('I save the IP {ip}')
def step_impl(context, ip):
    context.ip = ip
    context.address.public_ip = ip
    context.address.save()


@then('I expect to load it')
def step_impl(context):
    context.address.load()
    assert context.ip == context.address.public_ip

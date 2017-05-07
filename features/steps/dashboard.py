from behave import *

use_step_matcher("re")


@step("I am on the dashboard screen")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("I should be presented with a start workout button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("I press the start workout button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("I should be presented with an add exercise button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("I click the add exercise button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("I should be presented with an add exercise form")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("I submit a valid add exercise form")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("I should see the exercise populate on the screen")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("The add exercise form should disappear")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass
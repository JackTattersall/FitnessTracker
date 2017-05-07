from behave import given, when, then
from exercises.tests.factories import UserFactory
from nose.tools import assert_true, assert_equal
from selenium import webdriver


@given('an anonymous user')
def step_impl(context):

    # Creates a dummy user for our tests (user is not authenticated at this point)
    test_user = UserFactory(username='foo', email='foo@example.com')
    test_user.set_password('bar')

    # Don't omit to call save() to insert object in database
    test_user.save()


@when('I submit a valid login page')
def step_impl(context):
    browser = context.browser
    browser.get(context.base_url + '/account/login/')

    # Checks for Cross-Site Request Forgery protection input
    assert_true(browser.find_element_by_name('csrfmiddlewaretoken').is_enabled())

    # Fill login form and submit it (valid version)
    browser.find_element_by_name('username').send_keys('foo')
    browser.find_element_by_name('password').send_keys('bar')
    browser.find_element_by_name('submit').click()


@then('I am redirected to the "{text}" page')
def step_impl(context, text):
    browser = context.browser  # type: webdriver.PhantomJS

    # Checks success status
    assert_equal(browser.title, text)


@when('I submit an invalid login page')
def step_impl(context):
    browser = context.browser

    browser.get(context.base_url + '/account/login/')

    # Checks for Cross-Site Request Forgery protection input (once again)
    assert browser.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    # Fill login form and submit it (invalid version)
    browser.find_element_by_name('username').send_keys('foo')
    browser.find_element_by_name('password').send_keys('bar-is-invalid')
    browser.find_element_by_name('submit').click()


@when('I logout')
def step_impls(context):
    browser = context.browser  # type: webdriver.PhantomJS

    browser.get(context.base_url + '/account/logout/')


@when("I submit a valid change password form")
def step_impl(context):
    browser = context.browser  # type: webdriver.PhantomJS

    # Checks for Cross-Site Request Forgery protection input
    assert_true(browser.find_element_by_name('csrfmiddlewaretoken').is_enabled())

    # Fill login form and submit it (valid version)
    browser.find_element_by_name('old_password').send_keys('bar')
    browser.find_element_by_name('new_password1').send_keys('newpassword')
    browser.find_element_by_name('new_password2').send_keys('newpassword')
    browser.find_element_by_name('change').click()


@when("I navigate to the change password page")
def step_impl(context):
    browser = context.browser  # type: webdriver.PhantomJS

    browser.get(context.base_url + '/account/password_change/')

    # Checks success status
    assert_equal(browser.title, 'Change your password')


@when("I submit an invalid change password form")
def step_impl(context):
    browser = context.browser  # type: webdriver.PhantomJS

    # Checks for Cross-Site Request Forgery protection input
    assert_true(browser.find_element_by_name('csrfmiddlewaretoken').is_enabled())

    # Fill login form and submit it (valid version)
    browser.find_element_by_name('old_password').send_keys('bar')
    browser.find_element_by_name('new_password1').send_keys('newp')
    browser.find_element_by_name('new_password2').send_keys('newpassword')
    browser.find_element_by_name('change').click()


@when('I login with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    browser = context.browser
    browser.get(context.base_url + '/account/login/')

    # Checks for Cross-Site Request Forgery protection input
    assert_true(browser.find_element_by_name('csrfmiddlewaretoken').is_enabled())

    # Fill login form and submit it (valid version)
    browser.find_element_by_name('username').send_keys(username)
    browser.find_element_by_name('password').send_keys(password)
    browser.find_element_by_name('submit').click()


@given("I am logged in")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass
from behave import given, when, then
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unittest import TestCase
from time import sleep


@given('I am on {url} website')
def given_i_am_on_url_website(context, url):
    context.testCase = TestCase()
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()
    print("URL: ", url)
    context.driver.get(str(url))
    
def map_with(context, by_type, mapper):
    by_type = getattr(By, by_type.upper())
    mapping = (by_type, mapper)
    return WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(mapping))

def map_button_with(context, by_type, mapper):
    by_type = getattr(By, by_type.upper())
    mapping = (by_type, mapper)
    return WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable(mapping))


@when('I enter {text_value} in field with {by_type} equal to {mapper}')
def enter_text_on_mapped_field(context,text_value, by_type, mapper):
    element = map_with(context, by_type, mapper)
    element.clear()
    element.send_keys(text_value)
    
@when('I click the button with {by_type} equal to {mapper}')
def click_on_mapped_button(context, by_type, mapper):
    element = map_button_with(context, by_type, mapper)
    element.click()
    
@then('I should see the {url} page')
def assert_in_page(context, url):

    current_url = context.driver.current_url
    TestCase.assertEqual(context.testCase, url, current_url)
    
@then('I should see an error message with the text: {error_message_text}')
def assert_error_message(context, error_message_text):
    mapper = "h3[data-test='error']"
    element = map_with(context, "css_selector", mapper)
    actual_message = element.text
    TestCase.assertEqual(context.testCase, actual_message, error_message_text)
    
    

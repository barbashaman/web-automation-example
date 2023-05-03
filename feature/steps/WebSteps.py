from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unittest import TestCase

def map_with(context, by_type, mapper):
    by_type = getattr(By, by_type.upper())
    mapping = (by_type, mapper)
    return WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(mapping))

def map_button_with(context, by_type, mapper):
    by_type = getattr(By, by_type.upper())
    mapping = (by_type, mapper)
    return WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable(mapping))

@given('I am on {url} website')
def given_i_am_on_url_website(context, url):
    context.driver = webdriver.Chrome(executable_path=r"chromedriver")
    context.driver.maximize_window()
    print("URL: ", url)
    context.driver.get(str(url))

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
    TestCase.assertEqual(url, current_url)
    

from behave import *
from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pyvirtualdisplay import Display

display = Display(visible=0, size=(1024, 768))
display.start()

@given('Launch Chrome Browser')
def LaunchChrome(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    time.sleep(5)

@when('Go to Safework login page')
def SafewordDashboard(context):
    context.driver.get("https://qa.strongarmtech.com/login")
    time.sleep(5)

email = os.environ.get('EMAIL_DB')
pwd = os.environ.get('PASS_DB')

@when('Enter EMAIL_DB and PASS_DB')
def EnterCred(context):
    context.driver.find_element(By.ID, "username").send_keys(email)
    context.driver.find_element(By.ID, "password").send_keys(pwd)
    time.sleep(5)

@when('Click on login button')
def LoginButton(context):
    context.driver.find_element(By.XPATH, "//span[text()='Login']").click()
    time.sleep(9)

@then('User should be logged in')
def login(context):
    context.driver.find_element(By.XPATH, "//p[contains(text(),'Go to')]").is_displayed()
    assert True
    time.sleep(9)
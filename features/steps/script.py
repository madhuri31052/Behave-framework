from behave import *
from selenium import webdriver
import time
import os

@given('Launch Chrome Browser')
def LaunchChrome(context):
    context.driver=webdriver.Chrome(executable_path="C:\\Program Files\\chromedriver.exe")
    context.driver.maximize_window()
    time.sleep(5)

@when('Go to Safework login page')
def SafewordDashboard(context):
    context.driver.get("https://qa.strongarmtech.com/login")
    time.sleep(5)

email = os.environ.get('Email_DB')
pwd = os.environ.get('Pass_DB')

@when('Enter Email_DB and Pass_DB')
def EnterCred(context):
    context.driver.find_element_by_id("username").send_keys(email)
    context.driver.find_element_by_id("password").send_keys(pwd)
    time.sleep(5)

@when('Click on login button')
def LoginButton(context):
    context.driver.find_element_by_xpath("//span[text()='Login']").click()
    time.sleep(9)

@when('Click on Multibox tab')
def MultiboxTab(context):
    context.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/*[1]").click()
    time.sleep(5)

@when('Click on Signout tab')
def SignoutTab(context):
    context.driver.find_element_by_xpath("//p[contains(text(),'Sign out')]").click()
    time.sleep(5)

@then('User should be signed out')
def Signedout(context):
    context.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[1]/form[1]/div[1]/*[1]").is_displayed()
    assert True

@when('Select Analytics tab')
def AnalyticsTab(context):
    context.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/a[3]/button[1]/span[1]/div[1]").click()
    time.sleep(5)

@when('Click on Fuse Dashboard tab')
def step_impl(context):
    context.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/*[1]").click()
    time.sleep(7)

@when('Select corporate report tab')
def step_impl(context):
    context.driver.find_element_by_xpath("//span[contains(text(), 'Corporate Report')]").click()
    time.sleep(7)

@when('Click on sort icon of Warehouse')
def step_impl(context):
    context.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[2]/div[1]/div[2]/main[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/*[1]").click()
    time.sleep(7)

@then('User should be able to sort')
def step_impl(context):
    context.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[2]/div[1]/div[2]/main[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]").is_displayed()
    assert True
    time.sleep(5)

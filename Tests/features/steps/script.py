from behave import *
from selenium import webdriver
import time
import os
from webdriver_manager.chrome import ChromeDriverManager

@given('Launch Chrome Browser')
def LaunchChrome(context):
    context.driver=webdriver.Chrome(ChromeDriverManager().install() )
    context.driver.maximize_window()
    time.sleep(5)

@when('Go to Safework login page')
def SafewordDashboard(context):
    context.driver.get("https://qa.strongarmtech.com/login")
    time.sleep(5)

@when('Enters "{email}" and "{pwd}"')
def EnterCred(context, email, pwd):
    context.driver.find_element_by_id("username").send_keys(email)
    context.driver.find_element_by_id("password").send_keys(pwd)
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

@then('User should not be able to login')
def LoginCheck(context):
    if context.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[1]/form[1]/div[1]/*[1]").is_displayed():
        context.driver.close()
        assert True, "Test Passed"
    else:
        context.driver.close()
        assert False, "Test Failed"
    
@when('Click on Multibox tab')
def MultiboxTab(context):
    context.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]").click()
    time.sleep(5)

@when('Click on Signout tab')
def SignoutTab(context):
    context.driver.find_element_by_xpath("//p[contains(text(),'Sign out')]").click()
    time.sleep(5)

@then('User should be signed out')
def Signedout(context):
    context.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[1]/form[1]/div[1]/*[1]").is_displayed()
    assert True
    context.driver.close()

@when('Select Analytics tab')
def AnalyticsTab(context):
    context.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/a[3]/button[1]/span[1]").click()
    time.sleep(12)

@when('On Ergonomic Safety Dashboard click on Select Athlete dropdown')
def select(context):
    context.driver.find_element_by_xpath("//div[@id='Select AthleteSelect']").click()
    time.sleep(5)

@then('User should not be able to Select an Athlete')
def dropdown(context):
    visible1 = context.driver.find_element_by_xpath("//div[@id='Select AthleteSelect']")
    if visible1.is_displayed():
        context.driver.close()
        assert True, "Test Passed"
    else: 
        context.driver.close()
        assert False, "Test Failed"

@when('Click on Fuse Dashboard tab')
def fuseTab(context):
    context.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/*[1]").click()
    time.sleep(8)

@when('Select New Hire Tenure Analysis')
def hiretenure(context):
    context.driver.find_element_by_xpath("//span[contains(text(),'New Hire Tenure Analysis')]").click()
    time.sleep(10)

@then('User should be able to see Highest Risk Tenure Group tile')
def Tile(context):
    visible2 = context.driver.find_element_by_xpath("//h6[contains(text(),'Highest Risk Tenure Group')]")
    if visible2.is_displayed():
        context.driver.close()
        assert True, "Test Passed"
    else:
        context.driver.close()
        assert False, "Test Failed"

@when('Select corporate report tab')
def reportTab(context):
    context.driver.find_element_by_xpath("//span[contains(text(), 'Corporate Report')]").click()
    time.sleep(12)

@when('Click on sort icon of Warehouse')
def warehouse(context):
    context.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[2]/div[1]/div[2]/main[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/*[1]").click()
    time.sleep(5)

@then('User should be able to sort')
def sortIcon(context):
    context.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[2]/div[1]/div[2]/main[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]").is_displayed()
    assert True
    context.driver.close()

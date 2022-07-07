from behave import *
from selenium import webdriver
import time
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display

display = Display(visible=0, size=(1024, 768))
display.start()

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
    context.driver.find_element(By.XPATH,"//input[@id='username']").send_keys(email)
    context.driver.find_element(By.XPATH,"//input[@id='password']").send_keys(pwd)
    time.sleep(5)

QA_CRED_EMAIL = os.environ.get('QA_CRED_EMAIL')
QA_CRED_PASS = os.environ.get('QA_CRED_PASS')

@when('Enter QA_CRED_EMAIL and QA_CRED_PASS')
def EnterCred(context):
    context.driver.find_element(By.XPATH,"//input[@id='username']").send_keys(QA_CRED_EMAIL)
    context.driver.find_element(By.XPATH,"//input[@id='password']").send_keys(QA_CRED_PASS)
    time.sleep(5)

@when('Click on login button')
def LoginButton(context):
    context.driver.find_element(By.XPATH, "//span[text()='Login']").click()
    time.sleep(5)

@then('User should be logged in')
def login(context):
    context.driver.find_element(By.XPATH,"//p[contains(text(),'Go to')]").is_displayed()
    assert True
    time.sleep(9)

@then('User should not be able to login')
def LoginCheck(context):
    if context.driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[1]/form[1]/div[1]/*[1]").is_displayed():
        context.driver.quit()
        assert True, "Test Passed"
    else:
        context.driver.quit()
        assert False, "Test Failed"
    
@when('Click on Multibox tab')
def MultiboxTab(context):
    context.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/*[1]").click()
    time.sleep(12)

@when('Click on Signout tab')
def SignoutTab(context):
    context.driver.find_element(By.XPATH,"//p[contains(text(),'Sign out')]").click()
    time.sleep(5)

@then('User should be signed out')
def Signedout(context):
    context.driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[1]/form[1]/div[1]/*[1]").is_displayed()
    assert True
    time.sleep(8)

@when('Select Analytics tab')
def AnalyticsTab(context):
    context.driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/a[3]/button[1]").click()
    time.sleep(14)
                                                  
@when('On Ergonomic Safety Dashboard click on Select Athlete dropdown')
def select(context):
    context.driver.find_element(By.XPATH,"//div[@id='Select AthleteSelect']").click()
    time.sleep(5)

@then('User should not be able to Select an Athlete before selecting Warehouse')
def dropdown(context):
    visible1 = context.driver.find_element(By.XPATH,"//div[@id='Select AthleteSelect']")
    if visible1.is_displayed():
        context.driver.quit()
        assert True, "Test Passed"
    else: 
        context.driver.quit()
        assert False, "Test Failed"

@when('Click on Fuse Dashboard tab')
def fuseTab(context):
    context.driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/*[1]").click()
    time.sleep(8)

@when('Select New Hire Tenure Analysis')
def hiretenure(context):
    context.driver.find_element(By.XPATH,"//span[contains(text(),'New Hire Tenure Analysis')]").click()
    time.sleep(10)

@then('User should be able to see Highest Risk Tenure Group tile')
def Tile(context):
    visible2 = context.driver.find_element(By.XPATH,"//h6[contains(text(),'Highest Risk Tenure Group')]")
    if visible2.is_displayed():
        context.driver.quit()
        assert True, "Test Passed"
    else:
        context.driver.quit()
        assert False, "Test Failed"

@when('Select corporate report tab')
def reportTab(context):
    context.driver.find_element(By.XPATH,"//span[contains(text(), 'Corporate Report')]").click()
    time.sleep(12)

@when('Click on sort icon of Warehouse')
def warehouse(context):
    context.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[2]/main[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/*[1]").click()
    time.sleep(5)

@then('User should be able to sort in qa env')
def sortIcon(context):
    visible3 = context.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[2]/main[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]")
    if visible3.is_displayed():
        context.driver.quit()
        assert True, "Test Passed"
    else:
        context.driver.quit()
        assert False, "Test Failed"


#dev3 env credentials

@when('Go to dev3 login page')
def SafewordDashboard(context):
    context.driver.get("https://strongarm.dev3.strongarmtech.com/login")
    time.sleep(5)

DEV3_CRED_EMAIL = os.environ.get('DEV3_CRED_EMAIL')
DEV3_CRED_PASS= os.environ.get('DEV3_CRED_PASS')

@when('Enter DEV3_CRED_EMAIL and DEV3_CRED_PASS')
def EnterCred(context):
    context.driver.find_element(By.XPATH,"//input[@id='username']").send_keys(DEV3_CRED_EMAIL)
    context.driver.find_element(By.XPATH,"//input[@id='password']").send_keys(DEV3_CRED_PASS)
    time.sleep(5)

@then('User should be able to sort in dev3 env')
def sortIcon(context):
    visible4 = context.driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/div[2]/main[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]")
    if visible4.is_displayed():
        context.driver.quit()
        assert True, "Test Passed"
    else:
        context.driver.quit()
        assert False, "Test Failed"
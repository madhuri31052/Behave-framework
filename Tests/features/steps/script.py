from ast import Sub
from cmath import e
from lib2to3.pgen2 import driver
from multiprocessing import context
from operator import is_not
from re import X
from time import thread_time
from behave import *
import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from telnetlib import EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from BDDCommon.CommonSteps.webstepscommon import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
# from BDDCommon.CommonSteps import webcommon
# from BDDCommon.CommonSteps import *
from selenium.webdriver import chrome


@given(u'user is on client page')
def Loginconections(context):
    #webcommon.go_to(context,url,email,pwd)
    url="https://strongarm.dev3.strongarmtech.com/login"

    email = "raj@strongarmtech.com"
    pwd = "Whoknows@0"

    context.driver=webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()
    context.driver.get(url)
    WebDriverWait(context.driver,45).until(EC.presence_of_element_located((By.XPATH,"//input[@id='username']")))
    context.driver.find_element(By.XPATH,"//input[@id='username']").send_keys(email)
    WebDriverWait(context.driver,45).until(EC.presence_of_element_located((By.XPATH,"//input[@id='password']")))
    context.driver.find_element(By.XPATH,"//input[@id='password']").send_keys(pwd)
    WebDriverWait(context.driver,45).until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Login']")))
    context.driver.find_element(By.XPATH,"//span[text()='Login']").click()
    time.sleep(10)
    WebDriverWait(context.driver,45).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='MuiBox-root jss238']")))
    context.driver.find_element(By.XPATH,"//div[@class='MuiBox-root jss238']").click()#click on Menu button 
    time.sleep(10)
    context.driver.find_element(By.XPATH,"(//p[contains(text(),'Admin')])[1]").click()
    WebDriverWait(context.driver,45).until(EC.element_to_be_clickable((By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/*[1]")))
    context.driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/*[1]").click()


    #Click on client
    WebDriverWait(context.driver,45).until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Clients']")))
    context.driver.find_element(By.XPATH,"//span[text()='Clients']").click()
    time.sleep(5)
    print("working fine...")

@when('user clicks on add new button')
def adding_client(context):
    context.driver.find_element(By.XPATH,"//button[@id='addBtn']").click()
    time.sleep(5)



@when(u'user enters client_name as "appletech22" and  status as "PILOT" and ActiveInactive_date as "02/22/2022  " and  no_of_contractedusers as "5" and  sub_domain as ""and user click on next button and user selects first name/last name format')
def client_details(context):
    context.driver.find_element(By.XPATH,"//input[@id='clientName-input']").send_keys("appletech22") #slect client name
    time.sleep(3)
    context.driver.find_element(By.XPATH,"//div[@id='status-select']").click() #select staus text box
    context.driver.find_element(By.XPATH,"//li[contains(text(),'PILOT')]").click() #select value in dropdown
    datefield = context.driver.find_element(By.XPATH,"//input[@id='date-picker-inline']")#select date text box
    datefield.click()
    time.sleep(3)
    datefield.send_keys(Keys.CONTROL,"a") # Select all pre-existing text/input value
    datefield.send_keys(Keys.BACKSPACE)    # Remove that text
    datefield.send_keys("01012011") 
    time.sleep(3)
    context.driver.find_element(By.XPATH,"//input[@id='numOfUsers-input']").send_keys("5")#select no of contr user box
    context.driver.find_element(By.XPATH,"//input[@id='subdmian-input']").send_keys("")#select subdomain box
    context.driver.find_element(By.XPATH,"//button[@id='nextBtn']").click()#click on next button
    time.sleep(3)
    context.driver.find_element(By.XPATH,"//div[@id='first-last-name-format-select']").click()#select name formate text box
    context.driver.find_element(By.XPATH,"//li[contains(text(),'First Name + Last Name')]").click()#select value in dropdown box
    time.sleep(3)
    



@when(u'user click on confirm button')
def submit_client(context):
    context.driver.find_element(By.XPATH,"//span[contains(text(),'Confirm')]").click()#click on confirm
    time.sleep(5)

@then(u'user should see new client added successfully message.')
def check_client(context):
    try:
        text =WebDriverWait(context.driver,45).until(EC.presence_of_element_located((By.XPATH,"//p[contains(text(),'has been successfully added.')]"))).text
    except:
        context.driver.close()
        assert False,"test failed User enter wrong data"
    if text == "has been successfully added.":
        assert True,"test pass"
    elif text == "ADD NEW CLIENT":
        assert False,"test fail User enter wrong data"
    context.driver.close()


# from behave import *
# from selenium import webdriver
# import time
# import os
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from pyvirtualdisplay import Display

# display = Display(visible=0, size=(1024, 768))
# display.start()

# @given('Launch Chrome Browser')
# def LaunchChrome(context):
#     context.driver=webdriver.Chrome(ChromeDriverManager().install() )
#     context.driver.maximize_window()
#     time.sleep(5)

# @when('Go to Safework login page')
# def SafewordDashboard(context):
#     context.driver.get("https://qa.strongarmtech.com/login")
#     time.sleep(5)

# @when('Enters "{email}" and "{pwd}"')
# def EnterCred(context, email, pwd):
#     context.driver.find_element(By.XPATH,"//input[@id='username']").send_keys(email)
#     context.driver.find_element(By.XPATH,"//input[@id='password']").send_keys(pwd)
#     time.sleep(5)

# QA_CRED_EMAIL = os.environ.get('QA_CRED_EMAIL')
# QA_CRED_PASS = os.environ.get('QA_CRED_PASS')

# @when('Enter QA_CRED_EMAIL and QA_CRED_PASS')
# def EnterCred(context):
#     context.driver.find_element(By.XPATH,"//input[@id='username']").send_keys(QA_CRED_EMAIL)
#     context.driver.find_element(By.XPATH,"//input[@id='password']").send_keys(QA_CRED_PASS)
#     time.sleep(5)

# @when('Click on login button')
# def LoginButton(context):
#     context.driver.find_element(By.XPATH, "//span[text()='Login']").click()
#     time.sleep(5)

# @then('User should be logged in')
# def login(context):
#     context.driver.find_element(By.XPATH,"//p[contains(text(),'Go to')]").is_displayed()
#     assert True
#     time.sleep(9)

# @then('User should not be able to login')
# def LoginCheck(context):
#     if context.driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[1]/form[1]/div[1]/*[1]").is_displayed():
#         context.driver.quit()
#         assert True, "Test Passed"
#     else:
#         context.driver.quit()
#         assert False, "Test Failed"
    
# @when('Click on Multibox tab')
# def MultiboxTab(context):
#     context.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[3]/div[1]/*[1]").click()
#     time.sleep(12)

# @when('Click on Signout tab')
# def SignoutTab(context):
#     context.driver.find_element(By.XPATH,"//p[contains(text(),'Sign out')]").click()
#     time.sleep(5)

# @then('User should be signed out')
# def Signedout(context):
#     context.driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[1]/div[1]/form[1]/div[1]/*[1]").is_displayed()
#     assert True
#     time.sleep(8)

# @when('Select Analytics tab')
# def AnalyticsTab(context):
#     context.driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/a[3]/button[1]/span[1]/div[1]/*[1]").click()
#     time.sleep(14)
                                                  
# @when('On Ergonomic Safety Dashboard click on Select Athlete dropdown')
# def select(context):
#     context.driver.find_element(By.XPATH,"//div[@id='Select AthleteSelect']").click()
#     time.sleep(5)

# @then('User should not be able to Select an Athlete before selecting Warehouse')
# def dropdown(context):
#     visible1 = context.driver.find_element(By.XPATH,"//div[@id='Select AthleteSelect']")
#     if visible1.is_displayed():
#         context.driver.quit()
#         assert True, "Test Passed"
#     else: 
#         context.driver.quit()
#         assert False, "Test Failed"

# @when('Click on Fuse Dashboard tab')
# def fuseTab(context):
#     context.driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/*[1]").click()
#     time.sleep(8)

# @when('Select New Hire Tenure Analysis')
# def hiretenure(context):
#     context.driver.find_element(By.XPATH,"//span[contains(text(),'New Hire Tenure Analysis')]").click()
#     time.sleep(10)

# @then('User should be able to see Highest Risk Tenure Group tile')
# def Tile(context):
#     visible2 = context.driver.find_element(By.XPATH,"//h6[contains(text(),'Highest Risk Tenure Group')]")
#     if visible2.is_displayed():
#         context.driver.quit()
#         assert True, "Test Passed"
#     else:
#         context.driver.quit()
#         assert False, "Test Failed"

# @when('Select corporate report tab')
# def reportTab(context):
#     context.driver.find_element(By.XPATH,"//span[contains(text(), 'Corporate Report')]").click()
#     time.sleep(12)

# @when('Click on sort icon of Warehouse')
# def warehouse(context):
#     context.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[2]/main[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span[1]/*[1]").click()
#     time.sleep(5)

# @then('User should be able to sort in qa env')
# def sortIcon(context):
#     visible3 = context.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/div[2]/main[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]")
#     if visible3.is_displayed():
#         context.driver.quit()
#         assert True, "Test Passed"
#     else:
#         context.driver.quit()
#         assert False, "Test Failed"


# #dev3 env credentials

# @when('Go to dev3 login page')
# def SafewordDashboard(context):
#     context.driver.get("https://strongarm.dev3.strongarmtech.com/login")
#     time.sleep(5)

# DEV3_CRED_EMAIL = os.environ.get('DEV3_CRED_EMAIL')
# DEV3_CRED_PASS= os.environ.get('DEV3_CRED_PASS')

# @when('Enter DEV3_CRED_EMAIL and DEV3_CRED_PASS')
# def EnterCred(context):
#     context.driver.find_element(By.XPATH,"//input[@id='username']").send_keys(DEV3_CRED_EMAIL)
#     context.driver.find_element(By.XPATH,"//input[@id='password']").send_keys(DEV3_CRED_PASS)
#     time.sleep(5)

# @then('User should be able to sort in dev3 env')
# def sortIcon(context):
#     visible4 = context.driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/div[2]/div[1]/div[2]/main[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]")
#     if visible4.is_displayed():
#         context.driver.quit()
#         assert True, "Test Passed"
#     else:
#         context.driver.quit()
#         assert False, "Test Failed"
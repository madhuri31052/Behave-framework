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
from pyvirtualdisplay import Display

display = Display(visible=0, size=(1024, 768))
display.start()

@given(u'user is on client page')
def Loginconections(context):
    #webcommon.go_to(context,url,email,pwd)
    url="https://strongarm.dev3.strongarmtech.com/login"

    email = ""
    pwd = ""

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

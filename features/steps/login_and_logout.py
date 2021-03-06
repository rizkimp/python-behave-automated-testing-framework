from behave import*
from locators import*
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@given(u'go to homepage arena')
def step_impl(context):
    context.browser.get('https://arena.jog.ojodowo.com')
    sleep(5)
    context.browser.find_element(By.XPATH,locator.landing)
    context.browser.find_element(By.XPATH,locator.slide)

@when(u'login using username : richard & password : 12345678')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.button_login1).click()
    context.browser.find_element(By.XPATH,locator.form_login)
    context.browser.find_element(By.XPATH,locator.form_username).send_keys('richard')
    context.browser.find_element(By.XPATH,locator.form_password).send_keys('12345678')
    context.browser.find_element(By.XPATH,locator.button_login2).click()

@then(u'direct to homepage users')
def step_impl(context):
    sleep(5)
    context.browser.find_element(By.XPATH,locator.avatar)
    sleep(5)
    context.browser.find_element(By.XPATH,locator.slide)

@when(u'logout')
def step_impl(context):
    context.browser.find_element(By.XPATH,locator.avatar).click()
    context.browser.find_element(By.XPATH,locator.form_avatar)
    context.browser.find_element(By.XPATH,locator.button_logout).click()
    sleep(5)
    context.browser.find_element(By.XPATH,locator.popup_logout)
    context.browser.find_element(By.XPATH,locator.yes_logout).click()

@then(u'direct to homepage arena')
def step_impl(context):
    sleep(5)
    context.browser.find_element(By.XPATH,locator.landing)
    context.browser.find_element(By.XPATH,locator.slide)

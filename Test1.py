from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

os.environ['PATH'] += "c:\Selenium_Driver" #putanja do webdrivera, svaki browser ima svoj driver kojeg treba skinuti i treba paziti na verziju browsera, mora biti ista kao driver
driver = webdriver.Chrome()

driver.get('https://darkob-code.github.io/Selenium_Python_Pycharm_Sum_two_fields/')
sum1 = driver.find_element(By.NAME, 'firstBox')
sum2 = driver.find_element(By.NAME, 'secondBox')

sum1.send_keys(15)
sum2.send_keys(15)

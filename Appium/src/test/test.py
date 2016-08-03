#coding=utf-8
from appium import webdriver
import time


desired_caps = {}
desired_caps['platformName'] = 'Android'  
desired_caps['platformVersion'] = '4.2.2'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.example.zxjt108'
desired_caps['appActivity'] = '.activity.OpenCountActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(2)
driver.find_element(By.ID, 'com.example.zxjt108:id/new_user')
#driver.find_element_by_id('com.example.zxjt108:id/new_user').click()

time.sleep(2)

driver.quit()
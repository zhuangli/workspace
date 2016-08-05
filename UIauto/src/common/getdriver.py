#coding=utf-8
from selenium import webdriver
import os
class get_Driver():
    def get_driver(self,method_name):
        if('Firefox'==method_name):
            driver=webdriver.Firefox()
        elif('IE'==method_name):
            iedriver = "C:\Program Files\Internet Explorer\IEDriverServer.exe"
            os.environ["webdriver.ie.driver"] = iedriver
            driver = webdriver.Ie(iedriver)
        return driver
    
    
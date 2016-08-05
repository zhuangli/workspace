#coding=utf-8
'''
Created on 2016年8月4日
@author: asus
'''
import unittest
from common import getdriver
from common.method import getxml
import time
import login
class test(unittest.TestCase):    
    def setUp(self):
        self.driver=getdriver.get_Driver.get_driver(self,'Firefox')
        self.driver.get(getxml.get_xml('url',0))
        time.sleep(5)
        
    def tearDown(self):
        self.driver.quit()
    def test_Login(self):
        login.test_Login(self)

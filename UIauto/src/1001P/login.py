#coding=utf-8

import unittest,os
import  time
from common.method import getxml

def test_Login(self):
    self.driver.find_element_by_link_text('登录').click()
    time.sleep(2)
    self.driver.find_element_by_id('UnionLoginEmail').send_keys(self.get_xml('username',0))
    self.driver.find_element_by_id('UnionLoginPwd').send_keys(self.get_xml('password',0))
    self.driver.find_element_by_id('UnionLoginButton').click()#登录        

        


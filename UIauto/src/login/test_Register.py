#coding=utf-8
from selenium import webdriver
import time
import unittest
import os,random
class Mytest(unittest.TestCase):
    def setUp(self):
        #iedriver = "C:\Program Files\Internet Explorer\IEDriverServer.exe"
        #os.environ["webdriver.ie.driver"] = iedriver
        #self.driver = webdriver.Ie(iedriver)
        self.driver=webdriver.Firefox()
        self.driver.get('http://cecs-test.haituncun.com:8090/')
    def teardown(self):
        self.driver.quit()
    def test_Register(self):
        time.sleep(3)
        self.driver.find_element_by_xpath("//div[@class='HeaderTopRight']/span[2]/a[2]").click()#�����¼
        time.sleep(3)
        self.driver.find_element_by_id('EmailAddress').send_keys('@qq.com')
        self.driver.find_element_by_id('RPassword').send_keys('123456')
        self.driver.find_element_by_id('RConfirmPW').send_keys('123456')
        self.driver.find_element_by_id('PageRegister').click()
        time.sleep(3)
        #self.driver.find_element_by_xpath("//div[@class='HeaderTopRight']/span[1]").text()
        #self.assertEquals(self.driver.current_url(),'http://cecs-test.haituncun.com:8090/customer/account/')
            
if __name__ =='__main__': 
    unittest.main()

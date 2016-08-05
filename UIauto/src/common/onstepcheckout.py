#coding=utf-8
'''
Created on 2016年8月4日
@author: lizhuanglli
方法：添加地址，进行身份验证，跳转到支付界面
'''
from selenium.webdriver.support.ui import Select
import time
class test_checkout():
    def add_address(self):
        #添加地址
        self.driver.find_element_by_xpath("//a[@class='address-use-new']").click()
        self.driver.find_element_by_id('firstname').send_keys('李壮丽')
        Select(self.driver.find_element_by_id("country")).select_by_index(1)
        time.sleep(1)
        Select(self.driver.find_element_by_id("region_id")).select_by_index(9)
        time.sleep(1)
        Select(self.driver.find_element_by_id("city")).select_by_index(2)
        time.sleep(1)
        Select(self.driver.find_element_by_id("s_county")).select_by_index(2)
        time.sleep(1)
        self.driver.find_element_by_id('street_1').send_keys('1')
        self.driver.find_element_by_id('postcode').send_keys('518000')
        self.driver.find_element_by_id('telephone').send_keys('13620800558')
        self.driver.find_element_by_id('email').send_keys('1056204135@qq.com')
        self.driver.find_element_by_id('AjaxSaveAddress').click()
        self.driver.get_screenshot_as_file("D:/screenshots/dd.png")
    def test_ID(self):
        #身份验证
        self.driver.find_element_by_id('receiver-id').send_keys('371324199002042929')
        self.driver.find_element_by_id('idSubBtn').click()
        time.sleep(1)
        self.driver.get_screenshot_as_file("D:/screenshots/shenfen.png")#截图
    def test_pay(self): 
        #进行支付，跳转到支付宝，截图后返回
        self.driver.find_element_by_id('p_method_alipay_payment').click()#点击用支付宝支付
        self.driver.find_element_by_id('onestepcheckout-place-order').click()#点击支付
        self.driver.back()
#coding=utf-8
'''
Created on 2016年12月29日

@author: asus
'''
from  selenium import webdriver
import unittest,time
from HTMLTestRunner import HTMLTestRunner
from common.method import wait_by_linkText,dom_xml
from common.page import common_login
class test_MyAccount(unittest.TestCase):
    '''未登录的用例测试'''
    def setUp(self):
        print('开始了')
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(20)
    def test_MyOrder(self):
        '''进入我的订单页面'''
        try:
            base_url=dom_xml('url')
            self.driver.get(base_url)
            self.driver.maximize_window()
            self.driver.refresh()
            wait_by_linkText(self.driver,'登录')
            self.driver.find_element_by_link_text('登录').click()
            time.sleep(2)
            common_login(self.driver,dom_xml('username'),dom_xml('password'))
            self.assertIn('我的订单', self.driver.title, '不是我的订单界面')
        except Exception:
            print('没有打开页面')
    def test_MyAccount(self):
        '''进入我的账户页面'''
        try:
            base_url=dom_xml('url')
            self.driver.get(base_url)
            self.driver.maximize_window()
            self.driver.refresh()
            wait_by_linkText(self.driver,'登录')
            self.driver.find_element_by_link_text('登录').click()
            time.sleep(2)
            common_login(self.driver,dom_xml('username'),dom_xml('password'))
            wait_by_linkText(self.driver,'个人信息')
            self.driver.find_element_by_link_text('个人信息')
            self.assertIn('我的账户', self.driver.title, '不是我的账户界面')
        except Exception:
            print('没有打开页面')
    def test_MyAddress(self):
        '''未登录购物车界面，点击优惠券，跳转到购物车界面'''
        try:
            base_url=dom_xml('url')
            self.driver.get(base_url)
            self.driver.maximize_window()
            self.driver.refresh()
            wait_by_linkText(self.driver,'登录')
            self.driver.find_element_by_link_text('登录').click()
            time.sleep(2)
            common_login(self.driver,dom_xml('username'),dom_xml('password'))
            wait_by_linkText(self.driver,'收货地址')
            self.driver.find_element_by_link_text('收货地址')
            self.assertIn('收货地址', self.driver.title, '不是我的收货地址界面')
        except Exception:
            print('没有打开页面')
    def test_MyCoupon(self):
        '''进入我的优惠券页面'''
        try:
            base_url=dom_xml('url')
            self.driver.get(base_url)
            self.driver.maximize_window()
            self.driver.refresh()
            wait_by_linkText(self.driver,'登录')
            self.driver.find_element_by_link_text('登录').click()
            time.sleep(2)
            common_login(self.driver,dom_xml('username'),dom_xml('password'))
            wait_by_linkText(self.driver,'我的优惠券')
            self.driver.find_element_by_link_text('我的优惠券')
            self.assertIn('我的优惠券', self.driver.title, '不是我的优惠券界面')
        except Exception:
            print('没有打开页面')
    def test_Myfavourites(self):
        '''未登录购物车界面，点击优惠券，跳转到购物车界面'''
        try:
            base_url=dom_xml('url')
            self.driver.get(base_url)
            self.driver.maximize_window()
            self.driver.refresh()
            wait_by_linkText(self.driver,'登录')
            self.driver.find_element_by_link_text('登录').click()
            time.sleep(2)
            common_login(self.driver,dom_xml('username'),dom_xml('password'))
            wait_by_linkText(self.driver,'我的收藏')
            self.driver.find_element_by_link_text('我的收藏')
            self.assertIn('我的收藏', self.driver.title, '不是我的收藏界面')
        except Exception:
            print('没有打开页面')
            
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print('结束~~')
            
if __name__=="__main__":
    testsuite=unittest.TestSuite()
    testsuite.addTest(test_MyAccount("test_MyOrder"))
    testsuite.addTest(test_MyAccount("test_MyAccount"))
    testsuite.addTest(test_MyAccount("test_MyAddress"))
    testsuite.addTest(test_MyAccount("test_MyCoupon"))
    testsuite.addTest(test_MyAccount("test_Myfavourites"))
    fp=open('./myaccountresult.html','wb')
    runner=HTMLTestRunner(stream=fp,title='PO搜索测试报告',description='用例执行情况')
    runner.run(testsuite)
    fp.close()
#coding=utf-8
'''
Created on 2016年11月30日

'''
from  selenium import webdriver
import unittest,time
from HTMLTestRunner import HTMLTestRunner
from common.method import open_csv,wait_by_xpath,wait_by_id,wait_by_linkText,dom_xml
from common.page import common_search,search_add_cart,common_login,common_catalog,catalog_add_cart
class test_Unlogin(unittest.TestCase):
    '''未登录的用例测试'''
    def setUp(self):
        print('开始了')
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(20)
    def test_unlogin_coupon_returnCart(self):
        '''未登录购物车界面，点击优惠券，跳转到购物车界面'''
        base_url=dom_xml('url')
        self.driver.get(base_url)
        self.driver.refresh()
        data=open_csv('po_data.csv',2)
        common_catalog(self.driver,'婴幼儿')        
        catalog_add_cart(self.driver,True)
        wait_by_linkText(self.driver,'登录使用优惠券')
        time.sleep(2)
        self.driver.find_element_by_link_text('登录使用优惠券').click()
        time.sleep(2)
        self.assertIn('登录',self.driver.title,'现在页面不在登录界面')
        common_login(self.driver,data['username'],data['password'])
        self.assertIn('购物车',self.driver.title, '现在页面不在购物车界面')
    def test_unlogin_check_returnCart(self):
        '''未登录购物车界面，点击优惠券，跳转到购物车界面'''
        base_url=dom_xml('url')
        self.driver.get(base_url)
        self.driver.refresh()#防止首页出现弹框
        data=open_csv('po_data.csv',2)
        #common_search(self.driver,data['condition'])
        #dict=search_add_cart(self.driver,True)
        common_catalog(self.driver,'婴幼儿')        
        catalog_add_cart(self.driver,True)
        wait_by_id(self.driver,'AccountButton')
        self.driver.find_element_by_id('AccountButton').click()#点击去结账按钮
        time.sleep(2)
        self.assertIn('登录',self.driver.title,'现在页面不在登录界面')
        common_login(self.driver,data['username'],data['password'])
        time.sleep(2)
        self.assertIn('购物车',self.driver.title, '现在页面不在购物车界面')
            
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print('结束~~')
            
if __name__=="__main__":
    testsuite=unittest.TestSuite()
    testsuite.addTest(test_Unlogin("test_unlogin_coupon_returnCart"))
    testsuite.addTest(test_Unlogin("test_unlogin_check_returnCart"))
    fp=open('./unloginresult.html','wb')
    runner=HTMLTestRunner(stream=fp,title='PO搜索测试报告',description='用例执行情况')
    runner.run(testsuite)
    fp.close()
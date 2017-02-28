#coding=utf-8
'''
Created on 2016年12月12日

@author: asus
'''
from  selenium import webdriver
import unittest,time
from HTMLTestRunner import HTMLTestRunner
from common.method import open_csv,wait_by_xpath,wait_by_id,wait_by_linkText,dom_xml
import logging
class test_Catalog(unittest.TestCase):
    '''分类测试'''
    def setUp(self):
        print('开始了')
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(20)
    def test_Catalog(self):
        '''分类商品加入购物车'''
        base_url=dom_xml('url')
        self.driver.get(base_url)
        self.driver.refresh()
        self.driver.find_element_by_link_text('营养保健品').click()
        wait_by_xpath(self.driver,".//div[@class='category-products']/ul/li")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//div[@class='category-products']/ul[1]/li[1]/button").click()
        wait_by_id(self.driver,'easyDialogYesBtn')
        self.driver.find_element_by_id('easyDialogYesBtn').click()#进入购物车中查看商品
        time.sleep(2)
           
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print('结束~~')
            
if __name__=="__main__":
    testsuite=unittest.TestSuite()
    testsuite.addTest(test_Catalog("test_Catalog"))
    fp=open('./unloginresult.html','wb')
    runner=HTMLTestRunner(stream=fp,title='PO搜索测试报告',description='用例执行情况')
    runner.run(testsuite)
    fp.close()

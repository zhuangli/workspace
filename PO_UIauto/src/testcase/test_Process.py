#coding=utf-8
'''
Created on 2017.01.04
@author: asus
'''
from  selenium import webdriver
import unittest,time
from HTMLTestRunner import HTMLTestRunner

from common.method import open_csv,wait_by_xpath,wait_by_id,dom_xml,wait_by_linkText
from common.page import common_login,common_catalog,catalog_add_cart,common_add_address,common_cart_deleteAll,common_add_cart
class test_All_Process(unittest.TestCase):
    '''全流程的测试'''
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(20)        
    def test_Process(self):
        '''全流程测试'''
        base_url=dom_xml('url')
        self.driver.get(base_url)
        self.driver.refresh()
        time.sleep(5)
        self.driver.find_element_by_link_text(u'登录').click()
        data=open_csv('po_data.csv',10)
        time.sleep(5)
        common_login(self.driver,dom_xml('username'),dom_xml('password'))
        common_cart_deleteAll(self.driver)
        for i in range(1,30):
            common_catalog(self.driver,u'婴幼儿')
            time.sleep(2)
            print(i)
            common_add_cart(self.driver,i,True)
            wait_by_id(self.driver,'AccountButton')
            self.driver.find_element_by_id('AccountButton').click()
            time.sleep(5)
            if self.driver.find_element_by_xpath(".//div[@id='billing_address']/ul"):
                print('')
            else:
                wait_by_xpath(self.driver,".//div[@id='billing_address']")
                self.driver.find_element_by_xpath(".//div[@id='billing_address']/a").click()
                common_add_address(self.driver,data['name'])
            if self.driver.find_element_by_xpath(".//div[@class='pass-validate']/p"):
                print('该地址已经身份验证')
            else:
                self.driver.find_element_by_id('receiver-id').send_keys(data['ID'])
                self.driver.find_element_by_id('idSubBtn').click()
            time.sleep(5)
            self.driver.find_element_by_id('p_method_alipay_payment').click()#���֧����֧��
            self.driver.find_element_by_id('onestepcheckout-place-order').click()#���ȥ����
            time.sleep(5)
            self.driver.get(base_url)
            time.sleep(5)
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
if __name__=="__main__":
        testsuite=unittest.TestSuite()
        testsuite.addTest(test_All_Process("test_Process"))
        fp=open('./allprocess_result.html','wb')
        runner=HTMLTestRunner(stream=fp,title='PO搜索测试报告',description='用例执行情况')
        runner.run(testsuite)
        fp.close()
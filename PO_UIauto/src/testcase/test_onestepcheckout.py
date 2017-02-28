#coding=utf-8
'''
Created on 2016年11月25日

@author: asus
'''
from  selenium import webdriver
import unittest,time
from HTMLTestRunner import HTMLTestRunner

from common.method import open_csv,wait_by_xpath,wait_by_id,dom_xml,wait_by_linkText
from common.page import common_login,common_catalog,catalog_add_cart,common_add_address,common_cart_deleteAll
class test_Onestepcheckout(unittest.TestCase):
    '''确认订单页面的测试'''
    def setUp(self):
        print('开始了')
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(20)
    def test_add_address_ID(self):
        '''添加地址，并进行身份验证'''
        base_url=dom_xml('url')
        self.driver.get(base_url)
        self.driver.refresh()
        time.sleep(2)
        self.driver.find_element_by_link_text('登录').click()
        data=open_csv('po_data.csv',10)
        common_login(self.driver,data['username'],data['password'])
        common_cart_deleteAll(self.driver)
        wait_by_linkText(self.driver,'肌肤护理')
        common_catalog(self.driver,'肌肤护理')
        catalog_add_cart(self.driver,1)
        wait_by_id(self.driver,'AccountButton')
        time.sleep(3)
        self.driver.find_element_by_id('AccountButton').click()#点击去结账按钮
        time.sleep(5)
        wait_by_xpath(self.driver,".//div[@id='billing_address']")
        self.driver.find_element_by_xpath(".//div[@id='billing_address']/a").click()
        common_add_address(self.driver,data['name'])
        address_name=self.driver.find_element_by_xpath(".//*[@id='billing_address']/ul/li[1]/div/div[1]/div[1]/span[1]").text
        if address_name==data['name']:
            print('添加地址成功')
        else:
            print('添加地址失败')
        self.driver.find_element_by_id('receiver-id').send_keys(data['ID'])
        self.driver.find_element_by_id('idSubBtn').click()
        time.sleep(5)
        id_text=self.driver.find_element_by_xpath(".//div[@class='pass-validate']/p").text
        if id_text=='（您已通过实名验证）':
            print('身份验证成功')
        else:
            print('身份验证失败')
        
    def test_alipay(self):
        '''测试用支付宝支付'''
        base_url=dom_xml('url')
        self.driver.get(base_url)
        self.driver.refresh()
        time.sleep(5)
        self.driver.find_element_by_link_text('登录').click()
        data=open_csv('po_data.csv',10)
        time.sleep(5)
        common_login(self.driver,data['username'],data['password'])
        time.sleep(5)
        common_cart_deleteAll(self.driver)
        common_catalog(self.driver,'肌肤护理')
        catalog_add_cart(self.driver,1)
        wait_by_id(self.driver,'AccountButton')
        self.driver.find_element_by_id('AccountButton').click()#点击去结账按钮
        time.sleep(5)
        if self.driver.find_element_by_xpath(".//div[@id='billing_address']/ul"):
            print('有地址，直接跳过')
        else:
            wait_by_xpath(self.driver,".//div[@id='billing_address']")
            self.driver.find_element_by_xpath(".//div[@id='billing_address']/a").click()
            common_add_address(self.driver,data['name'])
        id_text=self.driver.find_element_by_xpath(".//div[@class='pass-validate']/p").text
        if self.driver.find_element_by_xpath(".//div[@class='pass-validate']/p"):
            print('该地址已经身份验证')
        else:
            self.driver.find_element_by_id('receiver-id').send_keys(data['ID'])
            self.driver.find_element_by_id('idSubBtn').click()
            time.sleep(5)
        self.driver.find_element_by_id('p_method_alipay_payment').click()#点击支付宝支付
        self.driver.find_element_by_id('onestepcheckout-place-order').click()#点击去结账
        time.sleep(5)
        #self.assertIn('alipay',str(self.driver.current_url()),'跳转到了支付宝界面')
        #self.driver.back()
        time.sleep(2)
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print('结束~~')
if __name__=="__main__":
        testsuite=unittest.TestSuite()
        testsuite.addTest(test_Onestepcheckout("test_alipay"))
        testsuite.addTest(test_Onestepcheckout("test_add_address_ID"))
        fp=open('./checkout_result.html','wb')
        runner=HTMLTestRunner(stream=fp,title='PO搜索测试报告',description='用例执行情况')
        runner.run(testsuite)
        fp.close()
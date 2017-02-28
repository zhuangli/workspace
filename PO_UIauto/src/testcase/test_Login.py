#coding=utf-8
'''
Created on 2016年11月22日

@author: lizhuangli
'''
from  selenium import webdriver
import unittest,time
from HTMLTestRunner import HTMLTestRunner
from common.method import open_csv,wait_by_linkText,dom_xml
from common.page import common_login
class Login_PO(unittest.TestCase):
    '''登录测试'''
    def setUp(self):
        print('开始了')
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(20)

    def test_po_login(self):
        '''测试正确的用户名和密码登录'''
        base_url=dom_xml('url')
        data=open_csv('po_data.csv',1)
        self.driver.get(base_url)
        #self.driver.get(self.base_url)
        self.driver.refresh()
        wait_by_linkText(self.driver,'登录')
        self.driver.find_element_by_link_text('登录').click()
        time.sleep(2)
        common_login(self.driver,data['username'],data['password'])
        time.sleep(5)
        name=self.driver.find_element_by_xpath(".//div[@class='HeaderTopRight']/span").text
        if name.find('2473518012'):
            print('登录成功')
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print('结束了')
            
if __name__=="__main__":
    testsuite=unittest.TestSuite()
    testsuite.addTest(Login_PO("test_po_login")) 
    fp=open('./loginresult.html','wb')
    runner=HTMLTestRunner(stream=fp,title='PO搜索测试报告',description='用例执行情况')
    runner.run(testsuite)
    fp.close()
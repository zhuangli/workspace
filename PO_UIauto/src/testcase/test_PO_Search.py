#coding=utf-8
'''
Created on 2016年11月17日

@author: lizhuangli
'''
from  selenium import webdriver
import unittest,time
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.common.keys import  Keys
from common.method import open_csv,dom_xml
from common.page import common_search
class Search_PO(unittest.TestCase):
    '''搜索测试'''
    def setUp(self):
        print('开始了')
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(20)
    def test_po_search_brand(self):
        '''测试按品牌名称搜索'''
        base_url=dom_xml('url')
        self.driver.get(base_url)
        self.driver.refresh()
        data=open_csv('po_data.csv',3)
        condition=data['condition']
        common_search(self.driver,condition)
        result=self.driver.find_element_by_xpath(".//*[@id='ListProduct']/li[1]/a[2]").text
        self.assertIn(condition,result,'搜索结果没有包含关键字')
    def test_po_search_enterKey(self):
        '''测试按Enter键模糊sku执行搜索'''
        base_url=dom_xml('url')
        data=open_csv('po_data.csv',4)
        self.driver.get(base_url)
        self.driver.refresh()
        self.driver.find_element_by_id('sli_search_1').send_keys(data['condition'])#找到输入框，按sku搜索
        self.driver.find_element_by_xpath(".//*[@id='top-search-form']/div/div/button").send_keys(Keys.ENTER)#点击搜索按钮
        time.sleep(5)
        result=self.driver.find_element_by_xpath(".//*[@id='ListProduct']/li[1]/a[2]").text
        if result:
            self.assert_("有搜索结果")
            print('搜索成功')
        else:
            print('错误的搜索结果'+result)
    def test_po_search_name(self):
        '''测试按商品名称执行搜索'''
        base_url=dom_xml('url')
        data=open_csv('po_data.csv',5)
        self.driver.get(base_url)
        self.driver.refresh()
        condition=data['condition']
        common_search(self.driver,condition)
        try:
            result=self.driver.find_element_by_xpath(".//*[@id='ListProduct']/li[1]/a[2]").text        
            self.assertEqual(condition, result, '搜索的结果不对')
        #------------------------------------------------------------ if result:
            #---------------------------------------------- print('搜索结果'+result)
            #------------------------------------- if result==data['condition']:
                #------------------------------------------------- print('搜索成功')
        #----------------------------------------------------------------- else:
            #------------------------------------------- print('错误的搜索结果'+result)
        except Exception:
            print("没有搜索结果")
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print('结束了')
            
if __name__=="__main__":
    testsuite=unittest.TestSuite()
    testsuite.addTest(Search_PO("test_po_search_brand"))
    testsuite.addTest(Search_PO("test_po_search_enterKey"))
    testsuite.addTest(Search_PO("test_po_search_name"))  
    fp=open('./search_result.html','wb')
    runner=HTMLTestRunner(stream=fp,title='PO搜索测试报告',description='用例执行情况')
    runner.run(testsuite)
    fp.close()
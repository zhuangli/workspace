#coding=utf-8
'''
Created on 2016年2月8日

@author: asus
'''
from  selenium import webdriver
import unittest,time
from HTMLTestRunner import HTMLTestRunner
from common.method import open_csv,wait_by_xpath,wait_by_id,dom_xml,wait_by_linkText
from common.page import common_login
class test_Coupon(unittest.TestCase):
    '''购物车优惠券的测试'''
    def setUp(self):
        print('开始了')
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(20)
    def test_Discount_Coupon(self):
        '''使用有码的优惠券查看减免是否对,7折，运费5折'''
        base_url=dom_xml('url')
        self.driver.get(base_url)
        self.driver.refresh()
        wait_by_linkText(self.driver,'登录')
        self.driver.find_element_by_link_text('登录').click()
        time.sleep(5)
        self.driver.maximize_window()
        data=open_csv('po_data.csv',11)
        common_login(self.driver,data['username'],data['password'])
        wait_by_xpath(self.driver,".//a[@class='HeaderCart']")
        self.driver.find_element_by_xpath('.//a[@class="HeaderCart"]').click()
        time.sleep(5)
        #=======================================================================
        # search(self.driver,data['condition'])
        # test_num=data['test_num']
        # for i in range(1,(int(test_num)+1)):
        #     if i==int(test_num):
        #         wait_by_xpath(self.driver,".//*[@id='ListProduct']/li[%s]"%(i))
        #         self.driver.find_element_by_xpath(".//*[@id='ListProduct']/li[%s]/button"%(i)).click()
        #         #wait_by_id(self.driver,'easyDialogYesBtn')
        #         wait_by_xpath(self.driver,".//div[@id='easyDialogWrapper']/div[1]/div[2]/button[2]")
        #         time.sleep(2)
        #         # easyDialogNoBtn 继续购物  easyDialogYesBtn 进入购物车
        #         #self.driver.find_element_by_xpath(".//div[@id='easyDialogWrapper']/div[1]/div[2]/button[2]").click()
        #         self.driver.find_element_by_id('easyDialogYesBtn').click()#进入购物车中查看商品
        #         time.sleep(5)
        #     else:
        #         wait_by_xpath(self.driver,".//*[@id='ListProduct']/li[%s]"%(i))
        #         self.driver.find_element_by_xpath(".//*[@id='ListProduct']/li[%s]/button"%(i)).click()#第一个商品点击加入购物车按钮
        #         wait_by_xpath(self.driver,".//div[@id='easyDialogWrapper']/div[1]/div[2]/button[1]")
        #         self.driver.find_element_by_xpath(".//div[@id='easyDialogWrapper']/div[1]/div[2]/button[1]").click()
        #=======================================================================
        wait_by_xpath(self.driver,".//div[@id='shopping-cart']/div[1]/table[1]/tbody[1]/tr[1]")
        trs=self.driver.find_elements_by_xpath(".//div[@id='shopping-cart']/div[1]/table[1]/tbody[1]/tr")
        self.driver.find_element_by_id('coupon_code').send_keys(data['coupon'])        
        self.driver.find_element_by_xpath(".//div[@class='hand-code']/input[2]").click()#使用优惠券之后
        time.sleep(5)
        total=(self.driver.find_element_by_id('quote_subtotal').text).strip('AU$')#商品总计,只有商品总价需要去掉单位
        shipping=self.driver.find_element_by_id('quote_shipping').text#总运费
        product_discount_amount=self.driver.find_element_by_id('product_discount_amount').text#商品总折扣
        shipping_discount_amount=self.driver.find_element_by_id('shipping_discount_amount').text#运费总折扣
        print(product_discount_amount)
        all_grandtotal=self.driver.find_element_by_xpath(".//span[@class='all-grandtotal']").text#应付总额
        if (float(total)*0.4)==float(product_discount_amount):
            print('商品打折成功')
        else:
            print('商品没有打折')
        if(float(shipping)*0.4)==float(shipping_discount_amount):
            print('运费打折成功')
        else:
            print('运费没有打折')
        if float(all_grandtotal)==float('%.2f'%(float(total)+float(shipping)-float(shipping_discount_amount)-float(product_discount_amount))):
            print('应付总额计算正确')
        else:
            print('商品总价不对')
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print('结束~~')
if __name__=="__main__":
    testsuite=unittest.TestSuite()
    #testsuite.addTest(test_Cart("test_cart_add_delete")) 
    #testsuite.addTest(test_Cart("test_cart_deleteAll"))
    testsuite.addTest(test_Coupon("test_Discount_Coupon"))
    fp=open('./couponresult.html','wb')
    runner=HTMLTestRunner(stream=fp,title='PO搜索测试报告',description='用例执行情况')
    runner.run(testsuite)
    fp.close()
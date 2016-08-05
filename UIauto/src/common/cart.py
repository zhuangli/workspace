#coding=utf-8
'''
Created on 2016��8��4��

@author: asus
'''
import time
class test_cart:
    def testcart(self,driver):
        #点击右上角搜索ﳵ
        self.driver.find_element_by_xpath("//div[@id='head-cart-contain']/div[1]/a[2]").click()#点击右上角进入购物车
        self.driver.find_element_by_id('coupon_code').send_keys('paypay')
        self.driver.find_element_by_xpath("//*[@id='discount-coupon-form']/div/div[1]/input[2]").click()
        disount_cart=round(float(self.driver.find_element_by_id('discount').text.strip('-€')))
        discout_checkout=round(float(self.driver.find_element_by_id('discount').text.strip('-AU$')))
        if((disount_cart)==discout_checkout):
            self.assertTrue_("打折正常显示")
        self.driver.find_element_by_id('AccountButton').click()#点击提交订单按钮
        time.sleep(5)
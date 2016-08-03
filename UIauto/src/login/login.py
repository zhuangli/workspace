#coding=utf-8
from selenium import webdriver
import unittest,os
import  time
import xml.dom.minidom
class Mytest(unittest.TestCase):
    
    def setUp(self):
        iedriver = "C:\Program Files\Internet Explorer\IEDriverServer.exe"
        os.environ["webdriver.ie.driver"] = iedriver
        self.driver = webdriver.Ie(iedriver)
        #self.driver=webdriver.Firefox()
        self.driver.get(self.get_xml('url',0))
        self.driver.implicitly_wait(30)
    def tearDown(self):
        self.driver.find_element_by_xpath("//div[@class='HeaderTopRight']/span[2]/a[3]").click()
        self.driver.quit()
    def test_Login(self):
        self.driver.find_element_by_xpath("//div[@class='HeaderTopRight']/span[2]/a[1]").click()#点击登录
        self.driver.find_element_by_id('LoginEmail').send_keys(self.get_xml('username', 0))
        self.driver.find_element_by_id('LoginPwd').send_keys(self.get_xml('password', 0))
        self.driver.find_element_by_id('PageLogin').click()
        #搜索功能
        self.driver.find_element_by_id('sli_search_1').send_keys(self.get_xml('sku', 0))
        self.driver.find_element_by_xpath("//*[@id='top-search-form']/div/div/button").click()#点击搜索按钮
        self.driver.find_element_by_xpath("//div[@class='col-main']/div[2]/ul[1]/li[1]/button").click()#点击加入购物车按钮
        self.driver.find_element_by_id('easyDialogYesBtn').click()#跳转到购物车界面
        #self.driver.find_element_by_id('coupon_code').send_keys('paypay')
        #self.driver.find_element_by_xpath("//*[@id='discount-coupon-form']/div/div[1]/input[2]").click()
        time.sleep(3)
        #disount_cart=round(float(self.driver.find_element_by_id('discount').text.strip('-€')))
        self.driver.find_element_by_id('AccountButton').click()#点击确认订单按钮
        time.sleep(3)
        discout_checkout=round(float(self.driver.find_element_by_id('discount').text.strip('-AU$')))
        #if((disount_cart)==discout_checkout):
            #self.assertTrue_("打折正常显示")
        #time.sleep(3)
        print(discout_checkout)
        #self.driver.find_element_by_id('p_method_alipay_payment').click()#点击用支付宝支付
        #self.driver.find_element_by_id('onestepcheckout-place-order').click()#点击支付
        #self.driver.back()
    def get_xml(self,item,index=0):
        #打开xml文档
        dom = xml.dom.minidom.parse('po_data.xml')
        #获得文档元素对象
        root = dom.documentElement
        bb=root.getElementsByTagName(item)
        b=bb[index]
        data=b.firstChild.data
        print(data)
        return data
        
            
if __name__ =='__main__': 
    unittest.main()
        


#coding=utf-8
'''
Created on 2016年11月22日

@author: lizhuangli
'''
from  selenium import webdriver
import unittest,time
from HTMLTestRunner import HTMLTestRunner
from common.method import open_csv,wait_by_xpath,wait_by_id,dom_xml
from common.page import common_catalog,common_add_cart,catalog_add_cart,common_cart_deleteAll
class test_Cart(unittest.TestCase):
    '''商品进入购物车的操作'''
    def setUp(self):
        print('开始了')
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(20)
    def test_cart_add_delete(self):
        '''添加单个商品进入购物车，校验价格和名称，并删除这个商品'''
        base_url=dom_xml('url')
        self.driver.get(base_url)
        self.driver.maximize_window()
        self.driver.refresh()
        data=open_csv('po_data.csv',7)
        product_num=int(data['product_num'])
        common_catalog(self.driver,'婴幼儿')
        time.sleep(2)
        common_add_cart(self.driver,product_num,False)
        common_cart_deleteAll(self.driver)
        #common_search(self,data['condition'])
        #下面用分类的结果，加入购物车
        common_catalog(self.driver,'婴幼儿')
        time.sleep(2)
        name=self.driver.find_elements_by_xpath(".//button[@class='OrangeButton']/../a[2]")[product_num-1].text     
        price=self.driver.find_elements_by_xpath(".//button[@class='OrangeButton']/../div[1]/p[1]")[product_num-1].text
        print(price)
        common_add_cart(self.driver,product_num)
        #购物车这里，第一个列是单选按钮  #第二列是图片  #第三列是商品名称
        try:
            wait_by_xpath(self.driver,".//div[@id='shopping-cart']/div[1]/table[1]/tbody[1]/tr[1]")
            cart_name=self.driver.find_element_by_xpath(".//div[@id='shopping-cart']/div[1]/table[1]/tbody[1]/tr[1]/td[3]").text #后者购物车中商品的名称
            cart_price=self.driver.find_element_by_xpath(".//div[@id='shopping-cart']/div[1]/table[1]/tbody[1]/tr[1]/td[6]").text
            print(cart_price)
            if (cart_name==name)&(price==cart_price):
                print('商品加入成功,并且名称和价格都正确')
            elif(price!=cart_price):
                print('加入购物车后，商品价格不对')
            else:
                print('加入购物车后，加入的不是那个商品')
            cart_price=self.driver.find_element_by_xpath(".//div[@id='shopping-cart']/div[1]/table[1]/tbody[1]/tr[1]/td[8]").click()#删除刚加入的商品
        except Exception:
            print('商品没有价格购物村，加入购物车失败')
    def test_cart_deleteAll(self):
        '''加入多个商品进入购物车，全选删除商品'''
        base_url=dom_xml('url')
        self.driver.get(base_url)
        self.driver.refresh()
        time.sleep(2)
        data=open_csv('po_data.csv',8)
        test_num=data['product_num']
        try:
            #分类结果加入购物车            
            common_catalog(self.driver,'婴幼儿')
            catalog_add_cart(self.driver,test_num)
            #购物车这里，第一个列是单选按钮  #第二列是图片  #第三列是商品名称
            wait_by_xpath(self.driver,".//div[@id='shopping-cart']/div[1]/table[1]/tbody[1]/tr[1]")
            if self.driver.find_element_by_xpath(".//div[@id='shopping-cart']/div[1]/div[1]/input").is_selected():
                self.driver.find_element_by_link_text('删除选择产品').click()
            else:
                self.driver.find_element_by_xpath(".//div[@id='shopping-cart']/div[1]/div[1]/input").click()
                self.driver.find_element_by_link_text('删除选择产品').click()
                time.sleep(2)
                
            try:
                self.driver.find_element_by_xpath(".//div[@id='easyDialogWrapper']/div[1]/div[2]/button[2]").click()
                time.sleep(2)
                self.driver.find_element_by_link_text('点击继续购物').click()
            except Exception as e:
                print(e)
                print('没有全部删除成功，购物车还有商品')
                                
        except Exception:
            print('商品没有加入购物车，加入购物车失败')
    def test_cart_changQTP(self):
        '''加入多个商品进入购物车，修改商品数量'''
        base_url=dom_xml('url')
        self.driver.get(base_url)
        self.driver.refresh()
        data=open_csv('po_data.csv',9)
        #common_search(self.driver,data['condition'])
        test_num=data['product_num']
        common_catalog(self.driver,'婴幼儿')
        catalog_add_cart(self.driver,test_num)
        wait_by_xpath(self.driver,".//div[@id='shopping-cart']/div[1]/table[1]/tbody[1]/tr[1]")
        trs=self.driver.find_elements_by_xpath(".//div[@id='shopping-cart']/div[1]/table[1]/tbody[1]/tr")
        sum=0.0
        if (len(trs)-1)==int(test_num):
            print('购物车商品都加入成功')
        #购物车这里，第一个列是单选按钮  #第二列是图片  #第三列是商品名称
            for j in range(1,(int(test_num)+1)):
                self.driver.find_element_by_xpath(".//div[@id='shopping-cart']/div[1]/table[1]/tbody[1]/tr[%s]/td[5]/div/p[2]"%(j)).click()#增加一个数量
                time.sleep(2)
                #self.driver.find_element_by_xpath(".//div[@id='shopping-cart']/div[1]/table[1]/tbody[1]/tr[2]/td[5]/div/p[2]").click()#增加一个数量
                firstprice=self.driver.find_element_by_xpath(".//div[@id='shopping-cart']/div[1]/table[1]/tbody[1]/tr[%s]/td[6]/span"%(j)).text
                sum+=float(firstprice.strip('AU$'))
                total=self.driver.find_element_by_id('quote_subtotal').text
                if sum==float(total.strip('AU$')):
                    print('商品小计计算成功')
                else:
                    print('商品小计计算失败')
        else:
            print('没有把全部商品都加入购物车')
    
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print('结束~~')
            
if __name__=="__main__":
    testsuite=unittest.TestSuite()
    testsuite.addTest(test_Cart("test_cart_add_delete")) 
    #testsuite.addTest(test_Cart("test_cart_deleteAll"))
    #testsuite.addTest(test_Cart("test_cart_changQTP"))
    fp=open('./cartresult.html','wb')
    runner=HTMLTestRunner(stream=fp,title='PO搜索测试报告',description='用例执行情况')
    runner.run(testsuite)
    fp.close()
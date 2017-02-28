#coding=utf-8
'''
Created on 2016年11月28日
'''
from common.method import wait_by_xpath,wait_by_id,isElementExist_xpath
import time
from selenium.webdriver.support.ui import Select
def common_search(driver,condition):
        wait_by_id(driver,'sli_search_1')    
        driver.find_element_by_id('sli_search_1').clear()
        driver.find_element_by_id('sli_search_1').send_keys(condition)#找到输入框，按sku搜索
        driver.find_element_by_xpath(".//*[@id='top-search-form']/div/div/button").click()#点击搜索按钮
        time.sleep(5)
def search_add_cart(driver,product_num=1):    
            #  第一个商品加入购物车
        for i in range(1,(int(product_num)+1)):
            if i==int(product_num):
                wait_by_xpath(driver,".//*[@id='ListProduct']/li[%s]"%(i))
                driver.find_element_by_xpath(".//*[@id='ListProduct']/li[%s]/button"%(i)).click()
                #wait_by_id(self.driver,'easyDialogYesBtn')
                wait_by_xpath(driver,".//div[@id='easyDialogWrapper']/div[1]/div[2]/button[2]")
                time.sleep(2)
                # easyDialogNoBtn 继续购物  easyDialogYesBtn 进入购物车
                #self.driver.find_element_by_xpath(".//div[@id='easyDialogWrapper']/div[1]/div[2]/button[2]").click()
                driver.find_element_by_id('easyDialogYesBtn').click()#进入购物车中查看商品
                time.sleep(5)
            else:
                wait_by_xpath(driver,".//*[@id='ListProduct']/li[%s]"%(i))
                driver.find_element_by_xpath(".//*[@id='ListProduct']/li[%s]/button"%(i)).click()#第一个商品点击加入购物车按钮
                wait_by_xpath(driver,".//div[@id='easyDialogWrapper']/div[1]/div[2]/button[1]")
                driver.find_element_by_id('easyDialogNoBtn').click()#进入购物车中查看商品
                time.sleep(3)
def catalog_add_cart(driver,product_num=1):    
    for i in range(1,(int(product_num)+1)):
            if i==int(product_num):
                wait_by_xpath(driver,".//div[@class='category-products']/ul/li[%s]"%(i))
                time.sleep(2)
                driver.find_element_by_xpath(".//div[@class='category-products']/ul/li[%s]/button"%(i)).click()
                #wait_by_id(self.driver,'easyDialogYesBtn')
                wait_by_id(driver,"easyDialogYesBtn")
                time.sleep(2)
                # easyDialogNoBtn 继续购物  easyDialogYesBtn 进入购物车
                #self.driver.find_element_by_xpath(".//div[@id='easyDialogWrapper']/div[1]/div[2]/button[2]").click()
                driver.find_element_by_id('easyDialogYesBtn').click()#进入购物车中查看商品
                time.sleep(5)
            else:
                wait_by_xpath(driver,".//div[@class='category-products']/ul/li[%s]"%(i))
                driver.find_element_by_xpath(".//div[@class='category-products']/ul/li[%s]/button"%(i)).click()#第一个商品点击加入购物车按钮
                wait_by_id(driver,"easyDialogNoBtn")
                driver.find_element_by_id('easyDialogNoBtn').click()#进入购物车中查看商品
                time.sleep(3)
def common_cart_deleteAll(driver):
        wait_by_xpath(driver,".//a[@class='HeaderCart']")
        driver.find_element_by_xpath('.//a[@class="HeaderCart"]').click()
        time.sleep(5)
        state=isElementExist_xpath(driver,".//div[@class='cart-empty']")
        if state:
            print('购物车中没有商品')
        else:
            print('购物车里有商品')        
            wait_by_xpath(driver,".//div[@id='shopping-cart']/div[1]/table[1]/tbody[1]/tr[1]")
            if driver.find_element_by_xpath(".//div[@id='shopping-cart']/div[1]/div[1]/input").is_selected():
                driver.find_element_by_link_text('删除选择产品').click()
                driver.find_element_by_xpath(".//div[@id='easyDialogWrapper']/div[1]/div[2]/button[2]").click()
            else:
                driver.find_element_by_xpath(".//div[@id='shopping-cart']/div[1]/div[1]/input").click()
                driver.find_element_by_link_text('删除选择产品').click()
                driver.find_element_by_xpath(".//div[@id='easyDialogWrapper']/div[1]/div[2]/button[2]").click()
        time.sleep(2)
def common_add_cart(driver,test_num=1,state=True):
    wait_by_xpath(driver,".//button[@class='OrangeButton']")
    webElements=driver.find_elements_by_xpath(".//button[@class='OrangeButton']")#公用的加入购物车功能
    if state==True:
        webElements[int(test_num)-1].click()
        wait_by_id(driver,'easyDialogYesBtn')
        driver.find_element_by_id('easyDialogYesBtn').click()
    elif state==False:
        webElements[int(test_num)-1].click()
        wait_by_id(driver,'easyDialogNoBtn')
        driver.find_element_by_id('easyDialogNoBtn').click()
    else:
        for webElement in webElements[0:int(test_num)-1]:
            webElement.click()
            time.sleep(2)
            wait_by_id(driver,'easyDialogNoBtn')
            driver.find_element_by_id('easyDialogNoBtn').click()
            time.sleep(2)
            webElements[int(test_num)-1].click()
            wait_by_id(driver,'easyDialogYesBtn')
            driver.find_element_by_id('easyDialogYesBtn').click()
    time.sleep(5)
    
        
def common_login(driver,username,password):
        driver.find_element_by_id('UnionLoginEmail').clear()
        driver.find_element_by_id('UnionLoginEmail').send_keys(username)
        driver.find_element_by_id('UnionLoginPwd').clear()
        driver.find_element_by_id('UnionLoginPwd').send_keys(password)
        wait_by_id(driver,'UnionLoginButton')
        driver.find_element_by_id('UnionLoginButton').click()
        time.sleep(5)
def common_catalog(driver,text):
    driver.find_element_by_link_text(text).click()
def common_add_address(driver,name):
        driver.find_element_by_id('firstname').clear()
        driver.find_element_by_id('firstname').send_keys(name)
        Select(driver.find_element_by_id("country")).select_by_index(1)
        time.sleep(1)
        Select(driver.find_element_by_id("region_id")).select_by_index(9)
        time.sleep(1)
        Select(driver.find_element_by_id("city")).select_by_index(2)
        time.sleep(1)
        Select(driver.find_element_by_id("s_county")).select_by_index(2)
        time.sleep(1)
        driver.find_element_by_id('street_1').clear()
        driver.find_element_by_id('street_1').send_keys('1')
        driver.find_element_by_id('postcode').clear()
        driver.find_element_by_id('postcode').send_keys('518000')
        driver.find_element_by_id('telephone').clear()
        driver.find_element_by_id('telephone').send_keys('13620800558')
        driver.find_element_by_id('email').clear()
        driver.find_element_by_id('email').send_keys('1056204135@qq.com')
        driver.find_element_by_id('primary_shipping').click()
        driver.find_element_by_id('AjaxSaveAddress').click()
        time.sleep(2)

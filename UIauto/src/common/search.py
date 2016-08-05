'''
Created on 2016年8月4日

@author: asus
'''
class Seach_test():
    def search_text(self,driver):        
        self.driver.find_element_by_id('sli_search_1').send_keys(self.get_xml('sku', 0))
        self.driver.find_element_by_xpath("//*[@id='top-search-form']/div/div/button").click()#点击搜索按钮
        self.driver.find_element_by_xpath("//div[@class='col-main']/div[2]/ul[1]/li[1]/button").click()#点击加入购物车按钮
        self.driver.find_element_by_id('easyDialogYesBtn').click()#跳转到购物车界面
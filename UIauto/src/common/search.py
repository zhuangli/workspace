'''
Created on 2016��8��4��

@author: asus
'''
class Seach_test():
    def search_text(self,driver):        
        self.driver.find_element_by_id('sli_search_1').send_keys(self.get_xml('sku', 0))
        self.driver.find_element_by_xpath("//*[@id='top-search-form']/div/div/button").click()#���������ť
        self.driver.find_element_by_xpath("//div[@class='col-main']/div[2]/ul[1]/li[1]/button").click()#������빺�ﳵ��ť
        self.driver.find_element_by_id('easyDialogYesBtn').click()#��ת�����ﳵ����
#coding=utf-8
'''
Created on 2016年11月25日

@author: lizhuangli
'''
import csv
from selenium.webdriver.support.ui import WebDriverWait
from xml.dom.minidom import parse
import xml.dom.minidom
def open_csv(file,rownum):
    try:
        csv_file=open(file,'r')
        reader = csv.DictReader(csv_file)
        for row in reader:
            if int(row['num'])==rownum:
                return row
            else:
                print('没有找到这个编号')     
    except Exception as e:
        print (e)

def wait_by_id(driver,id):
    WebDriverWait(driver, 60).until(lambda the_driver: the_driver.find_element_by_id(id).is_displayed())
def wait_by_xpath(driver,xpath):
    WebDriverWait(driver, 60).until(lambda the_driver: the_driver.find_element_by_xpath(xpath).is_displayed())
def wait_by_linkText(driver,link_text):
    WebDriverWait(driver, 60).until(lambda the_driver: the_driver.find_element_by_link_text(link_text).is_displayed())
def isElementExist_xpath(driver,element):
        flag=True
        try:
            driver.find_element_by_xpath(element)
            return flag        
        except:
            flag=False
            return flag
def dom_xml(item):
    DOMTree = xml.dom.minidom.parse("po_data.xml")
    collection = DOMTree.documentElement
    pos = collection.getElementsByTagName(item)
    item=pos[0]
    return item.childNodes[0].data
    
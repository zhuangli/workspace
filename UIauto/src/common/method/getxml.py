#coding=utf-8
'''
Created on 2016年8月4日

@author: asus
'''
import xml.dom.minidom

def get_xml(self,item,index=0):
    #打开xml文档
    data=0
    dom = xml.dom.minidom.parse('../data/1001_data.xml')
    print('success read')
    #获得文档元素对象
    root = dom.documentElement
    bb=root.getElementsByTagName('catalog')
    #b=bb[0]
    for movie in bb:
        bb=movie.getElementsByTagName(item)[0]
        data=bb.firstNodes[0].data
    return data
        
    
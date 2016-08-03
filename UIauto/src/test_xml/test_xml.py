#coding=utf-8
import xml.dom.minidom

#打开xml文档
dom = xml.dom.minidom.parse('abs.xml')

#获得文档元素对象
root = dom.documentElement
print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)
print(root.ELEMENT_NODE)
bb=root.getElementsByTagName('caption')
b=bb[2]
print(b.firstChild.data)
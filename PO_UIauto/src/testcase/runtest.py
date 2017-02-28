#coding=utf-8
'''
Created on 2016年11月21日

@author: lizhuangli
'''
import unittest,time
from HTMLTestRunner import HTMLTestRunner
#指定测试用例为当前文件夹下的某个目录
test_dir='../testcase'
discover=unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
if __name__=='__main__':
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    filename=test_dir+'/'+now+'poresult.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='PO测试报告',description='测试用例执行结果')
    runner.run(discover)
    fp.close()
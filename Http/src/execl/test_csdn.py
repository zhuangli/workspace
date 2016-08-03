#coding=utf-8
import os,sys, urllib, http.client, profile, datetime, time  
from xml2dict import XML2Dict  
import win32com.client  
import xml.etree.ElementTree as et  
#import MySQLdb  
  

OK_COLOR=0xffffff  
NG_COLOR=0xff  
#NT_COLOR=0xffff  
NT_COLOR=0xC0C0C0  
  

TESTTIME=[1, 14]  
TESTRESULT=[2, 14]  
  

class create_excel:  
    def __init__(self, sFile, dtitleindex=3, dcasebegin=4, dargbegin=3, dargcount=8):  
        self.xlApp = win32com.client.Dispatch('et.Application')   #MS:Excel  WPS:et  
        try:  
            self.book = self.xlApp.Workbooks.Open(sFile)  
        except:  
            print_error_info()  
            print("���ļ�ʧ��")  
            exit()  
        self.file=sFile  
        self.titleindex=dtitleindex  
        self.casebegin=dcasebegin  
        self.argbegin=dargbegin  
        self.argcount=dargcount  
        self.allresult=[]  
          
        self.retCol=self.argbegin+self.argcount  
        self.xmlCol=self.retCol+1  
        self.resultCol=self.xmlCol+1  
  
    def close(self):  
        #self.book.Close(SaveChanges=0)  
        self.book.Save()  
        self.book.Close()  
        #self.xlApp.Quit()  
        del self.xlApp  
          
    def read_data(self, iSheet, iRow, iCol):  
        try:  
            sht = self.book.Worksheets(iSheet)  
            sValue=str(sht.Cells(iRow, iCol).Value)  
        except:  
            self.close()  
            print('��ȡ���ʧ��')  
            exit()  
        #ȥ��'.0'  
        if sValue[-2:]=='.0':  
            sValue = sValue[0:-2]  
        return sValue  
  
    def write_data(self, iSheet, iRow, iCol, sData, color=OK_COLOR):  
        try:  
            sht = self.book.Worksheets(iSheet)  
            sht.Cells(iRow, iCol).Value = sData.decode("utf-8")  
            sht.Cells(iRow, iCol).Interior.Color=color  
            self.book.Save()  
        except:  
            self.close()  
            print('д�����ʧ��')  
            exit()  
      
    #��ȡ�������      
    def get_ncase(self, iSheet):  
        try:  
            return self.get_nrows(iSheet)-self.casebegin+1  
        except:  
            self.close()  
            print('��ȡCase����ʧ��')  
            exit()  
      
    def get_nrows(self, iSheet):  
        try:  
            sht = self.book.Worksheets(iSheet)  
            return sht.UsedRange.Rows.Count  
        except:  
            self.close()  
            print('��ȡnrowsʧ��')  
            exit()  
  
    def get_ncols(self, iSheet):  
        try:  
            sht = self.book.Worksheets(iSheet)  
            return sht.UsedRange.Columns.Count  
        except:  
            self.close()  
            print('��ȡncolsʧ��')  
            exit()  
      
    def del_testrecord(self, suiteid):  
        try:  
            #Ϊ���������ر��Forѭ����ȡ����  
            nrows=self.get_nrows(suiteid)+1  
            ncols=self.get_ncols(suiteid)+1  
            begincol=self.argbegin+self.argcount  
              
            #��������  
            sht = self.book.Worksheets(suiteid)  
  
            for row in range(self.casebegin, nrows):  
                for col in range(begincol, ncols):  
                    str=self.read_data(suiteid, row, col)  
                    startpos = str.find('[')  
                    if startpos>0:  
                        str = str[0:startpos].strip()  
                        self.write_data(suiteid, row, col, str, OK_COLOR)  
                    else:  
                        sht.Cells(row, col).Interior.Color = OK_COLOR  
                self.write_data(suiteid, row,  self.argbegin+self.argcount+1, ' ', OK_COLOR)  
                self.write_data(suiteid, row, self.resultCol, 'NT', NT_COLOR)  
        except:  
            self.close()  
            print('������ʧ��')  
            exit()  
  
#ִ�е���  
def HTTPInvoke(IPPort, url):  
    conn = http.client.HTTPConnection(IPPort)  
    conn.request("GET", url)  
    rsps = conn.getresponse()  
    data = rsps.read()  
    conn.close()  
    return data  
  

def get_caseinfo(Data, SuiteID):  
    caseinfolist=[]  
    sInterface=Data.read_data(SuiteID, 1, 2)   
    argcount=int(Data.read_data(SuiteID, 2, 2))   
      
    #��ȡ���������ArgNameList   
    ArgNameList=[]  
    for i in range(0, argcount):  
        ArgNameList.append(Data.read_data(SuiteID, Data.titleindex, Data.argbegin+i))    
      
    caseinfolist.append(sInterface)  
    caseinfolist.append(argcount)  
    caseinfolist.append(ArgNameList)  
    return caseinfolist  
  
#��ȡ����  
def get_input(Data, SuiteID, CaseID, caseinfolist):  
    sArge=''  
    #�������  
    for j in range(0, caseinfolist[1]):  
        if Data.read_data(SuiteID, Data.casebegin+CaseID, Data.argbegin+j) != "None":  
            sArge=sArge+caseinfolist[2][j]+'='+Data.read_data(SuiteID, Data.casebegin+CaseID, Data.argbegin+j)+'&'   
      
    #ȥ����β��&�ַ�  
    if sArge[-1:]=='&':  
        sArge = sArge[0:-1]     
    sInput=caseinfolist[0]+sArge    #���ȫ������  
    return sInput  
   
#����ж�   
def assert_result(sReal, sExpect):  
    sReal=str(sReal)  
    sExpect=str(sExpect)  
    if sReal==sExpect:  
        return 'OK'  
    else:  
        return 'NG'  
  
#�����Խ��д���ļ�  
def write_result(Data, SuiteId, CaseId, resultcol, *result):  
    if len(result)>1:  
        ret='OK'  
        for i in range(0, len(result)):  
            if result[i]=='NG':  
                ret='NG'  
                break  
        if ret=='NG':  
            Data.write_data(SuiteId, Data.casebegin+CaseId, resultcol,ret, NG_COLOR)  
        else:  
            Data.write_data(SuiteId, Data.casebegin+CaseId, resultcol,ret, OK_COLOR)  
        Data.allresult.append(ret)  
    else:  
        if result[0]=='NG':  
            Data.write_data(SuiteId, Data.casebegin+CaseId, resultcol,result[0], NG_COLOR)  
        elif result[0]=='OK':  
            Data.write_data(SuiteId, Data.casebegin+CaseId, resultcol,result[0], OK_COLOR)  
        else:  #NT  
            Data.write_data(SuiteId, Data.casebegin+CaseId, resultcol,result[0], NT_COLOR)  
        Data.allresult.append(result[0])  
      
    #����ǰ���������ӡ  
    print( 'case'+str(CaseId+1)+':', Data.allresult[-1])  
  
#��ӡ���Խ��  
def statisticresult(excelobj):  
    allresultlist=excelobj.allresult  
    count=[0, 0, 0]  
    for i in range(0, len(allresultlist)):  
        #print 'case'+str(i+1)+':', allresultlist[i]  
        count=countflag(allresultlist[i],count[0], count[1], count[2])  
    print( 'Statistic result as follow:')  
    print( 'OK:', count[0])
    print ('NG:', count[1])  
    print( 'NT:', count[2])  
  
#����XmlString����Dict  
def get_xmlstring_dict(xml_string):  
    xml = XML2Dict()  
    return xml.fromstring(xml_string)  
      
#����XmlFile����Dict   
def get_xmlfile_dict(xml_file):  
    xml = XML2Dict()  
    return xml.parse(xml_file)  
  
#ȥ����ʷ���expect[real]  
def delcomment(excelobj, suiteid, iRow, iCol, str):  
    startpos = str.find('[')  
    if startpos>0:  
        str = str[0:startpos].strip()  
        excelobj.write_data(suiteid, iRow, iCol, str, OK_COLOR)  
    return str  
      
#���ÿ��item ���ǽṹ�壩  
def check_item(excelobj, suiteid, caseid,real_dict, checklist, begincol):  
    ret='OK'  
    for checkid in range(0, len(checklist)):  
        real=real_dict[checklist[checkid]]['value']  
        expect=excelobj.read_data(suiteid, excelobj.casebegin+caseid, begincol+checkid)  
          
        #����鲻һ�²⽫ʵ�ʽ��д��expect�ֶΣ���ʽ��expect[real]  
        #��return NG  
        result=assert_result(real, expect)  
        if result=='NG':  
            writestr=expect+'['+real+']'  
            excelobj.write_data(suiteid, excelobj.casebegin+caseid, begincol+checkid, writestr, NG_COLOR)  
            ret='NG'  
    return ret  
  
#���ṹ������  
def check_struct_item(excelobj, suiteid, caseid,real_struct_dict, structlist, structbegin, structcount):  
    ret='OK'  
    if structcount>1:  #�������List  
        for structid in range(0, structcount):  
            structdict=real_struct_dict[structid]  
            temp=check_item(excelobj, suiteid, caseid,structdict, structlist, structbegin+structid*len(structlist))  
            if temp=='NG':  
                ret='NG'  
                       
    else: #�������Dict  
        temp=check_item(excelobj, suiteid, caseid,real_struct_dict, structlist, structbegin)  
        if temp=='NG':  
            ret='NG'  
              
    return ret  
  
#��ȡ�쳣�����к�  
def print_error_info():  
    """Return the frame object for the caller's stack frame."""  
    try:  
        raise Exception  
    except:  
        f = sys.exc_info()[2].tb_frame.f_back  
    print (f.f_code.co_name, f.f_lineno)    
  
#���Խ�������������Switch���ʵ��  
def countflag(flag,ok, ng, nt):   
    calculation  = {'OK':lambda:[ok+1, ng, nt],    
                         'NG':lambda:[ok, ng+1, nt],                        
                         'NT':lambda:[ok, ng, nt+1]}       
    return calculation[flag]()   
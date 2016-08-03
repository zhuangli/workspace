from test_csdn import *  
from common_lib import *
import os
  
httpString='http://xxx.com/xxx_product/test/'  
expectXmldir=os.getcwd()+'/TestDir/expect/'  
realXmldir=os.getcwd()+'/TestDir/real/'  
  
def run(interface_name, suiteid):  
    print '��'+interface_name+'��' + ' Test Begin,please waiting...'  
    global expectXmldir, realXmldir  
      
    #���ݽӿ����ֱ𴴽�Ԥ�ڽ��Ŀ¼��ʵ�ʽ��Ŀ¼  
    expectDir=expectXmldir+interface_name  
    realDir=realXmldir+interface_name  
    if os.path.exists(expectDir) == 0:  
        os.makedirs(expectDir)  
    if os.path.exists(realDir) == 0:  
        os.makedirs(realDir)  
      
    excelobj.del_testrecord(suiteid)  #�����ʷ��������  
    casecount=excelobj.get_ncase(suiteid) #��ȡcase����  
    caseinfolist=get_caseinfo(excelobj, suiteid) #��ȡCase������Ϣ  
      
    #����ִ��case  
    for caseid in range(0, casecount):  
        #����Ƿ�ִ�и�Case  
        if excelobj.read_data(suiteid,excelobj.casebegin+caseid, 2)=='N':  
            write_result(excelobj, suiteid, caseid, excelobj.resultCol, 'NT')  
            continue #��ǰCase����������ִ����һ��Case  
          
        #��ȡ��������  
        sInput=httpString+get_input(excelobj, suiteid, caseid, caseinfolist)     
        XmlString=HTTPInvoke(com_ipport, sInput)     #ִ�е���  
          
        #��ȡ�����벢�Ƚ�  
        result_code=et.fromstring(XmlString).find("result_code").text  
        ret1=check_result(excelobj, suiteid, caseid,result_code, excelobj.retCol)  
          
        #����Ԥ�ڽ���ļ�  
        expectPath=expectDir+'/'+str(caseid+1)+'.xml'  
        #saveXmlfile(expectPath, XmlString)  
          
        #����ʵ�ʽ���ļ�  
        realPath=realDir+'/'+str(caseid+1)+'.xml'  
        saveXmlfile(realPath, XmlString)  
          
        #�Ƚ�Ԥ�ڽ����ʵ�ʽ��  
        ret2= check_xmlfile(excelobj, suiteid, caseid,expectPath, realPath)  
          
        #д���Խ��  
        write_result(excelobj, suiteid, caseid, excelobj.resultCol, ret1, ret2)  
    print '��'+interface_name+'��' + ' Test End!'  